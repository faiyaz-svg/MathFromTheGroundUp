"""Figure for docs/06-cs-math/01-number-representation/04-floating-point-basics.md.

A toy float format with 3 fraction bits: the numbers (1 + k/8) * 2^e for k = 0..7 and e = 0..3.
Run from the repo root:

    .venv/Scripts/python tools/figures/06-cs-math/floating-point-basics.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import figstyle as fs  # noqa: E402

FOLDER = "06-cs-math"
SLUG = "floating-point-basics"


def spacing():
    """Positive toy floats on a number line; the gap doubles at each power of 2."""
    fig, ax = fs.figure(6.4, 2.9)
    colours = [fs.GREEN, fs.BLUE, fs.ORANGE, fs.RED]
    for e, colour in enumerate(colours):
        lo = 2**e
        gap = lo / 8
        xs = [lo + k * gap for k in range(8)]
        for x in xs:
            ax.plot([x, x], [0, 1], color=colour, lw=1.6, solid_capstyle="butt")
        ax.annotate("", xy=(lo + gap, 1.25), xytext=(lo, 1.25),
                    arrowprops=dict(arrowstyle="<->", color=colour, lw=1.0, shrinkA=0, shrinkB=0))
        label = f"gap {gap:g}" if gap >= 1 else f"gap 1/{round(1 / gap)}"
        ytxt = [3.2, 2.4, 1.75, 1.75][e]
        ax.text(lo + 4 * gap, ytxt, label, color=colour, fontsize=9, ha="center", va="bottom")
        if e < 2:
            ax.plot([lo + 4 * gap] * 2, [1.3, ytxt], color=colour, lw=0.7)
        ydn = [-1.5, -0.55, -0.55, -0.55][e]
        ax.text(lo + 4 * gap, ydn, f"[{lo}, {2 * lo})", color=colour, fontsize=9, ha="center", va="top")
        if e == 0:
            ax.plot([lo + 4 * gap] * 2, [-0.05, ydn], color=colour, lw=0.7)
    ax.plot([0], [0.5], "o", color=fs.DARK, ms=5)
    ax.plot([0, 1], [0.5, 0.5], color=fs.GRAY, lw=1.0, ls=":")
    ax.spines["left"].set_visible(False)
    ax.set_yticks([])
    ax.set_xlim(-0.5, 16.5)
    ax.set_ylim(-2.2, 4.0)
    ax.set_xticks([0, 1, 2, 4, 8, 16])
    ax.set_xlabel("value")
    fs.save(fig, FOLDER, f"{SLUG}-spacing")


if __name__ == "__main__":
    spacing()
