"""Figures for docs/03-high-school/03-functions/05-composition-and-inverse-functions.md.

Run from the repo root:

    .venv/Scripts/python tools/figures/03-high-school/composition-and-inverse-functions.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import matplotlib.pyplot as plt  # noqa: E402

import figstyle as fs  # noqa: E402

FOLDER = "03-high-school"
SLUG = "composition-and-inverse-functions"
M = "−"
BOX = dict(facecolor="white", edgecolor="none", pad=0.4, alpha=0.9)


def frange(a, b, n=400):
    return [a + (b - a) * i / n for i in range(n + 1)]


def through_zero(ax, xlim, ylim, xticks, yticks, size=9):
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.set_aspect("equal")
    ax.spines["left"].set_position("zero")
    ax.spines["bottom"].set_position("zero")
    ax.set_xticks([t for t in xticks if t != 0])
    ax.set_yticks([t for t in yticks if t != 0])
    ax.grid(True)
    ax.set_axisbelow(True)
    ax.tick_params(labelsize=size, length=3)
    ax.plot(1, 0, ">", color=fs.DARK, transform=ax.get_yaxis_transform(), clip_on=False, ms=5)
    ax.plot(0, 1, "^", color=fs.DARK, transform=ax.get_xaxis_transform(), clip_on=False, ms=5)


def dot(ax, x, y, color):
    ax.plot([x], [y], "o", color=color, ms=6, zorder=6)


def cbrt(t):
    return t ** (1 / 3) if t >= 0 else -((-t) ** (1 / 3))


def reflection():
    """f(x) = x^3 + 1 and its inverse, the cube root of (x - 1), mirror images in y = x."""
    fig, ax = fs.figure(5.0, 4.8)
    through_zero(ax, (-3.2, 3.8), (-3.2, 3.8), [-3, -2, -1, 1, 2, 3], [-3, -2, -1, 1, 2, 3])
    ax.plot([-3.2, 3.8], [-3.2, 3.8], color=fs.GRAY, lw=1.2, ls="--", zorder=2)
    xs = frange(-1.6, 1.4)
    ax.plot(xs, [t**3 + 1 for t in xs], color=fs.GREEN, zorder=4)
    xi = frange(-3.2, 3.8)
    ax.plot(xi, [cbrt(t - 1) for t in xi], color=fs.BLUE, zorder=4)
    for px, py in ((-1, 0), (0, 1), (1, 2)):
        dot(ax, px, py, fs.GREEN)
        dot(ax, py, px, fs.BLUE)
    ax.text(-1.0, 0.25, f"({M}1, 0)", color=fs.GREEN, fontsize=9, ha="right", va="bottom")
    ax.text(-0.1, 1.2, "(0, 1)", color=fs.GREEN, fontsize=9, ha="right", va="bottom")
    ax.text(1.1, 2.1, "(1, 2)", color=fs.GREEN, fontsize=9, ha="left", va="bottom")
    ax.text(0.25, -1.0, f"(0, {M}1)", color=fs.BLUE, fontsize=9, ha="left", va="top")
    ax.text(1.1, 0.3, "(1, 0)", color=fs.BLUE, fontsize=9, ha="left", va="bottom")
    ax.text(2.1, 1.0, "(2, 1)", color=fs.BLUE, fontsize=9, ha="left", va="top")
    ax.text(-1.5, 2.6, "f(x) = x³ + 1", color=fs.GREEN, fontsize=10, ha="center", va="center", bbox=BOX)
    ax.text(2.4, -1.6, f"f{chr(8315)}{chr(185)}(x) = ∛(x {M} 1)", color=fs.BLUE, fontsize=10, ha="center",
            va="center", bbox=BOX)
    ax.text(3.1, 3.45, "y = x", color=fs.GRAY, fontsize=9.5, ha="right", va="center")
    fs.save(fig, FOLDER, f"{SLUG}-reflection")


def restriction():
    fig, axes = plt.subplots(1, 2, figsize=(7.4, 3.8))
    ax = axes[0]
    through_zero(ax, (-3.4, 4.8), (-1.2, 5.8), [-3, -2, -1, 1, 2, 3, 4], [1, 2, 3, 4, 5])
    xs = frange(-2.3, 2.3)
    ax.plot(xs, [t * t for t in xs], color=fs.BLUE, zorder=4)
    ax.plot([-3.2, 3.2], [4, 4], color=fs.RED, lw=1.3, ls="--", zorder=3)
    dot(ax, -2, 4, fs.RED)
    dot(ax, 2, 4, fs.RED)
    ax.text(-3.3, -0.9, "fails: the line y = 4 meets it twice", color=fs.RED, fontsize=9, ha="left", va="center")
    ax.text(2.4, 1.6, "y = x²", color=fs.BLUE, fontsize=10, ha="left", va="center", bbox=BOX)
    ax = axes[1]
    through_zero(ax, (-1.2, 5.4), (-1.2, 5.8), [1, 2, 3, 4, 5], [1, 2, 3, 4, 5])
    ax.plot([-1.2, 5.4], [-1.2, 5.4], color=fs.GRAY, lw=1.2, ls="--", zorder=2)
    xs = frange(0, 2.3)
    ax.plot(xs, [t * t for t in xs], color=fs.BLUE, zorder=4)
    xr = frange(0, 5.3)
    ax.plot(xr, [t ** 0.5 for t in xr], color=fs.GREEN, zorder=4)
    dot(ax, 2, 4, fs.BLUE)
    dot(ax, 4, 2, fs.GREEN)
    ax.text(0.2, 5.0, "x² for x ≥ 0", color=fs.BLUE, fontsize=10, ha="left", va="center", bbox=BOX)
    ax.text(2.6, 0.6, "√x", color=fs.GREEN, fontsize=10.5, ha="left", va="center", bbox=BOX)
    ax.text(2.1, 4.25, "(2, 4)", color=fs.BLUE, fontsize=9, ha="left", va="bottom")
    ax.text(4.1, 2.1, "(4, 2)", color=fs.GREEN, fontsize=9, ha="left", va="bottom")
    fig.tight_layout(w_pad=1.0)
    fs.save(fig, FOLDER, f"{SLUG}-restriction")


if __name__ == "__main__":
    reflection()
    restriction()
