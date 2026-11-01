"""Figures for docs/03-high-school/10-vectors-and-matrices/03-vectors-in-3d-and-the-cross-product.md.

Run from the repo root:

    .venv/Scripts/python tools/figures/03-high-school/vectors-in-3d-and-the-cross-product.py
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
SLUG = "vectors-in-3d-and-the-cross-product"
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


def axes_and_vector():
    fig = fs.plt.figure(figsize=(9.4, 4.7))
    view = dict(elev=22, azim=-40)
    left = new_ax(fig, ((0, 2.6), (0, 2.6), (0, 2.6)), **view)
    right = new_ax(fig, ((0, 4.6), (0, 5.2), (0, 3.4)), **view)
    left.set_position([0.0, 0.0, 0.5, 1.0])
    right.set_position([0.40, 0.0, 0.6, 1.0])

    # Left: the axes, the unit vectors and the order x, y, z.
    axes_lines(left, (2.5, 2.5, 2.5))
    for q, name, off, ha, va in (((1, 0, 0), r"$\mathbf{i}$", (0.0, -0.1, -0.12), "center", "top"),
                                 ((0, 1, 0), r"$\mathbf{j}$", (0.1, 0.0, -0.1), "left", "top"),
                                 ((0, 0, 1), r"$\mathbf{k}$", (-0.12, 0.0, 0.1), "right", "center")):
        arrow(left, (0, 0, 0), q, fs.GREEN, lw=3.0, z=12, ms=13)
        label(left, np.array(q, float) + np.array(off), name, fs.GREEN, ha=ha, va=va, size=13)
    dot3(left, (0, 0, 0))
    label(left, (0, 0, -0.18), "origin", fs.GRAY, size=10, ha="right", va="top")

    # Right: the vector (3, 4, 2) and the box around it.
    box_edges = [((3, 0, 0), (3, 4, 0)), ((0, 4, 0), (3, 4, 0)), ((3, 0, 0), (3, 0, 2)),
                 ((0, 4, 0), (0, 4, 2)), ((3, 4, 0), (3, 4, 2)), ((3, 0, 2), (3, 4, 2)),
                 ((0, 4, 2), (3, 4, 2)), ((0, 0, 2), (3, 0, 2)), ((0, 0, 2), (0, 4, 2))]
    for a, b in box_edges:
        seg(right, a, b, color=fs.GRAY, lw=1.1, ls=DASH, z=3)
    poly(right, [(0, 0, 0), (3, 0, 0), (3, 4, 0), (0, 4, 0)], fs.GREEN, alpha=0.10, z=1)
    axes_lines(right, (4.2, 4.9, 3.1))
    arrow(right, (0, 0, 0), (3, 4, 0), fs.BLUE, lw=1.8, z=8)
    arrow(right, (0, 0, 0), (3, 4, 2), fs.RED, lw=2.6, z=9)
    dot3(right, (0, 0, 0))
    dot3(right, (3, 4, 2), fs.RED)
    label(right, (3.0, 4.0, 2.45), r"$(3, 4, 2)$", fs.RED)
    label(right, (1.2, 1.7, 1.5), r"$\sqrt{29}$", fs.RED, size=12, ha="right")
    label(right, (1.5, 2.0, -0.12), "5", fs.BLUE, va="top")
    label(right, (3.2, 4.0, 1.0), "2", fs.GRAY, ha="left")
    label(right, (3.35, 2.0, 0.0), "4", fs.GRAY, ha="left")
    label(right, (1.5, -0.15, 0.0), "3", fs.GRAY, va="top")
    finish(fig, [left, right], f"{SLUG}-axes")


def cross_panels():
    fig = fs.plt.figure(figsize=(9.4, 4.7))
    specs = [
        ((2, 0, 0), (1, 1, 0), r"$\mathbf{u}$", r"$\mathbf{v}$", r"$\mathbf{u} \times \mathbf{v}$", +1),
        ((1, 1, 0), (2, 0, 0), r"$\mathbf{v}$", r"$\mathbf{u}$", r"$\mathbf{v} \times \mathbf{u}$", -1),
    ]
    made = []
    for k, (a, b, na, nb, nc, sign) in enumerate(specs):
        ax = new_ax(fig, ((-0.3, 2.7), (-0.3, 1.9), (-2.6, 2.6)), elev=38, azim=-62, zoom=1.45)
        ax.set_position([0.58 * k, 0.0, 0.5, 1.0])
        para = [(0, 0, 0), tuple(a), tuple(np.add(a, b)), tuple(b)]
        poly(ax, para, fs.GREEN, alpha=0.22, edge=fs.GREEN, lw=1.0, z=2)
        n = (0, 0, 2 * sign)
        arrow(ax, (0, 0, 0), a, fs.BLUE, z=9)
        arrow(ax, (0, 0, 0), b, fs.ORANGE, z=9)
        arrow(ax, (0, 0, 0), n, fs.RED, lw=2.6, z=9)
        dot3(ax, (0, 0, 0))
        a_arr, b_arr = np.array(a, float), np.array(b, float)
        if sign > 0:
            label(ax, a_arr + np.array((0.0, -0.22, 0.0)), na, fs.BLUE, size=12, va="top")
            label(ax, b_arr + np.array((-0.1, 0.15, 0.0)), nb, fs.ORANGE, size=12, ha="right")
        else:
            label(ax, a_arr + np.array((-0.1, 0.15, 0.0)), na, fs.BLUE, size=12, ha="right")
            label(ax, b_arr + np.array((0.0, -0.22, 0.0)), nb, fs.ORANGE, size=12, va="top")
        label(ax, (0.0, 0.0, 2.2 * sign), nc[:-1] + r" = (0, 0, %d)$" % (2 * sign),
              fs.RED, size=11, ha="center", va="bottom" if sign > 0 else "top")
        right_angle(ax, (0, 0, 0), (1, 0, 0), (0, 0, sign), s=0.3)
        if sign > 0:
            # the height of the parallelogram and the angle between u and v
            seg(ax, (1, 1, 0), (1, 0, 0), color=fs.GRAY, lw=1.3, ls=DASH, z=7)
            label(ax, (1.1, 0.5, 0.0), "height 1", fs.GRAY, size=10, ha="left")
            ts = np.linspace(0, math.atan2(1, 1), 20)
            ax.plot(0.6 * np.cos(ts), 0.6 * np.sin(ts), 0 * ts, color=fs.DARK, lw=1.2, zorder=11)
            label(ax, (0.82, 0.18, 0.0), r"$\theta = 45^\circ$", fs.DARK, size=10, ha="left")
            label(ax, (2.15, 0.55, 0.0), "area 2", fs.GREEN, size=10.5, ha="center")
        made.append(ax)
    finish(fig, made, f"{SLUG}-cross")


def box():
    fig = fs.plt.figure(figsize=(5.8, 5.0))
    ax = new_ax(fig, ((-0.2, 5.4), (-0.2, 3.4), (-0.2, 2.8)), elev=18, azim=-66)
    a, b, c = np.array([3, 0, 0.0]), np.array([1, 2, 0.0]), np.array([1, 1, 2.0])
    O = np.zeros(3)
    poly(ax, [tuple(O), tuple(a), tuple(a + b), tuple(b)], fs.GREEN, alpha=0.28, edge=fs.GREEN, lw=1.2, z=2)
    for p, q in [(O, c), (b, b + c), (b + c, a + b + c), (b + c, c)]:
        seg(ax, p, q, color=fs.GRAY, lw=1.1, ls=DASH, z=3)
    for p, q in [(a, a + c), (a + b, a + b + c), (c, a + c), (a + c, a + b + c)]:
        seg(ax, p, q, color=fs.GRAY, lw=1.4, z=6)
    foot = np.array([c[0], c[1], 0.0])
    seg(ax, c, foot, color=fs.RED, lw=1.4, ls=DASH, z=7)
    dot3(ax, foot, fs.RED, ms=3.5)
    arrow(ax, O, a, fs.BLUE, z=9)
    arrow(ax, O, b, fs.ORANGE, z=9)
    arrow(ax, O, c, fs.GREEN, z=9)
    arrow(ax, O, (0, 0, 1.6), fs.RED, lw=1.6, z=8, ms=11)
    label(ax, (1.6, -0.15, 0), r"$\mathbf{a} = (3, 0, 0)$", fs.BLUE, va="top")
    label(ax, (0.2, 1.6, 0), r"$\mathbf{b} = (1, 2, 0)$", fs.ORANGE, ha="right")
    label(ax, (1.1, 1.0, 2.15), r"$\mathbf{c} = (1, 1, 2)$", fs.GREEN, ha="center", va="bottom")
    label(ax, (2.6, 1.15, 0.02), "base area\n" + r"$\Vert \mathbf{a} \times \mathbf{b} \Vert = 6$", fs.GREEN, size=10)
    label(ax, (1.1, 1.1, 0.8), "height 2", fs.RED, ha="left", size=10.5)
    label(ax, (-0.1, 0.0, 1.0), r"$\mathbf{a} \times \mathbf{b}$", fs.RED, ha="right", size=11)
    finish(fig, [ax], f"{SLUG}-box")


def triangle():
    fig = fs.plt.figure(figsize=(5.6, 5.0))
    ax = new_ax(fig, ((-0.1, 2.0), (-0.1, 2.6), (-0.1, 3.6)), elev=22, azim=-52)
    A, B, C = np.array([1, 0, 0.0]), np.array([0, 2, 0.0]), np.array([0, 0, 3.0])
    n = np.array([6, 3, 2.0]) / 7
    cen = (A + B + C) / 3
    light = np.array([1, 2, 2.0]) / 3
    poly(ax, [tuple(A), tuple(B), tuple(C)], fs.GREEN, alpha=0.30, edge=fs.GREEN, lw=1.5, z=2)
    arrow(ax, cen, cen + 1.45 * n, fs.RED, lw=2.4, z=10)
    arrow(ax, cen, cen + 1.45 * light, fs.ORANGE, lw=2.4, z=10)
    dot3(ax, cen)
    for P, nm, off, ha, va in ((A, r"$A\,(1, 0, 0)$", (0.0, 0.05, -0.12), "center", "top"),
                               (B, r"$B\,(0, 2, 0)$", (0.15, 0.25, -0.22), "left", "top"),
                               (C, r"$C\,(0, 0, 3)$", (0.12, 0.0, 0.1), "left", "bottom")):
        dot3(ax, P)
        label(ax, P + np.array(off), nm, fs.DARK, ha=ha, va=va, size=11)
    cosang = float(n @ light)
    th = math.acos(cosang)
    w = light - cosang * n
    w /= np.linalg.norm(w)
    ts = np.linspace(0, th, 25)
    arc = np.array([cen + 0.75 * (math.cos(t) * n + math.sin(t) * w) for t in ts])
    ax.plot(arc[:, 0], arc[:, 1], arc[:, 2], color=fs.DARK, lw=1.2, zorder=11)
    mid = cen + 0.95 * (math.cos(th / 2) * n + math.sin(th / 2) * w)
    label(ax, mid + np.array([0.0, 0.0, 0.05]), r"$\theta$", fs.DARK, size=12)
    label(ax, cen + 1.55 * n + np.array([0.1, 0.0, 0.05]), r"unit normal $\hat{\mathbf{n}}$", fs.RED, ha="left", size=10.5)
    label(ax, cen + 1.55 * light + np.array([-0.1, 0.0, 0.1]), "direction to\nthe light", fs.ORANGE, ha="right", size=10.5)
    axes_lines(ax, (1.8, 2.3, 3.4))
    print("theta (deg)", round(math.degrees(th), 2))
    finish(fig, [ax], f"{SLUG}-triangle")


if __name__ == "__main__":
    axes_and_vector()
    cross_panels()
    box()
    triangle()
