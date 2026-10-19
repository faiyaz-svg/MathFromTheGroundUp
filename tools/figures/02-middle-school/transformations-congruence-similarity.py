"""Figures for docs/02-middle-school/06-geometry/05-transformations-congruence-similarity.md."""

import sys
from pathlib import Path

import numpy as np
from matplotlib.patches import Polygon

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import figstyle as fs  # noqa: E402

FOLDER = "02-middle-school"
SLUG = "transformations-congruence-similarity"
DASH = (0, (4, 3))


def grid(ax, xmin, xmax, ymin, ymax):
    ax.set_xlim(xmin - 0.5, xmax + 0.5)
    ax.set_ylim(ymin - 0.5, ymax + 0.5)
    ax.set_xticks([t for t in range(xmin, xmax + 1) if t != 0])
    ax.set_yticks([t for t in range(ymin, ymax + 1) if t != 0])
    ax.tick_params(labelsize=9)
    ax.grid(True)
    ax.set_aspect("equal")
    ax.spines["left"].set_position("zero")
    ax.spines["bottom"].set_position("zero")


def tri(ax, pts, color, names=None, offsets=None, alpha=0.25, ls="-"):
    ax.add_patch(Polygon(pts, closed=True, facecolor=color, alpha=alpha, edgecolor="none", zorder=3))
    ax.add_patch(Polygon(pts, closed=True, fill=False, edgecolor=color, lw=2, ls=ls, zorder=4))
    if names:
        for (x, y), name, (dx, dy) in zip(pts, names, offsets):
            ax.text(x + dx, y + dy, name, color=color, ha="center", va="center", fontsize=12, zorder=5)


def blank(ax):
    ax.set_aspect("equal")
    ax.axis("off")


def right_mark(ax, p, u, v, s=0.25, color=fs.DARK):
    p, u, v = (np.array(a, float) for a in (p, u, v))
    u, v = u / np.linalg.norm(u), v / np.linalg.norm(v)
    ax.plot(*zip(p + s * u, p + s * (u + v), p + s * v), color=color, lw=1.2, zorder=5)


ABC = [(1, 1), (4, 1), (1, 3)]
OFF = [(-0.35, -0.3), (0.35, -0.3), (-0.35, 0.3)]


def translation():
    fig, ax = fs.figure(4.2, 3.4)
    grid(ax, -1, 8, -1, 6)
    tri(ax, ABC, fs.GREEN, ["$A$", "$B$", "$C$"], OFF)
    img = [(x + 3, y + 2) for x, y in ABC]
    tri(ax, img, fs.BLUE, ["$A'$", "$B'$", "$C'$"], [(0.3, -0.35), (0.35, -0.3), (-0.35, 0.3)])
    for p, q in zip(ABC, img):
        ax.annotate("", xy=q, xytext=p, arrowprops=dict(arrowstyle="->", color=fs.GRAY, lw=1.2), zorder=6)
    fs.save(fig, FOLDER, f"{SLUG}-translation")


def reflections():
    fig, ax = fs.figure(4.4, 4.0)
    grid(ax, -5, 5, -4, 4)
    tri(ax, ABC, fs.GREEN, ["$A$", "$B$", "$C$"], OFF)
    my = [(-x, y) for x, y in ABC]
    tri(ax, my, fs.BLUE, ["$A'$", "$B'$", "$C'$"], [(-dx, dy) for dx, dy in OFF])
    mx = [(x, -y) for x, y in ABC]
    tri(ax, mx, fs.ORANGE, ["$A''$", "$B''$", "$C''$"], [(dx, -dy) for dx, dy in OFF])
    ax.plot([1, -1], [3, 3], color=fs.GRAY, lw=1, ls=DASH, zorder=2)
    ax.plot([1, 1], [3, -3], color=fs.GRAY, lw=1, ls=DASH, zorder=2)
    fs.save(fig, FOLDER, f"{SLUG}-reflections")


def rotation():
    fig, ax = fs.figure(4.4, 4.0)
    grid(ax, -5, 5, -4, 5)
    x, y = 4, 2
    # The right triangle O, (x, 0), P and its image after a 90 degree turn.
    tri(ax, [(0, 0), (x, 0), (x, y)], fs.GREEN, alpha=0.25)
    tri(ax, [(0, 0), (0, x), (-y, x)], fs.BLUE, alpha=0.2)
    tri(ax, [(0, 0), (-x, 0), (-x, -y)], fs.ORANGE, alpha=0.2)
    right_mark(ax, (x, 0), (-1, 0), (0, 1))
    right_mark(ax, (0, x), (0, -1), (-1, 0))
    right_mark(ax, (-x, 0), (1, 0), (0, -1))
    for (px, py, t, dx, dy, c) in ((x, y, "$P(4, 2)$", 0.15, 0.25, fs.GREEN),
                                   (-y, x, "$P'(-2, 4)$", -1.1, 0.45, fs.BLUE),
                                   (-x, -y, "$P''(-4, -2)$", 0.0, -0.35, fs.ORANGE)):
        ax.plot(px, py, "o", color=c, ms=6, zorder=6)
        ax.text(px + dx, py + dy, t, color=c, ha="center", va="center", fontsize=11, zorder=6)
    ax.text(x / 2 + 0.6, 0.15, "4", color=fs.GREEN, ha="center", va="bottom", fontsize=11)
    ax.text(x + 0.2, y / 2, "2", color=fs.GREEN, ha="left", va="center", fontsize=11)
    ax.text(0.2, x * 0.75, "4", color=fs.BLUE, ha="left", va="center", fontsize=11)
    ax.text(-y / 2, x + 0.15, "2", color=fs.BLUE, ha="center", va="bottom", fontsize=11)
    t = np.radians(np.linspace(np.degrees(np.arctan2(y, x)), 90 + np.degrees(np.arctan2(y, x)), 40))
    ax.plot(1.3 * np.cos(t), 1.3 * np.sin(t), color=fs.DARK, lw=1.2)
    end = t[-1]
    ax.annotate("", xy=(1.3 * np.cos(end), 1.3 * np.sin(end)),
                xytext=(1.3 * np.cos(end - 0.05), 1.3 * np.sin(end - 0.05)),
                arrowprops=dict(arrowstyle="->", color=fs.DARK, lw=1.2))
    ax.text(0.95, 1.45, r"$90^\circ$", fontsize=11, ha="center", va="bottom")
    fs.save(fig, FOLDER, f"{SLUG}-rotation")


def dilation():
    fig, ax = fs.figure(4.2, 3.2)
    grid(ax, 0, 7, 0, 5)
    small = [(1, 1), (3, 1), (1, 2)]
    big = [(2 * a, 2 * b) for a, b in small]
    for p in big:
        ax.plot([0, p[0] * 1.08], [0, p[1] * 1.08], color=fs.GRAY, lw=1, ls=DASH, zorder=2)
    tri(ax, small, fs.GREEN, ["$A$", "$B$", "$C$"], [(-0.3, -0.3), (0.3, -0.3), (-0.3, 0.25)])
    tri(ax, big, fs.BLUE, ["$A'$", "$B'$", "$C'$"], [(0.35, -0.3), (0.35, -0.3), (-0.35, 0.25)])
    ax.text(-0.25, -0.3, "$O$", fontsize=11, ha="center", va="center")
    fs.save(fig, FOLDER, f"{SLUG}-dilation")


def shadows():
    fig, ax = fs.figure(5.6, 2.8)
    # Tree 10.5 m with shadow 14 m; person 1.8 m with shadow 2.4 m (drawn at the same scale).
    tx, ph = 0.0, 0.0
    tree_h, tree_s = 10.5, 14.0
    per_h, per_s = 1.8, 2.4
    px = 17.0
    ax.plot([-0.5, px + per_s + 0.8], [0, 0], color=fs.DARK, lw=1.5)
    ax.add_patch(Polygon([(tx, 0), (tx + tree_s, 0), (tx, tree_h)], closed=True, facecolor=fs.GREEN,
                         alpha=0.18, edgecolor="none"))
    ax.plot([tx, tx], [0, tree_h], color=fs.GREEN, lw=3)
    ax.plot([tx, tx + tree_s], [tree_h, 0], color=fs.ORANGE, lw=1.4, ls=DASH)
    ax.plot([tx, tx + tree_s], [0, 0], color=fs.DARK, lw=3)
    ax.add_patch(Polygon([(px, 0), (px + per_s, 0), (px, per_h)], closed=True, facecolor=fs.BLUE,
                         alpha=0.18, edgecolor="none"))
    ax.plot([px, px], [0, per_h], color=fs.BLUE, lw=3)
    ax.plot([px, px + per_s], [per_h, 0], color=fs.ORANGE, lw=1.4, ls=DASH)
    ax.plot([px, px + per_s], [0, 0], color=fs.DARK, lw=3)
    right_mark(ax, (tx, 0), (1, 0), (0, 1), s=0.6)
    right_mark(ax, (px, 0), (1, 0), (0, 1), s=0.35)
    ax.text(tx - 0.3, tree_h / 2, "tree", color=fs.GREEN, ha="right", va="center", fontsize=11)
    ax.text(tx + tree_s / 2, -0.4, "14 m shadow", ha="center", va="top", fontsize=11)
    ax.text(px - 0.3, per_h / 2 + 0.3, "1.8 m", color=fs.BLUE, ha="right", va="center", fontsize=11)
    ax.text(px + per_s / 2, -0.4, "2.4 m", ha="center", va="top", fontsize=11)
    ax.text(tx + tree_s * 0.55, tree_h * 0.5, "sun's rays", color=fs.ORANGE, ha="left", va="bottom",
            fontsize=10, rotation=np.degrees(np.arctan2(-tree_h, tree_s)), rotation_mode="anchor")
    blank(ax)
    fs.save(fig, FOLDER, f"{SLUG}-shadows")


def nested():
    fig, ax = fs.figure(3.8, 3.0)
    A, B, C = np.array([1.2, 3.0]), np.array([0.0, 0.0]), np.array([5.0, 0.0])
    t = 0.4
    D, E = A + t * (B - A), A + t * (C - A)
    ax.add_patch(Polygon([A, D, E], closed=True, facecolor=fs.GREEN, alpha=0.25, edgecolor="none"))
    ax.add_patch(Polygon([A, B, C], closed=True, fill=False, edgecolor=fs.DARK, lw=2))
    ax.plot(*zip(D, E), color=fs.GREEN, lw=2)
    for p, q in ((D, E), (B, C)):
        m = p + 0.55 * (q - p)
        ax.plot([m[0] - 0.12, m[0], m[0] - 0.12], [m[1] + 0.09, m[1], m[1] - 0.09], color=fs.DARK, lw=1.4)
    for p, name, d in ((A, "$A$", (0, 0.2)), (B, "$B$", (-0.2, -0.15)), (C, "$C$", (0.2, -0.15)),
                       (D, "$D$", (-0.25, 0.05)), (E, "$E$", (0.25, 0.05))):
        ax.text(p[0] + d[0], p[1] + d[1], name, ha="center", va="center", fontsize=13)
    blank(ax)
    fs.save(fig, FOLDER, f"{SLUG}-nested")


translation()
reflections()
rotation()
dilation()
shadows()
nested()
