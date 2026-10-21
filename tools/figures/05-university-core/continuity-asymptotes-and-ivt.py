"""Figures for docs/05-university-core/01-limits-and-continuity/03-continuity-asymptotes-and-ivt.md

discontinuities: removable, jump and infinite discontinuities side by side.
ivt: the intermediate value theorem on [a, b].
bisection: the intervals of the bisection method for x^3 + x - 1 = 0.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

import figstyle as fs  # noqa: E402

FOLDER = "05-university-core"
SLUG = "continuity-asymptotes-and-ivt"


def open_dot(ax, x, y, color):
    ax.plot([x], [y], "o", markerfacecolor="white", markeredgecolor=color, markeredgewidth=2, zorder=5)


def closed_dot(ax, x, y, color):
    ax.plot([x], [y], "o", color=color, zorder=5)


def discontinuities():
    fig, axes = plt.subplots(1, 3, figsize=(10.4, 3.3))

    ax = axes[0]  # removable: (x^2 - 4)/(x - 2), f(2) = 3
    x = np.linspace(0, 4, 200)
    ax.plot(x, x + 2, color=fs.GREEN)
    open_dot(ax, 2, 4, fs.GREEN)
    closed_dot(ax, 2, 3, fs.GREEN)
    ax.text(0.15, 5.3, "removable", color=fs.DARK, fontsize=11)
    ax.text(2.15, 2.6, "f(2) = 3", color=fs.DARK, fontsize=10)
    ax.text(0.15, 4.6, "limit 4", color=fs.DARK, fontsize=10)
    ax.set_xlim(0, 4)
    ax.set_ylim(1.5, 6.4)
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")

    ax = axes[1]  # jump
    xl = np.linspace(0, 2, 100, endpoint=False)
    xr = np.linspace(2, 4, 100)
    ax.plot(xl, 1 + 0.5 * xl, color=fs.BLUE)
    ax.plot(xr, 4 - 0.5 * (xr - 2), color=fs.BLUE)
    open_dot(ax, 2, 2, fs.BLUE)
    closed_dot(ax, 2, 4, fs.BLUE)
    ax.text(0.15, 4.9, "jump", color=fs.DARK, fontsize=11)
    ax.text(0.15, 2.4, "left limit 2", color=fs.DARK, fontsize=10)
    ax.text(2.2, 4.3, "right limit 4", color=fs.DARK, fontsize=10)
    ax.set_xlim(0, 4)
    ax.set_ylim(0.5, 5.6)
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")

    ax = axes[2]  # infinite
    xl = np.linspace(0, 2 - 0.05, 300)
    xr = np.linspace(2 + 0.05, 4, 300)
    ax.plot(xl, 1 / (2 - xl), color=fs.RED)
    ax.plot(xr, -1 / (xr - 2), color=fs.RED)
    ax.axvline(2, color=fs.GRAY, linestyle="--", linewidth=1.2)
    ax.text(0.15, 4.0, "infinite", color=fs.DARK, fontsize=11)
    ax.text(0.1, 3.0, "left: +infinity", color=fs.DARK, fontsize=9, ha="left")
    ax.text(2.5, -3.9, "right: -infinity", color=fs.DARK, fontsize=9, ha="left")
    ax.set_xlim(0, 4)
    ax.set_ylim(-4.5, 4.8)
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    # sides of the infinite discontinuity: left side up, right side down
    fig.tight_layout(w_pad=2.0)
    fs.save(fig, FOLDER, f"{SLUG}-discontinuities")


def ivt_figure():
    f = lambda x: 1 + x + 0.8 * np.sin(2.5 * x)
    a, b, N = 0.0, 4.0, 3.0
    # locate c by bisection (no extra libraries)
    lo, hi = 2.0, 2.5
    for _ in range(60):
        mid = (lo + hi) / 2
        if f(mid) < N:
            lo = mid
        else:
            hi = mid
    c = (lo + hi) / 2
    fig, ax = fs.figure(5.4, 3.8)
    x = np.linspace(a, b, 400)
    ax.plot(x, f(x), color=fs.GREEN)
    ax.plot([a, b], [N, N], color=fs.RED, linestyle="--", linewidth=1.4)
    ax.plot([c, c], [0, N], color=fs.GRAY, linestyle=":", linewidth=1.2)
    closed_dot(ax, a, f(a), fs.DARK)
    closed_dot(ax, b, f(b), fs.DARK)
    closed_dot(ax, c, N, fs.RED)
    ax.text(0.12, f(a) - 0.45, "(a, f(a))", fontsize=10, color=fs.DARK)
    ax.text(b - 0.1, f(b) - 0.6, "(b, f(b))", fontsize=10, color=fs.DARK, ha="right")
    ax.text(0.1, N + 0.12, "y = N", fontsize=10, color=fs.RED)
    ax.text(c + 0.08, 0.2, "c", fontsize=11, color=fs.RED)
    ax.set_xlim(-0.1, 4.2)
    ax.set_ylim(0, 6)
    ax.set_xticks([a, b])
    ax.set_xticklabels(["a", "b"])
    ax.set_yticks([f(a), N, f(b)])
    ax.set_yticklabels(["f(a)", "N", "f(b)"])
    fs.save(fig, FOLDER, f"{SLUG}-ivt")
    return c


def bisection():
    g = lambda x: x**3 + x - 1
    a, b = 0.0, 1.0
    rows = [(a, b)]
    for _ in range(6):
        m = (a + b) / 2
        if g(a) * g(m) <= 0:
            b = m
        else:
            a = m
        rows.append((a, b))
    root = 0.6823278038280193
    fig, ax = fs.figure(5.6, 3.4)
    for k, (lo, hi) in enumerate(rows):
        y = -k
        ax.plot([lo, hi], [y, y], color=fs.GREEN, linewidth=5, solid_capstyle="butt")
        label = "start" if k == 0 else f"step {k}"
        ax.text(-0.04, y, label, ha="right", va="center", fontsize=10, color=fs.DARK)
    ax.axvline(root, color=fs.RED, linestyle="--", linewidth=1.3, zorder=0)
    ax.text(root + 0.01, 0.55, "root, about 0.6823", color=fs.RED, fontsize=10, ha="left")
    ax.set_xlim(-0.2, 1.05)
    ax.set_ylim(-6.6, 1.0)
    ax.set_yticks([])
    ax.spines["left"].set_visible(False)
    ax.set_xlabel("x")
    ax.set_xticks([0, 0.25, 0.5, 0.75, 1.0])
    fs.save(fig, FOLDER, f"{SLUG}-bisection")
    return rows


if __name__ == "__main__":
    discontinuities()
    print("c =", ivt_figure())
    for r in bisection():
        print(r)
