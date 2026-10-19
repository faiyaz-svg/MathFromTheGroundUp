"""Figures for docs/03-high-school/05-quadratics-and-complex-numbers/01-quadratic-functions-and-graphs.md.

Run from the repo root:

    .venv/Scripts/python tools/figures/03-high-school/quadratic-functions-and-graphs.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import numpy as np  # noqa: E402

import figstyle as fs  # noqa: E402

FOLDER = "03-high-school"
SLUG = "quadratic-functions-and-graphs"
M = "\u2212"
BOX = dict(facecolor="white", edgecolor="none", pad=0.4, alpha=0.9)


def num(v):
    return f"{v:g}".replace("-", M)


def plane(ax, xmin, xmax, ymin, ymax, xstep=1, ystep=1, size=9, skip=()):
    """Axes through the origin with arrows, a light grid and tick labels."""
    padx = 0.04 * (xmax - xmin)
    pady = 0.04 * (ymax - ymin)
    ax.set_xlim(xmin - padx, xmax + 2 * padx)
    ax.set_ylim(ymin - pady, ymax + 2 * pady)
    ax.spines["left"].set_position("zero")
    ax.spines["bottom"].set_position("zero")
    xt = [v for v in np.arange(xmin, xmax + 1e-9, xstep)]
    yt = [v for v in np.arange(ymin, ymax + 1e-9, ystep)]
    ax.set_xticks(xt)
    ax.set_yticks(yt)
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.tick_params(length=3)
    ax.grid(True, zorder=0)
    ax.set_axisbelow(True)
    box = dict(facecolor="white", edgecolor="none", pad=0.2)
    for v in xt:
        if abs(v) > 1e-9 and v not in skip:
            ax.text(v, -0.2 * pady, num(v), ha="center", va="top", fontsize=size, zorder=4, bbox=box)
    for v in yt:
        if abs(v) > 1e-9:
            ax.text(-0.2 * padx, v, num(v), ha="right", va="center", fontsize=size, zorder=4, bbox=box)
    ax.plot(1, 0, ">", color=fs.DARK, transform=ax.get_yaxis_transform(), clip_on=False, ms=5)
    ax.plot(0, 1, "^", color=fs.DARK, transform=ax.get_xaxis_transform(), clip_on=False, ms=5)


def ball():
    fig, ax = fs.figure(5.2, 3.6)
    ts = np.linspace(0, 4, 200)
    ax.plot(ts, -5 * ts**2 + 20 * ts + 2, color=fs.GREEN, zorder=3)
    pts = [(0, 2), (1, 17), (2, 22), (3, 17), (4, 2)]
    ax.plot(*zip(*pts), "o", color=fs.DARK, zorder=5)
    for t, h in pts:
        dy = 1.4
        ax.text(t, h + dy, f"({t}, {h})", ha="center", va="bottom", fontsize=9.5, bbox=BOX, zorder=6)
    ax.set_xlim(-0.2, 4.4)
    ax.set_ylim(0, 27)
    ax.set_xticks(range(0, 5))
    ax.set_yticks(range(0, 26, 5))
    ax.grid(True)
    ax.set_axisbelow(True)
    ax.tick_params(labelsize=9)
    ax.set_xlabel("time $t$ (seconds)")
    ax.set_ylabel("height $h$ (metres)")
    fs.save(fig, FOLDER, f"{SLUG}-ball")


def anatomy():
    fig, ax = fs.figure(5.6, 4.2)
    plane(ax, -1, 8, -10, 14, 1, 2, size=9, skip=(1, 5))
    xs = np.linspace(-0.9, 6.9, 300)
    ys = 2 * xs**2 - 12 * xs + 10
    ax.plot(xs, ys, color=fs.GREEN, zorder=3)
    ax.plot([3, 3], [-10, 14], color=fs.BLUE, ls=(0, (5, 3)), lw=1.6, zorder=2)
    ax.text(3.15, 13.6, "axis of symmetry\n$x = 3$", ha="left", va="top", fontsize=10, color=fs.BLUE, bbox=BOX)
    ax.plot(3, -8, "o", color=fs.RED, zorder=6)
    ax.text(3.2, -8.3, "vertex $(3, -8)$", ha="left", va="top", fontsize=10, color=fs.RED, bbox=BOX, zorder=6)
    ax.plot([1, 5], [0, 0], "o", color=fs.DARK, zorder=6)
    ax.text(1.2, 0.9, "$(1, 0)$", ha="left", va="bottom", fontsize=10, bbox=BOX, zorder=6)
    ax.text(4.8, 0.9, "$(5, 0)$", ha="right", va="bottom", fontsize=10, bbox=BOX, zorder=6)
    ax.plot(0, 10, "o", color=fs.ORANGE, zorder=6)
    ax.text(0.25, 10.0, "$y$-intercept\n$(0, 10)$", ha="left", va="center", fontsize=10, color=fs.ORANGE, bbox=BOX, zorder=6)
    ax.plot(6, 10, "o", color=fs.ORANGE, mfc="white", zorder=6)
    ax.text(6.3, 9.0, "mirror image\n$(6, 10)$", ha="left", va="top", fontsize=9.5, color=fs.ORANGE, bbox=BOX, zorder=6)
    ax.text(8.9, 0.4, "$x$", ha="right", va="bottom", style="italic", fontsize=12)
    ax.text(0.2, 14.9, "$y$", ha="left", va="top", style="italic", fontsize=12)
    ax.text(8.1, -5.0, "$y = 2x^2 - 12x + 10$", ha="right", va="top", fontsize=10.5, color=fs.GREEN, bbox=BOX)
    fs.save(fig, FOLDER, f"{SLUG}-anatomy")


def shapes():
    fig, ax = fs.figure(5.4, 3.8)
    plane(ax, -3, 4, -4, 9, 1, 2, size=9)
    xs = np.linspace(-3, 3, 300)
    curves = [
        (1, fs.GREEN, "$a = 1$", (3.1, 8.6), "left"),
        (2, fs.BLUE, "$a = 2$", (1.95, 8.9), "right"),
        (0.5, fs.ORANGE, "$a = \\frac{1}{2}$", (3.1, 4.5), "left"),
        (-1, fs.RED, "$a = -1$", (2.1, -3.8), "left"),
    ]
    for a, colour, label, pos, ha in curves:
        ys = a * xs**2
        mask = (ys <= 9.0) & (ys >= -4.0)
        ax.plot(xs[mask], ys[mask], color=colour, zorder=3)
        ax.text(*pos, label, ha=ha, va="center", fontsize=10.5, color=colour, bbox=BOX, zorder=6)
    ax.text(4.9, 0.4, "$x$", ha="right", va="bottom", style="italic", fontsize=12)
    ax.text(0.15, 10.0, "$y$", ha="left", va="top", style="italic", fontsize=12)
    fs.save(fig, FOLDER, f"{SLUG}-shapes")


def revenue():
    fig, ax = fs.figure(5.4, 3.7)
    ps = np.linspace(0, 40, 300)
    ax.plot(ps, -20 * ps**2 + 800 * ps, color=fs.GREEN, zorder=3, clip_on=False)
    ax.plot([20], [8000], "o", color=fs.RED, zorder=6)
    ax.text(20, 8350, "maximum: \\$8,000 at $p = 20$", ha="center", va="bottom", fontsize=10, color=fs.RED, bbox=BOX, zorder=6)
    ax.plot([10, 30], [6000, 6000], "o", color=fs.DARK, zorder=6)
    ax.plot([10, 30], [6000, 6000], color=fs.GRAY, lw=1.2, ls=(0, (4, 3)), zorder=2)
    ax.text(10, 5500, "$p = 10$", ha="right", va="top", fontsize=9.5, bbox=BOX, zorder=6)
    ax.text(30, 5500, "$p = 30$", ha="left", va="top", fontsize=9.5, bbox=BOX, zorder=6)
    ax.text(20, 6000, "both give \\$6,000", ha="center", va="bottom", fontsize=9.5, color=fs.GRAY, bbox=BOX, zorder=6)
    ax.plot([20, 20], [0, 8000], color=fs.BLUE, lw=1.4, ls=(0, (5, 3)), zorder=2)
    ax.set_xlim(0, 40)
    ax.set_ylim(0, 9500)
    ax.set_xticks(range(0, 41, 5))
    ax.set_yticks(range(0, 9001, 1000))
    ax.set_yticklabels([f"{v:,}" for v in range(0, 9001, 1000)])
    ax.grid(True)
    ax.set_axisbelow(True)
    ax.tick_params(labelsize=9)
    ax.set_xlabel("price $p$ (dollars per month)")
    ax.set_ylabel("monthly revenue $R$ (dollars)")
    fs.save(fig, FOLDER, f"{SLUG}-revenue")


def fence():
    fig, ax = fs.figure(5.4, 3.7)
    xs = np.linspace(0, 50, 300)
    ax.plot(xs, xs * (100 - 2 * xs), color=fs.GREEN, zorder=3, clip_on=False)
    ax.axvspan(35, 50, color=fs.ORANGE, alpha=0.12, lw=0, zorder=1)
    ax.plot([25], [1250], "o", color=fs.RED, zorder=6)
    ax.text(24, 1265, "no limit on the wall:\nmaximum 1250 at $x = 25$", ha="right", va="bottom", fontsize=10,
            color=fs.RED, bbox=BOX, zorder=6)
    ax.plot([35], [1050], "o", color=fs.ORANGE, zorder=6)
    ax.text(36, 1085, "wall of 30 m:\nmaximum 1050\nat $x = 35$", ha="left", va="bottom", fontsize=10,
            color=fs.ORANGE, bbox=BOX, zorder=6)
    ax.text(41, 120, "allowed when\nthe wall is 30 m", ha="center", va="bottom", fontsize=9, color=fs.ORANGE)
    ax.set_xlim(0, 50)
    ax.set_ylim(0, 1450)
    ax.set_xticks(range(0, 51, 5))
    ax.set_yticks(range(0, 1401, 200))
    ax.grid(True)
    ax.set_axisbelow(True)
    ax.tick_params(labelsize=9)
    ax.set_xlabel("width $x$ (metres)")
    ax.set_ylabel("area $A$ (square metres)")
    fs.save(fig, FOLDER, f"{SLUG}-fence")


if __name__ == "__main__":
    ball()
    anatomy()
    shapes()
    revenue()
    fence()
