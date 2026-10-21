"""Figures for docs/05-university-core/03-applications-of-derivatives/03-mean-value-theorem-and-extrema.md.

Run from the repo root:

    .venv/Scripts/python tools/figures/05-university-core/mean-value-theorem-and-extrema.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

import figstyle as fs  # noqa: E402

FOLDER = "05-university-core"
SLUG = "mean-value-theorem-and-extrema"
BOX = dict(facecolor="white", edgecolor="none", pad=0.4, alpha=0.9)


def grid(ax, size=9):
    ax.tick_params(labelsize=size, length=3)
    ax.grid(True)
    ax.set_axisbelow(True)


def rolle_and_mvt():
    """f(x) = x^3/3 - 2x^2 + 3x + 1: Rolle on [0, 3], the mean value theorem on [0, 4]."""
    f = lambda t: t**3 / 3 - 2 * t**2 + 3 * t + 1
    fp = lambda t: t**2 - 4 * t + 3
    fig, (a, b) = plt.subplots(1, 2, figsize=(9.4, 3.8))
    x = np.linspace(-0.3, 4.3, 400)
    for ax in (a, b):
        grid(ax)
        ax.plot(x, f(x), color=fs.GREEN, lw=2.4, zorder=3)
        ax.set_xlim(-0.3, 4.3)
        ax.set_ylim(0, 3.6)
        ax.set_xlabel("x")

    # Rolle on [0, 3]
    a.plot([0, 3], [f(0), f(3)], color=fs.BLUE, lw=1.8)
    a.plot([0, 3], [f(0), f(3)], "o", color=fs.DARK, ms=6, zorder=5)
    a.plot([0.4, 1.6], [f(1)] * 2, color=fs.RED, lw=2.0)
    a.plot([1], [f(1)], "o", color=fs.RED, ms=6.5, zorder=5)
    a.text(1.0, f(1) + 0.18, "f′(c) = 0 at c = 1", color=fs.RED, fontsize=10, ha="center", va="bottom")
    a.text(1.5, 0.85, "f(0) = f(3) = 1", color=fs.BLUE, fontsize=10, ha="center", va="top")
    a.set_xticks([0, 1, 2, 3, 4])

    # MVT on [0, 4]
    m = (f(4) - f(0)) / 4
    b.plot([0, 4], [f(0), f(4)], color=fs.BLUE, lw=1.8)
    b.plot([0, 4], [f(0), f(4)], "o", color=fs.DARK, ms=6, zorder=5)
    for c in (2 - (4 / 3) ** 0.5, 2 + (4 / 3) ** 0.5):
        lx = np.array([c - 0.9, c + 0.9])
        b.plot(lx, f(c) + m * (lx - c), color=fs.RED, lw=2.0)
        b.plot([c], [f(c)], "o", color=fs.RED, ms=6.5, zorder=5)
    c1 = 2 - (4 / 3) ** 0.5
    c2 = 2 + (4 / 3) ** 0.5
    b.text(c1 - 0.1, f(c1) + 0.55, "c ≈ 0.85", color=fs.RED, fontsize=10, ha="right", va="center")
    b.text(c2 + 0.1, f(c2) - 0.45, "c ≈ 3.15", color=fs.RED, fontsize=10, ha="left", va="center")
    b.text(1.6, 0.5, "chord, slope 1/3", color=fs.BLUE, fontsize=10, ha="center", va="center")
    b.set_xticks([0, 1, 2, 3, 4])
    fs.save(fig, FOLDER, f"{SLUG}-rolle-and-mvt")


def extrema():
    """f(x) = x^3 - 3x^2 + 1 on [-0.5, 3.5] with its extreme points labelled."""
    f = lambda t: t**3 - 3 * t**2 + 1
    fig, ax = fs.figure(5.8, 4.0)
    grid(ax)
    x = np.linspace(-0.5, 3.5, 400)
    ax.plot(x, f(x), color=fs.GREEN, lw=2.4, zorder=3)
    pts = [(-0.5, fs.ORANGE), (0, fs.BLUE), (2, fs.RED), (3.5, fs.RED)]
    for px, c in pts:
        ax.plot([px], [f(px)], "o", color=c, ms=7, zorder=5)
    ax.text(0.12, 1.45, "local max, f(0) = 1\n(critical point)", color=fs.BLUE, fontsize=9.5, ha="left", va="center")
    ax.text(2.1, -3.0, "absolute min, f(2) = −3\n(critical point)", color=fs.RED, fontsize=9.5, ha="left", va="center")
    ax.text(3.2, 6.9, "absolute max\nf(3.5) = 7.125\n(endpoint)", color=fs.RED, fontsize=9.5, ha="right", va="center")
    ax.text(-0.42, -0.5, "endpoint\nf(−0.5) = 0.125", color=fs.ORANGE, fontsize=9.5, ha="left", va="top")
    ax.set_xlim(-0.8, 3.8)
    ax.set_ylim(-4.2, 8.2)
    ax.set_xlabel("x")
    fs.save(fig, FOLDER, f"{SLUG}-extrema")


def evt_fails():
    """Three ways the extreme value theorem's conditions can fail."""
    fig, axs = plt.subplots(1, 3, figsize=(9.6, 3.2))
    for ax in axs:
        grid(ax, 8)
        ax.set_xlabel("x", fontsize=9)

    a = axs[0]
    x = np.linspace(0, 1, 200)
    a.plot(x, x, color=fs.GREEN, lw=2.4)
    a.plot([0, 1], [0, 1], "o", mfc="white", mec=fs.GREEN, ms=7, zorder=5)
    a.text(0.05, 0.88, "f(x) = x on (0, 1)\nno max, no min", color=fs.DARK, fontsize=9.5, ha="left", va="center")
    a.set_xlim(-0.15, 1.15)
    a.set_ylim(-0.15, 1.15)

    b = axs[1]
    x = np.linspace(0.12, 1, 300)
    b.plot(x, 1 / x, color=fs.GREEN, lw=2.4)
    b.plot([1], [1], "o", color=fs.GREEN, ms=6.5, zorder=5)
    b.text(0.4, 6.5, "f(x) = 1/x on (0, 1]\nno max (unbounded)", color=fs.DARK, fontsize=9.5, ha="left", va="center")
    b.set_xlim(-0.05, 1.1)
    b.set_ylim(0, 8.5)

    c = axs[2]
    c.plot([0, 1], [0, 1], color=fs.GREEN, lw=2.4)
    c.plot([1, 2], [0, 0], color=fs.GREEN, lw=2.4)
    c.plot([0, 1], [0, 0], "o", color=fs.GREEN, ms=6.5, zorder=5)
    c.plot([1], [1], "o", mfc="white", mec=fs.GREEN, ms=7, zorder=5)
    c.plot([0, 1], [0, 1], "o", mfc="none", mec="none")
    c.plot([2], [0], "o", color=fs.GREEN, ms=6.5, zorder=5)
    c.plot([1], [0], "o", color=fs.GREEN, ms=6.5, zorder=6)
    c.text(0.05, 1.15, "jump at 1: no max", color=fs.DARK, fontsize=9.5, ha="left", va="center")
    c.set_xlim(-0.15, 2.15)
    c.set_ylim(-0.15, 1.35)
    fs.save(fig, FOLDER, f"{SLUG}-evt-fails")


def critical_points():
    """Three kinds of critical point at x = 0."""
    fig, axs = plt.subplots(1, 3, figsize=(9.6, 3.2))
    x = np.linspace(-1, 1, 400)
    specs = [
        (x**2, "f(x) = x²", "f′(0) = 0: local min"),
        (x**3, "f(x) = x³", "f′(0) = 0: no extremum"),
        (np.abs(x), "f(x) = |x|", "f′(0) does not exist:\nlocal min"),
    ]
    for ax, (y, name, note) in zip(axs, specs):
        grid(ax, 8)
        ax.plot(x, y, color=fs.GREEN, lw=2.4)
        ax.plot([0], [0], "o", color=fs.RED, ms=7, zorder=5)
        ax.set_xlim(-1.15, 1.15)
        ax.set_ylim(-1.3, 1.3)
        ax.text(-1.08, 1.12, name, color=fs.DARK, fontsize=10, ha="left", va="center")
        ax.text(0.0, -0.78, note, color=fs.RED, fontsize=9.5, ha="center", va="center")
        ax.set_xticks([-1, 0, 1])
        ax.set_yticks([-1, 0, 1])
    fs.save(fig, FOLDER, f"{SLUG}-critical-points")


if __name__ == "__main__":
    rolle_and_mvt()
    extrema()
    evt_fails()
    critical_points()
