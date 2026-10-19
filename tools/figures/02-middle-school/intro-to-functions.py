"""Figures for docs/02-middle-school/05-linear-relationships-and-functions/03-intro-to-functions.md.

Run from the repo root:

    .venv/Scripts/python tools/figures/02-middle-school/intro-to-functions.py
"""

import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import Ellipse  # noqa: E402

import figstyle as fs  # noqa: E402

FOLDER = "02-middle-school"
SLUG = "intro-to-functions"
M = "−"
BOX = dict(facecolor="white", edgecolor="none", pad=0.4, alpha=0.9)


def num(v):
    return f"{v:g}".replace("-", M)


def plane(ax, xmin, xmax, ymin, ymax, every=1, size=9):
    """Axes through the origin with arrows, a light grid and equal units."""
    ax.set_xlim(xmin - 0.5, xmax + 0.6)
    ax.set_ylim(ymin - 0.5, ymax + 0.6)
    ax.set_aspect("equal")
    ax.spines["left"].set_position("zero")
    ax.spines["bottom"].set_position("zero")
    ax.set_xticks(range(xmin, xmax + 1))
    ax.set_yticks(range(ymin, ymax + 1))
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.tick_params(length=3)
    ax.grid(True, zorder=0)
    ax.set_axisbelow(True)
    box = dict(facecolor="white", edgecolor="none", pad=0.2)
    for t in range(xmin, xmax + 1):
        if t != 0 and t % every == 0:
            ax.text(t, -0.18, num(t), ha="center", va="top", fontsize=size, zorder=4, bbox=box)
    for t in range(ymin, ymax + 1):
        if t != 0 and t % every == 0:
            ax.text(-0.18, t, num(t), ha="right", va="center", fontsize=size, zorder=4, bbox=box)
    ax.plot(1, 0, ">", color=fs.DARK, transform=ax.get_yaxis_transform(), clip_on=False, ms=5)
    ax.plot(0, 1, "^", color=fs.DARK, transform=ax.get_xaxis_transform(), clip_on=False, ms=5)
    ax.text(xmax + 0.6, 0.3, "x", ha="right", va="bottom", style="italic", fontsize=12)
    ax.text(0.3, ymax + 0.6, "y", ha="left", va="top", style="italic", fontsize=12)


def mapping_panel(ax, inputs, outputs, arrows, caption, colour):
    ax.set_xlim(0, 10)
    ax.set_ylim(-0.8, 10)
    ax.axis("off")
    ax.add_patch(Ellipse((2.2, 5), 3.0, 8.4, fill=False, ec=fs.DARK, lw=1.2))
    ax.add_patch(Ellipse((7.8, 5), 3.0, 8.4, fill=False, ec=fs.DARK, lw=1.2))
    ax.text(2.2, 9.6, "inputs", ha="center", va="bottom", fontsize=11)
    ax.text(7.8, 9.6, "outputs", ha="center", va="bottom", fontsize=11)

    def ys(n):
        return [5 + 2.4 * ((n - 1) / 2 - i) for i in range(n)]

    in_y = dict(zip(inputs, ys(len(inputs))))
    out_y = dict(zip(outputs, ys(len(outputs))))
    for v, y in in_y.items():
        ax.text(2.2, y, v, ha="center", va="center", fontsize=12)
    for v, y in out_y.items():
        ax.text(7.8, y, v, ha="center", va="center", fontsize=12)
    for a, b in arrows:
        ax.annotate("", xy=(7.1, out_y[b]), xytext=(2.9, in_y[a]),
                    arrowprops=dict(arrowstyle="-|>", color=colour, lw=1.5, shrinkA=2, shrinkB=2))
    ax.text(5, -0.6, caption, ha="center", va="bottom", fontsize=12, color=colour)


def mapping():
    fig, axes = plt.subplots(1, 2, figsize=(6.6, 3.4))
    mapping_panel(
        axes[0], [f"{M}2", f"{M}1", "1", "2"], ["1", "4"],
        [(f"{M}2", "4"), (f"{M}1", "1"), ("1", "1"), ("2", "4")],
        "a function", fs.GREEN,
    )
    mapping_panel(
        axes[1], ["4", "9"], [f"{M}2", "2", f"{M}3", "3"],
        [("4", "2"), ("4", f"{M}2"), ("9", "3"), ("9", f"{M}3")],
        "not a function", fs.RED,
    )
    fig.tight_layout(w_pad=2.0)
    fs.save(fig, FOLDER, f"{SLUG}-mapping")


def vertical_line_test():
    fig, axes = plt.subplots(1, 2, figsize=(6.6, 3.6))
    # A circle of radius 3 fails the test.
    ax = axes[0]
    plane(ax, -4, 4, -4, 4, every=2)
    t = [2 * math.pi * i / 400 for i in range(401)]
    ax.plot([3 * math.cos(s) for s in t], [3 * math.sin(s) for s in t], color=fs.BLUE, zorder=3)
    ax.axvline(2, color=fs.RED, lw=1.4, ls="--", zorder=3)
    h = math.sqrt(5)
    ax.plot([2, 2], [h, -h], "o", color=fs.RED, zorder=5)
    ax.text(0.5, -0.03, "fails: two points on\none vertical line", transform=ax.transAxes,
            ha="center", va="top", fontsize=11, color=fs.RED)
    # The parabola y = x^2 - 3 passes.
    ax = axes[1]
    plane(ax, -4, 4, -4, 4, every=2)
    xs = [-2.7 + 5.4 * i / 300 for i in range(301)]
    ax.plot(xs, [x * x - 3 for x in xs], color=fs.GREEN, zorder=3)
    ax.axvline(2, color=fs.GRAY, lw=1.4, ls="--", zorder=3)
    ax.plot(2, 1, "o", color=fs.GREEN, zorder=5)
    ax.text(0.5, -0.03, "passes: each vertical line\nmeets it at most once", transform=ax.transAxes,
            ha="center", va="top", fontsize=11, color=fs.GREEN)
    fig.tight_layout(w_pad=1.5)
    fs.save(fig, FOLDER, f"{SLUG}-vertical-line-test")


def linear_nonlinear():
    fig, ax = fs.figure(5.2, 4.6)
    plane(ax, -3, 3, -7, 9)
    ax.set_aspect("auto")
    xs = [-3 + 6 * i / 300 for i in range(301)]
    ax.plot([-3.4, 3.4], [2 * -3.4 - 1, 2 * 3.4 - 1], color=fs.BLUE, zorder=3)
    ax.plot(xs, [x * x for x in xs], color=fs.ORANGE, zorder=3)
    table = [-2, -1, 0, 1, 2]
    ax.plot(table, [2 * x - 1 for x in table], "o", color=fs.BLUE, zorder=5)
    ax.plot(table, [x * x for x in table], "o", color=fs.ORANGE, zorder=5)
    ax.text(0.3, 8.0, "g(x) = x²", ha="left", va="center", fontsize=11, color=fs.ORANGE,
            style="italic", bbox=BOX, zorder=6)
    ax.text(1.6, -1.8, f"f(x) = 2x {M} 1", ha="left", va="center", fontsize=11, color=fs.BLUE,
            style="italic", bbox=BOX, zorder=6)
    fs.save(fig, FOLDER, f"{SLUG}-linear-nonlinear")


def tickets():
    fig, ax = fs.figure(4.6, 3.4)
    ns = [0, 1, 2, 3, 4]
    ax.set_xlim(-0.3, 4.5)
    ax.set_ylim(0, 225)
    ax.set_xticks(ns)
    ax.set_yticks(range(0, 226, 51))
    ax.grid(True)
    ax.set_axisbelow(True)
    ax.tick_params(labelsize=9)
    ax.plot(ns, [51 * n for n in ns], "o", color=fs.GREEN, ms=7, zorder=5, clip_on=False)
    ax.set_xlabel("tickets bought")
    ax.set_ylabel("cost (dollars)")
    fs.save(fig, FOLDER, f"{SLUG}-tickets")


if __name__ == "__main__":
    mapping()
    vertical_line_test()
    linear_nonlinear()
    tickets()
