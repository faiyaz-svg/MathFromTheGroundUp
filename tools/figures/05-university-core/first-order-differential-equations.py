"""Figures for docs/05-university-core/10-differential-equations-light/01-first-order-differential-equations.md.

Run from the repo root:

    .venv/Scripts/python tools/figures/05-university-core/first-order-differential-equations.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

import figstyle as fs  # noqa: E402

FOLDER = "05-university-core"
SLUG = "first-order-differential-equations"
BOX = dict(facecolor="white", edgecolor="none", pad=0.4, alpha=0.9)


def slope_field():
    """The logistic equation N' = 0.5 N (1 - N) as a slope field with four solutions."""
    fig, ax = fs.figure(7.0, 4.2)
    t = np.linspace(0, 16, 22)
    N = np.linspace(0, 1.4, 15)
    L = 0.6
    for t0 in t:
        for n0 in N:
            s = 0.5 * n0 * (1 - n0)
            ax.plot([t0 - L / 2, t0 + L / 2], [n0 - s * L / 2, n0 + s * L / 2], color=fs.GRAY, lw=1.3)
    tt = np.linspace(0, 16, 400)
    for N0, col in [(0.001, fs.GREEN), (0.2, fs.BLUE), (0.6, fs.ORANGE), (1.3, fs.RED)]:
        ax.plot(tt, 1 / (1 + (1 / N0 - 1) * np.exp(-0.5 * tt)), color=col, lw=2.4)
    ax.axhline(1, color=fs.DARK, lw=1.0, ls="--")
    ax.text(15.8, 1.03, "N = 1 (capacity)", ha="right", va="bottom", fontsize=10)
    ax.text(15.8, 0.03, "N = 0", ha="right", va="bottom", fontsize=10)
    ax.text(4.5, 0.12, "starts at 0.001: S-shaped", color=fs.GREEN, fontsize=10, ha="left", va="center", bbox=BOX)
    ax.text(1.5, 1.39, "starts above capacity: falls", color=fs.RED, fontsize=10, ha="left", va="center", bbox=BOX)
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 1.45)
    ax.set_xlabel("time t (months)")
    ax.set_ylabel("N = P / K (share of capacity)")
    ax.tick_params(labelsize=9)
    fs.save(fig, FOLDER, f"{SLUG}-slope-field")


def euler():
    """Euler's method for y' = y, y(0) = 1, with step sizes 0.5, 0.25 and 0.1."""
    fig, ax = fs.figure(6.4, 4.0)
    t = np.linspace(0, 1, 200)
    ax.plot(t, np.exp(t), color=fs.DARK, lw=2.6)
    for h, col in [(0.5, fs.RED), (0.25, fs.ORANGE), (0.1, fs.BLUE)]:
        n = round(1 / h)
        ts = np.linspace(0, 1, n + 1)
        ys = (1 + h) ** np.arange(n + 1)
        ax.plot(ts, ys, "-o", color=col, lw=1.6, ms=4.5 if h > 0.1 else 3)
    ax.text(0.9, 2.78, "exact: e^t, ends at 2.718", color=fs.DARK, fontsize=10, ha="right", va="bottom")
    ax.text(1.02, 2.25, "h = 0.5: 2.250", color=fs.RED, fontsize=10, va="center")
    ax.text(1.02, 2.44, "h = 0.25: 2.441", color=fs.ORANGE, fontsize=10, va="center")
    ax.text(1.02, 2.62, "h = 0.1: 2.594", color=fs.BLUE, fontsize=10, va="center")
    ax.set_xlim(0, 1.45)
    ax.set_ylim(0.9, 3.0)
    ax.set_xlabel("t")
    ax.set_ylabel("y")
    ax.grid(True)
    ax.set_axisbelow(True)
    ax.tick_params(labelsize=9)
    fs.save(fig, FOLDER, f"{SLUG}-euler")


def cooling_price():
    """Left: Newton cooling of a coffee. Right: a price adjusting toward its equilibrium."""
    fig, (a, b) = plt.subplots(1, 2, figsize=(9.2, 3.7))
    kc = np.log(1.4) / 10
    t = np.linspace(0, 60, 300)
    a.plot(t, 20 + 70 * np.exp(-kc * t), color=fs.GREEN, lw=2.4)
    a.axhline(20, color=fs.GRAY, lw=1.0, ls="--")
    a.plot([0, 10, 37.23], [90, 70, 40], "o", color=fs.RED, ms=6, zorder=5)
    a.text(1.5, 90, "90 at t = 0", fontsize=9.5, va="center")
    a.text(11, 71.5, "70 at t = 10", fontsize=9.5, va="bottom")
    a.text(38.5, 42, "40 at t ≈ 37.2", fontsize=9.5, va="bottom")
    a.text(59, 22, "room: 20", ha="right", va="bottom", fontsize=9.5, color=fs.DARK)
    a.set_xlabel("time t (minutes)")
    a.set_ylabel("temperature T (°C)")
    a.set_ylim(10, 98)
    a.grid(True)
    a.set_axisbelow(True)
    a.tick_params(labelsize=9)
    t = np.linspace(0, 16, 300)
    b.plot(t, 15 + 10 * np.exp(-0.3 * t), color=fs.BLUE, lw=2.4)
    b.plot(t, 15 - 10 * np.exp(-0.3 * t), color=fs.ORANGE, lw=2.4)
    b.axhline(15, color=fs.GRAY, lw=1.0, ls="--")
    b.text(15.8, 14.4, "equilibrium price 15", ha="right", va="top", fontsize=9.5)
    b.text(0.4, 24.2, "starts at 25", color=fs.BLUE, fontsize=9.5, va="top")
    b.text(0.4, 5.8, "starts at 5", color=fs.ORANGE, fontsize=9.5, va="bottom")
    b.set_xlabel("time t")
    b.set_ylabel("price p")
    b.set_ylim(3, 27)
    b.grid(True)
    b.set_axisbelow(True)
    b.tick_params(labelsize=9)
    fig.subplots_adjust(wspace=0.28)
    fs.save(fig, FOLDER, f"{SLUG}-cooling-price")


if __name__ == "__main__":
    slope_field()
    euler()
    cooling_price()
