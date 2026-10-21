"""Figure for docs/04-proofs-and-logic/06-relations-and-functions/06-cardinality-and-countability.md

The zigzag listing of the positive rationals p/q, with the fractions that are not in lowest terms greyed out.
"""

import sys
from math import gcd
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import figstyle as fs  # noqa: E402

FOLDER = "04-proofs-and-logic"
SLUG = "cardinality-and-countability"
N = 6  # grid size: numerators 1..N across, denominators 1..N down


def zigzag_cells(limit):
    """All cells (p, q) with p + q <= limit + 1, in zigzag order."""
    order = []
    for s in range(2, limit + 1):
        cells = [(p, s - p) for p in range(1, s)]
        if s % 2 == 1:
            cells = cells[::-1]
        order += cells
    return order


def rationals():
    cells = zigzag_cells(N + 1)
    fig, ax = fs.figure(5.6, 4.4)
    xs = [p for p, q in cells]
    ys = [-q for p, q in cells]
    ax.plot(xs, ys, color=fs.GRAY, linewidth=1.2, zorder=1)
    count = 0
    for p, q in cells:
        keep = gcd(p, q) == 1
        color = fs.DARK if keep else fs.GRAY
        ax.text(p, -q, f"{p}/{q}", ha="center", va="center", fontsize=11, color=color,
                bbox=dict(boxstyle="round,pad=0.25", fc="white", ec=fs.GREEN if keep else fs.LIGHT, lw=1.4 if keep else 1.0),
                zorder=3)
        if keep:
            count += 1
            ax.text(p + 0.33, -q + 0.3, str(count), ha="center", va="center", fontsize=8, color=fs.GREEN, zorder=4)
    ax.set_xlim(0.4, N + 0.6)
    ax.set_ylim(-N - 0.6, -0.4)
    ax.set_xlabel("numerator p")
    ax.set_ylabel("denominator q")
    ax.set_xticks(range(1, N + 1))
    ax.set_yticks([-q for q in range(1, N + 1)])
    ax.set_yticklabels([str(q) for q in range(1, N + 1)])
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    fs.save(fig, FOLDER, f"{SLUG}-rationals")


if __name__ == "__main__":
    rationals()
