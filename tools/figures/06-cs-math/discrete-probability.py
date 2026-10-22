"""Figure for 06-cs-math/03-counting-and-discrete-probability/05-discrete-probability.md.

birthday: the exact probability of a shared birthday among k people (365 days),
the bounds 1 - exp(-k(k-1)/(2n)) and k(k-1)/(2n), and the point at k = 23.
"""

import sys
from math import exp
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from figstyle import BLUE, DARK, GRAY, GREEN, ORANGE, RED, figure, save  # noqa: E402

FOLDER = "06-cs-math"
SLUG = "discrete-probability"


def birthday():
    n = 365
    ks = list(range(0, 71))
    exact, lower, upper = [], [], []
    p = 1.0
    for k in ks:
        if k > 0:
            p *= (n - (k - 1)) / n
        exact.append(1 - p)
        x = k * (k - 1) / (2 * n)
        lower.append(1 - exp(-x))
        upper.append(min(1.0, x))
    fig, ax = figure(5.6, 3.8)
    ax.plot(ks, upper, color=GRAY, lw=1.6, ls="--")
    ax.plot(ks, exact, color=GREEN, lw=2.4)
    ax.plot(ks, lower, color=BLUE, lw=1.6, ls=":")
    ax.axhline(0.5, color=GRAY, lw=0.8)
    ax.plot([23], [exact[23]], "o", color=DARK, zorder=4)
    ax.annotate("k = 23: 0.507", xy=(23, exact[23]), xytext=(1.5, 0.60),
                color=DARK, fontsize=10,
                arrowprops=dict(arrowstyle="-", color=DARK, lw=0.9))
    ax.annotate("union bound\nk(k-1)/(2n)", xy=(19, upper[19]), xytext=(1.5, 0.80),
                color=GRAY, fontsize=9.5,
                arrowprops=dict(arrowstyle="-", color=GRAY, lw=0.9))
    ax.text(38, 0.25, "exact (solid green) and\n1 - exp(-k(k-1)/(2n)) (dotted blue)\nnearly coincide",
            color=DARK, fontsize=9.5, ha="left")
    ax.set_xlim(0, 70)
    ax.set_ylim(0, 1.03)
    ax.set_xlabel("number of people k")
    ax.set_ylabel("probability of a shared birthday")
    ax.grid(True, axis="y")
    save(fig, FOLDER, f"{SLUG}-birthday")


if __name__ == "__main__":
    birthday()
