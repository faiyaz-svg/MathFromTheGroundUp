"""Figures for docs/03-high-school/10-vectors-and-matrices/04-lines-and-planes-in-3d.md.

Run from the repo root:

    .venv/Scripts/python tools/figures/03-high-school/lines-and-planes-in-3d.py
"""

import math
import sys
from pathlib import Path

import numpy as np
from matplotlib import cbook
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.lines import Line2D
from matplotlib.patches import FancyArrowPatch
from matplotlib.text import Text
from matplotlib.transforms import Bbox
from mpl_toolkits.mplot3d import proj3d
from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Text3D

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import figstyle as fs  # noqa: E402

FOLDER = "03-high-school"
SLUG = "lines-and-planes-in-3d"
DASH = (0, (4, 3))


class Arrow3D(FancyArrowPatch):
    """A flat arrow (shaft and head) between two 3D points."""

    def __init__(self, p, q, color, lw=2.2, ls="-", z=10, ms=14):
        super().__init__((0, 0), (0, 0), arrowstyle="-|>", mutation_scale=ms, color=color,
                         lw=lw, ls=ls, shrinkA=0, shrinkB=0, zorder=z)
        self._p, self._q = p, q

    def do_3d_projection(self, renderer=None):
        xs, ys, zs = proj3d.proj_transform([self._p[0], self._q[0]], [self._p[1], self._q[1]],
                                           [self._p[2], self._q[2]], self.axes.M)
        self.set_positions((xs[0], ys[0]), (xs[1], ys[1]))
        return min(zs)


def new_ax(fig, lims, elev=20, azim=-58, zoom=1.0):
    """A 3D axes with no panes, a true-scale box and painter's-order drawing (by zorder)."""
    ax = fig.add_axes([0, 0, 1, 1], projection="3d")
    ax.computed_zorder = False
    ax.set_axis_off()
    (x0, x1), (y0, y1), (z0, z1) = lims
    ax.set_xlim(x0, x1)
    ax.set_ylim(y0, y1)
    ax.set_zlim(z0, z1)
    ax.set_box_aspect((x1 - x0, y1 - y0, z1 - z0), zoom=zoom)
    ax.view_init(elev=elev, azim=azim)
    return ax


def arrow(ax, p, q, color, lw=2.2, ls="-", z=10, ms=14):
    ax.add_artist(Arrow3D(p, q, color, lw=lw, ls=ls, z=z, ms=ms))


def seg(ax, p, q, color=fs.GRAY, lw=1.2, ls="-", z=4):
    ax.plot([p[0], q[0]], [p[1], q[1]], [p[2], q[2]], color=color, lw=lw, ls=ls, zorder=z,
            solid_capstyle="butt")


def poly(ax, pts, color, alpha=0.25, edge=None, lw=1.2, z=2):
    """A filled polygon, with its outline drawn as lines so the cropping sees it."""
    ax.add_collection3d(Poly3DCollection([pts], facecolor=color, alpha=alpha, edgecolor="none", zorder=z))
    closed = list(pts) + [pts[0]]
    for p, q in zip(closed[:-1], closed[1:]):
        seg(ax, p, q, color=edge or color, lw=lw if edge else 0.01, z=z + 1)


def label(ax, p, text, color=fs.DARK, size=11, ha="center", va="center", z=30, **kw):
    ax.text(p[0], p[1], p[2], text, color=color, fontsize=size, ha=ha, va=va, zorder=z, **kw)


def dot3(ax, p, color=fs.DARK, ms=4.5, z=14):
    ax.plot([p[0]], [p[1]], [p[2]], "o", color=color, ms=ms, zorder=z)


def right_angle(ax, corner, d1, d2, s=0.28, color=fs.DARK, z=12):
    d1 = np.array(d1, float) / np.linalg.norm(d1)
    d2 = np.array(d2, float) / np.linalg.norm(d2)
    c = np.array(corner, float)
    pts = [c + s * d1, c + s * (d1 + d2), c + s * d2]
    ax.plot(*zip(*pts), color=color, lw=1.0, zorder=z)


def axes_lines(ax, length, names=("x", "y", "z"), z=6, color=fs.DARK):
    """Positive half-axes with arrow heads and an italic letter past each tip."""
    for k, (c, name) in enumerate(zip(length, names)):
        tip = [0.0, 0.0, 0.0]
        tip[k] = c
        arrow(ax, (0, 0, 0), tuple(tip), color, lw=1.3, z=z, ms=11)
        pos = [0.0, 0.0, 0.0]
        pos[k] = c + 0.18
        label(ax, tuple(pos), name, color=color, size=12, style="italic")


def camera_dir(elev, azim):
    e, a = math.radians(elev), math.radians(azim)
    return np.array([math.cos(e) * math.cos(a), math.cos(e) * math.sin(a), math.sin(e)])


def _extent(ax, a, r):
    """Window extent of one artist; a Text3D needs its projected position put back first."""
    if isinstance(a, Text3D):
        x, y, _ = proj3d.proj_transform(a._x, a._y, a._z, ax.M)
        with cbook._setattr_cm(a, _x=x, _y=y):
            return Text.get_window_extent(a, r)
    return a.get_window_extent(r)


def finish(fig, axes, name, pad=0.14):
    """Crop the figure to the drawn content, then save it.

    An Axes3D keeps a square drawing area, so the default tight crop leaves white bands.
    Here we measure what was drawn, resize the figure to fit it and slide the axes to match.
    """
    for ax in axes:
        for a in ax.get_children():
            a.set_clip_on(False)
    r = FigureCanvasAgg(fig).get_renderer()
    fig.draw(r)
    dpi = fig.dpi
    boxes = []
    for ax in axes:
        for a in ax.get_children():
            if not a.get_visible():
                continue
            if isinstance(a, Text) and not a.get_text():
                continue
            if isinstance(a, (Line2D, Text, FancyArrowPatch)):
                bb = _extent(ax, a, r)
                if np.isfinite(bb.x0 + bb.y0 + bb.x1 + bb.y1) and (bb.width > 0 or bb.height > 0):
                    boxes.append(bb)
    u = Bbox.union(boxes)
    old_w, old_h = fig.get_size_inches()
    new_w = u.width / dpi + 2 * pad
    new_h = u.height / dpi + 2 * pad
    dx = pad - u.x0 / dpi
    dy = pad - u.y0 / dpi
    squares = []
    for ax in axes:
        pos = ax.get_position()
        squares.append((pos.x0 * old_w + dx, pos.y0 * old_h + dy, pos.width * old_w, pos.height * old_h))
    fig.set_size_inches(new_w, new_h)
    for ax, (x, y, w, h) in zip(axes, squares):
        ax.set_position([x / new_w, y / new_h, w / new_w, h / new_h])
    with fs.plt.rc_context({"savefig.bbox": "standard"}):
        fs.save(fig, FOLDER, name)


# ---------------------------------------------------------------------------


def plane_with_normal():
    """The plane 6x + 3y + 2z = 6 with its normal and a vector lying in the plane."""
    fig = fs.plt.figure(figsize=(5.6, 5.0))
    ax = new_ax(fig, ((-0.1, 2.0), (-0.1, 2.6), (-0.1, 3.6)), elev=22, azim=-52)
    A, B, C = np.array([1, 0, 0.0]), np.array([0, 2, 0.0]), np.array([0, 0, 3.0])
    P0 = (A + B + C) / 3
    X = (B + C) / 2
    n = np.array([6, 3, 2.0]) / 7
    poly(ax, [tuple(A), tuple(B), tuple(C)], fs.GREEN, alpha=0.28, edge=fs.GREEN, lw=1.5, z=2)
    axes_lines(ax, (1.8, 2.3, 3.4))
    seg(ax, P0, X, color=fs.BLUE, lw=0.01)
    arrow(ax, P0, X, fs.BLUE, lw=2.4, z=10)
    arrow(ax, P0, P0 + 1.5 * n, fs.RED, lw=2.4, z=10)
    dot3(ax, P0)
    dot3(ax, X, fs.BLUE)
    right_angle(ax, P0, X - P0, n, s=0.22)
    label(ax, P0 + np.array([0.12, -0.02, -0.15]), r"$P_0$", fs.DARK, size=12, ha="left", va="top")
    label(ax, X + np.array([0.0, 0.08, 0.12]), r"$P$", fs.BLUE, size=12, ha="center", va="bottom")
    label(ax, (P0 + X) / 2 + np.array([-0.05, -0.2, 0.0]), r"$\mathbf{r} - \mathbf{r}_0$", fs.BLUE,
          size=11.5, ha="right", va="top")
    label(ax, P0 + 1.5 * n + np.array([0.08, 0.0, 0.05]), r"normal $\mathbf{n}$", fs.RED, size=11.5, ha="left")
    finish(fig, [ax], f"{SLUG}-plane")


def line_meets_plane():
    """The line through E = (0, 0, 2) with direction (1, 2, -1) meets 2x + y + 2z = 8 at (2, 4, 0)."""
    elev, azim = 24, -20
    fig = fs.plt.figure(figsize=(6.0, 5.0))
    ax = new_ax(fig, ((-0.5, 4.5), (-0.5, 7.0), (-2.5, 3.5)), elev=elev, azim=azim)
    n = np.array([2, 1, 2.0])
    D = 8.0
    H = np.array([2.0, 4.0, 0.0])
    u1, u2 = np.array([1.0, 0, -1.0]), np.array([0, 2.0, -1.0])
    a, b = 1.7, 1.15
    corners = [tuple(H + s * a * u1 + t * b * u2) for s, t in ((-1, -1), (1, -1), (1, 1), (-1, 1))]
    E = np.array([0, 0, 2.0])
    d = np.array([1, 2, -1.0])
    cam = camera_dir(elev, azim)
    side = np.sign(n @ cam)
    t_end = 3.0

    def visible(t):
        return (n @ (E + t * d) - D) * side > 0

    # the part of the line behind the plane is dashed and drawn first
    t_hit = (D - n @ E) / (n @ d)
    near = (-0.0, t_hit) if visible(0.0) else (t_hit, t_end)
    far = (t_hit, t_end) if visible(0.0) else (0.0, t_hit)
    seg(ax, E + far[0] * d, E + far[1] * d, color=fs.ORANGE, lw=2.0, ls=DASH, z=3)
    poly(ax, corners, fs.GREEN, alpha=0.25, edge=fs.GREEN, lw=1.3, z=4)
    seg(ax, E + near[0] * d, E + near[1] * d, color=fs.ORANGE, lw=2.4, z=8)
    arrow(ax, E + (t_end - 0.01) * d if visible(t_end) else E + 0 * d, E + t_end * d, fs.ORANGE, lw=2.0,
          z=8 if visible(t_end) else 3, ms=12)
    arrow(ax, E, E + d, fs.RED, lw=2.8, z=12, ms=13)
    dot3(ax, E)
    dot3(ax, H, fs.RED, ms=6)
    label(ax, E + np.array([-0.15, 0.0, 0.0]), r"$E = (0, 0, 2)$", fs.DARK, ha="right", size=11)
    label(ax, E + 0.5 * d + np.array([0.0, -0.15, -0.55]), r"$\mathbf{m} = (1, 2, -1)$", fs.RED, ha="right", size=11)
    label(ax, H + np.array([0.0, 0.0, 0.45]), r"$(2, 4, 0)$", fs.RED, size=11.5)
    label(ax, np.array(corners[3]) + np.array([0.0, 0.0, 0.3]), r"$2x + y + 2z = 8$", fs.GREEN, size=11,
          ha="left")
    print("side", side, "t_hit", t_hit, "visible(0)", visible(0.0))
    finish(fig, [ax], f"{SLUG}-line-plane")


def two_lines():
    """Parallel, intersecting and skew lines, drawn on the edges of a cube."""
    fig = fs.plt.figure(figsize=(10.5, 3.6))
    titles = ["parallel", "intersecting", "skew"]
    cube = [((0, 0, 0), (1, 0, 0)), ((0, 1, 0), (1, 1, 0)), ((0, 0, 1), (1, 0, 1)), ((0, 1, 1), (1, 1, 1)),
            ((0, 0, 0), (0, 1, 0)), ((1, 0, 0), (1, 1, 0)), ((0, 0, 1), (0, 1, 1)), ((1, 0, 1), (1, 1, 1)),
            ((0, 0, 0), (0, 0, 1)), ((1, 0, 0), (1, 0, 1)), ((0, 1, 0), (0, 1, 1)), ((1, 1, 0), (1, 1, 1))]
    # each panel: the two lines as (start, end), extended a little past the cube
    ext = 0.35

    def line(p, q):
        p, q = np.array(p, float), np.array(q, float)
        d = q - p
        return p - ext * d, q + ext * d

    pairs = [
        (line((0, 0, 0), (0, 0, 1)), line((1, 1, 0), (1, 1, 1))),
        (line((0, 0, 0), (1, 0, 0)), line((0, 0, 0), (0, 0, 1))),
        (line((0, 0, 0), (1, 0, 0)), line((1, 0, 1), (1, 1, 1))),
    ]
    made = []
    for k, ((p1, q1), (p2, q2)) in enumerate(pairs):
        ax = new_ax(fig, ((-0.5, 1.5), (-0.5, 1.5), (-0.5, 1.5)), elev=20, azim=-52)
        ax.set_position([0.31 * k, 0.0, 0.36, 1.0])
        for p, q in cube:
            seg(ax, p, q, color="#c3c7cc", lw=1.0, z=1)
        seg(ax, p1, q1, color=fs.BLUE, lw=2.6, z=8)
        seg(ax, p2, q2, color=fs.ORANGE, lw=2.6, z=9)
        label(ax, (0.5, 0.5, -0.65), titles[k], fs.DARK, size=12.5, va="top")
        made.append(ax)
    finish(fig, made, f"{SLUG}-two-lines")


def vertical_plane(ax, center, theta_deg, half_w, z0, z1, color):
    """A rectangle of the plane through the vertical line at center, turned by theta in the xy-plane."""
    t = math.radians(theta_deg)
    d = np.array([math.cos(t), math.sin(t), 0.0])
    c = np.array([center[0], center[1], 0.0])
    p = [c - half_w * d + np.array([0, 0, z0]), c + half_w * d + np.array([0, 0, z0]),
         c + half_w * d + np.array([0, 0, z1]), c - half_w * d + np.array([0, 0, z1])]
    poly(ax, [tuple(q) for q in p], color, alpha=0.22, edge=color, lw=1.2, z=3)


def three_planes():
    """Three planes meeting in a point, in a line, and in no common point (a prism)."""
    fig = fs.plt.figure(figsize=(10.5, 3.6))
    made = []
    cols = [fs.GREEN, fs.BLUE, fs.ORANGE]

    # 1: the three coordinate planes meet at the origin
    ax = new_ax(fig, ((-0.2, 1.6), (-0.2, 1.6), (-0.2, 1.6)), elev=22, azim=-52)
    ax.set_position([0.0, 0.0, 0.36, 1.0])
    s = 1.4
    poly(ax, [(0, 0, 0), (s, 0, 0), (s, s, 0), (0, s, 0)], cols[0], alpha=0.22, edge=cols[0], z=3)
    poly(ax, [(0, 0, 0), (s, 0, 0), (s, 0, s), (0, 0, s)], cols[1], alpha=0.22, edge=cols[1], z=3)
    poly(ax, [(0, 0, 0), (0, s, 0), (0, s, s), (0, 0, s)], cols[2], alpha=0.22, edge=cols[2], z=3)
    dot3(ax, (0, 0, 0), fs.RED, ms=7)
    label(ax, (0.7, 0.7, -0.55), "one point", fs.DARK, size=12.5, va="top")
    made.append(ax)

    # 2: three planes through one vertical line, like the pages of an open book
    ax = new_ax(fig, ((-1.2, 1.2), (-1.2, 1.2), (-0.2, 1.6)), elev=22, azim=-52)
    ax.set_position([0.31, 0.0, 0.36, 1.0])
    for th, c in zip((0, 60, 120), cols):
        vertical_plane(ax, (0, 0), th, 1.1, 0, 1.4, c)
    seg(ax, (0, 0, -0.1), (0, 0, 1.5), color=fs.RED, lw=3.0, z=9)
    label(ax, (0, 0, -0.5), "a common line", fs.DARK, size=12.5, va="top")
    made.append(ax)

    # 3: three planes forming a triangular prism, with no common point
    ax = new_ax(fig, ((-1.2, 1.2), (-1.2, 1.2), (-0.2, 1.6)), elev=22, azim=-52)
    ax.set_position([0.62, 0.0, 0.36, 1.0])
    tri = [np.array([-1.0, -0.7]), np.array([1.0, -0.7]), np.array([0.0, 0.9])]
    for i, c in enumerate(cols):
        p, q = tri[i], tri[(i + 1) % 3]
        poly(ax, [(p[0], p[1], 0), (q[0], q[1], 0), (q[0], q[1], 1.4), (p[0], p[1], 1.4)], c, alpha=0.24, edge=c,
             lw=1.2, z=3)
    label(ax, (0, 0, -0.5), "no common point", fs.DARK, size=12.5, va="top")
    made.append(ax)
    finish(fig, made, f"{SLUG}-three-planes")


if __name__ == "__main__":
    plane_with_normal()
    line_meets_plane()
    two_lines()
    three_planes()
