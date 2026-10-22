"""Figures for docs/06-cs-math/04-sums-recurrences-and-algorithms/04-asymptotic-notation.md.

Run from the repo root:

    .venv/Scripts/python tools/figures/06-cs-math/asymptotic-notation.py
"""

import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

import figstyle as fs  # noqa: E402

FOLDER = "06-cs-math"
SLUG = "asymptotic-notation"
BOX = dict(facecolor="white", edgecolor="none", pad=0.4, alpha=0.9)


def hierarchy():
    """Growth of six common functions on a log scale for n from 1 to 20."""
    fig, ax = fs.figure(6.2, 5.0)
    n = np.arange(1, 21)
    fact = np.array([math.factorial(int(k)) for k in n], dtype=float)
    curves = [
        ("lg n", np.log2(n), fs.GRAY, 1.0),
        ("n", n.astype(float), fs.BLUE, 1.6),
        ("n lg n", n * np.log2(n), fs.GREEN, 2.0),
        ("n²", n.astype(float) ** 2, fs.ORANGE, 1.8),
        ("2ⁿ", 2.0**n, fs.RED, 1.8),
        ("n!", fact, fs.DARK, 1.8),
    ]
    for label, y, color, y_off in curves:
        yy = np.where(y <= 0, np.nan, y)
        ax.plot(n, yy, color=color, lw=2.2, zorder=3)
    ax.set_yscale("log")
    ax.set_xlim(1, 22.6)
    ax.set_ylim(0.8, 3e19)
    ax.grid(True, which="major")
    ax.set_axisbelow(True)
    ax.tick_params(labelsize=9, length=3)
    ax.set_xticks([1, 5, 10, 15, 20])
    ax.set_xlabel("n")
    ax.set_ylabel("steps (log scale)")
    ends = {"lg n": 2.3, "n": 8.5, "n lg n": 100, "n²": 900, "2ⁿ": 1.05e6, "n!": 2.43e18}
    cols = {"lg n": fs.GRAY, "n": fs.BLUE, "n lg n": fs.GREEN, "n²": fs.ORANGE, "2ⁿ": fs.RED, "n!": fs.DARK}
    for label, y in ends.items():
        ax.text(20.4, y, label, color=cols[label], fontsize=10.5, ha="left", va="center")
    fs.save(fig, FOLDER, f"{SLUG}-hierarchy")


def witness():
    """f(n) = 3n^2 + 10n + 7 squeezed between 3n^2 and 20n^2 from n0 = 1."""
    fig, ax = fs.figure(5.6, 3.9)
    n = np.linspace(0, 8, 300)
    f = 3 * n**2 + 10 * n + 7
    ax.plot(n, 20 * n**2, color=fs.RED, lw=1.8, ls="--", zorder=2)
    ax.plot(n, 3 * n**2, color=fs.BLUE, lw=1.8, ls="--", zorder=2)
    ax.plot(n, f, color=fs.GREEN, lw=2.6, zorder=3)
    k = np.arange(1, 9)
    ax.plot(k, 3 * k**2 + 10 * k + 7, "o", color=fs.GREEN, ms=5, zorder=4)
    ax.axvline(1, color=fs.GRAY, lw=1.0, ls=":")
    ax.text(1.08, 700, "n₀ = 1", color=fs.DARK, fontsize=10, ha="left", va="center", bbox=BOX)
    ax.text(4.35, 1270, "20n²", color=fs.RED, fontsize=10.5, ha="left", va="center")
    ax.text(7.6, 465, "3n² + 10n + 7", color=fs.GREEN, fontsize=10.5, ha="right", va="bottom", bbox=BOX)
    ax.text(7.9, 150, "3n²", color=fs.BLUE, fontsize=10.5, ha="right", va="top")
    ax.set_xlim(0, 8)
    ax.set_ylim(0, 1350)
    ax.grid(True)
    ax.set_axisbelow(True)
    ax.tick_params(labelsize=9, length=3)
    ax.set_xlabel("n")
    fs.save(fig, FOLDER, f"{SLUG}-witness")


if __name__ == "__main__":
    hierarchy()
    witness()
