"""Figure for 06-cs-math/03-counting-and-discrete-probability/03-binomial-theorem-and-combinatorial-proofs.md.

lattice: the number of lattice paths from (0, 0) to each point of a 5-by-4 grid,
with the last step into (4, 3) shown, to illustrate Pascal's rule.
"""

import sys
from math import comb
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from figstyle import BLUE, DARK, GRAY, GREEN, LIGHT, ORANGE, figure, save  # noqa: E402

FOLDER = "06-cs-math"
SLUG = "binomial-theorem-and-combinatorial-proofs"


def lattice():
    fig, ax = figure(5.6, 4.4)
    cols, rows = 5, 4  # x runs 0..4, y runs 0..3
    for x in range(cols):
        ax.plot([x, x], [0, rows - 1], color=LIGHT, lw=1.2, zorder=1)
    for y in range(rows):
        ax.plot([0, cols - 1], [y, y], color=LIGHT, lw=1.2, zorder=1)

    target = (4, 3)
    # the two last steps into the target
    ax.annotate("", xy=(4 - 0.02, 3), xytext=(3 + 0.2, 3),
                arrowprops=dict(arrowstyle="-|>", color=GREEN, lw=2.2), zorder=2)
    ax.annotate("", xy=(4, 3 - 0.02), xytext=(4, 2 + 0.2),
                arrowprops=dict(arrowstyle="-|>", color=ORANGE, lw=2.2), zorder=2)

    for x in range(cols):
        for y in range(rows):
            n = comb(x + y, x)
            if (x, y) == target:
                face, edge, tc = DARK, DARK, "white"
            elif (x, y) == (3, 3):
                face, edge, tc = "white", GREEN, DARK
            elif (x, y) == (4, 2):
                face, edge, tc = "white", ORANGE, DARK
            else:
                face, edge, tc = "white", GRAY, DARK
            ax.text(x, y, str(n), ha="center", va="center", fontsize=11, color=tc,
                    bbox=dict(boxstyle="round,pad=0.35", fc=face, ec=edge, lw=1.6), zorder=3)

    ax.text(3.5, 3.43, "right step: 20 paths", color=GREEN, ha="center", va="bottom", fontsize=9.5)
    ax.text(4.22, 2.5, "up step:\n15 paths", color=ORANGE, ha="left", va="center", fontsize=9.5)

    ax.set_xlim(-0.5, 5.15)
    ax.set_ylim(-0.5, 3.9)
    ax.set_aspect("equal")
    ax.set_xticks(range(cols))
    ax.set_yticks(range(rows))
    ax.set_xlabel("steps right")
    ax.set_ylabel("steps up")
    ax.spines["left"].set_visible(False)
    ax.spines["bottom"].set_visible(False)
    ax.tick_params(length=0)
    save(fig, FOLDER, f"{SLUG}-lattice")


if __name__ == "__main__":
    lattice()
