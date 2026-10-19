"""Figures for docs/03-high-school/03-functions/02-reading-function-graphs.md.

Run from the repo root:

    .venv/Scripts/python tools/figures/03-high-school/reading-function-graphs.py
"""

import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import matplotlib.pyplot as plt  # noqa: E402

import figstyle as fs  # noqa: E402

FOLDER = "03-high-school"
SLUG = "reading-function-graphs"
M = "−"
BOX = dict(facecolor="white", edgecolor="none", pad=0.5, alpha=0.9)
UP = fs.GREEN
DOWN = fs.ORANGE


def frange(a, b, n=400):
    return [a + (b - a) * i / n for i in range(n + 1)]


def through_zero(ax, xlim, ylim, xticks, yticks, size=9):
    """Axes crossing at the origin, light grid, labels placed clear of the curve."""
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.spines["left"].set_position("zero")
    ax.spines["bottom"].set_position("zero")
    ax.set_xticks([t for t in xticks if t != 0])
    ax.set_yticks([t for t in yticks if t != 0])
    ax.grid(True)
    ax.set_axisbelow(True)
    ax.tick_params(labelsize=size, length=3)
    ax.plot(1, 0, ">", color=fs.DARK, transform=ax.get_yaxis_transform(), clip_on=False, ms=5)
    ax.plot(0, 1, "^", color=fs.DARK, transform=ax.get_xaxis_transform(), clip_on=False, ms=5)


def temperature():
    """A made-up winter day: T(t) = -4 + 6 sin(pi (t - 9) / 12)."""
    def T(t):
        return -4 + 6 * math.sin(math.pi * (t - 9) / 12)

    fig, ax = fs.figure(6.2, 3.7)
    ts = frange(0, 24)
    ax.set_xlim(0, 24)
    ax.set_ylim(-12.5, 5.5)
    ax.axvspan(0, 3, color=DOWN, alpha=0.12, lw=0)
    ax.axvspan(3, 15, color=UP, alpha=0.12, lw=0)
    ax.axvspan(15, 24, color=DOWN, alpha=0.12, lw=0)
    ax.axhline(0, color=fs.GRAY, lw=1.0, ls="--", zorder=2)
    ax.plot(ts, [T(t) for t in ts], color=fs.BLUE, zorder=3)
    ax.set_xticks(range(0, 25, 3))
    ax.set_yticks([-10, -5, 0, 5])
    ax.set_xticklabels([f"{t}:00" for t in range(0, 25, 3)], fontsize=9)
    ax.tick_params(axis="y", labelsize=9)
    ax.set_ylabel("temperature (°C)")
    ax.set_xlabel("time of day")
    z1 = 9 + 12 / math.pi * math.asin(2 / 3)
    z2 = 30 - z1
    ax.plot([z1, z2], [0, 0], "o", mfc="white", mec=fs.BLUE, ms=7, mew=1.6, zorder=5)
    ax.plot([15], [2], "o", color=fs.BLUE, zorder=5)
    ax.plot([3], [-10], "o", color=fs.BLUE, zorder=5)
    ax.text(15.0, 3.0, "warmest: 2 °C at 15:00", ha="center", va="bottom", fontsize=9.5, color=fs.BLUE)
    ax.text(3.4, -10.9, "coldest: −10 °C at 3:00", ha="left", va="center", fontsize=9.5,
            color=fs.BLUE, bbox=BOX)
    ax.text(z1 - 0.5, 0.8, "0 °C at about 11:45", ha="right", va="bottom", fontsize=9, color=fs.DARK)
    ax.text(z2 + 0.4, 0.8, "and 18:15", ha="left", va="bottom", fontsize=9, color=fs.DARK)
    ax.text(1.5, 4.7, "falling", ha="center", va="center", fontsize=9.5, color=DOWN)
    ax.text(9, 4.7, "rising", ha="center", va="center", fontsize=9.5, color=UP)
    ax.text(19.5, 4.7, "falling", ha="center", va="center", fontsize=9.5, color=DOWN)
    fs.save(fig, FOLDER, f"{SLUG}-temperature")


def cubic():
    """f(x) = x^3 - 3x on [-2, 2], with its turning points, zeros and intervals marked."""
    def f(x):
        return x**3 - 3 * x

    fig, ax = fs.figure(5.8, 4.4)
    through_zero(ax, (-2.55, 2.75), (-3.9, 3.6), [-2, -1, 1, 2], [-3, -2, -1, 1, 2, 3])
    ax.axvspan(-2, -1, color=UP, alpha=0.12, lw=0)
    ax.axvspan(-1, 1, color=DOWN, alpha=0.12, lw=0)
    ax.axvspan(1, 2, color=UP, alpha=0.12, lw=0)
    xs = frange(-2, 2)
    ax.plot(xs, [f(t) for t in xs], color=fs.BLUE, zorder=3)
    r = math.sqrt(3)
    ax.plot([-r, 0, r], [0, 0, 0], "o", mfc="white", mec=fs.DARK, ms=6.5, mew=1.5, zorder=5)
    ax.plot([-2, -1, 1, 2], [-2, 2, -2, 2], "o", color=fs.BLUE, zorder=5)
    ax.text(-1.0, 2.35, f"({M}1, 2)  local max", ha="center", va="bottom", fontsize=9.5, color=fs.BLUE)
    ax.text(1.0, -2.45, "(1, −2)  local min", ha="center", va="top", fontsize=9.5, color=fs.BLUE)
    ax.text(2.1, 2.0, "(2, 2)", ha="left", va="center", fontsize=9.5, color=fs.BLUE)
    ax.text(-2.1, -2.0, f"({M}2, {M}2)", ha="right", va="center", fontsize=9.5, color=fs.BLUE)
    ax.text(r + 0.1, 0.35, "zero at √3", ha="left", va="bottom", fontsize=9, color=fs.DARK)
    ax.text(-r - 0.05, 0.35, "zero at −√3", ha="right", va="bottom", fontsize=9, color=fs.DARK)
    ax.text(0.12, 0.35, "zero at 0", ha="left", va="bottom", fontsize=9, color=fs.DARK)
    ax.text(-1.5, -3.55, "increasing", ha="center", va="center", fontsize=9.5, color=UP)
    ax.text(0.0, -3.55, "decreasing", ha="center", va="center", fontsize=9.5, color=DOWN)
    ax.text(1.5, -3.55, "increasing", ha="center", va="center", fontsize=9.5, color=UP)
    fs.save(fig, FOLDER, f"{SLUG}-cubic")


def stock():
    """Closing prices for ten days (made-up) with two secant lines."""
    prices = [40, 42, 41, 45, 47, 46, 43, 41, 44, 49, 52]
    days = list(range(11))
    fig, ax = fs.figure(6.2, 3.8)
    ax.set_xlim(-0.4, 10.6)
    ax.set_ylim(36, 56)
    ax.set_xticks(days)
    ax.set_yticks(range(40, 55, 4))
    ax.grid(True)
    ax.set_axisbelow(True)
    ax.tick_params(labelsize=9)
    ax.set_xlabel("trading day")
    ax.set_ylabel("closing price (dollars)")
    ax.plot(days, prices, "-o", color=fs.GRAY, lw=1.2, ms=5, zorder=3)
    # secant, days 2 to 5
    ax.plot([2, 5], [41, 46], "-o", color=fs.RED, lw=2.2, ms=7, zorder=5)
    ax.plot([4, 7], [47, 41], "-o", color=fs.BLUE, lw=2.2, ms=7, zorder=5)
    ax.text(2.6, 37.9, "secant, days 2 to 5: slope about $" + "1.67 per day", ha="left",
            va="center", fontsize=9.5, color=fs.RED)
    ax.text(5.8, 51.2, "secant, days 4 to 7:\nslope −$2 per day", ha="left", va="center",
            fontsize=9.5, color=fs.BLUE, bbox=BOX)
    fs.save(fig, FOLDER, f"{SLUG}-stock")


def even_odd():
    """An even function and an odd function, with a pair of points that show the symmetry."""
    fig, axes = plt.subplots(1, 2, figsize=(7.2, 3.8))
    # even: x^4 - 3x^2 + 1
    ax = axes[0]
    through_zero(ax, (-2.5, 2.5), (-2.4, 5.8), [-2, -1, 1, 2], [-2, 2, 4])
    xs = frange(-2.1, 2.1)
    ax.plot(xs, [t**4 - 3 * t**2 + 1 for t in xs], color=fs.BLUE, zorder=3)
    ax.plot([-2, 2], [5, 5], "o", color=fs.BLUE, zorder=5)
    ax.plot([-1, 1], [-1, -1], "o", color=fs.BLUE, zorder=5)
    ax.plot([-2, 2], [5, 5], color=fs.RED, lw=1.2, ls="--", zorder=4)
    ax.plot([-1, 1], [-1, -1], color=fs.RED, lw=1.2, ls="--", zorder=4)
    ax.text(0, 5.35, "(−2, 5) and (2, 5)", ha="center", va="bottom", fontsize=9, color=fs.RED)
    ax.text(-1.0, -1.45, f"({M}1, {M}1)", ha="center", va="top", fontsize=9, color=fs.RED)
    ax.text(1.0, -1.45, f"(1, {M}1)", ha="center", va="top", fontsize=9, color=fs.RED)
    ax.text(0, -2.7, "even: mirror image in the y-axis\nf(x) = x⁴ − 3x² + 1", ha="center", va="top",
            fontsize=10, color=fs.DARK)
    # odd: x^3 - 3x
    ax = axes[1]
    through_zero(ax, (-2.5, 2.5), (-4.3, 4.3), [-2, -1, 1, 2], [-4, -2, 2, 4])
    xs = frange(-2.15, 2.15)
    ax.plot(xs, [t**3 - 3 * t for t in xs], color=fs.BLUE, zorder=3)
    for px in (-1, 1):
        ax.plot([px], [px**3 - 3 * px], "o", color=fs.BLUE, zorder=5)
    ax.plot([-1, 1], [2, -2], color=fs.RED, lw=1.2, ls="--", zorder=4)
    ax.plot(0, 0, "o", color=fs.RED, ms=4, zorder=6)
    ax.text(-1.0, 2.45, f"({M}1, 2)", ha="center", va="bottom", fontsize=9, color=fs.RED)
    ax.text(1.0, -2.45, f"(1, {M}2)", ha="center", va="top", fontsize=9, color=fs.RED)
    ax.text(0, -5.0, "odd: half turn about the origin\ng(x) = x³ − 3x", ha="center", va="top",
            fontsize=10, color=fs.DARK)
    fig.tight_layout(w_pad=1.5)
    fs.save(fig, FOLDER, f"{SLUG}-even-odd")


def cost():
    """C(q) = 1000 + 10q + 0.05 q^2 for 0 <= q <= 200, with two secant lines."""
    def C(q):
        return 1000 + 10 * q + 0.05 * q * q

    fig, ax = fs.figure(5.8, 3.8)
    ax.set_xlim(-10, 215)
    ax.set_ylim(0, 5600)
    ax.set_xticks(range(0, 201, 50))
    ax.set_yticks(range(0, 5001, 1000))
    ax.grid(True)
    ax.set_axisbelow(True)
    ax.tick_params(labelsize=9)
    ax.set_xlabel("widgets made per day, q")
    ax.set_ylabel("daily cost (dollars)")
    qs = frange(0, 200)
    ax.plot(qs, [C(q) for q in qs], color=fs.GRAY, lw=1.6, zorder=3)
    ax.plot([0, 100], [C(0), C(100)], "-o", color=fs.RED, lw=2.2, ms=7, zorder=5)
    ax.plot([100, 200], [C(100), C(200)], "-o", color=fs.BLUE, lw=2.2, ms=7, zorder=5)
    ax.text(8, 2400, "secant from\nq = 0 to 100", ha="left", va="center", fontsize=9.5, color=fs.RED)
    ax.text(112, 2300, "secant from\nq = 100 to 200", ha="left", va="center", fontsize=9.5, color=fs.BLUE,
            bbox=BOX)
    fs.save(fig, FOLDER, f"{SLUG}-cost")


if __name__ == "__main__":
    temperature()
    cubic()
    stock()
    even_odd()
    cost()
