"""Figures for docs/05-university-core/05-sequences-and-series/01-sequences-and-their-limits.md.

Run from the repo root:

    .venv/Scripts/python tools/figures/05-university-core/sequences-and-their-limits.py
"""

import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

import figstyle as fs  # noqa: E402

FOLDER = "05-university-core"
SLUG = "sequences-and-their-limits"
BOX = dict(facecolor="white", edgecolor="none", pad=0.4, alpha=0.9)


def grid(ax, size=9):
    ax.tick_params(labelsize=size, length=3)
    ax.grid(True)
    ax.set_axisbelow(True)


def epsilon_n():
    """a_n = (2n+1)/(n+3) with the band of half-width 0.5 around 2; N = 8."""
    fig, ax = fs.figure(6.0, 3.8)
    grid(ax)
    n = np.arange(1, 21)
    a = (2 * n + 1) / (n + 3)
    ax.axhspan(1.5, 2.5, color=fs.GREEN, alpha=0.14, lw=0)
    ax.axhline(2, color=fs.DARK, lw=1.2, ls="--")
    ax.axvline(7.5, color=fs.RED, lw=1.4)
    out = n < 8
    ax.plot(n[out], a[out], "o", color=fs.RED, ms=6)
    ax.plot(n[~out], a[~out], "o", color=fs.GREEN, ms=6)
    ax.text(20.3, 2.0, "L = 2", color=fs.DARK, fontsize=10, ha="left", va="center", bbox=BOX)
    ax.text(20.3, 2.5, "L + ε", color=fs.GREEN, fontsize=10, ha="left", va="center")
    ax.text(20.3, 1.5, "L − ε", color=fs.GREEN, fontsize=10, ha="left", va="center")
    ax.text(7.9, 0.45, "from n = N = 8 on,\nevery term is inside the band", color=fs.RED, fontsize=10, ha="left", va="center")
    ax.text(1.1, 2.7, "aₙ = (2n + 1)/(n + 3),  ε = 0.5", color=fs.DARK, fontsize=10, ha="left", va="center")
    ax.set_xlim(0, 23.5)
    ax.set_ylim(0, 3.0)
    ax.set_xticks([0, 5, 8, 10, 15, 20])
    ax.set_xlabel("n")
    fs.save(fig, FOLDER, f"{SLUG}-epsilon-n")


def recursive():
    """Terms of a_{n+1} = sqrt(2 + a_n) and a cobweb on y = sqrt(2 + x), y = x."""
    fig, (a, b) = plt.subplots(1, 2, figsize=(9.4, 3.9), gridspec_kw={"width_ratios": [1, 1.05]})
    grid(a)
    terms = [0.0]
    for _ in range(9):
        terms.append(math.sqrt(2 + terms[-1]))
    idx = np.arange(0, 10)
    a.axhline(2, color=fs.DARK, lw=1.2, ls="--")
    a.plot(idx, terms, "o-", color=fs.GREEN, lw=1.6, ms=6)
    a.text(9.2, 2.07, "L = 2", color=fs.DARK, fontsize=10, ha="right", va="bottom")
    a.text(1.0, 0.35, "a₀ = 0, a₁ = √2 ≈ 1.414,\na₂ ≈ 1.848, a₃ ≈ 1.962", color=fs.GREEN, fontsize=9.5, ha="left", va="center")
    a.set_xlim(-0.3, 9.5)
    a.set_ylim(-0.1, 2.4)
    a.set_xlabel("n")
    a.set_xticks(range(0, 10))

    grid(b)
    x = np.linspace(0, 2.5, 300)
    b.plot(x, np.sqrt(2 + x), color=fs.GREEN, lw=2.2)
    b.plot(x, x, color=fs.BLUE, lw=1.6)
    p = 0.0
    for _ in range(5):
        q = math.sqrt(2 + p)
        b.plot([p, p], [p, q], color=fs.RED, lw=1.2)
        b.plot([p, q], [q, q], color=fs.RED, lw=1.2)
        p = q
    b.plot([2], [2], "o", color=fs.DARK, ms=6.5, zorder=5)
    b.text(2.05, 1.85, "(2, 2)", color=fs.DARK, fontsize=10, ha="left", va="top")
    b.text(0.1, 1.95, "y = √(2 + x)", color=fs.GREEN, fontsize=10, ha="left", va="center")
    b.text(2.4, 2.55, "y = x", color=fs.BLUE, fontsize=10, ha="right", va="center")
    b.text(0.1, 0.18, "start at 0, move up to the curve,\nacross to the line, and repeat", color=fs.RED, fontsize=9.5, ha="left", va="bottom")
    b.set_xlim(0, 2.5)
    b.set_ylim(0, 2.7)
    b.set_xlabel("aₙ")
    fs.save(fig, FOLDER, f"{SLUG}-recursive")


def growth():
    """ln n, n^2, 2^n and n! on a log scale."""
    fig, ax = fs.figure(6.0, 4.0)
    grid(ax)
    n = np.arange(1, 21)
    lg = np.log(n)
    ax.plot(n, np.maximum(lg, 1e-2), "o-", color=fs.GREEN, ms=4, lw=1.8)
    ax.plot(n, n.astype(float) ** 2, "o-", color=fs.BLUE, ms=4, lw=1.8)
    ax.plot(n, 2.0**n, "o-", color=fs.ORANGE, ms=4, lw=1.8)
    ax.plot(n, [float(math.factorial(int(k))) for k in n], "o-", color=fs.RED, ms=4, lw=1.8)
    ax.set_yscale("log")
    ax.text(20.3, 3.0, "ln n", color=fs.GREEN, fontsize=10, ha="left", va="center")
    ax.text(20.3, 400, "n²", color=fs.BLUE, fontsize=10, ha="left", va="center")
    ax.text(20.3, 1.05e6, "2ⁿ", color=fs.ORANGE, fontsize=10, ha="left", va="center")
    ax.text(14.3, 3e15, "n!", color=fs.RED, fontsize=10, ha="right", va="center")
    ax.set_xlim(0, 22.5)
    ax.set_ylim(5e-3, 1e19)
    ax.set_yticks([1, 1e3, 1e6, 1e9, 1e12, 1e15, 1e18])
    ax.set_xlabel("n")
    fs.save(fig, FOLDER, f"{SLUG}-growth")


if __name__ == "__main__":
    epsilon_n()
    recursive()
    growth()
