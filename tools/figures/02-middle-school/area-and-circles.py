"""Figures for docs/02-middle-school/06-geometry/02-area-and-circles.md."""

import sys
from pathlib import Path

import numpy as np
from matplotlib.patches import Circle, Polygon, Wedge

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import figstyle as fs  # noqa: E402

FOLDER = "02-middle-school"
SLUG = "area-and-circles"


def blank(ax):
    ax.set_aspect("equal")
    ax.axis("off")


def shape(ax, pts, face="none", alpha=1.0, edge=fs.DARK, lw=2, ls="-"):
    ax.add_patch(Polygon(pts, closed=True, facecolor=face, alpha=alpha, edgecolor="none"))
    ax.add_patch(Polygon(pts, closed=True, fill=False, edgecolor=edge, lw=lw, ls=ls))


def right_mark(ax, p, u, v, s=0.22):
    p, u, v = (np.array(a, float) for a in (p, u, v))
    u, v = u / np.linalg.norm(u), v / np.linalg.norm(v)
    pts = [p + s * u, p + s * (u + v), p + s * v]
    ax.plot(*zip(*pts), color=fs.DARK, lw=1.2)


def height_line(ax, top, bottom_y, label, side="right"):
    ax.plot([top[0], top[0]], [bottom_y, top[1]], color=fs.DARK, lw=1.3, ls=(0, (4, 3)))
    right_mark(ax, (top[0], bottom_y), (1 if side == "right" else -1, 0), (0, 1))
    dx = 0.15 if side == "right" else -0.15
    ax.text(top[0] + dx, (bottom_y + top[1]) / 2, label, ha="left" if side == "right" else "right",
            va="center", fontsize=13)


def parallelogram():
    fig, (ax1, ax2) = fs.plt.subplots(1, 2, figsize=(6.6, 2.4))
    b, h, s = 4.0, 2.2, 1.3
    para = [(0, 0), (b, 0), (b + s, h), (s, h)]
    shape(ax1, para)
    shape(ax1, [(0, 0), (s, 0), (s, h)], face=fs.GREEN, alpha=0.3, edge=fs.GREEN, lw=1.2)
    height_line(ax1, (s, h), 0, "$h$")
    ax1.text(b / 2 + 0.4, -0.25, "$b$", ha="center", va="top", fontsize=13)
    ax1.set_xlim(-0.3, b + s + 0.3)
    ax1.set_ylim(-0.7, h + 0.3)
    blank(ax1)

    shape(ax2, [(s, 0), (b + s, 0), (b + s, h), (s, h)])
    shape(ax2, [(b, 0), (b + s, 0), (b + s, h)], face=fs.GREEN, alpha=0.3, edge=fs.GREEN, lw=1.2)
    ax2.plot([b, b + s], [0, h], color=fs.GREEN, lw=1.2)
    right_mark(ax2, (s, 0), (1, 0), (0, 1))
    ax2.text(s + b / 2, -0.25, "$b$", ha="center", va="top", fontsize=13)
    ax2.text(s - 0.15, h / 2, "$h$", ha="right", va="center", fontsize=13)
    ax2.set_xlim(-0.3, b + s + 0.3)
    ax2.set_ylim(-0.7, h + 0.3)
    blank(ax2)
    ax1.annotate("", xy=(1.05, 0.5), xytext=(0.93, 0.5), xycoords="axes fraction",
                 arrowprops=dict(arrowstyle="->", color=fs.DARK, lw=1.5))
    fs.save(fig, FOLDER, f"{SLUG}-parallelogram")


def triangle():
    fig, ax = fs.figure(4.4, 2.3)
    b, h, top = 4.0, 2.2, 1.2
    shape(ax, [(0, 0), (b, 0), (top, h)], face=fs.GREEN, alpha=0.3)
    shape(ax, [(b, 0), (b + top, h), (top, h)], face=fs.BLUE, alpha=0.18, ls=(0, (5, 3)))
    height_line(ax, (top, h), 0, "$h$", side="left")
    ax.text(b / 2, -0.22, "$b$", ha="center", va="top", fontsize=13)
    ax.text(top + b / 2, h + 0.15, "$b$", ha="center", va="bottom", fontsize=13)
    blank(ax)
    fs.save(fig, FOLDER, f"{SLUG}-triangle")


def trapezoid():
    fig, ax = fs.figure(6.0, 2.4)
    b1, b2, h, off = 4.0, 2.2, 2.0, 0.8
    trap = [(0, 0), (b1, 0), (off + b2, h), (off, h)]
    # The copy, turned 180 degrees and fitted against the slanted right side.
    copy = [(b1, 0), (b1 + b2, 0), (off + b2 + b1, h), (off + b2, h)]
    shape(ax, trap, face=fs.GREEN, alpha=0.3)
    shape(ax, copy, face=fs.BLUE, alpha=0.18, ls=(0, (5, 3)))
    height_line(ax, (off + 1.1, h), 0, "$h$")
    ax.text(b1 / 2, -0.22, "$b_1$", ha="center", va="top", fontsize=13, color=fs.GREEN)
    ax.text(b1 + b2 / 2, -0.22, "$b_2$", ha="center", va="top", fontsize=13, color=fs.BLUE)
    ax.text(off + b2 / 2, h + 0.15, "$b_2$", ha="center", va="bottom", fontsize=13, color=fs.GREEN)
    ax.text(off + b2 + b1 / 2, h + 0.15, "$b_1$", ha="center", va="bottom", fontsize=13, color=fs.BLUE)
    blank(ax)
    fs.save(fig, FOLDER, f"{SLUG}-trapezoid")


def circle_parts():
    fig, (ax1, ax2) = fs.plt.subplots(1, 2, figsize=(6.4, 3.0))
    r = 1.0
    ax1.add_patch(Circle((0, 0), r, fill=False, edgecolor=fs.ORANGE, lw=2.5))
    ax2.add_patch(Circle((0, 0), r, fill=False, edgecolor=fs.DARK, lw=2))
    for ax in (ax1, ax2):
        ax.plot(0, 0, "o", color=fs.DARK, ms=4)
    ax1.plot([-r, r], [0, 0], color=fs.BLUE, lw=2)
    ax1.text(0, -0.08, "$d$", color=fs.BLUE, ha="center", va="top", fontsize=13)
    a = np.radians(60)
    ax1.plot([0, r * np.cos(a)], [0, r * np.sin(a)], color=fs.GREEN, lw=2)
    ax1.text(0.5 * np.cos(a) - 0.12, 0.5 * np.sin(a) + 0.06, "$r$", color=fs.GREEN, ha="right",
             va="bottom", fontsize=13)
    ax1.text(0.06, 0.06, "$O$", fontsize=12, ha="left", va="bottom")
    ax1.text(-0.8, -0.8, "$C$", color=fs.ORANGE, fontsize=13, ha="right", va="top")
    ax1.set_xlim(-1.35, 1.35)
    ax1.set_ylim(-1.3, 1.3)
    blank(ax1)

    a1, a2 = 20, 95
    ax2.add_patch(Wedge((0, 0), r, a1, a2, facecolor=fs.GREEN, alpha=0.3, edgecolor="none"))
    for ang in (a1, a2):
        ax2.plot([0, r * np.cos(np.radians(ang))], [0, r * np.sin(np.radians(ang))], color=fs.DARK, lw=1.6)
    t = np.radians(np.linspace(a1, a2, 40))
    ax2.plot(r * np.cos(t), r * np.sin(t), color=fs.RED, lw=3.5)
    t = np.radians(np.linspace(a1, a2, 40))
    ax2.plot(0.25 * np.cos(t), 0.25 * np.sin(t), color=fs.DARK, lw=1.3)
    mid = np.radians((a1 + a2) / 2)
    ax2.text(0.38 * np.cos(mid), 0.38 * np.sin(mid), r"$\theta$", ha="center", va="center", fontsize=13)
    ax2.text(1.12 * np.cos(mid), 1.12 * np.sin(mid), "arc", color=fs.RED, ha="center", va="center",
             fontsize=12)
    ax2.text(0.66 * np.cos(mid), 0.66 * np.sin(mid), "sector", color=fs.GREEN, ha="center",
             va="center", fontsize=11)
    ax2.set_xlim(-1.35, 1.35)
    ax2.set_ylim(-1.3, 1.3)
    blank(ax2)
    fs.save(fig, FOLDER, f"{SLUG}-circle-parts")


def sector_wedge(apex, centre_dir, delta, r):
    t = np.radians(np.linspace(centre_dir - delta / 2, centre_dir + delta / 2, 20))
    arc = np.column_stack([apex[0] + r * np.cos(t), apex[1] + r * np.sin(t)])
    return np.vstack([apex, arc])


def circle_sectors():
    n, r = 16, 1.0
    delta = 360 / n
    fig, (ax1, ax2) = fs.plt.subplots(1, 2, figsize=(6.8, 2.4), gridspec_kw={"width_ratios": [1, 1.9]})
    for k in range(n):
        c = 90 + delta / 2 + k * delta  # sector centres; top half first
        top_half = np.sin(np.radians(c)) > 0
        col = fs.GREEN if top_half else fs.BLUE
        pts = sector_wedge((0, 0), c, delta, r)
        shape(ax1, pts, face=col, alpha=0.3, edge=fs.DARK, lw=0.8)
    ax1.set_xlim(-1.15, 1.15)
    ax1.set_ylim(-1.15, 1.15)
    blank(ax1)

    w = r * np.sin(np.radians(delta / 2))
    h = r * np.cos(np.radians(delta / 2))
    for k in range(n):
        if k % 2 == 0:  # arc on top, apex at the bottom: from the top half
            apex = (k * w + w, 0.0)
            pts = sector_wedge(apex, 90, delta, r)
            col = fs.GREEN
        else:  # arc on the bottom, apex at the top
            apex = (k * w + w, h)
            pts = sector_wedge(apex, -90, delta, r)
            col = fs.BLUE
        shape(ax2, pts, face=col, alpha=0.3, edge=fs.DARK, lw=0.8)
    right = n * w + w
    ax2.annotate("", xy=(w, -0.22), xytext=(right - w, -0.22),
                 arrowprops=dict(arrowstyle="<->", color=fs.DARK, lw=1.2))
    ax2.text((right) / 2, -0.3, r"about $\pi r$ (half the circumference)", ha="center", va="top", fontsize=11)
    ax2.annotate("", xy=(-0.12, 0), xytext=(-0.12, h),
                 arrowprops=dict(arrowstyle="<->", color=fs.DARK, lw=1.2))
    ax2.text(-0.22, h / 2, "about $r$", ha="right", va="center", fontsize=11)
    ax2.set_xlim(-1.2, right + 0.2)
    ax2.set_ylim(-0.75, h + 0.25)
    blank(ax2)
    fs.save(fig, FOLDER, f"{SLUG}-sectors")


parallelogram()
triangle()
trapezoid()
circle_parts()
circle_sectors()
