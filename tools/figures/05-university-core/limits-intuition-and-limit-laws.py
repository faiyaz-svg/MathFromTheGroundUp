"""Figures for docs/05-university-core/01-limits-and-continuity/01-limits-intuition-and-limit-laws.md

hole: a graph with a missing point, where the limit exists but the value does not.
no-limit: a jump, a blow-up and an oscillation (three ways a limit can fail to exist).
sine-geometry: the unit-circle picture behind sin(x)/x -> 1.
squeeze: x^2 sin(1/x) trapped between -x^2 and x^2.
at-infinity: a rational function settling toward a horizontal asymptote.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
from matplotlib.patches import Polygon, Wedge  # noqa: E402

import figstyle as fs  # noqa: E402

FOLDER = "05-university-core"
SLUG = "limits-intuition-and-limit-laws"


def open_dot(ax, x, y, color=None):
    ax.plot([x], [y], "o", markerfacecolor="white", markeredgecolor=color or fs.GREEN, markeredgewidth=2, zorder=5)


def closed_dot(ax, x, y, color=None):
    ax.plot([x], [y], "o", color=color or fs.GREEN, zorder=5)


def hole():
    fig, ax = fs.figure(5.0, 3.6)
    x = np.linspace(-1, 3, 400)
    ax.plot(x, x + 1, color=fs.GREEN)
    open_dot(ax, 1, 2)
    ax.plot([0, 1], [2, 2], color=fs.GRAY, linestyle="--", linewidth=1.2)
    ax.plot([1, 1], [0, 2], color=fs.GRAY, linestyle="--", linewidth=1.2)
    ax.text(1.12, 1.62, "f(1) is undefined", color=fs.DARK, fontsize=10)
    ax.text(-0.95, 2.12, "limit is 2", color=fs.DARK, fontsize=10)
    ax.text(0.7, 3.5, "f(x) = (x$^2$ - 1) / (x - 1)", color=fs.GREEN, fontsize=11)
    ax.set_xlim(-1, 3)
    ax.set_ylim(0, 4.2)
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    ax.set_xticks([-1, 0, 1, 2, 3])
    fs.save(fig, FOLDER, f"{SLUG}-hole")


def no_limit():
    fig, axes = plt.subplots(1, 3, figsize=(10.4, 3.3))

    # jump at x = 1
    ax = axes[0]
    xl = np.linspace(-0.5, 1, 100, endpoint=False)
    xr = np.linspace(1, 2.5, 100)
    ax.plot(xl, xl, color=fs.GREEN)
    ax.plot(xr, xr + 1, color=fs.GREEN)
    open_dot(ax, 1, 1)
    closed_dot(ax, 1, 2)
    ax.text(-0.45, 1.5, "left limit 1", color=fs.DARK, fontsize=10)
    ax.text(1.1, 1.15, "right limit 2", color=fs.DARK, fontsize=10)
    ax.set_xlim(-0.5, 2.5)
    ax.set_ylim(-0.5, 3.7)
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")

    # blow-up 1/x^2
    ax = axes[1]
    xl = np.linspace(-2, -0.2, 200)
    xr = np.linspace(0.2, 2, 200)
    ax.plot(xl, 1 / xl**2, color=fs.BLUE)
    ax.plot(xr, 1 / xr**2, color=fs.BLUE)
    ax.axvline(0, color=fs.GRAY, linestyle="--", linewidth=1.2)
    ax.text(0.2, 15.5, "grows without bound", color=fs.DARK, fontsize=10)
    ax.text(0.35, 10.5, r"$f(x)=\frac{1}{x^2}$", color=fs.BLUE, fontsize=11)
    ax.set_xlim(-2, 2)
    ax.set_ylim(0, 18)
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")

    # oscillation sin(1/x)
    ax = axes[2]
    x = np.linspace(0.004, 0.6, 30000)
    ax.plot(x, np.sin(1 / x), color=fs.RED, linewidth=0.9)
    x = -x
    ax.plot(x, np.sin(1 / x), color=fs.RED, linewidth=0.9)
    ax.axvline(0, color=fs.GRAY, linestyle="--", linewidth=1.2)
    ax.text(-0.58, 1.45, r"$f(x)=\sin\frac{1}{x}$", color=fs.RED, fontsize=11)
    ax.text(0.03, -1.55, "swings between -1 and 1", color=fs.DARK, fontsize=10, ha="left")
    ax.set_xlim(-0.6, 0.6)
    ax.set_ylim(-1.8, 1.9)
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")

    fig.tight_layout(w_pad=2.0)
    fs.save(fig, FOLDER, f"{SLUG}-no-limit")


def sine_geometry():
    t = 0.8
    fig, ax = fs.figure(4.8, 4.4)
    th = np.linspace(0, np.pi / 2, 200)
    ax.plot(np.cos(th), np.sin(th), color=fs.DARK, linewidth=1.4)
    P = (np.cos(t), np.sin(t))
    A = (1.0, 0.0)
    T = (1.0, np.tan(t))
    O = (0.0, 0.0)
    # triangle OAT (largest), sector, triangle OAP
    ax.add_patch(Polygon([O, A, T], closed=True, facecolor=fs.LIGHT, edgecolor=fs.BLUE, linewidth=1.6, zorder=1))
    ax.add_patch(Wedge(O, 1.0, 0, np.degrees(t), facecolor="#bfe9d7", edgecolor=fs.GREEN, linewidth=1.6, zorder=2))
    ax.add_patch(Polygon([O, A, P], closed=True, facecolor="#f4c8cb", edgecolor=fs.RED, linewidth=1.6, zorder=3))
    ax.plot([P[0], P[0]], [0, P[1]], color=fs.DARK, linestyle="--", linewidth=1.0, zorder=4)
    for name, pt, off in [("O", O, (-0.07, -0.07)), ("A", A, (0.04, -0.09)), ("P", P, (-0.09, 0.05)), ("T", T, (0.04, 0.03))]:
        ax.plot(*pt, "o", color=fs.DARK, markersize=4, zorder=6)
        ax.text(pt[0] + off[0], pt[1] + off[1], name, fontsize=11, color=fs.DARK)
    ax.text(0.05, 0.035, "x", fontsize=11, color=fs.DARK)
    ax.text(P[0] - 0.115, P[1] / 2 - 0.02, r"$\sin x$", fontsize=10, color=fs.DARK)
    ax.text(1.04, np.tan(t) / 2 - 0.02, r"$\tan x$", fontsize=10, color=fs.BLUE)
    ax.text(0.28, 0.03, "", fontsize=10)
    ax.text(0.45, -0.1, "radius 1", fontsize=10, color=fs.DARK)
    ax.set_aspect("equal")
    ax.set_xlim(-0.15, 1.35)
    ax.set_ylim(-0.18, 1.2)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.spines["left"].set_visible(False)
    ax.spines["bottom"].set_visible(False)
    fs.save(fig, FOLDER, f"{SLUG}-sine-geometry")


def squeeze():
    fig, ax = fs.figure(5.4, 3.6)
    x = np.linspace(-0.3, 0.3, 40001)
    x = x[x != 0]
    ax.plot(x, x**2 * np.sin(1 / x), color=fs.GREEN, linewidth=0.9)
    xs = np.linspace(-0.3, 0.3, 300)
    ax.plot(xs, xs**2, color=fs.BLUE, linewidth=1.6)
    ax.plot(xs, -(xs**2), color=fs.RED, linewidth=1.6)
    ax.text(0.205, 0.062, r"$x^2$", color=fs.BLUE, fontsize=11)
    ax.text(0.205, -0.07, r"$-x^2$", color=fs.RED, fontsize=11)
    ax.text(-0.29, 0.07, r"$x^2\sin\frac{1}{x}$", color=fs.GREEN, fontsize=11)
    ax.set_xlim(-0.3, 0.3)
    ax.set_ylim(-0.1, 0.1)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    fs.save(fig, FOLDER, f"{SLUG}-squeeze")


def at_infinity():
    fig, ax = fs.figure(5.4, 3.6)
    x = np.linspace(-30, 40, 1400)
    ax.plot(x, (3 * x**2 + x) / (2 * x**2 + 5), color=fs.GREEN)
    ax.axhline(1.5, color=fs.RED, linestyle="--", linewidth=1.4)
    ax.text(-29, 1.58, "y = 3/2", color=fs.RED, fontsize=10)
    ax.text(10, 0.6, "f(x) = (3x$^2$ + x) / (2x$^2$ + 5)", color=fs.GREEN, fontsize=11)
    ax.plot([7.5], [1.5], "o", color=fs.DARK, markersize=4, zorder=5)
    ax.text(9, 1.68, "crosses y = 3/2 at x = 7.5", color=fs.DARK, fontsize=10)
    ax.set_xlim(-30, 40)
    ax.set_ylim(-0.2, 2.0)
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    fs.save(fig, FOLDER, f"{SLUG}-at-infinity")


if __name__ == "__main__":
    hole()
    no_limit()
    sine_geometry()
    squeeze()
    at_infinity()
