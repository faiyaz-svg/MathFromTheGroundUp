"""Figure for docs/08-financial-math/02-interest-and-growth/02-compound-interest.md.

Run from the repo root:

    .venv/Scripts/python tools/figures/08-financial-math/compound-interest.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import figstyle as fs  # noqa: E402

FOLDER = "08-financial-math"
SLUG = "compound-interest"
BOX = dict(facecolor="white", edgecolor="none", pad=0.4, alpha=0.9)


def frange(a, b, n=400):
    return [a + (b - a) * i / n for i in range(n + 1)]


def simple_vs_compound():
    """1000 dollars at 5% a year: simple interest against annual compounding."""
    fig, ax = fs.figure(5.4, 3.8)
    ts = frange(0, 30)
    simple = [1000 + 50 * t for t in ts]
    comp = [1000 * 1.05**t for t in ts]
    ax.fill_between(ts, simple, comp, color=fs.LIGHT, zorder=1)
    ax.plot(ts, simple, color=fs.BLUE, zorder=4)
    ax.plot(ts, comp, color=fs.GREEN, zorder=4)
    ax.plot([30, 30], [2500, 4321.94], "o", color=fs.DARK, ms=6, zorder=6)
    ax.set_xlim(0, 36)
    ax.set_ylim(0, 4800)
    ax.set_xticks([0, 5, 10, 15, 20, 25, 30])
    ax.set_yticks([0, 1000, 2000, 3000, 4000])
    ax.set_yticklabels(["0", "1,000", "2,000", "3,000", "4,000"])
    ax.set_xlabel("years t")
    ax.set_ylabel("balance (dollars)")
    ax.grid(True)
    ax.set_axisbelow(True)
    ax.text(12, 1400, "simple: $1000 + 50t$", color=fs.BLUE, fontsize=10, ha="left", va="center", bbox=BOX)
    ax.text(10, 3300, "compound: $1000 \\cdot 1.05^t$", color=fs.GREEN, fontsize=10, ha="left", va="center",
            bbox=BOX)
    ax.text(30.6, 2500, "\\$2,500", color=fs.DARK, fontsize=9, ha="left", va="center")
    ax.text(29.5, 4321.94, "\\$4,321.94", color=fs.DARK, fontsize=9, ha="right", va="bottom")
    ax.text(30.6, 3500, "interest\non interest", color=fs.GRAY, fontsize=8.5, ha="left", va="center")
    fs.save(fig, FOLDER, f"{SLUG}-simple-vs-compound")


if __name__ == "__main__":
    simple_vs_compound()
