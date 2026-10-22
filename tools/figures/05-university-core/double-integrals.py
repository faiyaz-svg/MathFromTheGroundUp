"""Figures for docs/05-university-core/09-multivariable-calculus-light/04-double-integrals.md.

Run from the repo root:

    .venv/Scripts/python tools/figures/05-university-core/double-integrals.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
from matplotlib.patches import Polygon  # noqa: E402

import figstyle as fs  # noqa: E402

FOLDER = "05-university-core"
SLUG = "double-integrals"


def region():
    """The triangle 0 <= x <= y <= 1 sliced in the two orders."""
    fig, (a, b) = plt.subplots(1, 2, figsize=(9.0, 4.0))
    for ax in (a, b):
        ax.add_patch(Polygon([[0, 0], [0, 1], [1, 1]], closed=True, fc="#e3f4ec", ec=fs.GREEN, lw=2.2))
        ax.plot([0, 1], [0, 1], color=fs.GREEN, lw=2.2)
        ax.set_aspect("equal")
        ax.set_xlim(-0.15, 1.3)
        ax.set_ylim(-0.15, 1.2)
        ax.axhline(0, color=fs.GRAY, lw=0.8)
        ax.axvline(0, color=fs.GRAY, lw=0.8)
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.tick_params(labelsize=9)
        ax.text(1.03, 1.02, "y = x", color=fs.GREEN, fontsize=10, va="bottom")
        ax.text(0.5, 1.03, "y = 1", color=fs.GREEN, fontsize=10, ha="center", va="bottom")
        ax.text(0.2, 0.62, "region R", color=fs.DARK, fontsize=10, ha="center")
    for x in np.linspace(0.06, 0.94, 8):
        a.plot([x, x], [x, 1], color=fs.RED, lw=1.4)
    a.annotate("", xy=(0.4, 1.0), xytext=(0.4, 0.4), arrowprops=dict(arrowstyle="-|>", color=fs.RED, lw=2.0))
    a.text(0.43, 0.76, "y from x to 1", color=fs.RED, fontsize=10, ha="left", va="center",
           bbox=dict(fc="white", ec="none", alpha=0.9, pad=0.4))
    a.set_title("dy first, then x from 0 to 1", fontsize=10, color=fs.DARK)
    for yv in np.linspace(0.06, 0.94, 8):
        b.plot([0, yv], [yv, yv], color=fs.BLUE, lw=1.4)
    b.annotate("", xy=(0.6, 0.6), xytext=(0.0, 0.6), arrowprops=dict(arrowstyle="-|>", color=fs.BLUE, lw=2.0))
    b.text(0.04, 0.5, "x from 0 to y", color=fs.BLUE, fontsize=10, ha="left", va="top",
           bbox=dict(fc="white", ec="none", alpha=0.9, pad=0.4))
    b.set_title("dx first, then y from 0 to 1", fontsize=10, color=fs.DARK)
    fig.subplots_adjust(wspace=0.3)
    fs.save(fig, FOLDER, f"{SLUG}-region")


def polar_patch():
    """A small polar patch: sides dr and r dtheta."""
    fig, ax = fs.figure(5.6, 4.6)
    th = np.linspace(0, np.pi / 2, 100)
    for rr in (1, 2, 3):
        ax.plot(rr * np.cos(th), rr * np.sin(th), color=fs.GRAY, lw=1.0)
    for ang in np.linspace(0, 90, 7):
        c, s = np.cos(np.radians(ang)), np.sin(np.radians(ang))
        ax.plot([0, 3.2 * c], [0, 3.2 * s], color=fs.GRAY, lw=1.0)
    r0, r1 = 2.0, 2.7
    t0, t1 = np.radians(30), np.radians(52)
    tt = np.linspace(t0, t1, 40)
    xs = np.concatenate([r0 * np.cos(tt), r1 * np.cos(tt[::-1])])
    ys = np.concatenate([r0 * np.sin(tt), r1 * np.sin(tt[::-1])])
    ax.fill(xs, ys, color=fs.RED, alpha=0.55, lw=0)
    ax.plot(xs, ys, color=fs.RED, lw=1.6)
    ax.annotate("dA ≈ r dr dθ", xy=(1.95, 1.75), xytext=(2.3, 2.9), color=fs.RED, fontsize=11, ha="left",
                va="center", arrowprops=dict(arrowstyle="-", color=fs.RED, lw=0.9))
    ax.text(2.3, 0.92, "dr", color=fs.DARK, fontsize=10.5, ha="center", va="center")
    ax.text(1.3, 1.1, "r dθ", color=fs.DARK, fontsize=10.5, ha="right", va="center")
    ax.text(3.15, -0.12, "x", fontsize=10)
    ax.text(-0.15, 3.15, "y", fontsize=10, ha="right")
    ax.set_aspect("equal")
    ax.set_xlim(-0.3, 3.8)
    ax.set_ylim(-0.3, 3.5)
    ax.axis("off")
    fs.save(fig, FOLDER, f"{SLUG}-polar")


def solids():
    """Left: the cap z = 4 - x^2 - y^2 (volume 8 pi). Right: the bell z = exp(-(x^2 + y^2)) (volume pi)."""
    fig = plt.figure(figsize=(9.2, 3.9))
    a = fig.add_subplot(1, 2, 1, projection="3d")
    b = fig.add_subplot(1, 2, 2, projection="3d")
    r = np.linspace(0, 2, 40)
    th = np.linspace(0, 2 * np.pi, 80)
    R, T = np.meshgrid(r, th)
    a.plot_surface(R * np.cos(T), R * np.sin(T), 4 - R**2, color=fs.GREEN, alpha=0.45, linewidth=0, shade=False)
    a.plot(2 * np.cos(th), 2 * np.sin(th), np.zeros_like(th), color=fs.DARK, lw=1.6)
    a.set_zlim(0, 4.2)
    a.set_title("z = 4 − x² − y² over r ≤ 2", fontsize=10, color=fs.DARK)
    r = np.linspace(0, 2.6, 50)
    R, T = np.meshgrid(r, th)
    b.plot_surface(R * np.cos(T), R * np.sin(T), np.exp(-R**2), color=fs.BLUE, alpha=0.45, linewidth=0, shade=False)
    b.set_zlim(0, 1.1)
    b.set_title("z = e^(−(x² + y²))", fontsize=10, color=fs.DARK)
    for ax in (a, b):
        ax.set_xlabel("x", labelpad=-6)
        ax.set_ylabel("y", labelpad=-6)
        ax.tick_params(labelsize=8, pad=-3)
        ax.view_init(elev=24, azim=-58)
        ax.set_box_aspect((1, 1, 0.7))
    a.set_xticks([-2, 0, 2])
    a.set_yticks([-2, 0, 2])
    a.set_zticks([0, 2, 4])
    b.set_xticks([-2, 0, 2])
    b.set_yticks([-2, 0, 2])
    b.set_zticks([0, 0.5, 1])
    fig.subplots_adjust(wspace=0.05)
    fs.save(fig, FOLDER, f"{SLUG}-solids")


if __name__ == "__main__":
    region()
    polar_patch()
    solids()
