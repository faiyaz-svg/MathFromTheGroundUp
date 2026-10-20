"""Figures for docs/03-high-school/09-trigonometry/02-radians-and-the-unit-circle.md.

Run from the repo root:

    .venv/Scripts/python tools/figures/03-high-school/radians-and-the-unit-circle.py
"""

import math
import sys
from pathlib import Path

import numpy as np
from matplotlib.patches import Arc, Circle

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import figstyle as fs  # noqa: E402

FOLDER = "03-high-school"
SLUG = "radians-and-the-unit-circle"
BOX = dict(facecolor="white", edgecolor="none", pad=0.5, alpha=0.9)


def axes_lines(ax, lim, ticks=True):
    ax.annotate("", xy=(lim, 0), xytext=(-lim, 0), arrowprops=dict(arrowstyle="-|>", color=fs.DARK, lw=1.0))
    ax.annotate("", xy=(0, lim), xytext=(0, -lim), arrowprops=dict(arrowstyle="-|>", color=fs.DARK, lw=1.0))
    ax.text(lim, -0.08 * lim, "$x$", ha="right", va="top", fontsize=11)
    ax.text(0.04 * lim, lim, "$y$", ha="left", va="top", fontsize=11)


def blank(ax):
    ax.set_aspect("equal")
    ax.axis("off")


def radian():
    """The angle that cuts off an arc as long as the radius."""
    fig, ax = fs.figure(4.6, 4.0)
    r = 1.0
    ax.add_patch(Circle((0, 0), r, fill=False, edgecolor=fs.DARK, lw=1.6))
    one = math.degrees(1.0)
    t = np.linspace(0, 1.0, 60)
    ax.plot(np.cos(t), np.sin(t), color=fs.GREEN, lw=4.2, solid_capstyle="butt", zorder=4)
    ax.plot([0, 1], [0, 0], color=fs.DARK, lw=1.8)
    ax.plot([0, math.cos(1)], [0, math.sin(1)], color=fs.DARK, lw=1.8)
    ax.add_patch(Arc((0, 0), 0.7, 0.7, theta1=0, theta2=one, color=fs.DARK, lw=1.2))
    ax.text(0.5, 0.17, r"$\theta = 1$ rad", ha="left", va="center", fontsize=11)
    ax.text(0.5, -0.1, "$r$", ha="center", va="top", fontsize=12)
    ax.text(0.2, 0.36, "$r$", ha="right", va="center", fontsize=12)
    ax.text(0.98, 0.62, "arc length\n$s = r$", ha="left", va="center", fontsize=11, color=fs.GREEN)
    ax.plot([0], [0], "o", color=fs.DARK, ms=4)
    ax.set_xlim(-1.15, 1.9)
    ax.set_ylim(-1.2, 1.2)
    blank(ax)
    fs.save(fig, FOLDER, f"{SLUG}-radian")


def definition():
    """Sine and cosine as the coordinates of a point on the unit circle (second quadrant)."""
    fig, ax = fs.figure(5.0, 4.2)
    th = math.radians(140)
    c, s = math.cos(th), math.sin(th)
    ax.add_patch(Circle((0, 0), 1, fill=False, edgecolor=fs.GRAY, lw=1.4))
    axes_lines(ax, 1.4)
    ax.plot([0, c], [0, s], color=fs.DARK, lw=2)
    ax.plot([c, c], [0, s], color=fs.ORANGE, lw=2.4)
    ax.plot([c, 0], [0, 0], color=fs.BLUE, lw=2.4)
    ax.plot([c], [s], "o", color=fs.DARK, ms=6, zorder=5)
    t = np.linspace(0, th, 80)
    ax.plot(0.28 * np.cos(t), 0.28 * np.sin(t), color=fs.GREEN, lw=1.6)
    ax.text(0.2, 0.24, r"$\theta$", ha="left", va="center", fontsize=12, color=fs.GREEN)
    ax.text(c - 0.05, s + 0.07, r"$P = (\cos\theta,\ \sin\theta)$", ha="right", va="bottom", fontsize=11)
    ax.text(c - 0.06, s / 2, r"$\sin\theta$", ha="right", va="center", fontsize=11, color=fs.ORANGE)
    ax.text(c / 2, -0.08, r"$\cos\theta$ (negative here)", ha="center", va="top", fontsize=10.5, color=fs.BLUE)
    ax.text(0.5 * c - 0.02, 0.5 * s + 0.1, "1", ha="right", va="center", fontsize=11)
    ax.plot([1], [0], "o", color=fs.DARK, ms=4)
    ax.text(1.04, 0.07, "$(1, 0)$", ha="left", va="bottom", fontsize=10)
    ax.set_xlim(-1.5, 1.7)
    ax.set_ylim(-1.2, 1.5)
    blank(ax)
    fs.save(fig, FOLDER, f"{SLUG}-definition")


ANGLES = [
    (0, "0", "(1, 0)"),
    (30, r"$\pi/6$", r"$(\sqrt{3}/2,\ 1/2)$"),
    (45, r"$\pi/4$", r"$(\sqrt{2}/2,\ \sqrt{2}/2)$"),
    (60, r"$\pi/3$", r"$(1/2,\ \sqrt{3}/2)$"),
    (90, r"$\pi/2$", "(0, 1)"),
    (120, r"$2\pi/3$", r"$(-1/2,\ \sqrt{3}/2)$"),
    (135, r"$3\pi/4$", r"$(-\sqrt{2}/2,\ \sqrt{2}/2)$"),
    (150, r"$5\pi/6$", r"$(-\sqrt{3}/2,\ 1/2)$"),
    (180, r"$\pi$", "(−1, 0)"),
    (210, r"$7\pi/6$", r"$(-\sqrt{3}/2,\ -1/2)$"),
    (225, r"$5\pi/4$", r"$(-\sqrt{2}/2,\ -\sqrt{2}/2)$"),
    (240, r"$4\pi/3$", r"$(-1/2,\ -\sqrt{3}/2)$"),
    (270, r"$3\pi/2$", "(0, −1)"),
    (300, r"$5\pi/3$", r"$(1/2,\ -\sqrt{3}/2)$"),
    (315, r"$7\pi/4$", r"$(\sqrt{2}/2,\ -\sqrt{2}/2)$"),
    (330, r"$11\pi/6$", r"$(\sqrt{3}/2,\ -1/2)$"),
]


def unit_circle(kind, width, xlim, size):
    """The special angles around the unit circle: angles only, or exact coordinates only."""
    ylim = 1.42
    fig, ax = fs.figure(width, width * 2 * ylim / (2 * xlim))
    fig.subplots_adjust(left=0, right=1, bottom=0, top=1)
    ax.add_patch(Circle((0, 0), 1, fill=False, edgecolor=fs.DARK, lw=1.5))
    ax.annotate("", xy=(xlim, 0), xytext=(-xlim, 0), arrowprops=dict(arrowstyle="-|>", color=fs.DARK, lw=1.0))
    ax.annotate("", xy=(0, ylim), xytext=(0, -ylim), arrowprops=dict(arrowstyle="-|>", color=fs.DARK, lw=1.0))
    for deg, rad, coords in ANGLES:
        a = math.radians(deg)
        x, y = math.cos(a), math.sin(a)
        ax.plot([0, x], [0, y], color=fs.GRAY, lw=0.8, zorder=1)
        ax.plot([x], [y], "o", color=fs.GREEN, ms=6, zorder=5)
        tx, ty = 1.07 * x, 1.07 * y
        if abs(x) < 0.2:
            ha, va = "center", ("bottom" if y > 0 else "top")
        else:
            ha, va = ("left" if x > 0 else "right"), "center"
        label = f"{deg}$^\\circ$,  {rad}" if kind == "angles" else coords
        ax.text(tx, ty, label, ha=ha, va=va, fontsize=size, bbox=BOX, zorder=6)
    ax.set_xlim(-xlim, xlim)
    ax.set_ylim(-ylim, ylim)
    blank(ax)
    fs.save(fig, FOLDER, f"{SLUG}-circle-{kind}")


if __name__ == "__main__":
    radian()
    definition()
    unit_circle("angles", 5.6, 1.62, 10)
    unit_circle("coords", 6.6, 1.85, 9.5)
