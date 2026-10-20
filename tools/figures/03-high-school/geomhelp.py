"""Small drawing helpers shared by the geometry-and-proof figure scripts (chapter 8)."""

import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import numpy as np  # noqa: E402
from matplotlib.patches import Arc, Polygon  # noqa: E402

import figstyle as fs  # noqa: E402

FOLDER = "03-high-school"
BOX = dict(facecolor="white", edgecolor="none", pad=0.5, alpha=0.9)


def canvas(width, height, xlim, ylim):
    fig, ax = fs.figure(width, height)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    return fig, ax


def seg(ax, p, q, color=fs.DARK, lw=2.0, ls="-", z=3):
    ax.plot([p[0], q[0]], [p[1], q[1]], color=color, lw=lw, ls=ls, zorder=z, solid_capstyle="round")


def poly(ax, pts, face=None, edge=fs.DARK, alpha=0.15, lw=2.0, z=2):
    if face is not None:
        ax.add_patch(Polygon(pts, closed=True, facecolor=face, alpha=alpha, edgecolor="none", zorder=z))
    ax.add_patch(Polygon(pts, closed=True, fill=False, edgecolor=edge, lw=lw, zorder=z + 1, joinstyle="round"))


def dot(ax, p, color=fs.DARK, size=5):
    ax.plot(p[0], p[1], "o", color=color, ms=size, zorder=6)


def name(ax, p, text, off=(0.0, 0.0), size=12, color=fs.DARK, ha="center", va="center", box=False, style="italic"):
    ax.text(p[0] + off[0], p[1] + off[1], text, ha=ha, va=va, fontsize=size, color=color,
            style=style, zorder=7, bbox=BOX if box else None)


def label(ax, xy, text, size=10.5, color=fs.DARK, ha="center", va="center", box=True, style="normal"):
    ax.text(xy[0], xy[1], text, ha=ha, va=va, fontsize=size, color=color, style=style,
            zorder=8, bbox=BOX if box else None)


def tick(ax, p, q, n=1, color=fs.DARK, size=0.11, gap=0.09):
    """n short tick marks across the middle of segment pq (equal-side marks)."""
    mx, my = (p[0] + q[0]) / 2, (p[1] + q[1]) / 2
    dx, dy = q[0] - p[0], q[1] - p[1]
    L = math.hypot(dx, dy)
    ux, uy = dx / L, dy / L
    nx, ny = -uy, ux
    for i in range(n):
        o = (i - (n - 1) / 2) * gap
        cx, cy = mx + ux * o, my + uy * o
        ax.plot([cx - nx * size, cx + nx * size], [cy - ny * size, cy + ny * size],
                color=color, lw=1.6, zorder=6)


def arc(ax, v, p1, p2, r=0.45, n=1, color=fs.GREEN, text=None, text_r=None, size=10.5, fill=True):
    """n concentric arcs for the angle at v between directions to p1 and p2."""
    a1 = math.degrees(math.atan2(p1[1] - v[1], p1[0] - v[0])) % 360
    a2 = math.degrees(math.atan2(p2[1] - v[1], p2[0] - v[0])) % 360
    d = (a2 - a1) % 360
    if d > 180:
        a1, d = a2, 360 - d
    for i in range(n):
        rr = r + 0.07 * i
        ax.add_patch(Arc(v, 2 * rr, 2 * rr, theta1=a1, theta2=a1 + d, color=color, lw=1.8, zorder=5))
    if text:
        tr = text_r if text_r else r + 0.07 * (n - 1) + 0.28
        m = math.radians(a1 + d / 2)
        ax.text(v[0] + tr * math.cos(m), v[1] + tr * math.sin(m), text, ha="center", va="center",
                fontsize=size, color=color, zorder=8)


def right_angle(ax, v, p1, p2, s=0.22, color=fs.DARK):
    u1 = np.array(p1, float) - np.array(v, float)
    u2 = np.array(p2, float) - np.array(v, float)
    u1 /= np.linalg.norm(u1)
    u2 /= np.linalg.norm(u2)
    a = np.array(v, float) + u1 * s
    b = a + u2 * s
    c = np.array(v, float) + u2 * s
    ax.plot([a[0], b[0], c[0]], [a[1], b[1], c[1]], color=color, lw=1.5, zorder=5)


def shade_angle(ax, v, p1, p2, r=0.7, color=fs.GREEN, alpha=0.18):
    a1 = math.degrees(math.atan2(p1[1] - v[1], p1[0] - v[0])) % 360
    a2 = math.degrees(math.atan2(p2[1] - v[1], p2[0] - v[0])) % 360
    d = (a2 - a1) % 360
    if d > 180:
        a1, d = a2, 360 - d
    t = np.radians(np.linspace(a1, a1 + d, 40))
    pts = [v] + [(v[0] + r * math.cos(x), v[1] + r * math.sin(x)) for x in t]
    ax.add_patch(Polygon(pts, closed=True, facecolor=color, alpha=alpha, edgecolor="none", zorder=1))


def save(fig, slug, nm):
    fs.save(fig, FOLDER, f"{slug}-{nm}")
