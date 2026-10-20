"""Figures for docs/03-high-school/07-exponentials-and-logarithms/02-logarithms.md.

Run from the repo root:

    .venv/Scripts/python tools/figures/03-high-school/logarithms.py
"""

import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import figstyle as fs  # noqa: E402

FOLDER = "03-high-school"
SLUG = "logarithms"
BOX = dict(facecolor="white", edgecolor="none", pad=0.4, alpha=0.9)


def frange(a, b, n=400):
    return [a + (b - a) * i / n for i in range(n + 1)]


def through_zero(ax, lo, hi, ticks):
    ax.set_xlim(lo, hi)
    ax.set_ylim(lo, hi)
    ax.set_aspect("equal")
    ax.spines["left"].set_position("zero")
    ax.spines["bottom"].set_position("zero")
    ax.set_xticks([t for t in ticks if t != 0])
    ax.set_yticks([t for t in ticks if t != 0])
    ax.grid(True)
    ax.set_axisbelow(True)
    ax.tick_params(labelsize=9, length=3)
    ax.plot(1, 0, ">", color=fs.DARK, transform=ax.get_yaxis_transform(), clip_on=False, ms=5)
    ax.plot(0, 1, "^", color=fs.DARK, transform=ax.get_xaxis_transform(), clip_on=False, ms=5)


def reflection():
    """y = 2^x and y = log_2 x, mirror images in the line y = x."""
    fig, ax = fs.figure(5.0, 5.0)
    through_zero(ax, -2.5, 9.5, [-2, 0, 2, 4, 6, 8])
    ax.plot([-2.5, 9.5], [-2.5, 9.5], color=fs.GRAY, lw=1.2, ls="--", zorder=2)
    xs = frange(-2.5, 3.2)
    ax.plot(xs, [2**t for t in xs], color=fs.GREEN, zorder=4)
    xl = frange(0.04, 9.5)
    ax.plot(xl, [math.log2(t) for t in xl], color=fs.BLUE, zorder=4)
    for px, py in ((0, 1), (1, 2), (2, 4), (3, 8)):
        ax.plot([px], [py], "o", color=fs.GREEN, ms=6, zorder=6)
        ax.plot([py], [px], "o", color=fs.BLUE, ms=6, zorder=6)
    ax.annotate("(0, 1)", xy=(0, 1), xytext=(-1.6, 3.6), color=fs.GREEN, fontsize=9, ha="center", va="center",
                arrowprops=dict(arrowstyle="-", color=fs.GREEN, lw=0.9))
    ax.text(3.2, 7.3, "(3, 8)", color=fs.GREEN, fontsize=9, ha="left", va="center")
    ax.annotate("(1, 0)", xy=(1, 0), xytext=(-1.6, -1.5), color=fs.BLUE, fontsize=9, ha="center", va="center",
                arrowprops=dict(arrowstyle="-", color=fs.BLUE, lw=0.9))
    ax.text(8.0, 2.55, "(8, 3)", color=fs.BLUE, fontsize=9, ha="center", va="bottom")
    ax.text(-2.3, 1.9, "$y = 2^x$", color=fs.GREEN, fontsize=11, ha="left", va="center", bbox=BOX)
    ax.text(5.4, 1.0, "$y = \\log_2 x$", color=fs.BLUE, fontsize=11, ha="left", va="center", bbox=BOX)
    ax.text(7.0, 8.4, "$y = x$", color=fs.GRAY, fontsize=10, ha="left", va="center")
    fs.save(fig, FOLDER, f"{SLUG}-reflection")


def bases():
    """Logarithms in base 2, e and 10 all pass through (1, 0)."""
    fig, ax = fs.figure(5.4, 3.8)
    xs = frange(0.06, 10, 600)
    ax.plot(xs, [math.log2(t) for t in xs], color=fs.GREEN, zorder=4)
    ax.plot(xs, [math.log(t) for t in xs], color=fs.BLUE, zorder=4)
    ax.plot(xs, [math.log10(t) for t in xs], color=fs.ORANGE, zorder=4)
    ax.axhline(0, color=fs.DARK, lw=1.0, zorder=3)
    ax.plot([1], [0], "o", color=fs.DARK, ms=6, zorder=6)
    ax.set_xlim(0, 10.8)
    ax.set_ylim(-3.2, 4)
    ax.set_xticks([1, 2, 4, 6, 8, 10])
    ax.set_yticks([-3, -2, -1, 0, 1, 2, 3, 4])
    ax.spines["bottom"].set_visible(False)
    ax.tick_params(axis="x", length=0, pad=2)
    ax.grid(True)
    ax.set_axisbelow(True)
    ax.set_xlabel("x")
    ax.xaxis.set_label_coords(0.5, -0.08)
    ax.text(10.15, 3.32, "$\\log_2 x$", color=fs.GREEN, fontsize=10.5, ha="left", va="center")
    ax.text(10.15, 2.3, "$\\ln x$", color=fs.BLUE, fontsize=10.5, ha="left", va="center")
    ax.text(10.15, 1.0, "$\\log_{10} x$", color=fs.ORANGE, fontsize=10.5, ha="left", va="center")
    ax.text(1.2, -0.45, "(1, 0)", color=fs.DARK, fontsize=9, ha="left", va="top")
    ax.text(0.2, -2.7, "x = 0 is the vertical asymptote", color=fs.GRAY, fontsize=8.5, ha="left", va="center")
    fs.save(fig, FOLDER, f"{SLUG}-bases")


if __name__ == "__main__":
    reflection()
    bases()
