"""Figures for docs/02-middle-school/06-geometry/03-volume-and-surface-area.md.

Solids are drawn in oblique projection: x across, z up, and depth y drawn
at 35 degrees, shortened by half. Hidden edges are dashed.
"""

import sys
from pathlib import Path

import numpy as np
from matplotlib.patches import Circle, Polygon, Rectangle, Wedge

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import figstyle as fs  # noqa: E402

FOLDER = "02-middle-school"
SLUG = "volume-and-surface-area"
DASH = (0, (4, 3))
K, ANG = 0.5, np.radians(35)


def P(x, y, z):
    """Project a 3D point to the page."""
    return np.array([x + K * np.cos(ANG) * y, z + K * np.sin(ANG) * y])


def blank(ax):
    ax.set_aspect("equal")
    ax.axis("off")


def seg(ax, a, b, hidden=False, color=fs.DARK, lw=1.8):
    ax.plot(*zip(a, b), color=color, lw=lw if not hidden else 1.2, ls=DASH if hidden else "-")


def fill(ax, pts, color, alpha=0.25):
    ax.add_patch(Polygon(pts, closed=True, facecolor=color, alpha=alpha, edgecolor="none"))


def right_mark(ax, p, u, v, s=0.18):
    p, u, v = (np.array(a, float) for a in (p, u, v))
    u, v = u / np.linalg.norm(u), v / np.linalg.norm(v)
    ax.plot(*zip(p + s * u, p + s * (u + v), p + s * v), color=fs.DARK, lw=1.1)


def box(ax, xy, w, h, color):
    ax.add_patch(Rectangle(xy, w, h, facecolor=color, alpha=0.22, edgecolor="none"))
    ax.add_patch(Rectangle(xy, w, h, fill=False, edgecolor=fs.DARK, lw=1.4))


def disk(ax, c, r, color):
    ax.add_patch(Circle(c, r, facecolor=color, alpha=0.22, edgecolor="none"))
    ax.add_patch(Circle(c, r, fill=False, edgecolor=fs.DARK, lw=1.4))


def ellipse_pts(cx, cy, rx, ry, t0, t1, n=80):
    t = np.radians(np.linspace(t0, t1, n))
    return cx + rx * np.cos(t), cy + ry * np.sin(t)


def prism_cylinder():
    fig, (ax1, ax2) = fs.plt.subplots(1, 2, figsize=(6.4, 3.0))
    # Triangular prism: base triangle in the x-y plane, height h up.
    h = 2.2
    base = [(0, 0, 0), (2.4, 0, 0), (0.9, 2.2, 0)]
    bot = [P(*q) for q in base]
    top = [P(x, y, z + h) for x, y, z in base]
    fill(ax1, bot, fs.GREEN, 0.3)
    fill(ax1, top, fs.GREEN, 0.3)
    seg(ax1, bot[0], bot[1])
    seg(ax1, bot[1], bot[2], hidden=True)
    seg(ax1, bot[2], bot[0], hidden=True)
    for k in range(3):
        seg(ax1, top[k], top[(k + 1) % 3])
    seg(ax1, bot[0], top[0])
    seg(ax1, bot[1], top[1])
    seg(ax1, bot[2], top[2], hidden=True)
    c = np.mean(bot, axis=0)
    ax1.text(c[0], c[1] + 0.02, "$B$", color=fs.GREEN, ha="center", va="center", fontsize=13)
    ax1.annotate("", xy=(bot[1][0] + 0.25, bot[1][1]), xytext=(bot[1][0] + 0.25, top[1][1]),
                 arrowprops=dict(arrowstyle="<->", color=fs.DARK, lw=1.2))
    ax1.text(bot[1][0] + 0.35, (bot[1][1] + top[1][1]) / 2, "$h$", va="center", fontsize=13)
    ax1.set_xlim(-0.3, 3.4)
    ax1.set_ylim(-0.4, 3.4)
    blank(ax1)

    # Cylinder.
    r, ry, h = 1.0, 0.32, 2.2
    x, y = ellipse_pts(0, 0, r, ry, 180, 360)
    ax2.plot(x, y, color=fs.DARK, lw=1.8)
    x, y = ellipse_pts(0, 0, r, ry, 0, 180)
    ax2.plot(x, y, color=fs.DARK, lw=1.2, ls=DASH)
    x, y = ellipse_pts(0, h, r, ry, 0, 360)
    ax2.fill(x, y, color=fs.GREEN, alpha=0.3, lw=0)
    ax2.plot(x, y, color=fs.DARK, lw=1.8)
    x, y = ellipse_pts(0, 0, r, ry, 0, 360)
    ax2.fill(x, y, color=fs.GREEN, alpha=0.18, lw=0)
    seg(ax2, (-r, 0), (-r, h))
    seg(ax2, (r, 0), (r, h))
    seg(ax2, (0, h), (r, h), color=fs.BLUE)
    ax2.plot(0, h, "o", color=fs.DARK, ms=3)
    ax2.text(r / 2, h + 0.08, "$r$", color=fs.BLUE, ha="center", va="bottom", fontsize=13)
    ax2.text(0, 0.0, "$B$", color=fs.GREEN, ha="center", va="center", fontsize=13)
    ax2.annotate("", xy=(r + 0.25, 0), xytext=(r + 0.25, h),
                 arrowprops=dict(arrowstyle="<->", color=fs.DARK, lw=1.2))
    ax2.text(r + 0.35, h / 2, "$h$", va="center", fontsize=13)
    ax2.set_xlim(-1.4, 1.9)
    ax2.set_ylim(-0.6, 3.0)
    blank(ax2)
    fs.save(fig, FOLDER, f"{SLUG}-prism-cylinder")


def pyramid_cone():
    fig, (ax1, ax2) = fs.plt.subplots(1, 2, figsize=(6.4, 3.0))
    s, h = 2.4, 2.4
    base = [(0, 0, 0), (s, 0, 0), (s, s, 0), (0, s, 0)]
    b = [P(*q) for q in base]
    apex = P(s / 2, s / 2, h)
    foot = P(s / 2, s / 2, 0)
    fill(ax1, b, fs.GREEN, 0.25)
    seg(ax1, b[0], b[1])
    seg(ax1, b[1], b[2])
    seg(ax1, b[2], b[3], hidden=True)
    seg(ax1, b[3], b[0], hidden=True)
    for k in (0, 1, 2):
        seg(ax1, apex, b[k])
    seg(ax1, apex, b[3], hidden=True)
    ax1.plot(*zip(apex, foot), color=fs.RED, lw=1.4, ls=DASH)
    right_mark(ax1, foot, (1, 0), (0, 1), s=0.15)
    ax1.text(foot[0] - 0.1, (foot[1] + apex[1]) / 2 + 0.2, "$h$", color=fs.RED, fontsize=13, va="center", ha="right")
    ax1.text(b[0][0] + 0.55, b[0][1] + 0.18, "$B$", color=fs.GREEN, fontsize=13, ha="center", va="center")
    ax1.set_xlim(-0.3, 3.6)
    ax1.set_ylim(-0.3, 3.0)
    blank(ax1)

    r, ry, h = 1.1, 0.33, 2.4
    x, y = ellipse_pts(0, 0, r, ry, 180, 360)
    ax2.plot(x, y, color=fs.DARK, lw=1.8)
    x, y = ellipse_pts(0, 0, r, ry, 0, 180)
    ax2.plot(x, y, color=fs.DARK, lw=1.2, ls=DASH)
    x, y = ellipse_pts(0, 0, r, ry, 0, 360)
    ax2.fill(x, y, color=fs.GREEN, alpha=0.25, lw=0)
    seg(ax2, (-r, 0), (0, h))
    seg(ax2, (r, 0), (0, h))
    ax2.plot([0, 0], [0, h], color=fs.RED, lw=1.4, ls=DASH)
    right_mark(ax2, (0, 0), (1, 0), (0, 1), s=0.15)
    ax2.plot([0, r], [0, 0], color=fs.BLUE, lw=1.6)
    ax2.text(r / 2, -0.06, "$r$", color=fs.BLUE, ha="center", va="top", fontsize=13)
    ax2.text(-0.1, h * 0.55, "$h$", color=fs.RED, ha="right", va="center", fontsize=13)
    ax2.text(r / 2 + 0.2, h / 2 + 0.05, r"$\ell$", color=fs.DARK, ha="left", va="center", fontsize=14)
    ax2.set_xlim(-1.5, 1.6)
    ax2.set_ylim(-0.6, 2.7)
    blank(ax2)
    fs.save(fig, FOLDER, f"{SLUG}-pyramid-cone")


def cube_pyramids():
    fig, axes = fs.plt.subplots(1, 3, figsize=(6.6, 2.4))
    s = 2.0
    V = {(i, j, k): P(i * s, j * s, k * s) for i in (0, 1) for j in (0, 1) for k in (0, 1)}
    apex = (0, 0, 1)  # the top front left corner
    edges = [((0, 0, 0), (1, 0, 0)), ((1, 0, 0), (1, 1, 0)), ((1, 1, 0), (0, 1, 0)), ((0, 1, 0), (0, 0, 0)),
             ((0, 0, 1), (1, 0, 1)), ((1, 0, 1), (1, 1, 1)), ((1, 1, 1), (0, 1, 1)), ((0, 1, 1), (0, 0, 1)),
             ((0, 0, 0), (0, 0, 1)), ((1, 0, 0), (1, 0, 1)), ((1, 1, 0), (1, 1, 1)), ((0, 1, 0), (0, 1, 1))]
    bases = [
        ([(0, 0, 0), (1, 0, 0), (1, 1, 0), (0, 1, 0)], fs.GREEN, "bottom face"),
        ([(1, 0, 0), (1, 1, 0), (1, 1, 1), (1, 0, 1)], fs.BLUE, "right face"),
        ([(0, 1, 0), (1, 1, 0), (1, 1, 1), (0, 1, 1)], fs.ORANGE, "back face"),
    ]
    for ax, (face, col, name) in zip(axes, bases):
        for a, b in edges:
            ax.plot(*zip(V[a], V[b]), color=fs.GRAY, lw=0.9)
        pts = [V[q] for q in face]
        fill(ax, pts, col, 0.35)
        ax.add_patch(Polygon(pts, closed=True, fill=False, edgecolor=col, lw=1.8))
        for q in face:
            if q != apex:
                ax.plot(*zip(V[apex], V[q]), color=fs.DARK, lw=1.5)
        ax.plot(*V[apex], "o", color=fs.RED, ms=5)
        ax.text(V[(1, 0, 0)][0] / 2 + 0.5, -0.25, name, ha="center", va="top", fontsize=10, color=fs.DARK)
        ax.set_xlim(-0.2, 3.0)
        ax.set_ylim(-0.7, 2.8)
        blank(ax)
    axes[0].text(V[apex][0] - 0.08, V[apex][1] + 0.08, "apex", color=fs.RED, ha="right", va="bottom", fontsize=10)
    fs.save(fig, FOLDER, f"{SLUG}-cube-pyramids")


def nets():
    fig, (ax1, ax2) = fs.plt.subplots(1, 2, figsize=(6.6, 3.0), gridspec_kw={"width_ratios": [1.25, 1]})
    l, w, h = 2.0, 1.2, 0.8
    # Cross-shaped net of an l by w by h box: a row of four side faces, plus top and bottom.
    xs = [0, h, h + l, 2 * h + l, 2 * h + 2 * l]
    row = [(xs[k], w, xs[k + 1] - xs[k]) for k in range(4)]
    cols = [fs.BLUE, fs.GREEN, fs.BLUE, fs.GREEN]
    for (x0, hh, ww), col in zip(row, cols):
        box(ax1, (x0, h), ww, w, col)
    for y0 in (0, h + w):
        box(ax1, (h, y0), l, h, fs.ORANGE)
    ax1.text(h + l / 2, h + w / 2, "$l \\times w$", ha="center", va="center", fontsize=11)
    ax1.text(h / 2, h + w / 2, "$h \\times w$", ha="center", va="center", fontsize=9, rotation=90)
    ax1.text(h + l / 2, h / 2, "$l \\times h$", ha="center", va="center", fontsize=11)
    ax1.text(h + l / 2, -0.12, "$l$", ha="center", va="top", fontsize=12)
    ax1.text(h - 0.08, h / 2, "$h$", ha="right", va="center", fontsize=12)
    ax1.text(-0.08, h + w / 2, "$w$", ha="right", va="center", fontsize=12)
    ax1.set_xlim(-0.4, 2 * h + 2 * l + 0.2)
    ax1.set_ylim(-0.5, 2 * h + w + 0.2)
    blank(ax1)

    r, hc = 0.55, 1.6
    circ = 2 * np.pi * r
    box(ax2, (0, 0), circ, hc, fs.GREEN)
    for cy in (hc + r, -r):
        disk(ax2, (circ / 2, cy), r, fs.ORANGE)
    ax2.plot([circ / 2, circ / 2 + r], [hc + r, hc + r], color=fs.BLUE, lw=1.5)
    ax2.text(circ / 2 + r / 2, hc + r + 0.05, "$r$", color=fs.BLUE, ha="center", va="bottom", fontsize=12)
    ax2.text(circ / 2, hc / 2, r"$2\pi r$ by $h$", ha="center", va="center", fontsize=11)
    ax2.text(circ + 0.1, hc / 2, "$h$", ha="left", va="center", fontsize=12)
    ax2.text(circ / 2 + r + 0.12, -r - 0.05, r"$2\pi r$ around", ha="left", va="center", fontsize=10)
    ax2.set_xlim(-0.2, circ + 1.0)
    ax2.set_ylim(-2 * r - 0.2, hc + 2 * r + 0.2)
    blank(ax2)
    fs.save(fig, FOLDER, f"{SLUG}-nets")


def cone_net():
    fig, ax = fs.figure(4.2, 2.8)
    ell, r = 2.0, 0.8
    theta = 360 * r / ell
    a0 = 90 - theta / 2
    ax.add_patch(Wedge((0, 0), ell, a0, a0 + theta, facecolor=fs.GREEN, alpha=0.22, edgecolor="none"))
    for a in (a0, a0 + theta):
        ax.plot([0, ell * np.cos(np.radians(a))], [0, ell * np.sin(np.radians(a))], color=fs.DARK, lw=1.5)
    t = np.radians(np.linspace(a0, a0 + theta, 60))
    ax.plot(ell * np.cos(t), ell * np.sin(t), color=fs.RED, lw=3)
    ax.text(0, ell + 0.12, r"arc $2\pi r$", color=fs.RED, ha="center", va="bottom", fontsize=11)
    m = np.radians(a0 + theta)
    ax.text(0.5 * ell * np.cos(m) - 0.1, 0.5 * ell * np.sin(m) + 0.05, r"$\ell$", ha="right", va="bottom", fontsize=14)
    disk(ax, (ell + 1.1, 0.4), r, fs.ORANGE)
    ax.plot([ell + 1.1, ell + 1.1 + r], [0.4, 0.4], color=fs.BLUE, lw=1.5)
    ax.text(ell + 1.1 + r / 2, 0.45, "$r$", color=fs.BLUE, ha="center", va="bottom", fontsize=12)
    ax.set_xlim(-ell - 0.2, ell + 2.1)
    ax.set_ylim(-0.4, ell + 0.6)
    blank(ax)
    fs.save(fig, FOLDER, f"{SLUG}-cone-net")


prism_cylinder()
pyramid_cone()
cube_pyramids()
nets()
cone_net()
