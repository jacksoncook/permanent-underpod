#!/usr/bin/env python
"""Cross-episode retention study: every chapter of every episode as one row.

Joins the audience-retention curve of each long-form episode (analytics/channel-data.json)
to the chapter table in episodes/epN/segment-times.md and, where a speaker-attributed
final-cut SRT exists, to who was talking and how fast.  Then asks, across all episodes:

  * position   -- how much of the loss is just "it's minute 40"
  * format     -- cold open / welcome / perp / marquee / explainer / ... (title regex)
  * topic      -- TF-IDF + NMF clusters over chapter title + transcript text
  * speaker    -- share of words per host, crosstalk (speaker switches / min), words / min
  * length     -- does the per-minute loss rate climb the longer a chapter runs

Two retention measures per chapter:
  hazard   = -ln(ret_end / ret_start) / minutes   (raw per-minute loss; position-confounded)
  vs_typ   = mean of YouTube's relativeRetentionPerformance over the chapter
             (already position-normalised against similar-length videos; 0.5 = typical)

Usage:
  analytics/.venv/bin/python .claude/skills/channel-analytics/scripts/episode_study.py \
      analytics/channel-data.json episodes analytics/study [--daily analytics/episode-daily.json]
"""
import json
import math
import os
import re
import sys
from collections import Counter, defaultdict

import numpy as np
import pandas as pd

MIN_EPISODE_S = 2400
MIN_CHAPTER_S = 45
SPEAKERS = ("Jackson", "Chris", "Tyler")
TOPIC_K = 8

CATEGORY_RULES = {
    "perp_trading": r"perp|leverage|\b(long|short)(ed|ing)?\b.*\b(x|×)\b|dashboard|hyperliquid|bet(s|ting)?\b|stake",
    "bitcoin_l2": r"lightning|\bspark\b|\bark\b|liquid|\bl2s?\b|layer-?2|channel|unilateral exit|statechain|sats\b|self-custody|hardware wallet|cold ?card|ledger|multisig|seed phrase|on-chain|bitcoin",
    "stablecoin_regulation": r"stablecoin|usdt|usdc|tether|circle|genius act|clarity|treasur|yield|regulat|\bbill\b|\bsec\b|cftc|tornado|legal|bank secrecy|sanction|kyc|open ?usd|ousd|tempo",
    "ai_industry": r"openai|anthropic|deepseek|gemini|\bgpt|claude|astra|fable|\bjev\b|\bglm\b|benchmark|\bagi\b|frontier|\blabs?\b|x-risk|rationalist|saas|github|model release|open[- ]weights?|haiku|opus|sycophan",
    "ai_agents_doing_things": r"agents?\b|instinct|\bmuse\b|\bmcps?\b|swarm|sandbox|escaped|vibe[- ]?cod|built (a|an|his|her|the)|my agent|clones?\b|soul\.md|roomba|toaster|fridge|doordash|tennis",
    "hack_security_privacy": r"hack|exploit|heist|drained|stolen|implant|malware|lazarus|dprk|quantum|q-day|privacy|opsec|\btor\b|tails|de-?anonymi|surveillance|enclave|\btee\b|attestation|cryptograph|encrypt|private key",
    "markets_mev": r"korea|seoul|trading competition|exchange|bitget|\bmev\b|sandwich|flashbots|auction|order ?flow|wintermute|market maker|liquidit",
    "banter_personal": r"confession|story|girlfriend|wife|cult\b|shirtless|wife beater|cigarette|rubik|beer|chopstick|sushi|freestyle|roast|housekeeping|check-?in|props?\b|microphone|smell",
}
TITLE_WEIGHT = 6.0


FORMAT_RULES = [
    ("cold_open", r"cold open"),
    ("title_card", r"^title card"),
    ("end_card", r"^end card|outro"),
    ("welcome", r"^welcome|^flying solo|meet the hosts|housekeeping|check-?in|^confession"),
    ("perp", r"perp of fortune|^perp\b|perp halftime|perp check|perp final|the og perp|dashboard"),
    ("marquee", r"marquee"),
    ("explainer", r"explain|how (a|the) .* works?|what (is|are) (a |an )?|layer-2|l2 series|series:|101|primer|history of"),
    ("ai_bit", r"ai clone|clone|ai bit|our ai|avatar|sadtalker"),
]


def ts_to_s(t):
    parts = [int(p) for p in t.split(":")]
    return parts[0] * 3600 + parts[1] * 60 + parts[2] if len(parts) == 3 else parts[0] * 60 + parts[1]


def parse_chapters(path):
    """Longest monotonic run of `| m:ss | title |` rows = the chapter table."""
    rows = []
    for line in open(path, encoding="utf-8", errors="ignore"):
        m = re.match(r"^\|\s*((?:\d+:)?\d+:\d\d)\s*\|\s*(.*?)\s*\|\s*$", line)
        if m:
            rows.append((ts_to_s(m.group(1)), m.group(2)))
    runs, cur = [], []
    for r in rows:
        if cur and r[0] < cur[-1][0]:
            runs.append(cur)
            cur = []
        cur.append(r)
    if cur:
        runs.append(cur)
    return max(runs, key=len) if runs else []


def parse_srt(path):
    cues = []
    txt = open(path, encoding="utf-8", errors="ignore").read()
    for block in re.split(r"\n\s*\n", txt.strip()):
        lines = block.strip().splitlines()
        if len(lines) < 3:
            continue
        m = re.match(r"(\d\d):(\d\d):(\d\d)[,.](\d+)\s*-->\s*(\d\d):(\d\d):(\d\d)[,.](\d+)", lines[1])
        if not m:
            continue
        g = [int(x) for x in m.groups()]
        start = g[0] * 3600 + g[1] * 60 + g[2] + g[3] / 1000
        end = g[4] * 3600 + g[5] * 60 + g[6] + g[7] / 1000
        text = " ".join(lines[2:]).strip()
        spk = None
        sm = re.match(r"^([A-Z][a-z]+):\s*(.*)$", text)
        if sm:
            spk, text = sm.group(1), sm.group(2)
        cues.append({"start": start, "end": end, "spk": spk, "text": text})
    return cues


def transcript_for(ep_dir, ep):
    for name in ("transcript-attributed.srt", f"ep{ep}-final-cut.srt"):
        p = os.path.join(ep_dir, name)
        if os.path.exists(p):
            return parse_srt(p), name
    if ep == 17:
        p = os.path.join(ep_dir, "transcript.srt")
        if os.path.exists(p):
            return parse_srt(p), "transcript.srt"
    return [], None


def classify_category(title, text):
    """Keyword taxonomy: title hits weigh TITLE_WEIGHT, text hits are per 1,000 words."""
    t = title.lower()
    x = (text or "").lower()
    n_words = max(1, len(x.split()))
    best, best_score = "other", 0.0
    for cat, pat in CATEGORY_RULES.items():
        score = TITLE_WEIGHT * len(re.findall(pat, t)) + 1000.0 * len(re.findall(pat, x)) / n_words
        if score > best_score:
            best, best_score = cat, score
    return best


def classify_format(title):
    t = title.lower()
    for name, pat in FORMAT_RULES:
        if re.search(pat, t):
            return name
    return "segment"


def interp(curve, dur, key, t):
    xs = np.array([p["ratio"] * dur for p in curve])
    ys = np.array([(p.get(key) if p.get(key) is not None else np.nan) for p in curve], dtype=float)
    ok = ~np.isnan(ys)
    if ok.sum() < 2:
        return np.nan
    return float(np.interp(t, xs[ok], ys[ok]))


def mean_over(curve, dur, key, a, b):
    xs = np.array([p["ratio"] * dur for p in curve])
    ys = np.array([(p.get(key) if p.get(key) is not None else np.nan) for p in curve], dtype=float)
    sel = (xs >= a) & (xs < b) & ~np.isnan(ys)
    if sel.sum() == 0:
        mid = (a + b) / 2
        return interp(curve, dur, key, mid)
    return float(ys[sel].mean())


def build_segments(data, episodes_dir):
    eps = [v for v in data["videos"] if not v["is_short"] and v["privacyStatus"] == "public"
           and v["duration_s"] > MIN_EPISODE_S and v["retention"]]
    eps.sort(key=lambda v: v["publishedAt"])
    rows, ep_meta = [], []
    for n, v in enumerate(eps, 1):
        ep_dir = os.path.join(episodes_dir, f"ep{n}")
        chapters = parse_chapters(os.path.join(ep_dir, "segment-times.md"))
        cues, tname = transcript_for(ep_dir, n)
        dur = v["duration_s"]
        curve = v["retention"]
        has_spk = any(c["spk"] in SPEAKERS for c in cues)
        ep_meta.append({"ep": n, "id": v["id"], "title": v["title"], "published": v["publishedAt"][:10],
                        "duration_s": dur, "views": v["stats"]["views"],
                        "avg_view_pct": (v["analytics"] or {}).get("avg_view_pct"),
                        "chapters": len(chapters), "transcript": tname, "speakers": has_spk})
        for i, (start, title) in enumerate(chapters):
            end = chapters[i + 1][0] if i + 1 < len(chapters) else dur
            if end <= start:
                continue
            seg_cues = [c for c in cues if start <= (c["start"] + c["end"]) / 2 < end]
            words = Counter()
            n_words = 0
            switches = 0
            prev = None
            longest_run_s = 0.0
            run_start = None
            for c in seg_cues:
                w = len(c["text"].split())
                n_words += w
                if c["spk"] in SPEAKERS:
                    words[c["spk"]] += w
                    if prev is not None and c["spk"] != prev:
                        switches += 1
                        longest_run_s = max(longest_run_s, c["start"] - run_start)
                        run_start = c["start"]
                    if run_start is None:
                        run_start = c["start"]
                    prev = c["spk"]
            if run_start is not None and seg_cues:
                longest_run_s = max(longest_run_s, seg_cues[-1]["end"] - run_start)
            spoken = sum(words.values())
            mins = (end - start) / 60
            r0 = interp(curve, dur, "watch_ratio", max(start, 0.01 * dur))
            r1 = interp(curve, dur, "watch_ratio", min(end, 0.995 * dur))
            r0c = min(max(r0, 1e-3), 1.0)
            r1c = min(max(r1, 1e-3), 1.0)
            hazard = -math.log(r1c / r0c) / mins if mins > 0 else np.nan
            rows.append({
                "ep": n, "idx": i, "title": title, "format": classify_format(title),
                "start_s": start, "end_s": end, "len_min": mins, "pos": start / dur,
                "pos_end": end / dur, "ret_start": r0, "ret_end": r1,
                "hazard": hazard,
                "vs_typ": mean_over(curve, dur, "vs_typical", start, end),
                "n_words": n_words, "wpm": n_words / mins if mins > 0 else np.nan,
                "has_speakers": has_spk and spoken > 0,
                "share_jackson": words["Jackson"] / spoken if spoken else np.nan,
                "share_chris": words["Chris"] / spoken if spoken else np.nan,
                "share_tyler": words["Tyler"] / spoken if spoken else np.nan,
                "switches_per_min": switches / mins if (mins > 0 and spoken) else np.nan,
                "longest_turn_s": longest_run_s if spoken else np.nan,
                "text": " ".join(c["text"] for c in seg_cues),
            })
            rows[-1]["category"] = classify_category(title, rows[-1]["text"])
    return pd.DataFrame(rows), pd.DataFrame(ep_meta)


def topic_clusters(df, k=TOPIC_K, seed=7):
    """NMF over body chapters only (structural chapters would otherwise own half the topics)."""
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.decomposition import NMF
    mask = ~df["format"].isin(["title_card", "end_card", "cold_open", "welcome"])
    sub = df[mask]
    docs = (sub["title"] + " " + sub["title"] + " " + sub["text"].fillna("")).tolist()
    stop = "english"
    extra = {"yeah", "like", "just", "know", "right", "gonna", "think", "really", "thing", "things",
             "okay", "mean", "kind", "going", "got", "want", "say", "said", "people", "don", "ve",
             "ll", "oh", "um", "uh", "actually", "little", "lot", "way", "good", "yes", "stuff",
             "jackson", "chris", "tyler", "beats", "beat", "card", "title", "basically", "maybe",
             "did", "does", "doing", "use", "using", "come", "comes", "big", "pretty", "sure", "guys",
             "look", "looks", "cool", "wait", "yo", "dude", "man", "hey", "time", "day", "week", "year",
             "years", "money", "didn", "isn", "wasn", "doesn", "let", "lets", "need", "make", "makes",
             "point", "case", "talk", "talking", "episode", "pod", "podcast", "underpod", "permanent"}
    vec = TfidfVectorizer(stop_words=stop, min_df=3, max_df=0.6, ngram_range=(1, 2), sublinear_tf=True)
    X = vec.fit_transform(docs)
    for w in extra:
        if w in vec.vocabulary_:
            X[:, vec.vocabulary_[w]] = 0
    nmf = NMF(n_components=k, random_state=seed, init="nndsvda", max_iter=600)
    W = nmf.fit_transform(X)
    terms = np.array(vec.get_feature_names_out())
    tops = {c: terms[np.argsort(nmf.components_[c])[::-1][:12]].tolist() for c in range(k)}
    labels = np.full(len(df), -1)
    lab = W.argmax(axis=1)
    lab = np.where(W.max(axis=1) < 1e-6, -1, lab)
    labels[np.where(mask.values)[0]] = lab
    return labels, tops


def wmean(x, w):
    x, w = np.asarray(x, float), np.asarray(w, float)
    ok = ~np.isnan(x) & ~np.isnan(w)
    return float(np.sum(x[ok] * w[ok]) / np.sum(w[ok])) if w[ok].sum() > 0 else np.nan


def boot_ci(x, w, n=2000, seed=1):
    x, w = np.asarray(x, float), np.asarray(w, float)
    ok = ~np.isnan(x)
    x, w = x[ok], w[ok]
    if len(x) < 3:
        return (np.nan, np.nan)
    rng = np.random.default_rng(seed)
    idx = rng.integers(0, len(x), size=(n, len(x)))
    ms = (x[idx] * w[idx]).sum(1) / w[idx].sum(1)
    return (float(np.percentile(ms, 5)), float(np.percentile(ms, 95)))


def group_table(df, col, w="len_min"):
    out = []
    for g, sub in df.groupby(col):
        lo, hi = boot_ci(sub["vs_typ"], sub[w])
        out.append({col: g, "n": len(sub), "minutes": round(sub["len_min"].sum(), 1),
                    "vs_typ": round(wmean(sub["vs_typ"], sub[w]), 3),
                    "vs_typ_ci90": f"{lo:.2f}–{hi:.2f}",
                    "hazard_per_min": round(wmean(sub["hazard"], sub[w]), 4),
                    "median_len_min": round(sub["len_min"].median(), 1),
                    "mean_pos": round(sub["pos"].mean(), 2)})
    return pd.DataFrame(out).sort_values("vs_typ", ascending=False)


def within_episode_demean(df, cols):
    d = df.copy()
    for c in cols:
        d[c + "_dm"] = d[c] - d.groupby("ep")[c].transform("mean")
    return d


def ridge_table(df, features, target, w="len_min"):
    from sklearn.linear_model import Ridge
    sub = df.dropna(subset=features + [target, w]).copy()
    if len(sub) < 20:
        return None, 0
    X = sub[features].values
    mu, sd = X.mean(0), X.std(0) + 1e-9
    Xs = (X - mu) / sd
    y = sub[target].values
    m = Ridge(alpha=1.0).fit(Xs, y, sample_weight=sub[w].values)
    # bootstrap coefficient CIs
    rng = np.random.default_rng(3)
    coefs = []
    for _ in range(500):
        idx = rng.integers(0, len(sub), len(sub))
        coefs.append(Ridge(alpha=1.0).fit(Xs[idx], y[idx], sample_weight=sub[w].values[idx]).coef_)
    coefs = np.array(coefs)
    lo, hi = np.percentile(coefs, 5, 0), np.percentile(coefs, 95, 0)
    rows = [{"feature": f, "coef_per_sd": round(c, 4), "ci90": f"{a:+.3f}…{b:+.3f}",
             "sd": round(s, 3)} for f, c, a, b, s in zip(features, m.coef_, lo, hi, sd)]
    return pd.DataFrame(rows).reindex(np.argsort(-np.abs(m.coef_))), len(sub)


def minute_into_segment(df, data_eps, episodes_dir):
    """Per-minute hazard binned by minute-into-chapter, chapters >= 4 min, pooled."""
    bins = defaultdict(list)
    eps = {v["id"]: v for v in data_eps}
    for _, r in df[(df["len_min"] >= 4) & (df["format"].isin(["segment", "marquee", "explainer", "perp"]))].iterrows():
        v = [e for e in data_eps if e["_ep"] == r["ep"]][0]
        curve, dur = v["retention"], v["duration_s"]
        t = r["start_s"]
        k = 0
        while t + 60 <= r["end_s"] and k < 15:
            a = interp(curve, dur, "watch_ratio", max(t, 0.01 * dur))
            b = interp(curve, dur, "watch_ratio", t + 60)
            if a > 0.005 and b > 0.005:
                bins[k].append(-math.log(min(b, 1) / min(a, 1)))
            t += 60
            k += 1
    rows = [{"minute_into_chapter": k + 1, "n": len(v), "hazard_per_min": round(float(np.mean(v)), 4),
             "median": round(float(np.median(v)), 4)} for k, v in sorted(bins.items())]
    return pd.DataFrame(rows)


def position_curve(df):
    sub = df[(df["format"].isin(["segment", "marquee", "explainer", "perp"])) & (df["len_min"] >= 1)]
    sub = sub.assign(decile=(sub["pos"] * 10).clip(0, 9).astype(int))
    return sub.groupby("decile").apply(
        lambda g: pd.Series({"n": len(g), "hazard_per_min": round(wmean(g["hazard"], g["len_min"]), 4),
                             "vs_typ": round(wmean(g["vs_typ"], g["len_min"]), 3)})).reset_index()


def merge_blocks(df):
    """Consecutive body chapters sharing a category = one topic block (true segment length)."""
    out = []
    for ep, g in df.sort_values(["ep", "start_s"]).groupby("ep"):
        g = g[~g["format"].isin(["title_card", "end_card", "cold_open", "welcome"])]
        cur = None
        for _, r in g.iterrows():
            key = (r["category"], r["format"] == "perp")
            if cur and cur["key"] == key and r["start_s"] - cur["end_s"] < 1:
                cur["end_s"] = r["end_s"]
                cur["chapters"] += 1
                cur["titles"].append(r["title"])
                cur["n_words"] += r["n_words"]
                for h in ("jackson", "chris", "tyler"):
                    if not np.isnan(r[f"share_{h}"]):
                        cur[f"w_{h}"] += r[f"share_{h}"] * r["n_words"]
            else:
                if cur:
                    out.append(cur)
                cur = {"ep": ep, "key": key, "category": r["category"], "is_perp": r["format"] == "perp",
                       "start_s": r["start_s"], "end_s": r["end_s"], "chapters": 1, "titles": [r["title"]],
                       "n_words": r["n_words"], "w_jackson": 0.0, "w_chris": 0.0, "w_tyler": 0.0}
                for h in ("jackson", "chris", "tyler"):
                    if not np.isnan(r[f"share_{h}"]):
                        cur[f"w_{h}"] += r[f"share_{h}"] * r["n_words"]
        if cur:
            out.append(cur)
    return out


def enrich_blocks(blocks, eps):
    rows = []
    byep = {v["_ep"]: v for v in eps}
    for b in blocks:
        v = byep[b["ep"]]
        curve, dur = v["retention"], v["duration_s"]
        mins = (b["end_s"] - b["start_s"]) / 60
        r0 = interp(curve, dur, "watch_ratio", max(b["start_s"], 0.01 * dur))
        r1 = interp(curve, dur, "watch_ratio", min(b["end_s"], 0.995 * dur))
        r0c, r1c = min(max(r0, 1e-3), 1.0), min(max(r1, 1e-3), 1.0)
        tot = b["w_jackson"] + b["w_chris"] + b["w_tyler"]
        rows.append({"ep": b["ep"], "category": b["category"], "is_perp": b["is_perp"],
                     "start_s": b["start_s"], "len_min": mins, "pos": b["start_s"] / dur,
                     "chapters": b["chapters"], "title": b["titles"][0][:80],
                     "ret_start": r0, "ret_end": r1,
                     "hazard": -math.log(r1c / r0c) / mins if mins > 0 else np.nan,
                     "vs_typ": mean_over(curve, dur, "vs_typical", b["start_s"], b["end_s"]),
                     "share_jackson": b["w_jackson"] / tot if tot else np.nan,
                     "share_chris": b["w_chris"] / tot if tot else np.nan,
                     "share_tyler": b["w_tyler"] / tot if tot else np.nan,
                     "format": "perp" if b["is_perp"] else "segment"})
    return pd.DataFrame(rows)


def opening_table(df, eps):
    """What the first six minutes contain, and what was left at 1:05 and 6:00."""
    rows = []
    byep = {v["_ep"]: v for v in eps}
    for ep, g in df.groupby("ep"):
        v = byep[ep]
        curve, dur = v["retention"], v["duration_s"]
        g = g.sort_values("start_s")
        def first(fmt):
            s = g[g["format"] == fmt]
            return float(s.iloc[0]["start_s"]) if len(s) else np.nan
        welcome = g[g["format"] == "welcome"]
        body = g[~g["format"].isin(["cold_open", "title_card", "welcome", "end_card"])]
        co = g[g["format"] == "cold_open"]
        r = {"ep": ep, "cold_open_s": round(float(co.iloc[0]["end_s"]), 0) if len(co) else np.nan,
             "welcome_s": round(float(welcome.iloc[0]["end_s"] - welcome.iloc[0]["start_s"]), 0) if len(welcome) else np.nan,
             "first_body_at": round(float(body.iloc[0]["start_s"]), 0) if len(body) else np.nan,
             "first_body": body.iloc[0]["title"][:50] if len(body) else "",
             "first_body_cat": body.iloc[0]["category"] if len(body) else "",
             "perp_at": first("perp"), "marquee_at": first("marquee"),
             "ret_0_32": round(min(1.0, interp(curve, dur, "watch_ratio", 32)) * 100, 1),
             "ret_1_05": round(interp(curve, dur, "watch_ratio", 65) * 100, 1),
             "ret_6_00": round(interp(curve, dur, "watch_ratio", 360) * 100, 1),
             "ret_12_00": round(interp(curve, dur, "watch_ratio", 720) * 100, 1),
             "avg_view_pct": (v["analytics"] or {}).get("avg_view_pct")}
        r["kept_1_05_to_6"] = round(r["ret_6_00"] / r["ret_1_05"], 2) if r["ret_1_05"] else np.nan
        rows.append(r)
    return pd.DataFrame(rows)


def episode_table(meta, daily):
    rows = []
    for _, m in meta.iterrows():
        r = {"ep": m["ep"], "published": m["published"], "min": round(m["duration_s"] / 60),
             "views": m["views"], "avg_view_pct": m["avg_view_pct"], "chapters": m["chapters"],
             "speakers": "Y" if m["speakers"] else "-"}
        d = daily.get(f"ep{m['ep']}") if daily else None
        if d:
            rows_d = sorted(d["rows"], key=lambda x: x["day"])
            v7 = sum(x["views"] for x in rows_d[:7])
            v14 = sum(x["views"] for x in rows_d[:14])
            r.update({"d0": rows_d[0]["views"] if rows_d else 0, "d1": rows_d[1]["views"] if len(rows_d) > 1 else 0,
                      "d2": rows_d[2]["views"] if len(rows_d) > 2 else 0,
                      "views_d7": v7, "views_d14": v14,
                      "share_d7": round(v7 / max(1, m["views"]), 2)})
            src = d.get("sources", {})
            tot = sum(x[0] for x in src.values()) or 1
            r["subscriber_share"] = round(src.get("SUBSCRIBER", [0])[0] / tot, 2)
            r["search_share"] = round(src.get("YT_SEARCH", [0])[0] / tot, 2)
            r["browse_share"] = round(src.get("YT_OTHER_PAGE", [0])[0] / tot, 2)
        rows.append(r)
    return pd.DataFrame(rows)


def main():
    args = sys.argv[1:]
    daily_path = None
    if "--daily" in args:
        i = args.index("--daily")
        daily_path = args[i + 1]
        del args[i:i + 2]
    exclude = set()
    if "--exclude" in args:
        i = args.index("--exclude")
        exclude = {int(x) for x in args[i + 1].split(",") if x}
        del args[i:i + 2]
    data_path, episodes_dir, out_dir = args[0], args[1], args[2]
    os.makedirs(out_dir, exist_ok=True)
    data = json.load(open(data_path))
    daily = json.load(open(daily_path)) if daily_path and os.path.exists(daily_path) else None

    df, meta = build_segments(data, episodes_dir)
    eps = [v for v in data["videos"] if not v["is_short"] and v["privacyStatus"] == "public"
           and v["duration_s"] > MIN_EPISODE_S and v["retention"]]
    eps.sort(key=lambda v: v["publishedAt"])
    for n, v in enumerate(eps, 1):
        v["_ep"] = n
    if exclude:
        print(f"excluding episodes {sorted(exclude)} (bot-traffic episodes; see study.md §7)")
        df = df[~df["ep"].isin(exclude)].copy()
        eps = [v for v in eps if v["_ep"] not in exclude]

    labels, tops = topic_clusters(df)
    df["topic"] = labels
    body = df[(df["len_min"] >= MIN_CHAPTER_S / 60) & (~df["format"].isin(["title_card", "end_card", "cold_open"]))]

    results = {
        "n_episodes": int(df["ep"].nunique()),
        "n_chapters": int(len(df)),
        "n_body_chapters": int(len(body)),
        "n_with_speakers": int(body["has_speakers"].sum()),
        "topic_terms": tops,
        "format": group_table(body, "format").to_dict("records"),
        "topic": group_table(body[body["topic"] >= 0], "topic").to_dict("records"),
        "position_deciles": position_curve(df).to_dict("records"),
        "minute_into_chapter": minute_into_segment(df, eps, episodes_dir).to_dict("records"),
    }

    spk = body[body["has_speakers"]].copy()
    spk["dominant"] = spk[["share_jackson", "share_chris", "share_tyler"]].idxmax(axis=1).str.replace("share_", "")
    spk["dominance"] = spk[["share_jackson", "share_chris", "share_tyler"]].max(axis=1)
    spk["crosstalk"] = pd.cut(spk["switches_per_min"], [0, 2, 4, 100], labels=["low<2", "mid2-4", "high>4"], include_lowest=True)
    spk["len_bucket"] = pd.cut(spk["len_min"], [0, 2, 4, 7, 100], labels=["<2", "2-4", "4-7", "7+"])
    body2 = body.assign(len_bucket=pd.cut(body["len_min"], [0, 2, 4, 7, 100], labels=["<2", "2-4", "4-7", "7+"]))
    results["category"] = group_table(body, "category").to_dict("records")
    blocks = enrich_blocks(merge_blocks(df), eps)
    blocks["len_bucket"] = pd.cut(blocks["len_min"], [0, 3, 6, 10, 100], labels=["<3", "3-6", "6-10", "10+"])
    results["block_length"] = group_table(blocks, "len_bucket").to_dict("records")
    results["block_category"] = group_table(blocks[~blocks["is_perp"]], "category").to_dict("records")
    blocks.to_csv(os.path.join(out_dir, "blocks.csv"), index=False)
    results["opening"] = opening_table(df, eps).to_dict("records")
    # category x position half: does the same content do worse early?
    body_h = body.assign(half=np.where(body["pos"] < 0.33, "first_third", "later"))
    results["category_by_third"] = [
        {"category": c, "half": h, "n": int(len(g)), "vs_typ": round(wmean(g["vs_typ"], g["len_min"]), 3),
         "hazard": round(wmean(g["hazard"], g["len_min"]), 4)}
        for (c, h), g in body_h.groupby(["category", "half"]) if len(g) >= 4]
    results["dominant_speaker"] = group_table(spk, "dominant").to_dict("records")
    results["crosstalk"] = group_table(spk, "crosstalk").to_dict("records")
    results["length_bucket"] = group_table(body2, "len_bucket").to_dict("records")
    results["topic_by_host"] = [
        {"topic": int(t), "dominant": d, "n": int(len(g)), "vs_typ": round(wmean(g["vs_typ"], g["len_min"]), 3)}
        for (t, d), g in spk[spk["topic"] >= 0].groupby(["topic", "dominant"]) if len(g) >= 3]

    feats = ["pos", "len_min", "wpm", "switches_per_min", "share_jackson", "share_chris", "share_tyler", "dominance", "longest_turn_s"]
    spk_dm = within_episode_demean(spk, feats + ["vs_typ", "hazard"])
    for target in ("vs_typ", "hazard"):
        tbl, n = ridge_table(spk_dm, [f + "_dm" for f in feats], target + "_dm")
        results[f"ridge_{target}_within_episode"] = {"n": n, "coefs": tbl.to_dict("records") if tbl is not None else []}

    etab = episode_table(meta, daily)
    results["episodes"] = etab.to_dict("records")

    # per-episode worst and best chapters by vs_typ (>= 2 min)
    wb = []
    for ep, g in body[body["len_min"] >= 2].groupby("ep"):
        g = g.sort_values("vs_typ")
        wb.append({"ep": int(ep), "worst": g.iloc[0]["title"][:70], "worst_vs": round(g.iloc[0]["vs_typ"], 2),
                   "worst_at": f"{int(g.iloc[0]['start_s']//60)}:{int(g.iloc[0]['start_s']%60):02d}",
                   "best": g.iloc[-1]["title"][:70], "best_vs": round(g.iloc[-1]["vs_typ"], 2),
                   "best_at": f"{int(g.iloc[-1]['start_s']//60)}:{int(g.iloc[-1]['start_s']%60):02d}"})
    results["per_episode_extremes"] = wb

    df["category_display"] = df["category"]
    df.drop(columns=["text"]).to_csv(os.path.join(out_dir, "segments.csv"), index=False)
    df[["ep", "idx", "title", "topic", "text"]].to_json(os.path.join(out_dir, "segment-text.json"), orient="records")
    json.dump(results, open(os.path.join(out_dir, "results.json"), "w"), indent=1, default=str)

    def show(name, recs):
        print(f"\n== {name}")
        if recs:
            print(pd.DataFrame(recs).to_string(index=False))
    print(f"episodes {results['n_episodes']}  chapters {results['n_chapters']}  body {results['n_body_chapters']}  with speakers {results['n_with_speakers']}")
    for k, v in tops.items():
        n = int((df["topic"] == k).sum())
        print(f"topic {k} (n={n}): {', '.join(v)}")
    for name in ("format", "category", "topic", "position_deciles", "minute_into_chapter", "dominant_speaker",
                 "crosstalk", "length_bucket", "block_length", "block_category", "category_by_third",
                 "topic_by_host", "opening", "episodes", "per_episode_extremes"):
        show(name, results[name])
    for t in ("vs_typ", "hazard"):
        r = results[f"ridge_{t}_within_episode"]
        show(f"ridge {t} (within-episode, n={r['n']})", r["coefs"])


if __name__ == "__main__":
    main()
