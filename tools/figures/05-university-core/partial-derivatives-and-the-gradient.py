"""Figures for docs/05-university-core/09-multivariable-calculus-light/02-partial-derivatives-and-the-gradient.md.

Run from the repo root:

    .venv/Scripts/python tools/figures/05-university-core/partial-derivatives-and-the-gradient.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

import figstyle as fs  # noqa: E402

FOLDER = "05-university-core"
SLUG = "partial-derivatives-and-the-gradient"


def limit_paths():
    """f(x, y) = xy / (x^2 + y^2): the limit along y = mx depends on m."""
    fig, (a, b) = plt.subplots(1, 2, figsize=(9.0, 3.7), gridspec_kw={"width_ratios": [1, 1.1]})
    x = np.linspace(-1, 1, 10)
    spec = [(0, fs.GREEN, "m = 0: values 0"), (1, fs.RED, "m = 1: values 1/2"),
            (-1, fs.BLUE, "m = −1: values −1/2")]
    for m, col, lab in spec:
        a.plot(x, m * x, color=col, lw=2.2)
    a.plot([0, 0], [-1, 1], color=fs.ORANGE, lw=2.2)
    a.plot([0], [0], "o", mfc="white", mec=fs.DARK, ms=7, zorder=5)
    a.text(1.03, 0.0, "m = 0\nvalue 0", color=fs.GREEN, fontsize=9.5, va="center")
    a.text(1.03, 1.0, "m = 1\nvalue 1/2", color=fs.RED, fontsize=9.5, va="center")
    a.text(1.03, -1.0, "m = −1\nvalue −1/2", color=fs.BLUE, fontsize=9.5, va="center")
    a.text(-0.05, 1.05, "x = 0: value 0", color=fs.ORANGE, fontsize=9.5, va="bottom", ha="right")
    a.set_aspect("equal")
    a.set_xlim(-1.25, 1.95)
    a.set_ylim(-1.3, 1.4)
    a.axhline(0, color=fs.GRAY, lw=0.6)
    a.axvline(0, color=fs.GRAY, lw=0.6)
    a.set_xlabel("x")
    a.set_ylabel("y")
    a.tick_params(labelsize=9)
    m = np.linspace(-6, 6, 400)
    b.plot(m, m / (1 + m**2), color=fs.GREEN, lw=2.4)
    b.axhline(0, color=fs.GRAY, lw=0.8)
    b.plot([1, -1, 0], [0.5, -0.5, 0], "o", color=fs.RED, ms=6, zorder=5)
    b.text(1.0, 0.57, "m = 1", color=fs.RED, fontsize=9.5, va="bottom", ha="center")
    b.text(-1.0, -0.57, "m = −1", color=fs.RED, fontsize=9.5, va="top", ha="center")
    b.text(0.2, -0.08, "m = 0", color=fs.RED, fontsize=9.5, va="top")
    b.set_xlabel("slope m of the line y = mx")
    b.set_ylabel("f(x, mx) for x ≠ 0")
    b.set_ylim(-0.75, 0.75)
    b.grid(True)
    b.set_axisbelow(True)
    b.tick_params(labelsize=9)
    fs.save(fig, FOLDER, f"{SLUG}-limit")


def gradient():
    """Contours of f = 4 - x^2 - 2y^2 with gradient arrows, and the hiker at (1, 1)."""
    fig, ax = fs.figure(6.2, 4.6)
    X, Y = np.meshgrid(np.linspace(-3, 3, 200), np.linspace(-2.2, 2.2, 200))
    Z = 4 - X**2 - 2 * Y**2
    levels = [-8, -6, -4, -2, 0, 1, 2, 3]
    ax.contour(X, Y, Z, levels=levels, colors=fs.GRAY, linewidths=1.2)
    gx, gy = np.meshgrid(np.arange(-2.5, 2.6, 1.0), np.arange(-1.5, 1.6, 1.0))
    mask = ~((np.abs(gx - 1) < 0.1) & (np.abs(gy - 1) < 0.1))
    ax.quiver(gx[mask], gy[mask], (-2 * gx)[mask], (-4 * gy)[mask], color=fs.GREEN, angles="xy",
              scale_units="xy", scale=6, width=0.005)
    ax.quiver([1], [1], [-2], [-4], color=fs.RED, angles="xy", scale_units="xy", scale=3, width=0.009)
    ax.plot([1], [1], "o", color=fs.DARK, ms=6, zorder=5)
    ax.plot([1 - 0.9, 1 + 0.9], [1 + 0.45, 1 - 0.45], color=fs.BLUE, lw=1.6, ls="--")
    ax.text(1.12, 1.07, "(1, 1)", fontsize=10, ha="left", va="bottom")
    ax.text(0.45, -0.55, "∇f = (−2, −4)", color=fs.RED, fontsize=10, ha="left", va="top", bbox=dict(fc="white", ec="none", alpha=0.9, pad=0.5))
    ax.text(2.0, 1.0, "contour\ndirection\n(2, −1)", color=fs.BLUE, fontsize=9.5, ha="left", va="center")
    ax.text(-2.9, 2.3, "green arrows: gradient at grid points (scaled down)", fontsize=9.5, va="top")
    ax.plot([0], [0], "o", color=fs.DARK, ms=4)
    ax.text(0.1, 0.06, "peak", fontsize=9.5, va="bottom", bbox=dict(fc="white", ec="none", alpha=0.9, pad=0.3))
    ax.set_aspect("equal")
    ax.set_xlim(-3, 3.3)
    ax.set_ylim(-2.2, 2.5)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.tick_params(labelsize=9)
    fs.save(fig, FOLDER, f"{SLUG}-gradient")


def descent():
    """Gradient descent on f = x^2 + 5y^2 from (4, 1.5): learning rates 0.18 and 0.05."""
    fig, ax = fs.figure(7.0, 3.6)
    X, Y = np.meshgrid(np.linspace(-0.5, 4.6, 300), np.linspace(-1.8, 1.8, 300))
    Z = X**2 + 5 * Y**2
    ax.contour(X, Y, Z, levels=[0.5, 2, 4, 8, 12, 16, 20, 24], colors=fs.GRAY, linewidths=1.0)
    for eta, col, n, lab, pos in [(0.18, fs.RED, 12, "η = 0.18: zigzags across the valley", (0.9, 1.75)),
                                  (0.05, fs.GREEN, 25, "η = 0.05: smooth but slow", (3.0, -1.5))]:
        p = np.array([4.0, 1.5])
        pts = [p.copy()]
        for _ in range(n):
            p = p - eta * np.array([2 * p[0], 10 * p[1]])
            pts.append(p.copy())
        pts = np.array(pts)
        ax.plot(pts[:, 0], pts[:, 1], "-o", color=col, ms=3.8, lw=1.6)
        ax.text(pos[0], pos[1], lab, color=col, fontsize=10, ha="left", va="center")
    ax.plot([4], [1.5], "o", color=fs.DARK, ms=6, zorder=6)
    ax.text(4.1, 1.5, "start (4, 1.5)", fontsize=9.5, ha="left", va="center")
    ax.plot([0], [0], "*", color=fs.DARK, ms=10, zorder=6)
    ax.text(0.0, -0.5, "minimum", fontsize=9.5, ha="center", va="top")
    ax.set_xlim(-0.5, 5.3)
    ax.set_ylim(-1.8, 2.1)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.tick_params(labelsize=9)
    fs.save(fig, FOLDER, f"{SLUG}-descent")


if __name__ == "__main__":
    limit_paths()
    gradient()
    descent()
