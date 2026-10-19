"""Figures for docs/02-middle-school/06-geometry/01-angles-and-triangles.md."""

import sys
from pathlib import Path

import numpy as np
from matplotlib.patches import Polygon, Wedge

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import figstyle as fs  # noqa: E402

FOLDER = "02-middle-school"
SLUG = "angles-and-triangles"


def blank(ax):
    ax.set_aspect("equal")
    ax.axis("off")


def direction(p, q):
    """Angle in degrees of the ray from p through q."""
    return np.degrees(np.arctan2(q[1] - p[1], q[0] - p[0]))


def angle_mark(ax, c, a1, a2, color, text=None, r=0.45, tr=None, size=13):
    """Shade the angle at c from direction a1 counterclockwise to a2."""
    a1, a2 = a1 % 360, a2 % 360
    if a2 <= a1:
        a2 += 360
    ax.add_patch(Wedge(c, r, a1, a2, facecolor=color, alpha=0.22, edgecolor="none"))
    t = np.radians(np.linspace(a1, a2, 60))
    ax.plot(c[0] + r * np.cos(t), c[1] + r * np.sin(t), color=color, lw=1.6)
    if text:
        mid = np.radians((a1 + a2) / 2)
        tr = tr if tr is not None else r + 0.28
        ax.text(c[0] + tr * np.cos(mid), c[1] + tr * np.sin(mid), text,
                color=color, ha="center", va="center", fontsize=size)


def chevron(ax, p, q, t=0.5, size=0.16, count=1):
    """Arrow marks on segment pq, the sign that lines are parallel."""
    p, q = np.array(p, float), np.array(q, float)
    u = (q - p) / np.linalg.norm(q - p)
    n = np.array([-u[1], u[0]])
    for k in range(count):
        m = p + t * (q - p) + k * 0.18 * u
        ax.plot([m[0] - size * u[0] + size * 0.7 * n[0], m[0], m[0] - size * u[0] - size * 0.7 * n[0]],
                [m[1] - size * u[1] + size * 0.7 * n[1], m[1], m[1] - size * u[1] - size * 0.7 * n[1]],
                color=fs.DARK, lw=1.4)


def vertical_angles():
    fig, ax = fs.figure(4.2, 3.0)
    o = np.array([0.0, 0.0])
    for ang in (20, 130):
        d = np.array([np.cos(np.radians(ang)), np.sin(np.radians(ang))])
        ax.plot(*zip(o - 2.2 * d, o + 2.2 * d), color=fs.DARK, lw=2)
    angle_mark(ax, o, 130, 200, fs.GREEN, r"$\alpha$")
    angle_mark(ax, o, 310, 380, fs.GREEN, r"$\gamma$")
    angle_mark(ax, o, 20, 130, fs.BLUE, r"$\beta$", r=0.38)
    angle_mark(ax, o, 200, 310, fs.BLUE, r"$\delta$", r=0.38)
    ax.text(2.25 * np.cos(np.radians(20)), 2.25 * np.sin(np.radians(20)) + 0.12, "line 1", fontsize=11)
    ax.text(2.2 * np.cos(np.radians(130)) - 0.2, 2.2 * np.sin(np.radians(130)) + 0.1, "line 2", fontsize=11, ha="right")
    blank(ax)
    fs.save(fig, FOLDER, f"{SLUG}-vertical-angles")


def transversal():
    fig, ax = fs.figure(4.8, 3.4)
    y1, y2 = 2.0, 0.0
    ax.plot([-2.6, 2.8], [y1, y1], color=fs.DARK, lw=2)
    ax.plot([-2.6, 2.8], [y2, y2], color=fs.DARK, lw=2)
    chevron(ax, (-2.6, y1), (2.8, y1), t=0.9)
    chevron(ax, (-2.6, y2), (2.8, y2), t=0.9)
    slope = np.radians(62)
    d = np.array([np.cos(slope), np.sin(slope)])
    top = np.array([y1 / np.tan(slope), y1])
    bot = np.array([0.0, y2])
    ax.plot(*zip(bot - 1.15 * d, top + 1.15 * d), color=fs.DARK, lw=2)
    a = 62
    for c, nums in ((top, (1, 2, 3, 4)), (bot, (5, 6, 7, 8))):
        # 1 upper left, 2 upper right, 3 lower left, 4 lower right
        angle_mark(ax, c, a, 180, fs.BLUE, str(nums[0]), r=0.34, tr=0.62, size=12)
        angle_mark(ax, c, 0, a, fs.GREEN, str(nums[1]), r=0.42, tr=0.72, size=12)
        angle_mark(ax, c, 180, 180 + a, fs.GREEN, str(nums[2]), r=0.42, tr=0.72, size=12)
        angle_mark(ax, c, 180 + a, 360, fs.BLUE, str(nums[3]), r=0.34, tr=0.62, size=12)
    ax.text(-2.7, y1, r"$\ell$", ha="right", va="center", fontsize=13)
    ax.text(-2.7, y2, r"$m$", ha="right", va="center", fontsize=13)
    tip = top + 1.15 * d
    ax.text(tip[0] + 0.12, tip[1], r"$t$", fontsize=13, va="center")
    blank(ax)
    fs.save(fig, FOLDER, f"{SLUG}-transversal")


def triangle_sum():
    fig, ax = fs.figure(4.8, 3.0)
    A, B, C = np.array([0.0, 0.0]), np.array([5.0, 0.0]), np.array([1.9, 2.8])
    ax.add_patch(Polygon([A, B, C], closed=True, fill=False, edgecolor=fs.DARK, lw=2))
    ax.plot([-1.0, 6.0], [C[1], C[1]], color=fs.DARK, lw=2)
    chevron(ax, A, B, t=0.62)
    chevron(ax, (-1.0, C[1]), (6.0, C[1]), t=0.8)
    angle_mark(ax, A, 0, direction(A, C), fs.GREEN, r"$\alpha$", r=0.55, tr=0.85)
    angle_mark(ax, B, direction(B, C), 180, fs.BLUE, r"$\beta$", r=0.55, tr=0.85)
    angle_mark(ax, C, direction(C, A), direction(C, B), fs.ORANGE, r"$\gamma$", r=0.45, tr=0.75)
    angle_mark(ax, C, 180, direction(C, A), fs.GREEN, r"$\alpha$", r=0.55, tr=0.85)
    angle_mark(ax, C, direction(C, B), 0, fs.BLUE, r"$\beta$", r=0.55, tr=0.85)
    ax.text(A[0] - 0.15, A[1] - 0.12, "$A$", ha="right", va="top", fontsize=13)
    ax.text(B[0] + 0.15, B[1] - 0.12, "$B$", ha="left", va="top", fontsize=13)
    ax.text(C[0], C[1] + 0.2, "$C$", ha="center", va="bottom", fontsize=13)
    ax.text(6.05, C[1], r"$\ell$", va="center", fontsize=13)
    blank(ax)
    fs.save(fig, FOLDER, f"{SLUG}-triangle-sum")


def exterior_angle():
    fig, ax = fs.figure(4.8, 2.8)
    A, B, C = np.array([0.0, 0.0]), np.array([3.8, 0.0]), np.array([1.2, 2.5])
    ax.add_patch(Polygon([A, B, C], closed=True, fill=False, edgecolor=fs.DARK, lw=2))
    ax.plot([B[0], 6.2], [0, 0], color=fs.DARK, lw=2, ls=(0, (5, 3)))
    angle_mark(ax, A, 0, direction(A, C), fs.GREEN, r"$\alpha$", r=0.5, tr=0.8)
    angle_mark(ax, C, direction(C, A), direction(C, B), fs.ORANGE, r"$\gamma$", r=0.42, tr=0.7)
    angle_mark(ax, B, direction(B, C), 180, fs.BLUE, r"$\beta$", r=0.42, tr=0.7)
    angle_mark(ax, B, 0, direction(B, C), fs.RED, r"$\alpha + \gamma$", r=0.55, tr=1.25)
    ax.text(A[0] - 0.12, -0.12, "$A$", ha="right", va="top", fontsize=13)
    ax.text(B[0], -0.15, "$B$", ha="center", va="top", fontsize=13)
    ax.text(C[0], C[1] + 0.18, "$C$", ha="center", va="bottom", fontsize=13)
    ax.text(6.25, 0, "$D$", va="center", fontsize=13)
    blank(ax)
    fs.save(fig, FOLDER, f"{SLUG}-exterior-angle")


def polygons():
    fig, (ax1, ax2) = fs.plt.subplots(1, 2, figsize=(6.4, 3.0))
    hexagon = np.array([[0, 0], [2.6, -0.3], [3.8, 1.3], [3.1, 3.0], [1.0, 3.3], [-0.6, 1.7]])
    colours = [fs.GREEN, fs.BLUE, fs.ORANGE, fs.RED]
    for k in range(4):
        tri = [hexagon[0], hexagon[k + 1], hexagon[k + 2]]
        ax1.add_patch(Polygon(tri, closed=True, facecolor=colours[k], alpha=0.2, edgecolor="none"))
        cx, cy = np.mean(tri, axis=0)
        ax1.text(cx, cy, str(k + 1), ha="center", va="center", fontsize=13, color=colours[k])
    ax1.add_patch(Polygon(hexagon, closed=True, fill=False, edgecolor=fs.DARK, lw=2))
    for k in (2, 3, 4):
        ax1.plot(*zip(hexagon[0], hexagon[k]), color=fs.DARK, lw=1.2, ls=(0, (4, 3)))
    blank(ax1)
    ax1.set_xlim(-1.0, 4.2)
    ax1.set_ylim(-0.7, 3.7)

    pent = np.array([[0, 0], [2.4, 0], [3.2, 2.0], [1.3, 3.3], [-0.6, 1.9]])
    ax2.add_patch(Polygon(pent, closed=True, facecolor=fs.LIGHT, edgecolor=fs.DARK, lw=2))
    for k in range(5):
        p, q = pent[k], pent[(k + 1) % 5]
        u = (q - p) / np.linalg.norm(q - p)
        ext = q + 1.0 * u
        ax2.plot(*zip(q, ext), color=fs.DARK, lw=1.4, ls=(0, (4, 3)))
        nxt = pent[(k + 2) % 5]
        angle_mark(ax2, q, direction(q, ext), direction(q, nxt), fs.GREEN, r=0.42)
    blank(ax2)
    ax2.set_xlim(-1.7, 4.4)
    ax2.set_ylim(-1.1, 4.3)
    fig.subplots_adjust(wspace=0.15)
    fs.save(fig, FOLDER, f"{SLUG}-polygons")


vertical_angles()
transversal()
triangle_sum()
exterior_angle()
polygons()
