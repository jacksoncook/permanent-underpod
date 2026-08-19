"""Perp of Fortune research loop: GLM 4.7 Flash (local ollama) + live Hyperliquid data.

The model gets a small tool protocol, runs its own research rounds, then must
commit to one pick. Full transcript written to stdout + file.
"""
import json
import time
import urllib.request

HL = "https://api.hyperliquid.xyz/info"
OLLAMA = "http://localhost:11434/api/chat"
MODEL = "glm-4.7-flash:latest"
BANNED = {"BTC", "PUMP"}
MAX_TOOL_ROUNDS = 5


def hl(payload):
    req = urllib.request.Request(HL, json.dumps(payload).encode(),
                                 {"Content-Type": "application/json"})
    return json.loads(urllib.request.urlopen(req, timeout=30).read())


print("fetching market snapshot...", flush=True)
meta, ctxs = hl({"type": "metaAndAssetCtxs"})
COINS = {}
for asset, ctx in zip(meta["universe"], ctxs):
    if asset.get("isDelisted"):
        continue
    name = asset["name"]
    mark, prev = float(ctx["markPx"]), float(ctx["prevDayPx"] or 0)
    COINS[name] = {
        "mark": mark,
        "chg24h_pct": round((mark - prev) / prev * 100, 2) if prev else None,
        "funding_hourly_pct": round(float(ctx["funding"]) * 100, 5),
        "open_interest_usd": round(float(ctx["openInterest"]) * mark),
        "vol24h_usd": round(float(ctx["dayNtlVlm"])),
        "max_leverage": asset["maxLeverage"],
    }
print(f"{len(COINS)} live perps", flush=True)


def market_overview():
    rows = [(k, v) for k, v in COINS.items() if v["chg24h_pct"] is not None]
    fmt = lambda k, v: f"{k}: 24h {v['chg24h_pct']:+.1f}%, funding {v['funding_hourly_pct']:+.4f}%/hr, OI ${v['open_interest_usd']:,}, vol ${v['vol24h_usd']:,}"
    out = ["TOP 10 BY 24H VOLUME:"]
    out += [fmt(k, v) for k, v in sorted(rows, key=lambda r: -r[1]["vol24h_usd"])[:10]]
    out.append("\nTOP 10 GAINERS (24h):")
    out += [fmt(k, v) for k, v in sorted(rows, key=lambda r: -r[1]["chg24h_pct"])[:10]]
    out.append("\nTOP 10 LOSERS (24h):")
    out += [fmt(k, v) for k, v in sorted(rows, key=lambda r: r[1]["chg24h_pct"])[:10]]
    out.append("\nMOST EXTREME FUNDING (longs pay + / shorts pay -):")
    out += [fmt(k, v) for k, v in sorted(rows, key=lambda r: -abs(r[1]["funding_hourly_pct"]))[:10]]
    return "\n".join(out)


def coin_stats(ticker):
    t = ticker.upper().strip()
    if t not in COINS:
        return f"ERROR: {t} is not a live Hyperliquid perp."
    v = dict(COINS[t])
    now = int(time.time() * 1000)
    try:
        candles = hl({"type": "candleSnapshot", "req": {
            "coin": t, "interval": "1d",
            "startTime": now - 8 * 86400_000, "endTime": now}})
        closes = [float(c["c"]) for c in candles]
        if len(closes) >= 2:
            v["chg7d_pct"] = round((closes[-1] - closes[0]) / closes[0] * 100, 2)
        v["daily_closes_last_week"] = [round(c, 6) for c in closes]
    except Exception as e:
        v["candles"] = f"unavailable ({e})"
    return f"{t}: " + json.dumps(v)


SYSTEM = """You are this week's guest picker on "Perp of Fortune," a recurring bit on a Bitcoin/stablecoins/AI podcast. The hosts run a tiny real-money entertainment account on Hyperliquid; an AI picks one leveraged perp each episode. Last week's pick (long PUMP 10x) drew down -61.6% and survived at -$36. Record: 3 wins, 1 open loser.

You are GLM, running locally as open weights on the host's machine. This time you must DO YOUR OWN RESEARCH before picking, using these tools. To call a tool, reply with EXACTLY one line and nothing else:
TOOL: market_overview
TOOL: coin_stats <TICKER>

Rules:
- Up to 5 tool calls total. Use them — do not pick blind.
- BANNED picks: BTC (house rule, the show never does BTC price talk) and PUMP (position still open).
- When (and only when) you are ready, give your final answer in EXACTLY this format:
PICK: <ticker>
DIRECTION: <long|short>
LEVERAGE: <number>x
RESEARCH BASIS: <2-3 sentences citing the actual numbers you pulled>
REASONING: <2-3 sentences, entertainment-grade, in your own voice — this is a comedy bit with real (tiny) money>
ONE-LINER FOR THE HOSTS: <a single spicy line to read on air>"""


def chat(messages):
    req = urllib.request.Request(OLLAMA, json.dumps({
        "model": MODEL, "messages": messages, "stream": False,
        "options": {"num_ctx": 16384},
    }).encode(), {"Content-Type": "application/json"})
    msg = json.loads(urllib.request.urlopen(req, timeout=600).read())["message"]
    return msg.get("thinking") or "", msg.get("content") or ""


messages = [{"role": "system", "content": SYSTEM},
            {"role": "user", "content": "The board is live. Do your research, then pick."}]
transcript = []

for rnd in range(MAX_TOOL_ROUNDS + 1):
    thinking, content = chat(messages)
    transcript.append({"round": rnd, "thinking": thinking, "content": content})
    print(f"\n===== ROUND {rnd} MODEL OUTPUT =====\n{content}", flush=True)
    messages.append({"role": "assistant", "content": content})
    calls = [l.split("TOOL:", 1)[1].strip() for l in content.splitlines()
             if l.strip().startswith("TOOL:")]
    if calls and rnd < MAX_TOOL_ROUNDS:
        results = []
        for call in calls:
            if call == "market_overview":
                results.append(market_overview())
            elif call.startswith("coin_stats"):
                arg = call.split(None, 1)[1] if len(call.split()) > 1 else ""
                results.append(coin_stats(arg))
            else:
                results.append(f"ERROR: unknown tool '{call}'")
        result = "\n\n".join(f"[{c}]\n{r}" for c, r in zip(calls, results))
        print(f"\n----- TOOL RESULTS ({', '.join(calls)}) -----\n{result[:1200]}...", flush=True)
        messages.append({"role": "user", "content": f"TOOL RESULTS:\n{result}\n\nResearch rounds used: {rnd + 1}/{MAX_TOOL_ROUNDS}. Continue researching or give your final answer."})
    elif "PICK:" in content:
        pick = content.split("PICK:", 1)[1].split()[0].strip().upper().strip("*`")
        if pick in BANNED:
            messages.append({"role": "user", "content": f"{pick} is BANNED. Pick something else, final answer format."})
            continue
        break
    else:
        messages.append({"role": "user", "content": "That was neither a valid TOOL line nor a final answer. Give one or the other."})

with open("/Users/jcook/Personal/permanent-underpod/episodes/ep11/perp-pick-glm-v2-raw.json", "w") as f:
    json.dump(transcript, f, indent=2)
print("\ntranscript saved: episodes/ep11/perp-pick-glm-v2-raw.json", flush=True)
