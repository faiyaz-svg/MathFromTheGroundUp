"""Figures for docs/05-university-core/09-multivariable-calculus-light/01-parametric-polar-and-3d-coordinates.md.

Run from the repo root:

    .venv/Scripts/python tools/figures/05-university-core/parametric-polar-and-3d-coordinates.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
from matplotlib.patches import Wedge  # noqa: E402

import figstyle as fs  # noqa: E402

FOLDER = "05-university-core"
SLUG = "parametric-polar-and-3d-coordinates"
BOX = dict(facecolor="white", edgecolor="none", pad=0.4, alpha=0.9)


def projectile():
    """The path x = 20t, y = 15t - 4.9t^2 with velocity vectors at t = 0, 1, 2, 3."""
    fig, ax = fs.figure(8.4, 3.4)
    t = np.linspace(0, 150 / 49, 300)
    ax.plot(20 * t, 15 * t - 4.9 * t**2, color=fs.GREEN, lw=2.4)
    for tk in (0, 1, 2, 3):
        x, y = 20 * tk, 15 * tk - 4.9 * tk**2
        vx, vy = 20, 15 - 9.8 * tk
        ax.annotate("", xy=(x + 0.9 * vx, y + 0.9 * vy), xytext=(x, y),
                    arrowprops=dict(arrowstyle="-|>", color=fs.RED, lw=1.8, shrinkA=0, shrinkB=0))
        ax.plot([x], [y], "o", color=fs.DARK, ms=5, zorder=5)
        if tk == 3:
            ax.text(x - 1.5, y + 1.4, f"t = {tk}", ha="right", va="bottom", fontsize=9.5, color=fs.DARK)
        else:
            ax.text(x, y - 1.6, f"t = {tk}", ha="center", va="top", fontsize=9.5, color=fs.DARK)
    ax.text(68, 14.5, "red arrows: velocity (20, 15 − 9.8t)", color=fs.RED, fontsize=10, ha="right", va="bottom")
    ax.text(68, -3.2, "lands at t ≈ 3.06, x ≈ 61.2", color=fs.DARK, fontsize=9.5, ha="right", va="center")
    ax.set_aspect("equal")
    ax.set_xlim(-4, 70)
    ax.set_ylim(-5, 17)
    ax.set_xlabel("x (m)")
    ax.set_ylabel("y (m)")
    ax.grid(True)
    ax.set_axisbelow(True)
    ax.tick_params(labelsize=9)
    fs.save(fig, FOLDER, f"{SLUG}-projectile")


def polar():
    """Left: polar and Cartesian coordinates of a point. Right: the cardioid r = 1 + cos(theta) and a thin sector."""
    fig, (a, b) = plt.subplots(1, 2, figsize=(9.0, 3.8), gridspec_kw={"width_ratios": [1, 1.1]})
    # left
    r, th = 2.0, np.radians(50)
    px, py = r * np.cos(th), r * np.sin(th)
    a.set_aspect("equal")
    a.axhline(0, color=fs.GRAY, lw=1)
    a.axvline(0, color=fs.GRAY, lw=1)
    a.plot([0, px], [0, py], color=fs.GREEN, lw=2.4)
    a.plot([px, px], [0, py], color=fs.BLUE, lw=1.6, ls="--")
    a.plot([0, px], [0, 0], color=fs.BLUE, lw=1.6, ls="--")
    a.add_patch(Wedge((0, 0), 0.7, 0, 50, fc="none", ec=fs.RED, lw=1.8))
    a.plot([px], [py], "o", color=fs.DARK, ms=6, zorder=5)
    a.text(px + 0.1, py + 0.12, "(r, θ) = (x, y)", fontsize=10, ha="left", va="bottom")
    a.text(0.62 * px - 0.18, 0.62 * py + 0.12, "r", color=fs.GREEN, fontsize=11, ha="right", va="bottom")
    a.text(0.85, 0.2, "θ", color=fs.RED, fontsize=11, ha="left", va="center")
    a.text(px / 2, -0.12, "x = r cos θ", color=fs.BLUE, fontsize=10, ha="center", va="top")
    a.text(px + 0.1, py / 2, "y = r sin θ", color=fs.BLUE, fontsize=10, ha="left", va="center")
    a.set_xlim(-0.6, 3.6)
    a.set_ylim(-0.7, 2.6)
    a.axis("off")
    # right
    th_all = np.linspace(0, 2 * np.pi, 400)
    rr = 1 + np.cos(th_all)
    b.plot(rr * np.cos(th_all), rr * np.sin(th_all), color=fs.GREEN, lw=2.4)
    t0, t1 = np.radians(40), np.radians(58)
    tt = np.linspace(t0, t1, 30)
    r_t = 1 + np.cos(tt)
    xs = np.concatenate([[0], r_t * np.cos(tt), [0]])
    ys = np.concatenate([[0], r_t * np.sin(tt), [0]])
    b.fill(xs, ys, color=fs.RED, alpha=0.55, lw=0)
    b.text(1.25, 1.2, "sliver of area\n½ r² dθ", color=fs.RED, fontsize=10, ha="left", va="bottom")
    b.axhline(0, color=fs.GRAY, lw=1)
    b.axvline(0, color=fs.GRAY, lw=1)
    b.text(1.0, -1.8, "r = 1 + cos θ, area 3π/2", ha="center", fontsize=10)
    b.set_aspect("equal")
    b.set_xlim(-0.8, 2.6)
    b.set_ylim(-2.0, 2.1)
    b.axis("off")
    fs.save(fig, FOLDER, f"{SLUG}-polar")


def surface():
    """The hill z = 4 - x^2 - 2y^2 as a surface and as a contour map."""
    fig = plt.figure(figsize=(9.2, 3.9))
    a = fig.add_subplot(1, 2, 1, projection="3d")
    b = fig.add_subplot(1, 2, 2)
    X, Y = np.meshgrid(np.linspace(-2, 2, 60), np.linspace(-1.6, 1.6, 60))
    Z = 4 - X**2 - 2 * Y**2
    Zm = np.where(Z >= 0, Z, np.nan)
    a.plot_surface(X, Y, Zm, color=fs.GREEN, alpha=0.35, linewidth=0, shade=False, rstride=2, cstride=2)
    a.contour(X, Y, Z, levels=[0, 1, 2, 3], zdir="z", offset=0, colors=fs.DARK, linewidths=1.0)
    for lev in (1, 2, 3):
        th = np.linspace(0, 2 * np.pi, 120)
        xs = np.sqrt(4 - lev) * np.cos(th)
        ys = np.sqrt((4 - lev) / 2) * np.sin(th)
        a.plot(xs, ys, np.full_like(th, lev), color=fs.RED, lw=1.4)
    a.set_zlim(0, 4.2)
    a.set_xlabel("x", labelpad=-6)
    a.set_ylabel("y", labelpad=-6)
    a.set_zlabel("z", labelpad=-8)
    a.set_xticks([-2, 0, 2])
    a.set_yticks([-1, 0, 1])
    a.set_zticks([0, 2, 4])
    a.tick_params(labelsize=8, pad=-3)
    a.view_init(elev=24, azim=-58)
    a.set_box_aspect((1.2, 1, 0.8))
    cs = b.contour(X, Y, Z, levels=[0, 1, 2, 3], colors=[fs.GREEN, fs.BLUE, fs.ORANGE, fs.RED], linewidths=2)
    b.clabel(cs, fmt=lambda v: f"z = {v:.0f}", fontsize=9, inline=True)
    b.plot([0], [0], "o", color=fs.DARK, ms=5)
    b.text(0.08, 0.08, "peak z = 4", fontsize=9.5, va="bottom")
    b.set_aspect("equal")
    b.set_xlabel("x")
    b.set_ylabel("y")
    b.tick_params(labelsize=9)
    b.grid(True)
    b.set_axisbelow(True)
    fs.save(fig, FOLDER, f"{SLUG}-surface")


if __name__ == "__main__":
    projectile()
    polar()
    surface()
