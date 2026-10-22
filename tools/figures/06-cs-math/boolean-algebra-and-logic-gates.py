"""Figure for docs/06-cs-math/01-number-representation/06-boolean-algebra-and-logic-gates.md.

A 3-variable Karnaugh map for f = m(0, 2, 3, 4, 6) with its two groups.
Run from the repo root:

    .venv/Scripts/python tools/figures/06-cs-math/boolean-algebra-and-logic-gates.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import matplotlib.patches as mp  # noqa: E402

import figstyle as fs  # noqa: E402

FOLDER = "06-cs-math"
SLUG = "boolean-algebra-and-logic-gates"

MINTERMS = {0, 2, 3, 4, 6}
COLS = ["00", "01", "11", "10"]  # Gray code order of QR


def kmap():
    fig, ax = fs.figure(5.2, 3.3)
    for p in (0, 1):
        for c, qr in enumerate(COLS):
            q, r = int(qr[0]), int(qr[1])
            m = p * 4 + q * 2 + r
            y = 1 - p
            ax.add_patch(mp.Rectangle((c, y), 1, 1, facecolor="white", edgecolor=fs.DARK, lw=1.2))
            ax.text(c + 0.5, y + 0.5, "1" if m in MINTERMS else "0", ha="center", va="center",
                    fontsize=16, color=fs.DARK if m in MINTERMS else fs.GRAY)
            ax.text(c + 0.92, y + 0.08, f"m{m}", ha="right", va="bottom", fontsize=8, color=fs.GRAY)
    for c, qr in enumerate(COLS):
        ax.text(c + 0.5, 2.12, qr, ha="center", va="bottom", fontsize=11)
    ax.text(2.0, 2.62, "QR", ha="center", va="bottom", fontsize=11, fontweight="bold")
    ax.text(-0.15, 1.5, "0", ha="right", va="center", fontsize=11)
    ax.text(-0.15, 0.5, "1", ha="right", va="center", fontsize=11)
    ax.text(-0.15, 2.62, "P", ha="right", va="bottom", fontsize=11, fontweight="bold")

    g1 = dict(facecolor="none", edgecolor=fs.GREEN, lw=2.4)
    g2 = dict(facecolor="none", edgecolor=fs.BLUE, lw=2.4)
    ax.add_patch(mp.FancyBboxPatch((0.07, 0.07), 0.86, 1.86, boxstyle="round,pad=0,rounding_size=0.15", **g1))
    ax.add_patch(mp.FancyBboxPatch((3.07, 0.07), 0.86, 1.86, boxstyle="round,pad=0,rounding_size=0.15", **g1))
    ax.add_patch(mp.FancyBboxPatch((2.2, 1.2), 1.6, 0.6, boxstyle="round,pad=0,rounding_size=0.15", **g2))

    ax.text(0.0, -0.3, "green: the four corners, one group that wraps around the edge", color=fs.GREEN,
            fontsize=9, ha="left", va="top")
    ax.text(0.0, -0.62, "blue: m2 and m3, where P = 0 and Q = 1", color=fs.BLUE, fontsize=9,
            ha="left", va="top")
    ax.set_xlim(-0.6, 4.2)
    ax.set_ylim(-0.9, 3.1)
    ax.set_aspect("equal")
    ax.axis("off")
    fs.save(fig, FOLDER, f"{SLUG}-kmap")


if __name__ == "__main__":
    kmap()
