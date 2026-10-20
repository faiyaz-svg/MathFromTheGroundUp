"""Figures for docs/03-high-school/09-trigonometry/01-right-triangle-trigonometry.md.

Run from the repo root:

    .venv/Scripts/python tools/figures/03-high-school/right-triangle-trigonometry.py
"""

import math
import sys
from pathlib import Path

import numpy as np
from matplotlib.patches import Arc, Polygon

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import figstyle as fs  # noqa: E402

FOLDER = "03-high-school"
SLUG = "right-triangle-trigonometry"


def blank(ax):
    ax.set_aspect("equal")
    ax.axis("off")


def right_mark(ax, p, u, v, s=0.25, color=fs.DARK):
    p, u, v = (np.array(a, float) for a in (p, u, v))
    u, v = u / np.linalg.norm(u), v / np.linalg.norm(v)
    ax.plot(*zip(p + s * u, p + s * (u + v), p + s * v), color=color, lw=1.2)


def angle_arc(ax, centre, r, start, end, text, tr, color=fs.DARK, size=12):
    ax.add_patch(Arc(centre, 2 * r, 2 * r, theta1=start, theta2=end, color=color, lw=1.3))
    mid = math.radians((start + end) / 2)
    ax.text(centre[0] + tr * math.cos(mid), centre[1] + tr * math.sin(mid), text,
            ha="center", va="center", fontsize=size, color=color)


def sides():
    """One right triangle with the three sides named from the angle theta."""
    fig, ax = fs.figure(5.2, 3.4)
    A, B, C = np.array([0.0, 0]), np.array([5.0, 0]), np.array([5.0, 3.0])
    ax.add_patch(Polygon([A, B, C], closed=True, facecolor=fs.GREEN, alpha=0.18, edgecolor="none"))
    ax.add_patch(Polygon([A, B, C], closed=True, fill=False, edgecolor=fs.DARK, lw=2))
    right_mark(ax, B, (-1, 0), (0, 1))
    th = math.degrees(math.atan2(3, 5))
    angle_arc(ax, A, 0.9, 0, th, r"$\theta$", 1.25)
    ax.text(2.5, -0.35, "adjacent (next to $\\theta$)", ha="center", va="top", fontsize=11, color=fs.BLUE)
    ax.text(5.2, 1.5, "opposite\n(across from $\\theta$)", ha="left", va="center", fontsize=11, color=fs.ORANGE)
    ax.text(2.35, 1.95, "hypotenuse", ha="center", va="center", fontsize=11, color=fs.RED,
            rotation=th, rotation_mode="anchor")
    ax.set_xlim(-0.6, 7.6)
    ax.set_ylim(-1.0, 3.5)
    blank(ax)
    fs.save(fig, FOLDER, f"{SLUG}-sides")


def similar():
    """Three right triangles with the same angle: the ratios agree."""
    fig, ax = fs.figure(5.6, 3.6)
    th = math.radians(35)
    base = 6.0
    ax.plot([0, base], [0, 0], color=fs.DARK, lw=1.5)
    ax.plot([0, base * math.cos(th) / math.cos(th)], [0, base * math.tan(th)], color=fs.DARK, lw=1.5)
    for L, col in ((2.0, fs.GREEN), (4.0, fs.BLUE), (6.0, fs.ORANGE)):
        top = np.array([L, L * math.tan(th)])
        ax.plot([L, L], [0, top[1]], color=col, lw=2)
        ax.plot([L], [0], "o", color=col, ms=4)
        ax.plot([L], [top[1]], "o", color=col, ms=4)
        ax.text(L + 0.1, top[1] / 2, f"{L * math.tan(th):.2f}", color=col, fontsize=10, ha="left", va="center")
    ax.plot([0, 6.0], [0, 6.0 * math.tan(th)], color=fs.DARK, lw=1.5)
    angle_arc(ax, (0, 0), 0.9, 0, 35, r"$35^\circ$", 1.35, size=11)
    for L, col in ((2.0, fs.GREEN), (4.0, fs.BLUE), (6.0, fs.ORANGE)):
        ax.text(L, -0.3, f"{L:.0f}", color=col, fontsize=10, ha="center", va="top")
    ax.text(3.0, -0.95, "opposite / adjacent is the same in all three:  $\\tan 35^\\circ \\approx 0.70$",
            ha="center", va="center", fontsize=10.5)
    ax.set_xlim(-0.5, 7.0)
    ax.set_ylim(-1.3, 4.6)
    blank(ax)
    fs.save(fig, FOLDER, f"{SLUG}-similar")


def special():
    """The 45-45-90 triangle and the 30-60-90 triangle, built from an equilateral triangle."""
    fig, (ax1, ax2) = fs.plt.subplots(1, 2, figsize=(7.4, 3.5), gridspec_kw={"width_ratios": [1, 1.1]})
    # 45-45-90 with legs 1
    A, B, C = np.array([0.0, 0]), np.array([2.0, 0]), np.array([2.0, 2.0])
    ax1.add_patch(Polygon([A, B, C], closed=True, facecolor=fs.GREEN, alpha=0.18, edgecolor="none"))
    ax1.add_patch(Polygon([A, B, C], closed=True, fill=False, edgecolor=fs.DARK, lw=2))
    right_mark(ax1, B, (-1, 0), (0, 1), s=0.2)
    angle_arc(ax1, A, 0.6, 0, 45, r"$45^\circ$", 0.9, size=11)
    angle_arc(ax1, C, 0.45, 225, 270, r"$45^\circ$", 0.8, size=11)
    ax1.text(1.0, -0.2, "1", ha="center", va="top", fontsize=12)
    ax1.text(2.2, 1.0, "1", ha="left", va="center", fontsize=12)
    ax1.text(0.85, 1.25, r"$\sqrt{2}$", ha="center", va="center", fontsize=12, rotation=45, rotation_mode="anchor")
    ax1.set_xlim(-0.4, 2.8)
    ax1.set_ylim(-0.7, 2.4)
    blank(ax1)
    # equilateral triangle of side 2, cut in half
    P, Q, T, M = np.array([0.0, 0]), np.array([2.0, 0]), np.array([1.0, math.sqrt(3)]), np.array([1.0, 0])
    ax2.add_patch(Polygon([P, Q, T], closed=True, fill=False, edgecolor=fs.GRAY, lw=1.4))
    ax2.add_patch(Polygon([P, M, T], closed=True, facecolor=fs.GREEN, alpha=0.18, edgecolor="none"))
    ax2.add_patch(Polygon([P, M, T], closed=True, fill=False, edgecolor=fs.DARK, lw=2))
    ax2.plot([M[0], T[0]], [M[1], T[1]], color=fs.DARK, lw=2)
    right_mark(ax2, M, (-1, 0), (0, 1), s=0.16)
    angle_arc(ax2, P, 0.45, 0, 60, r"$60^\circ$", 0.72, size=11)
    angle_arc(ax2, T, 0.55, 240, 270, r"$30^\circ$", 0.9, size=11)
    ax2.text(0.5, -0.12, "1", ha="center", va="top", fontsize=12)
    ax2.text(1.5, -0.12, "1", ha="center", va="top", fontsize=12, color=fs.GRAY)
    ax2.text(1.07, 0.87, r"$\sqrt{3}$", ha="left", va="center", fontsize=12)
    ax2.text(0.38, 0.95, "2", ha="right", va="center", fontsize=12)
    ax2.text(1.62, 0.95, "2", ha="left", va="center", fontsize=12, color=fs.GRAY)
    ax2.set_xlim(-0.4, 2.4)
    ax2.set_ylim(-0.6, 2.0)
    blank(ax2)
    fig.tight_layout(w_pad=0.5)
    fs.save(fig, FOLDER, f"{SLUG}-special")


def elevation():
    """Angle of elevation from the ground and angle of depression from the lookout."""
    fig, ax = fs.figure(6.0, 3.6)
    ground_y = 0.0
    x_obs, x_tower = 0.0, 8.0
    h = 4.0
    ax.plot([-0.8, 9.4], [0, 0], color=fs.DARK, lw=1.6)
    ax.plot([x_tower, x_tower], [0, h], color=fs.DARK, lw=3)
    ax.plot([x_obs], [0], "o", color=fs.DARK, ms=6)
    ax.plot([x_tower], [h], "o", color=fs.DARK, ms=6)
    # line of sight
    ax.plot([x_obs, x_tower], [0, h], color=fs.GREEN, lw=2)
    ax.plot([x_obs, x_tower + 0.2], [0, 0], color=fs.GRAY, lw=1.0, ls=(0, (4, 3)))
    ax.plot([x_tower - 8.0, x_tower], [h, h], color=fs.GRAY, lw=1.0, ls=(0, (4, 3)))
    th = math.degrees(math.atan2(h, x_tower - x_obs))
    angle_arc(ax, (x_obs, 0), 1.7, 0, th, "elevation", 2.55, color=fs.GREEN, size=10.5)
    ax.add_patch(Arc((x_tower, h), 6.8, 6.8, theta1=180, theta2=180 + th, color=fs.ORANGE, lw=1.3))
    ax.text(x_tower - 4.7, h - 0.6, "depression", ha="center", va="center", fontsize=10.5, color=fs.ORANGE)
    ax.text(x_obs, -0.35, "observer", ha="center", va="top", fontsize=11)
    ax.text(x_tower + 0.2, h + 0.25, "top of tower", ha="left", va="bottom", fontsize=11)
    ax.text(x_tower + 0.25, h / 2, "height", ha="left", va="center", fontsize=11)
    ax.text(4.0, -0.35, "horizontal distance", ha="center", va="top", fontsize=11, color=fs.GRAY)
    ax.text(4.4, h + 0.2, "horizontal line from the top", ha="center", va="bottom", fontsize=10, color=fs.GRAY)
    ax.set_xlim(-1.0, 10.8)
    ax.set_ylim(-1.0, 5.2)
    blank(ax)
    fs.save(fig, FOLDER, f"{SLUG}-elevation")


if __name__ == "__main__":
    sides()
    similar()
    special()
    elevation()
