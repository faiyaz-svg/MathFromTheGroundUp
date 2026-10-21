"""Figures for docs/05-university-core/01-limits-and-continuity/02-epsilon-delta-definition.md

band-and-window: the epsilon-band around L and the delta-window around a.
square-near-3: x^2 near 3, with the window from delta = min(1, epsilon/7) and the exact window.
jump-fails: a step function and a band around a proposed limit that cannot hold both sides.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

import figstyle as fs  # noqa: E402

FOLDER = "05-university-core"
SLUG = "epsilon-delta-definition"


def open_dot(ax, x, y, color):
    ax.plot([x], [y], "o", markerfacecolor="white", markeredgecolor=color, markeredgewidth=2, zorder=6)


def band_and_window():
    a, L, eps, delta = 2.0, 2.0, 0.5, 0.4
    f = lambda x: x**2 / 4 + 1
    fig, ax = fs.figure(5.4, 4.2)
    x = np.linspace(1.0, 3.2, 300)
    ax.axhspan(L - eps, L + eps, color=fs.GREEN, alpha=0.18, zorder=0)
    ax.axvspan(a - delta, a + delta, color=fs.BLUE, alpha=0.16, zorder=0)
    ax.plot(x, f(x), color=fs.DARK, linewidth=2)
    # the part of the graph over the window
    xw = np.linspace(a - delta, a + delta, 100)
    ax.plot(xw, f(xw), color=fs.RED, linewidth=3.2, zorder=4)
    open_dot(ax, a, L, fs.RED)
    # guide lines to the axes
    for y in (L - eps, L, L + eps):
        ax.plot([1.0, a - delta if y != L else a], [y, y], color=fs.GRAY, linestyle=":", linewidth=1.0, zorder=1)
    for xv in (a - delta, a, a + delta):
        ax.plot([xv, xv], [0.8, f(xv) if xv != a else L], color=fs.GRAY, linestyle=":", linewidth=1.0, zorder=1)
    ax.set_xlim(1.0, 3.2)
    ax.set_ylim(0.8, 3.6)
    ax.set_xticks([a - delta, a, a + delta])
    ax.set_xticklabels([r"$a-\delta$", r"$a$", r"$a+\delta$"])
    ax.set_yticks([L - eps, L, L + eps])
    ax.set_yticklabels([r"$L-\varepsilon$", r"$L$", r"$L+\varepsilon$"])
    ax.text(2.55, 2.0, r"$\varepsilon$-band", color=fs.GREEN, fontsize=11, va="center")
    ax.text(a + delta + 0.03, 3.3, r"$\delta$-window", color=fs.BLUE, fontsize=11, va="center")
    ax.text(2.55, 3.05, "y = f(x)", color=fs.DARK, fontsize=10)
    fs.save(fig, FOLDER, f"{SLUG}-band-and-window")


def square_near_3():
    eps = 1.0
    d_formula = min(1, eps / 7)
    d_lo, d_hi = 3 - np.sqrt(9 - eps), np.sqrt(9 + eps) - 3
    fig, ax = fs.figure(5.4, 4.2)
    x = np.linspace(2.7, 3.3, 300)
    ax.axhspan(9 - eps, 9 + eps, color=fs.GREEN, alpha=0.18, zorder=0)
    ax.plot(x, x**2, color=fs.DARK, linewidth=2)
    ax.axvspan(3 - d_formula, 3 + d_formula, color=fs.BLUE, alpha=0.2, zorder=0)
    for xv in (3 - d_lo, 3 + d_hi):
        ax.plot([xv, xv], [7.2, xv**2], color=fs.RED, linestyle="--", linewidth=1.2, zorder=1)
    open_dot(ax, 3, 9, fs.DARK)
    ax.set_xlim(2.7, 3.3)
    ax.set_ylim(7.2, 10.8)
    ax.set_xticks([2.8, 3, 3.2])
    ax.set_yticks([8, 9, 10])
    ax.text(2.72, 9.3, r"$\varepsilon$-band", color=fs.GREEN, fontsize=10, va="bottom")
    ax.text(3.17, 7.45, "exact window", color=fs.RED, fontsize=10)
    ax.text(3.0, 7.45, r"$\delta = 1/7$", color=fs.BLUE, fontsize=10, ha="center")
    ax.text(3.0 - 0.28, 10.2, r"$y=x^2$", color=fs.DARK, fontsize=11)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    fs.save(fig, FOLDER, f"{SLUG}-square-near-3")


def jump_fails():
    L, eps, delta = 0.4, 0.5, 0.6
    fig, ax = fs.figure(5.4, 3.6)
    ax.axhspan(L - eps, L + eps, color=fs.GREEN, alpha=0.18, zorder=0)
    ax.plot([-1.5, 0], [0, 0], color=fs.DARK, linewidth=2)
    ax.plot([0, 1.5], [1, 1], color=fs.DARK, linewidth=2)
    open_dot(ax, 0, 0, fs.DARK)
    ax.plot([0], [1], "o", color=fs.DARK, zorder=6)
    ax.axvspan(-delta, delta, color=fs.BLUE, alpha=0.16, zorder=0)
    # the two test points
    ax.plot([-delta / 2], [0], "s", color=fs.GREEN, zorder=7)
    ax.plot([delta / 2], [1], "s", color=fs.RED, zorder=7)
    ax.text(-delta / 2 - 0.05, 0.1, "inside the band", color=fs.GREEN, fontsize=10, ha="right")
    ax.text(delta / 2 + 0.07, 1.0, "outside the band", color=fs.RED, fontsize=10, va="center")
    ax.text(1.45, 0.4, r"$\varepsilon$-band around $L$", color=fs.GREEN, fontsize=10, va="center", ha="right")
    ax.text(-0.58, 1.3, r"$\delta$-window", color=fs.BLUE, fontsize=10)
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-0.3, 1.5)
    ax.set_yticks([L - eps, L, L + eps])
    ax.set_yticklabels([r"$L-\varepsilon$", r"$L$", r"$L+\varepsilon$"])
    ax.set_xticks([-delta / 2, 0, delta / 2])
    ax.set_xticklabels([r"$-\delta/2$", "0", r"$\delta/2$"])
    fs.save(fig, FOLDER, f"{SLUG}-jump-fails")


if __name__ == "__main__":
    band_and_window()
    square_near_3()
    jump_fails()
