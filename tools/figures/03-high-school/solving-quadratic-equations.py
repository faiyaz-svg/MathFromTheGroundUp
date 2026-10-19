"""Figures for docs/03-high-school/05-quadratics-and-complex-numbers/02-solving-quadratic-equations.md.

Run from the repo root:

    .venv/Scripts/python tools/figures/03-high-school/solving-quadratic-equations.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

import figstyle as fs  # noqa: E402

FOLDER = "03-high-school"
SLUG = "solving-quadratic-equations"
M = "−"
BOX = dict(facecolor="white", edgecolor="none", pad=0.4, alpha=0.9)


def num(v):
    return f"{v:g}".replace("-", M)


def plane(ax, xmin, xmax, ymin, ymax, xstep=1, ystep=1, size=9):
    """Axes through the origin with arrows, a light grid and tick labels."""
    padx = 0.04 * (xmax - xmin)
    pady = 0.04 * (ymax - ymin)
    ax.set_xlim(xmin - padx, xmax + 2 * padx)
    ax.set_ylim(ymin - pady, ymax + 2 * pady)
    ax.spines["left"].set_position("zero")
    ax.spines["bottom"].set_position("zero")
    xt = list(np.arange(xmin, xmax + 1e-9, xstep))
    yt = list(np.arange(ymin, ymax + 1e-9, ystep))
    ax.set_xticks(xt)
    ax.set_yticks(yt)
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.tick_params(length=3)
    ax.grid(True, zorder=0)
    ax.set_axisbelow(True)
    box = dict(facecolor="white", edgecolor="none", pad=0.2)
    for v in xt:
        if abs(v) > 1e-9:
            ax.text(v, -0.2 * pady, num(v), ha="center", va="top", fontsize=size, zorder=4, bbox=box)
    for v in yt:
        if abs(v) > 1e-9:
            ax.text(-0.2 * padx, v, num(v), ha="right", va="center", fontsize=size, zorder=4, bbox=box)
    ax.plot(1, 0, ">", color=fs.DARK, transform=ax.get_yaxis_transform(), clip_on=False, ms=5)
    ax.plot(0, 1, "^", color=fs.DARK, transform=ax.get_xaxis_transform(), clip_on=False, ms=5)


def discriminant():
    fig, axes = plt.subplots(1, 3, figsize=(8.4, 3.0))
    xs = np.linspace(-0.45, 4.45, 300)
    cases = [
        (3, "$y = x^2 - 4x + 3$", "$D = 4 > 0$\ntwo solutions", [1, 3]),
        (4, "$y = x^2 - 4x + 4$", "$D = 0$\none solution", [2]),
        (5, "$y = x^2 - 4x + 5$", "$D = -4 < 0$\nno real solution", []),
    ]
    for ax, (c, eq, text, roots) in zip(axes, cases):
        plane(ax, -1, 4, -2, 5, 1, 1, size=8)
        ax.plot(xs, xs**2 - 4 * xs + c, color=fs.GREEN, zorder=3)
        for r in roots:
            ax.plot(r, 0, "o", color=fs.RED, zorder=6)
            ax.text(r, -1.2, f"$x = {r}$", ha="center", va="top", fontsize=9, color=fs.RED, bbox=BOX, zorder=6)
        ax.text(0.5, -0.1, eq, transform=ax.transAxes, ha="center", va="top", fontsize=10.5, color=fs.GREEN)
        ax.text(0.5, -0.27, text, transform=ax.transAxes, ha="center", va="top", fontsize=10.5)
    fig.tight_layout(w_pad=1.2)
    fs.save(fig, FOLDER, f"{SLUG}-discriminant")


def landing():
    fig, ax = fs.figure(5.6, 3.8)
    plane(ax, -1, 5, -5, 25, 1, 5, size=9)
    neg = np.linspace(-1, 0, 50)
    pos = np.linspace(0, 5, 200)

    def h(t):
        return -4.9 * t**2 + 19.6 * t + 1.5

    neg = neg[h(neg) >= -5]
    pos = pos[h(pos) >= -5]
    ax.plot(neg, h(neg), color=fs.GRAY, ls=(0, (4, 3)), zorder=3)
    ax.plot(pos, h(pos), color=fs.GREEN, zorder=3)
    r1 = 2 - np.sqrt(211) / 7
    r2 = 2 + np.sqrt(211) / 7
    ax.plot(r2, 0, "o", color=fs.RED, zorder=6)
    ax.text(r2 - 0.1, 3.0, "lands at\n$t \\approx 4.08$", ha="right", va="bottom", fontsize=10, color=fs.RED, bbox=BOX, zorder=6)
    ax.plot(r1, 0, "o", color=fs.GRAY, mfc="white", zorder=6)
    ax.text(r1 + 0.45, -2.2,"$t \\approx -0.08$: before the throw,\nso not an answer", ha="left", va="top", fontsize=9.5, color=fs.GRAY, bbox=BOX, zorder=6)
    ax.plot(0, 1.5, "o", color=fs.DARK, zorder=6)
    ax.text(0.15, 3.2, "thrown at $t = 0$\nfrom 1.5 m", ha="left", va="bottom", fontsize=9.5, bbox=BOX, zorder=6)
    ax.text(5.9, 0.6, "$t$", ha="right", va="bottom", style="italic", fontsize=12)
    ax.text(0.15, 26.8, "$h$", ha="left", va="top", style="italic", fontsize=12)
    fs.save(fig, FOLDER, f"{SLUG}-landing")


if __name__ == "__main__":
    discriminant()
    landing()
