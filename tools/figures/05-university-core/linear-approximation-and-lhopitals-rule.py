"""Figures for docs/05-university-core/03-applications-of-derivatives/02-linear-approximation-and-lhopitals-rule.md.

Run from the repo root:

    .venv/Scripts/python tools/figures/05-university-core/linear-approximation-and-lhopitals-rule.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

import figstyle as fs  # noqa: E402

FOLDER = "05-university-core"
SLUG = "linear-approximation-and-lhopitals-rule"
BOX = dict(facecolor="white", edgecolor="none", pad=0.4, alpha=0.9)


def grid(ax, size=9):
    ax.tick_params(labelsize=size, length=3)
    ax.grid(True)
    ax.set_axisbelow(True)


def linearization():
    """sqrt(x) with its tangent at 4, and the size of the error near 4."""
    fig, (a, b) = plt.subplots(1, 2, figsize=(9.0, 3.8), gridspec_kw={"width_ratios": [1.15, 1]})
    grid(a)
    x = np.linspace(0, 9, 400)
    a.plot(x, np.sqrt(x), color=fs.GREEN, lw=2.4)
    a.plot(x, 2 + (x - 4) / 4, color=fs.BLUE, lw=1.8)
    a.plot([4], [2], "o", color=fs.DARK, ms=6.5, zorder=5)
    a.text(4.15, 1.55, "(4, 2)", color=fs.DARK, fontsize=10, ha="left", va="top")
    a.text(8.9, 3.18, "y = √x", color=fs.GREEN, fontsize=10.5, ha="right", va="bottom")
    a.text(4.6, 0.75, "tangent at 4:\nL(x) = 2 + (x − 4)/4", color=fs.BLUE, fontsize=10, ha="left", va="center")
    a.set_xlim(0, 9)
    a.set_ylim(0, 3.7)
    a.set_xlabel("x")

    grid(b)
    h = np.linspace(-2, 2, 400)
    err = (2 + h / 4) - np.sqrt(4 + h)
    b.plot(h, err, color=fs.RED, lw=2.4)
    b.plot(h, h**2 / 64, color=fs.DARK, lw=1.4, ls="--")
    b.text(0.0, 0.07, "error L(x) − √x", color=fs.RED, fontsize=10, ha="center", va="center")
    b.text(0.0, 0.04, "dashed: h²/64", color=fs.DARK, fontsize=9.5, ha="center", va="center", bbox=BOX)
    b.set_xlabel("h = x − 4")
    b.set_xlim(-2.1, 2.1)
    b.set_ylim(-0.005, 0.08)
    fs.save(fig, FOLDER, f"{SLUG}-linearization")


def newton_steps():
    """Newton's method for x^2 - 2 = 0 from x0 = 2."""
    fig, ax = fs.figure(5.6, 4.0)
    grid(ax)
    ax.axhline(0, color=fs.DARK, lw=1.0)
    f = lambda t: t**2 - 2
    xs = np.linspace(1.15, 2.25, 300)
    ax.plot(xs, f(xs), color=fs.GREEN, lw=2.4, zorder=3)
    pts = [2.0, 1.5, 1.4166666667]
    cols = [fs.RED, fs.ORANGE, fs.BLUE]
    for p, c in zip(pts, cols):
        slope = 2 * p
        lx = np.array([p - f(p) / slope - 0.02, p + 0.2])
        ax.plot(lx, f(p) + slope * (lx - p), color=c, lw=1.6, zorder=2)
        ax.plot([p, p], [0, f(p)], color=c, lw=1.1, ls="--", zorder=2)
        ax.plot([p], [f(p)], "o", color=c, ms=5.5, zorder=5)
        ax.plot([p], [0], "o", color=c, ms=5.5, zorder=5)
    ax.text(2.0, -0.17, "x₀ = 2", color=fs.RED, fontsize=10, ha="center", va="top")
    ax.text(1.5, -0.17, "x₁ = 1.5", color=fs.ORANGE, fontsize=10, ha="center", va="top")
    ax.text(1.38, 0.22, "x₂ ≈ 1.4167", color=fs.BLUE, fontsize=10, ha="right", va="bottom")
    ax.text(1.5, 2.4, "y = x² − 2", color=fs.GREEN, fontsize=10.5, ha="left", va="center")
    ax.set_xlim(1.15, 2.3)
    ax.set_ylim(-0.6, 3.0)
    ax.set_xlabel("x")
    fs.save(fig, FOLDER, f"{SLUG}-newton")


def newton_fails():
    """A cycle for x^3 - 2x + 2 from 0, and divergence for the cube root from 1."""
    fig, (a, b) = plt.subplots(1, 2, figsize=(9.2, 3.8))
    for ax in (a, b):
        grid(ax)
        ax.spines["bottom"].set_position("zero")
        ax.spines["left"].set_position("zero")

    x = np.linspace(-1.9, 1.9, 400)
    f = lambda t: t**3 - 2 * t + 2
    a.plot(x, f(x), color=fs.GREEN, lw=2.4, zorder=3)
    a.plot([-0.4, 1.3], [2 + 0.8, 2 - 2.6], color=fs.RED, lw=1.6)
    a.plot([-0.6, 1.4], [-0.6, 1.4], color=fs.BLUE, lw=1.6)
    a.plot([0, 1], [0, 0], "o", color=fs.DARK, ms=5.5, zorder=5)
    a.plot([0, 1], [2, 1], "o", color=fs.DARK, ms=5.5, zorder=5)
    a.text(0.15, 2.35, "start x₀ = 0", color=fs.RED, fontsize=9.5, ha="left", va="bottom")
    a.text(1.2, 0.55, "x₁ = 1", color=fs.BLUE, fontsize=9.5, ha="left", va="center")
    a.set_yticks([1, 2, 3, 4])
    a.text(-1.9, 3.9, "y = x³ − 2x + 2", color=fs.GREEN, fontsize=10, ha="left", va="center")
    a.text(-0.2, -0.9, "the next step\nreturns to 0", color=fs.DARK, fontsize=9.5, ha="right", va="center")
    a.set_xlim(-2.0, 2.0)
    a.set_ylim(-1.8, 4.6)
    a.set_xticks([-1, 1, 2])

    xs = np.linspace(-4.6, 4.6, 600)
    cb = np.cbrt(xs)
    b.plot(xs, cb, color=fs.GREEN, lw=2.4, zorder=3)
    lx = np.array([-2.4, 4.4])
    b.plot(lx, 1 + (lx - 1) / 3, color=fs.RED, lw=1.6)
    p = -2.0
    s = 1 / (3 * abs(p) ** (2 / 3))
    lx2 = np.array([-3.0, 4.6])
    b.plot(lx2, np.cbrt(p) + s * (lx2 - p), color=fs.BLUE, lw=1.6)
    b.plot([1, -2, 4], [1, np.cbrt(-2), np.cbrt(4)], "o", color=fs.DARK, ms=5, zorder=5)
    b.plot([-2, 4], [0, 0], "o", color=fs.DARK, ms=5, zorder=5)
    b.text(1.3, 0.6, "x₀ = 1", color=fs.RED, fontsize=9.5, ha="left", va="center")
    b.text(-2.1, -1.5, "x₁ = −2", color=fs.BLUE, fontsize=9.5, ha="right", va="top")
    b.text(4.0, 0.4, "x₂ = 4", color=fs.DARK, fontsize=9.5, ha="right", va="bottom")
    b.text(-4.4, 1.5, "y = ∛x", color=fs.GREEN, fontsize=10, ha="left", va="center")
    b.set_xlim(-4.7, 4.7)
    b.set_ylim(-2.1, 2.3)
    b.set_xticks([-4, -2, 2, 4])
    fs.save(fig, FOLDER, f"{SLUG}-newton-fails")


def growth():
    """Ratios that go to 0 only eventually: ln x over sqrt x, and x^5 over e^x."""
    fig, (a, b) = plt.subplots(1, 2, figsize=(9.0, 3.6))
    grid(a)
    x = np.linspace(1, 600, 1200)
    a.plot(x, np.log(x) / np.sqrt(x), color=fs.GREEN, lw=2.4)
    pk = np.e**2
    a.plot([pk], [2 / np.e], "o", color=fs.DARK, ms=6)
    a.text(pk + 12, 2 / np.e + 0.03, "peak 2/e ≈ 0.74 at x = e² ≈ 7.4", color=fs.DARK, fontsize=9.5, ha="left", va="bottom")
    a.text(590, 0.1, "ln x / √x", color=fs.GREEN, fontsize=10.5, ha="right", va="bottom")
    a.set_xlim(0, 600)
    a.set_ylim(0, 0.95)
    a.set_xlabel("x")

    grid(b)
    x2 = np.linspace(0, 35, 800)
    b.plot(x2, x2**5 * np.exp(-x2), color=fs.RED, lw=2.4)
    b.plot([5], [5**5 * np.exp(-5)], "o", color=fs.DARK, ms=6)
    b.text(6.2, 5**5 * np.exp(-5) - 1.5, "peak ≈ 21 at x = 5", color=fs.DARK, fontsize=9.5, ha="left", va="top")
    b.text(34, 3.5, "x⁵ / eˣ", color=fs.RED, fontsize=10.5, ha="right", va="bottom")
    b.axhline(1, color=fs.GRAY, lw=1.0, ls="--")
    b.text(34, 1.2, "ratio = 1", color=fs.GRAY, fontsize=9, ha="right", va="bottom")
    b.set_xlim(0, 35)
    b.set_ylim(0, 25)
    b.set_xlabel("x")
    fs.save(fig, FOLDER, f"{SLUG}-growth")


if __name__ == "__main__":
    linearization()
    newton_steps()
    newton_fails()
    growth()
