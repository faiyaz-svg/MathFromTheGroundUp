"""Figures for docs/03-high-school/08-geometry-and-proof/05-conic-sections.md.

Run from the repo root:

    .venv/Scripts/python tools/figures/03-high-school/conic-sections.py
"""

import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import numpy as np  # noqa: E402
from matplotlib.patches import Polygon  # noqa: E402

import figstyle as fs  # noqa: E402
import geomhelp as g  # noqa: E402

SLUG = "conic-sections"
M = "\N{MINUS SIGN}"


def num(v):
    return f"{v:g}".replace("-", M)


def plane(ax, xmin, xmax, ymin, ymax, every=1, size=9):
    ax.set_xlim(xmin - 0.6, xmax + 0.7)
    ax.set_ylim(ymin - 0.6, ymax + 0.7)
    ax.set_aspect("equal")
    ax.spines["left"].set_position("zero")
    ax.spines["bottom"].set_position("zero")
    ax.set_xticks(range(xmin, xmax + 1))
    ax.set_yticks(range(ymin, ymax + 1))
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.tick_params(length=3)
    ax.grid(True, zorder=0)
    ax.set_axisbelow(True)
    box = dict(facecolor="white", edgecolor="none", pad=0.2)
    for t in range(xmin, xmax + 1):
        if t != 0 and t % every == 0:
            ax.text(t, -0.2, num(t), ha="center", va="top", fontsize=size, zorder=4, bbox=box)
    for t in range(ymin, ymax + 1):
        if t != 0 and t % every == 0:
            ax.text(-0.2, t, num(t), ha="right", va="center", fontsize=size, zorder=4, bbox=box)
    ax.plot(1, 0, ">", color=fs.DARK, transform=ax.get_yaxis_transform(), clip_on=False, ms=5)
    ax.plot(0, 1, "^", color=fs.DARK, transform=ax.get_xaxis_transform(), clip_on=False, ms=5)
    ax.text(xmax + 0.7, 0.3, "x", ha="right", va="bottom", style="italic", fontsize=12)
    ax.text(0.3, ymax + 0.7, "y", ha="left", va="top", style="italic", fontsize=12)


def pt(ax, p, text, off, color=fs.DARK, size=10.5, ha="center", va="center"):
    ax.plot(*p, "o", color=color, zorder=6, ms=5)
    ax.text(p[0] + off[0], p[1] + off[1], text, ha=ha, va=va, fontsize=size, color=color, zorder=7, bbox=g.BOX)


def cone():
    """A double cone seen from the side, cut by four planes drawn edge-on."""
    fig, axes = fs.plt.subplots(1, 4, figsize=(10.0, 3.0))
    cases = [
        ("circle", lambda x: 1.6 + 0 * x, fs.GREEN),
        ("ellipse", lambda x: 0.4 * x + 2.2, fs.BLUE),
        ("parabola", lambda x: x + 1.6, fs.RED),
        ("hyperbola", None, fs.ORANGE),
    ]
    for ax, (title, f, col) in zip(axes, cases):
        ax.set_aspect("equal")
        ax.axis("off")
        ax.set_xlim(-4.2, 4.2)
        ax.set_ylim(-4.3, 4.6)
        up = [(0, 0), (-4, 4), (4, 4)]
        lo = [(0, 0), (-4, -4), (4, -4)]
        for tri in (up, lo):
            ax.add_patch(Polygon(tri, closed=True, facecolor=fs.LIGHT, edgecolor="none", zorder=1))
            ax.add_patch(Polygon(tri, closed=True, fill=False, edgecolor=fs.GRAY, lw=1.6, zorder=2))
        ax.plot(0, 0, "o", color=fs.DARK, ms=4, zorder=5)
        if f is not None:
            xs = np.linspace(-3.9, 3.9, 50)
            ys = f(xs)
            ok = (ys <= 4.2) & (ys >= -0.1)
            ax.plot(xs[ok], ys[ok], color=col, lw=2.6, zorder=4)
        else:
            ax.plot([1.6, 1.6], [-4.0, 4.0], color=col, lw=2.6, zorder=4)
        ax.text(0, -4.55, title, ha="center", va="center", fontsize=12, color=col, weight="bold")
    fig.subplots_adjust(wspace=0.04)
    g.save(fig, SLUG, "cone")


def parabola():
    """y = x^2/4: focus (0, 1), directrix y = -1, and a point with its two equal distances."""
    fig, ax = fs.figure(5.0, 3.8)
    plane(ax, -5, 5, -2, 6)
    xs = np.linspace(-4.9, 4.9, 300)
    ax.plot(xs, xs**2 / 4, color=fs.GREEN, zorder=3)
    ax.plot([-5.5, 5.5], [-1, -1], color=fs.BLUE, lw=1.8, zorder=3)
    P, F, D = (3, 2.25), (0, 1), (3, -1)
    ax.plot([P[0], F[0]], [P[1], F[1]], color=fs.RED, lw=1.8, zorder=4)
    ax.plot([P[0], D[0]], [P[1], D[1]], color=fs.RED, lw=1.8, zorder=4)
    g.tick(ax, P, F, 2, fs.RED, 0.12)
    g.tick(ax, P, D, 2, fs.RED, 0.12)
    pt(ax, P, "P", (0.25, 0.3))
    pt(ax, F, "focus F(0, 1)", (0.0, 0.5), fs.GREEN)
    pt(ax, D, "D", (0.0, -0.4))
    ax.text(-5.2, -1.45, "directrix y = " + M + "1", ha="left", va="center", fontsize=10, color=fs.BLUE)
    ax.text(3.4, 0.6, "PF = PD", ha="left", va="center", fontsize=10, color=fs.RED)
    fs.save(fig, g.FOLDER, f"{SLUG}-parabola")


def ellipse():
    """x^2/25 + y^2/16 = 1 with foci (+-3, 0) and the point (4, 2.4)."""
    fig, ax = fs.figure(5.4, 3.8)
    plane(ax, -6, 6, -5, 5, every=2)
    t = np.linspace(0, 2 * math.pi, 400)
    ax.plot(5 * np.cos(t), 4 * np.sin(t), color=fs.GREEN, zorder=3)
    F1, F2, P = (-3, 0), (3, 0), (4, 2.4)
    ax.plot([P[0], F1[0]], [P[1], F1[1]], color=fs.RED, lw=1.6, zorder=4)
    ax.plot([P[0], F2[0]], [P[1], F2[1]], color=fs.RED, lw=1.6, zorder=4)
    ax.plot([0, 3], [4, 0], color=fs.GRAY, lw=1.4, ls=(0, (4, 3)), zorder=3)
    pt(ax, F1, "F₁", (0, -0.6), fs.DARK)
    pt(ax, F2, "F₂", (0.1, -0.6), fs.DARK)
    pt(ax, P, "P", (0.3, 0.3))
    ax.text(1.95, 2.35, "length 5", ha="center", va="center", fontsize=9.5, color=fs.DARK, rotation=-53)
    ax.text(-4.6, 1.5, "PF₁ + PF₂ = 10", ha="center", va="center", fontsize=10, color=fs.RED)
    fs.save(fig, g.FOLDER, f"{SLUG}-ellipse")


def hyperbola():
    """x^2/16 - y^2/9 = 1 with foci (+-5, 0) and asymptotes y = +-(3/4)x."""
    fig, ax = fs.figure(5.4, 3.9)
    plane(ax, -8, 8, -5, 5, every=4)
    s = np.linspace(-1.9, 1.9, 300)
    for sign in (1, -1):
        ax.plot(sign * 4 * np.cosh(s), 3 * np.sinh(s), color=fs.GREEN, zorder=3)
    xs = np.array([-7.6, 7.6])
    ax.plot(xs, 0.75 * xs, color=fs.GRAY, lw=1.3, ls=(0, (5, 3)), zorder=2)
    ax.plot(xs, -0.75 * xs, color=fs.GRAY, lw=1.3, ls=(0, (5, 3)), zorder=2)
    ax.plot([-4, 4, 4, -4, -4], [-3, -3, 3, 3, -3], color=fs.GRAY, lw=1.0, zorder=2)
    F1, F2, P = (-5, 0), (5, 0), (5, 2.25)
    ax.plot([P[0], F1[0]], [P[1], F1[1]], color=fs.RED, lw=1.5, zorder=4)
    ax.plot([P[0], F2[0]], [P[1], F2[1]], color=fs.RED, lw=1.5, zorder=4)
    pt(ax, F1, "F₁", (0, -0.55))
    pt(ax, F2, "F₂", (0.55, -0.45))
    pt(ax, P, "P", (0.35, 0.35))
    ax.text(0, -4.5, "|PF₁ − PF₂| = 8", ha="center", va="center", fontsize=10, color=fs.RED, bbox=g.BOX)
    fs.save(fig, g.FOLDER, f"{SLUG}-hyperbola")


def dish():
    """Rays parallel to the axis reflect off a parabola and pass through the focus."""
    fig, ax = g.canvas(4.8, 4.0, (-4.6, 4.6), (-0.9, 5.6))
    xs = np.linspace(-4.0, 4.0, 300)
    ax.plot(xs, xs**2 / 4, color=fs.GREEN, lw=2.6, zorder=3)
    F = (0, 1)
    for x in (-3.2, -1.8, 1.8, 3.2):
        y = x * x / 4
        ax.annotate("", xy=(x, y), xytext=(x, 5.2), arrowprops=dict(arrowstyle="-|>", color=fs.BLUE, lw=1.5), zorder=4)
        g.seg(ax, (x, y), F, fs.RED, 1.5)
    g.dot(ax, F, fs.RED)
    g.name(ax, F, "focus", (0.0, -0.45), color=fs.RED, size=11, style="normal", box=True)
    g.label(ax, (0, -0.5), "axis of the dish", box=False, size=9.5, color=fs.GRAY)
    g.seg(ax, (0, -0.1), (0, 5.3), fs.GRAY, 1.0, ls=(0, (4, 3)), z=1)
    g.save(fig, SLUG, "dish")


def reflection():
    """The tangent at P is the perpendicular bisector of FD, so it bisects angle FPD."""
    fig, ax = g.canvas(5.0, 4.0, (-1.6, 6.4), (-1.9, 5.6))
    xs = np.linspace(-1.0, 5.2, 300)
    ax.plot(xs, xs**2 / 4, color=fs.GREEN, lw=2.2, zorder=3)
    P, F, D = (3, 2.25), (0, 1), (3, -1)
    g.seg(ax, (-1.6, -1), (6.2, -1), fs.BLUE, 1.6)
    u = np.array((2.0, 3.0)) / math.sqrt(13)
    T0 = np.array((1.5, 0.0))
    g.seg(ax, tuple(T0 - 1.2 * u), tuple(T0 + 5.0 * u), fs.DARK, 1.8)
    g.seg(ax, P, F, fs.RED, 1.8)
    g.seg(ax, P, D, fs.RED, 1.8)
    g.seg(ax, F, D, fs.GRAY, 1.4, ls=(0, (4, 3)))
    g.seg(ax, P, (3, 4.9), fs.BLUE, 1.6, ls=(0, (4, 3)))
    g.tick(ax, P, F, 2, fs.RED, 0.12)
    g.tick(ax, P, D, 2, fs.RED, 0.12)
    up = (3 + 0.0, 4.0)
    g.arc(ax, P, up, tuple(np.array(P) + u), 0.75, 1, fs.ORANGE, text="\N{GREEK SMALL LETTER ALPHA}", text_r=1.1, size=11)
    g.arc(ax, P, F, tuple(np.array(P) - u), 0.75, 1, fs.ORANGE, text="\N{GREEK SMALL LETTER ALPHA}", text_r=1.1, size=11)
    g.right_angle(ax, tuple(T0), tuple(T0 + u), (0, 1), 0.0001, fs.DARK)
    mid = (1.5, 0.0)
    g.dot(ax, mid)
    g.label(ax, (1.55, -0.45), "midpoint of FD", box=False, size=9, color=fs.GRAY, ha="left")
    for X, t, o, c in [(P, "P", (0.3, 0.25), fs.DARK), (F, "F", (-0.3, 0.1), fs.DARK), (D, "D", (0.0, -0.4), fs.DARK)]:
        g.dot(ax, X)
        g.name(ax, X, t, o, color=c)
    g.label(ax, (5.4, 4.8), "tangent at P", box=False, size=9.5, ha="left")
    g.label(ax, (3.1, 5.15), "incoming ray", box=False, size=9.5, ha="left", color=fs.BLUE)
    g.label(ax, (4.7, -1.45), "directrix", box=False, size=9.5, ha="left", color=fs.BLUE)
    g.save(fig, SLUG, "reflection")


if __name__ == "__main__":
    cone()
    parabola()
    ellipse()
    hyperbola()
    dish()
    reflection()
