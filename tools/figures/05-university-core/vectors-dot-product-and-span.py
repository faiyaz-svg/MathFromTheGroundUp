"""Figures for docs/05-university-core/06-linear-algebra/01-vectors-dot-product-and-span.md.

Run from the repo root:

    .venv/Scripts/python tools/figures/05-university-core/vectors-dot-product-and-span.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

import figstyle as fs  # noqa: E402

FOLDER = "05-university-core"
SLUG = "vectors-dot-product-and-span"
BOX = dict(facecolor="white", edgecolor="none", pad=0.4, alpha=0.9)


def arrow(ax, tail, tip, color, lw=2.2, z=4, style="-|>"):
    ax.annotate(
        "",
        xy=tip,
        xytext=tail,
        arrowprops=dict(arrowstyle=style, color=color, lw=lw, shrinkA=0, shrinkB=0, mutation_scale=14),
        zorder=z,
    )


def plane_axes(ax, xlim, ylim):
    ax.set_aspect("equal")
    ax.grid(True)
    ax.set_axisbelow(True)
    ax.axhline(0, color=fs.DARK, lw=1.0)
    ax.axvline(0, color=fs.DARK, lw=1.0)
    ax.spines["bottom"].set_visible(False)
    ax.spines["left"].set_visible(False)
    ax.tick_params(labelsize=9, length=0)
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)


def combination():
    """w = 2u + v built tip to tail."""
    fig, ax = fs.figure(5.2, 4.6)
    u = np.array([2.0, 1.0])
    v = np.array([-1.0, 2.0])
    plane_axes(ax, (-3.2, 5.6), (-1.6, 5.6))
    arrow(ax, (0, 0), tuple(u), fs.GREEN)
    arrow(ax, (0, 0), tuple(v), fs.BLUE)
    arrow(ax, (0, 0), tuple(2 * u), fs.GREEN, lw=1.4, style="-|>")
    arrow(ax, tuple(2 * u), tuple(2 * u + v), fs.BLUE, lw=1.4)
    arrow(ax, (0, 0), tuple(2 * u + v), fs.RED, lw=2.6)
    ax.text(1.1, 0.2, "u = (2, 1)", color=fs.GREEN, fontsize=10.5, ha="left", va="top", bbox=BOX)
    ax.text(-1.15, 2.1, "v = (−1, 2)", color=fs.BLUE, fontsize=10.5, ha="right", va="center")
    ax.text(2.9, 1.0, "2u", color=fs.GREEN, fontsize=10.5, ha="left", va="top")
    ax.text(3.35, 3.0, "v", color=fs.BLUE, fontsize=10.5, ha="left", va="center")
    ax.text(1.55, 3.6, "2u + v = (3, 4)", color=fs.RED, fontsize=10.5, ha="right", va="center", bbox=BOX)
    fs.save(fig, FOLDER, f"{SLUG}-combination")


def angle():
    """The angle between u and v and the shadow of u on the line of v."""
    fig, ax = fs.figure(5.4, 3.4)
    u = np.array([3.0, 2.0])
    v = np.array([4.0, 1.0])
    plane_axes(ax, (-0.6, 5.4), (-0.9, 3.0))
    ax.spines["bottom"].set_visible(False)
    t = u @ v / (v @ v)
    s = t * v
    ax.plot([0, 4.8], [0, 4.8 / 4.0], color=fs.BLUE, lw=0.9, ls=":", zorder=1)
    arrow(ax, (0, 0), tuple(v), fs.BLUE)
    arrow(ax, (0, 0), tuple(u), fs.GREEN)
    ax.plot([u[0], s[0]], [u[1], s[1]], color=fs.RED, lw=1.4, ls="--", zorder=3)
    d = v / np.linalg.norm(v)
    n = np.array([-d[1], d[0]])
    off = -0.16 * n
    ax.plot([0 + off[0], s[0] + off[0]], [0 + off[1], s[1] + off[1]], color=fs.RED, lw=3.4, solid_capstyle="butt", zorder=3)
    sq = 0.2
    ax.plot(
        [s[0] - sq * d[0], s[0] - sq * d[0] + sq * n[0], s[0] + sq * n[0]],
        [s[1] - sq * d[1], s[1] - sq * d[1] + sq * n[1], s[1] + sq * n[1]],
        color=fs.RED, lw=1.0,
    )
    # angle arc
    th_u = np.arctan2(u[1], u[0])
    th_v = np.arctan2(v[1], v[0])
    arc = np.linspace(th_v, th_u, 30)
    ax.plot(0.9 * np.cos(arc), 0.9 * np.sin(arc), color=fs.DARK, lw=1.2)
    ax.text(1.05, 0.62, "θ", color=fs.DARK, fontsize=11, ha="left", va="center")
    ax.text(3.1, 2.15, "u", color=fs.GREEN, fontsize=11, ha="left", va="bottom")
    ax.text(4.1, 0.95, "v", color=fs.BLUE, fontsize=11, ha="left", va="top")
    ax.text(1.7, -0.5, "shadow of u on v: length u·v / ‖v‖", color=fs.RED, fontsize=10, ha="left", va="center")
    fs.save(fig, FOLDER, f"{SLUG}-angle")


def _axes3d(ax, lim=3.2):
    ax.set_xlim(-lim, lim)
    ax.set_ylim(-lim, lim)
    ax.set_zlim(-lim, lim)
    ax.set_box_aspect((1, 1, 1))
    ax.set_axis_off()
    ax.view_init(elev=20, azim=-52)
    for vec, lab in (((lim, 0, 0), "x"), ((0, lim, 0), "y"), ((0, 0, lim), "z")):
        ax.plot([-vec[0], vec[0]], [-vec[1], vec[1]], [-vec[2], vec[2]], color=fs.GRAY, lw=0.9)
        ax.text(vec[0] * 1.08, vec[1] * 1.08, vec[2] * 1.08, lab, color=fs.DARK, fontsize=10, ha="center", va="center")
    ax.plot([0], [0], [0], "o", color=fs.DARK, ms=4)


def span3d():
    """The span of one vector is a line, of two vectors a plane, both through the origin."""
    fig = plt.figure(figsize=(9.0, 4.2))
    a = fig.add_subplot(1, 2, 1, projection="3d")
    b = fig.add_subplot(1, 2, 2, projection="3d")
    for ax in (a, b):
        _axes3d(ax)
    v = np.array([1.0, 1.0, 1.0])
    t = np.array([-2.7, 2.7])
    a.plot(t * v[0], t * v[1], t * v[2], color=fs.GREEN, lw=2.2)
    a.quiver(0, 0, 0, *v, color=fs.RED, lw=2.4, arrow_length_ratio=0.18)
    a.text(-0.2, -0.2, 1.9, "v = (1, 1, 1)", color=fs.RED, fontsize=10, ha="right")
    a.text(-3.0, 0.0, 3.4, "span{v}: a line", color=fs.GREEN, fontsize=10.5)

    u = np.array([2.0, -1.0, 0.5])
    w = np.array([0.0, 1.5, 1.5])
    s, r = np.meshgrid(np.linspace(-1.0, 1.0, 2), np.linspace(-1.0, 1.0, 2))
    X = s * u[0] + r * w[0]
    Y = s * u[1] + r * w[1]
    Z = s * u[2] + r * w[2]
    b.plot_surface(X, Y, Z, color=fs.GREEN, alpha=0.28, linewidth=0, shade=False)
    corners = np.array([[-1, -1], [1, -1], [1, 1], [-1, 1], [-1, -1]])
    pts = np.array([c0 * u + c1 * w for c0, c1 in corners])
    b.plot(pts[:, 0], pts[:, 1], pts[:, 2], color=fs.GREEN, lw=1.2)
    b.quiver(0, 0, 0, *u, color=fs.RED, lw=2.4, arrow_length_ratio=0.14)
    b.quiver(0, 0, 0, *w, color=fs.BLUE, lw=2.4, arrow_length_ratio=0.14)
    b.text(2.2, -1.1, 0.6, "u", color=fs.RED, fontsize=11)
    b.text(-0.3, 1.6, 1.8, "w", color=fs.BLUE, fontsize=11)
    b.text(-3.0, 0.0, 3.4, "span{u, w}: a plane", color=fs.GREEN, fontsize=10.5)
    fig.subplots_adjust(wspace=0.02)
    fs.save(fig, FOLDER, f"{SLUG}-span")


if __name__ == "__main__":
    combination()
    angle()
    span3d()
