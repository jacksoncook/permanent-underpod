#!/usr/bin/env python
"""Charts for the cross-episode study (reads analytics/study/*.{json,csv} + channel-data.json).

Usage:
  analytics/.venv/bin/python .claude/skills/channel-analytics/scripts/study_charts.py \
      analytics/channel-data.json analytics/study
"""
import json
import os
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

SURFACE = "#17171f"
PANEL = "#26262f"
INK = "#f2f2f5"
MUTED = "#9a9aa8"
GRID = "#2a2a35"
BLUE = "#4a94d0"
GOLD = "#b08a1e"
MIN_EPISODE_S = 2400


def style(ax, title, ylabel=None, xlabel=None):
    ax.set_facecolor(SURFACE)
    ax.figure.set_facecolor(SURFACE)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    for s in ("left", "bottom"):
        ax.spines[s].set_color(GRID)
    ax.tick_params(colors=MUTED, labelsize=9)
    ax.yaxis.grid(True, color=GRID, linewidth=0.8)
    ax.set_axisbelow(True)
    ax.set_title(title, color=INK, fontsize=12, loc="left", pad=12)
    if ylabel:
        ax.set_ylabel(ylabel, color=MUTED, fontsize=9)
    if xlabel:
        ax.set_xlabel(xlabel, color=MUTED, fontsize=9)


def first_12_minutes(data, out):
    eps = [v for v in data["videos"] if not v["is_short"] and v["privacyStatus"] == "public"
           and v["duration_s"] > MIN_EPISODE_S and v["retention"]]
    eps.sort(key=lambda v: v["publishedAt"])
    fig, ax = plt.subplots(figsize=(10, 5.2), dpi=160)
    t = np.arange(0, 721, 10)
    for n, v in enumerate(eps, 1):
        dur = v["duration_s"]
        xs = np.array([p["ratio"] * dur for p in v["retention"]])
        ys = np.minimum(1.0, np.array([p["watch_ratio"] for p in v["retention"]])) * 100
        y = np.interp(t, xs, ys)
        perp_first = n >= 15 or n == 12
        ax.plot(t / 60, y, color=GOLD if perp_first else BLUE, linewidth=2 if perp_first else 1.2,
                alpha=0.95 if perp_first else 0.45)
    style(ax, "The first 12 minutes of every episode: ~60% of the opening audience is gone by minute 6",
          ylabel="% of starting viewers still watching", xlabel="minutes into the episode")
    ax.set_xlim(0, 13)
    ax.set_ylim(0, 100)
    ax.plot([], [], color=GOLD, linewidth=2, label="perp opens the show (Ep 12, 15–19)")
    ax.plot([], [], color=BLUE, linewidth=1.2, label="other openings (Ep 1–11, 13–14)")
    leg = ax.legend(loc="upper right", frameon=False, fontsize=8)
    for txt in leg.get_texts():
        txt.set_color(INK)
    fig.tight_layout()
    fig.savefig(os.path.join(out, "first-12-minutes.png"))
    plt.close(fig)


def hazard_by_decile(results, out):
    rows = results["position_deciles"]
    fig, ax = plt.subplots(figsize=(8, 4.2), dpi=160)
    x = [r["decile"] for r in rows]
    y = [r["hazard_per_min"] * 100 for r in rows]
    bars = ax.bar(x, y, color=BLUE, width=0.72)
    for b, val in zip(bars, y):
        ax.text(b.get_x() + b.get_width() / 2, b.get_height() + 0.15, f"{val:.1f}", ha="center",
                color=INK, fontsize=8)
    style(ax, "Per-minute audience loss by tenth of the runtime (all 19 episodes, body chapters)",
          ylabel="% of remaining viewers lost per minute", xlabel="tenth of the episode (0 = first 10%)")
    ax.set_xticks(x)
    fig.tight_layout()
    fig.savefig(os.path.join(out, "loss-by-position.png"))
    plt.close(fig)


def block_length(results, out):
    rows = results["block_length"]
    order = ["<3", "3-6", "6-10", "10+"]
    rows = sorted(rows, key=lambda r: order.index(str(r["len_bucket"])))
    fig, ax = plt.subplots(figsize=(8, 4.2), dpi=160)
    x = np.arange(len(rows))
    y = [r["vs_typ"] for r in rows]
    bars = ax.bar(x, y, color=BLUE, width=0.72)
    for b, r in zip(bars, rows):
        ax.text(b.get_x() + b.get_width() / 2, b.get_height() + 0.01,
                f"{r['vs_typ']:.2f}  (n={r['n']})", ha="center", color=INK, fontsize=8)
    ax.axhline(0.5, color=GOLD, linewidth=1, linestyle="--")
    ax.text(len(rows) - 0.5, 0.505, "YouTube 'typical' = 0.50", color=GOLD, fontsize=8, ha="right", va="bottom")
    style(ax, "Longer topic blocks hold viewers better (relative retention vs YouTube typical)",
          ylabel="mean relative retention (0.5 = typical)", xlabel="topic block length, minutes")
    ax.set_xticks(x)
    ax.set_xticklabels([str(r["len_bucket"]) for r in rows], color=MUTED)
    ax.set_ylim(0, 0.6)
    fig.tight_layout()
    fig.savefig(os.path.join(out, "block-length.png"))
    plt.close(fig)


def category_by_third(results, out):
    rows = pd.DataFrame(results["category_by_third"])
    piv = rows.pivot(index="category", columns="half", values="vs_typ").dropna()
    piv = piv.sort_values("later")
    fig, ax = plt.subplots(figsize=(9, 5), dpi=160)
    y = np.arange(len(piv))
    ax.hlines(y, piv["first_third"], piv["later"], color=GRID, linewidth=2)
    ax.scatter(piv["first_third"], y, color=GOLD, s=60, zorder=3, label="placed in the first third")
    ax.scatter(piv["later"], y, color=BLUE, s=60, zorder=3, label="placed later")
    ax.set_yticks(y)
    ax.set_yticklabels([c.replace("_", " ") for c in piv.index], color=INK, fontsize=9)
    ax.axvline(0.5, color=MUTED, linewidth=0.8, linestyle="--")
    style(ax, "Same topic, different slot: relative retention by content type and placement",
          xlabel="mean relative retention (0.5 = typical)")
    ax.xaxis.grid(True, color=GRID, linewidth=0.8)
    ax.yaxis.grid(False)
    leg = ax.legend(loc="lower right", frameon=False, fontsize=8)
    for txt in leg.get_texts():
        txt.set_color(INK)
    fig.tight_layout()
    fig.savefig(os.path.join(out, "category-by-placement.png"))
    plt.close(fig)


def main():
    data = json.load(open(sys.argv[1]))
    out = sys.argv[2]
    results = json.load(open(os.path.join(out, "results.json")))
    first_12_minutes(data, out)
    hazard_by_decile(results, out)
    block_length(results, out)
    category_by_third(results, out)
    print("wrote 4 charts to", out)


if __name__ == "__main__":
    main()
