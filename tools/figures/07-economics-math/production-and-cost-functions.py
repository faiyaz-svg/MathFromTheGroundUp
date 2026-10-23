"""Figures for docs/07-economics-math/03-firms-and-consumers/02-production-and-cost-functions.md.

Run from the repo root:

    .venv/Scripts/python tools/figures/07-economics-math/production-and-cost-functions.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

import figstyle as fs  # noqa: E402

FOLDER = "07-economics-math"
SLUG = "production-and-cost-functions"
BOX = dict(facecolor="white", edgecolor="none", pad=0.5, alpha=0.9)

W, F = 18.0, 300.0


def q_of_l(l):
    return 0.6 * l**2 - 0.02 * l**3


def mp(l):
    return 1.2 * l - 0.06 * l**2


def ap(l):
    return 0.6 * l - 0.02 * l**2


def grid(ax):
    ax.tick_params(labelsize=9, length=3)
    ax.grid(True)
    ax.set_axisbelow(True)


def cost_curves():
    """Left: marginal and average product. Right: the cost curves they produce."""
    fig, (a, b) = plt.subplots(1, 2, figsize=(10.2, 3.9))

    l = np.linspace(0.01, 20, 400)
    grid(a)
    a.plot(l, mp(l), color=fs.RED, lw=2.3)
    a.plot(l, ap(l), color=fs.BLUE, lw=2.3)
    a.axhline(0, color=fs.DARK, lw=0.8)
    a.plot([10], [6], "o", color=fs.RED, ms=6, zorder=5)
    a.plot([15], [4.5], "o", color=fs.DARK, ms=6, zorder=5)
    a.text(0.4, 6.5, "marginal product", color=fs.RED, fontsize=10, ha="left")
    a.text(2.2, 0.55, "average product", color=fs.BLUE, fontsize=10, ha="left")
    a.annotate("MP is largest at L = 10", (10, 6), (10.8, 6.9), color=fs.RED, fontsize=9, arrowprops=dict(arrowstyle="-", color=fs.GRAY))
    a.annotate("MP = AP at L = 15,\nwhere AP is largest", (15, 4.5), (14.2, 1.9), color=fs.DARK, fontsize=9, ha="right", arrowprops=dict(arrowstyle="-", color=fs.GRAY))
    a.set_xlabel("labour L (hours)", fontsize=10)
    a.set_ylabel("units of output per hour", fontsize=10)
    a.set_xlim(0, 20.5)
    a.set_ylim(-0.6, 7.8)

    l = np.linspace(2, 19.4, 4000)
    q = q_of_l(l)
    mc = W / mp(l)
    avc = W / ap(l)
    atc = avc + F / q
    afc = F / q
    grid(b)
    b.plot(q, mc, color=fs.RED, lw=2.3)
    b.plot(q, atc, color=fs.GREEN, lw=2.3)
    b.plot(q, avc, color=fs.BLUE, lw=2.3)
    b.plot(q, afc, color=fs.GRAY, lw=2.0)
    b.plot([40], [3], "o", color=fs.RED, ms=6, zorder=5)
    b.plot([67.5], [4], "o", color=fs.BLUE, ms=6, zorder=5)
    b.plot([77.57], [8.02], "o", color=fs.GREEN, ms=6, zorder=5)
    b.text(74, 10.8, "MC", color=fs.RED, fontsize=11, ha="center")
    b.text(45, 12.6, "ATC", color=fs.GREEN, fontsize=11, ha="center")
    b.text(20, 3.3, "AVC", color=fs.BLUE, fontsize=11, ha="center")
    b.text(54, 2.6, "AFC", color=fs.GRAY, fontsize=11, ha="center")
    b.annotate("MC lowest: 3\nat Q = 40", (40, 3), (41, 0.35), color=fs.RED, fontsize=9, ha="left", arrowprops=dict(arrowstyle="-", color=fs.GRAY))
    b.annotate("AVC lowest: 4\nat Q = 67.5,\nwhere MC = AVC", (67.5, 4), (48.5, 5.3), color=fs.BLUE, fontsize=9, ha="left", arrowprops=dict(arrowstyle="-", color=fs.GRAY))
    b.annotate("ATC lowest: 8.02\nat Q = 77.6", (77.57, 8.02), (53.5, 12.4), color=fs.GREEN, fontsize=9, ha="left", arrowprops=dict(arrowstyle="-", color=fs.GRAY))
    b.axvline(80, color=fs.GRAY, lw=1.0, ls="--")
    b.text(78.6, 0.5, "capacity\nQ = 80", color=fs.GRAY, fontsize=8.5, ha="right", va="bottom")
    b.set_xlabel("output Q", fontsize=10)
    b.set_ylabel("dollars per unit", fontsize=10)
    b.set_xlim(0, 83)
    b.set_ylim(0, 14)
    fs.save(fig, FOLDER, f"{SLUG}-cost-curves")


def short_and_long_run():
    """Short-run cost curves for three fixed capital levels against the long-run cost line."""
    fig, ax = fs.figure(5.4, 3.9)
    grid(ax)
    q = np.linspace(0, 30, 400)
    ax.plot(q, 8 * q, color=fs.GREEN, lw=2.6, zorder=4)
    for kbar, col in [(5, fs.ORANGE), (20, fs.BLUE), (45, fs.RED)]:
        ax.plot(q, 2 * kbar + 8 * q**2 / kbar, color=col, lw=1.9, zorder=3)
        qt = kbar / 2
        ax.plot([qt], [8 * qt], "o", color=col, ms=6, zorder=5)
    ax.text(17, 100, "long run: C = 8Q", color=fs.GREEN, fontsize=10, ha="left", va="top")
    ax.text(5.3, 205, "K fixed at 5", color=fs.ORANGE, fontsize=9.5, ha="left")
    ax.text(14.0, 231, "K fixed at 20", color=fs.BLUE, fontsize=9.5, ha="left")
    ax.text(0.8, 100, "K fixed at 45", color=fs.RED, fontsize=9.5, ha="left")
    ax.annotate("touches at Q = 2.5", (2.5, 20), (4.3, 5), color=fs.ORANGE, fontsize=9, arrowprops=dict(arrowstyle="-", color=fs.GRAY))
    ax.annotate("Q = 10", (10, 80), (12.3, 50), color=fs.BLUE, fontsize=9, arrowprops=dict(arrowstyle="-", color=fs.GRAY))
    ax.annotate("Q = 22.5", (22.5, 180), (23, 128), color=fs.RED, fontsize=9, arrowprops=dict(arrowstyle="-", color=fs.GRAY))
    ax.set_xlabel("output Q", fontsize=10)
    ax.set_ylabel("total cost, dollars", fontsize=10)
    ax.set_xlim(0, 30.5)
    ax.set_ylim(0, 250)
    fs.save(fig, FOLDER, f"{SLUG}-short-and-long-run")


if __name__ == "__main__":
    cost_curves()
    short_and_long_run()
