"""Figures for docs/02-middle-school/08-mental-math/02-mental-multiplication-and-division.md."""

import sys
from pathlib import Path

from matplotlib.patches import Rectangle

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import figstyle as fs  # noqa: E402

FOLDER = "02-middle-school"
SLUG = "mental-multiplication-and-division"


def block(ax, x, y, w, h, color, label, size=10):
    """A filled block with a unit grid inside and a centred label."""
    ax.add_patch(Rectangle((x, y), w, h, facecolor=color, alpha=0.26, edgecolor="none"))
    for i in range(1, w):
        ax.plot([x + i, x + i], [y, y + h], color="white", lw=0.5)
    for j in range(1, h):
        ax.plot([x, x + w], [y + j, y + j], color="white", lw=0.5)
    ax.add_patch(Rectangle((x, y), w, h, fill=False, edgecolor=color, lw=2))
    ax.text(x + w / 2, y + h / 2, label, ha="center", va="center", fontsize=size, color=fs.DARK,
            linespacing=1.15)


def difference_of_squares():
    """13 x 7 = (10 + 3)(10 - 3) = 10^2 - 3^2, drawn as a strip that moves."""
    fig, ax = fs.figure(7.6, 3.5)
    ox = 18.5  # left edge of the right-hand drawing

    # Left: the 13 by 7 rectangle, with a strip 3 wide at its right end.
    block(ax, 0, 0, 10, 7, fs.GREEN, r"$10 \times 7 = 70$")
    block(ax, 10, 0, 3, 7, fs.BLUE, r"$3 \times 7$" + "\n" + r"$= 21$")
    ax.text(5, -0.35, "10", ha="center", va="top", fontsize=12, color=fs.GREEN)
    ax.text(11.5, -0.35, "3", ha="center", va="top", fontsize=12, color=fs.BLUE)
    ax.text(-0.35, 3.5, "7", ha="right", va="center", fontsize=12)
    ax.text(6.5, -2.0, r"$13 \times 7 = 70 + 21 = 91$", ha="center", va="top", fontsize=11)

    # Right: the strip turned on its side and laid on top of the green block.
    block(ax, ox, 0, 10, 7, fs.GREEN, r"$10 \times 7 = 70$")
    block(ax, ox, 7, 7, 3, fs.BLUE, r"$3 \times 7 = 21$")
    ax.add_patch(Rectangle((ox + 7, 7), 3, 3, fill=False, edgecolor=fs.RED, lw=1.8, ls=(0, (4, 3))))
    ax.text(ox + 8.5, 8.5, r"$3 \times 3$" + "\n" + r"$= 9$" + "\n" + "missing",
            ha="center", va="center", fontsize=8.5, color=fs.RED, linespacing=1.15)
    ax.text(ox + 5, -0.35, "10", ha="center", va="top", fontsize=12)
    ax.text(ox - 0.35, 5, "10", ha="right", va="center", fontsize=12)
    ax.text(ox + 5, -2.0, r"$10^2 - 3^2 = 100 - 9 = 91$", ha="center", va="top", fontsize=11)

    ax.annotate("", xy=(16.3, 4.0), xytext=(13.9, 4.0),
                arrowprops=dict(arrowstyle="->", color=fs.DARK, lw=1.5))
    ax.set_xlim(-1.5, ox + 10.6)
    ax.set_ylim(-3.0, 10.4)
    ax.set_aspect("equal")
    ax.axis("off")
    fs.save(fig, FOLDER, f"{SLUG}-difference-of-squares")


if __name__ == "__main__":
    difference_of_squares()
