"""Figure for docs/08-financial-math/02-interest-and-growth/05-doubling-time-rule-of-72-and-logs.md.

Run from the repo root:

    .venv/Scripts/python tools/figures/08-financial-math/doubling-time-rule-of-72-and-logs.py
"""

import sys
from math import log
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import figstyle as fs  # noqa: E402

FOLDER = "08-financial-math"
SLUG = "doubling-time-rule-of-72-and-logs"
BOX = dict(facecolor="white", edgecolor="none", pad=0.4, alpha=0.9)


def frange(a, b, n=400):
    return [a + (b - a) * i / n for i in range(n + 1)]


def rate_times_time():
    """R times the exact doubling time, against the constants 69.3, 70 and 72."""
    fig, ax = fs.figure(5.6, 3.8)
    rs = frange(0.2, 30)
    ax.plot(rs, [R * log(2) / log(1 + R / 100) for R in rs], color=fs.GREEN, zorder=5)
    for c, col in ((72, fs.RED), (70, fs.ORANGE), (69.3, fs.BLUE)):
        ax.axhline(c, color=col, lw=1.2, ls="--", zorder=3)
    ax.plot([7.85], [72], "o", color=fs.DARK, ms=6, zorder=6)
    ax.set_xlim(0, 36)
    ax.set_ylim(68, 80.5)
    ax.set_xticks([0, 5, 10, 15, 20, 25, 30])
    ax.set_yticks([70, 72, 74, 76, 78, 80])
    ax.set_yticklabels(["70", "72", "74", "76", "78", "80"])
    ax.set_xlabel("rate R (percent per period)")
    ax.set_ylabel("R times the exact doubling time")
    ax.grid(True)
    ax.set_axisbelow(True)
    ax.text(30.6, 72, "rule of 72", color=fs.RED, fontsize=9, ha="left", va="bottom")
    ax.text(30.6, 70.1, "rule of 70", color=fs.ORANGE, fontsize=9, ha="left", va="bottom")
    ax.text(30.6, 69.3, "69.3", color=fs.BLUE, fontsize=9, ha="left", va="top")
    ax.text(17, 77.6, "exact: $R \\cdot \\ln 2 \\,/\\, \\ln(1 + R/100)$", color=fs.GREEN, fontsize=10, ha="center",
            va="center", bbox=BOX)
    ax.annotate("rule of 72 is exact at R = 7.85", xy=(7.85, 72), xytext=(11, 70.8), color=fs.DARK, fontsize=9,
                ha="left", va="center", arrowprops=dict(arrowstyle="-", color=fs.GRAY, lw=1.0))
    fs.save(fig, FOLDER, f"{SLUG}-rate-times-time")


if __name__ == "__main__":
    rate_times_time()
