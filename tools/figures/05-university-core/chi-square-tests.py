"""Figures for docs/05-university-core/08-statistics/05-chi-square-tests.md.

Run from the repo root:

    .venv/Scripts/python tools/figures/05-university-core/chi-square-tests.py
"""

import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

import figstyle as fs  # noqa: E402

FOLDER = "05-university-core"
SLUG = "chi-square-tests"


def style(ax, grid="y"):
    ax.tick_params(labelsize=9, length=3)
    ax.grid(True, axis=grid)
    ax.set_axisbelow(True)


def chi2_pdf(x, k):
    x = np.asarray(x, dtype=float)
    logc = -(k / 2) * math.log(2) - math.lgamma(k / 2)
    return np.exp(logc + (k / 2 - 1) * np.log(x) - x / 2)


def distribution():
    """Left: chi-square curves for 1, 2, 4 and 9 df. Right: simulated statistic for 500 tickets under H0."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8.8, 3.5), gridspec_kw={"width_ratios": [1, 1.1]})
    style(ax1)
    xs = np.linspace(0.02, 20, 800)
    for k, color, pos in ((1, fs.RED, (0.9, 0.46)), (2, fs.ORANGE, (2.6, 0.36)), (4, fs.GREEN, (4.4, 0.19)), (9, fs.BLUE, (11.2, 0.085))):
        ys = np.minimum(chi2_pdf(xs, k), 0.62)
        ax1.plot(xs, ys, color=color, lw=2)
        ax1.text(pos[0], pos[1], f"{k} df", color=color, fontsize=10, fontweight="bold")
    ax1.set_xlim(0, 20)
    ax1.set_ylim(0, 0.55)
    ax1.set_xlabel("chi-square statistic", fontsize=10)
    ax1.set_ylabel("density", fontsize=10)

    # Right: 10,000 simulated tables of 500 tickets spread evenly over 5 weekdays.
    style(ax2)
    rng = np.random.default_rng(4)
    counts = rng.multinomial(500, [0.2] * 5, size=10_000)
    stat = ((counts - 100) ** 2 / 100).sum(axis=1)
    ax2.hist(stat, bins=np.arange(0, 24.5, 1.0), density=True, color=fs.GRAY, alpha=0.65, zorder=2)
    xs = np.linspace(0.02, 24, 600)
    ax2.plot(xs, chi2_pdf(xs, 4), color=fs.DARK, lw=2, zorder=4)
    xt = np.linspace(14.8, 24, 100)
    ax2.fill_between(xt, 0, chi2_pdf(xt, 4), color=fs.RED, alpha=0.75, zorder=3)
    ax2.axvline(14.8, color=fs.RED, lw=1.2, ls="--", zorder=5)
    ax2.text(15.3, 0.075, "observed 14.8\narea = 0.0051", color=fs.RED, fontsize=9.5, ha="left")
    ax2.text(3.2, 0.2, "chi-square curve, 4 df", color=fs.DARK, fontsize=9.5, ha="left")
    ax2.text(8.6, 0.105, "10,000 simulated\nweeks with no\nweekday effect", color="#5a5f68", fontsize=9, ha="left")
    ax2.set_xlim(0, 24)
    ax2.set_ylim(0, 0.24)
    ax2.set_xlabel("chi-square statistic of one simulated table", fontsize=10)
    ax2.set_ylabel("density", fontsize=10)
    fig.tight_layout(w_pad=1.5)
    fs.save(fig, FOLDER, f"{SLUG}-distribution")


def tickets():
    """Observed tickets by weekday against the expected 100, with each day's share of the statistic."""
    fig, ax = plt.subplots(figsize=(6.0, 3.5))
    style(ax)
    days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
    obs = [132, 104, 88, 90, 86]
    contrib = [(o - 100) ** 2 / 100 for o in obs]
    colors = [fs.RED, fs.GRAY, fs.GRAY, fs.GRAY, fs.GRAY]
    ax.bar(days, obs, color=colors, width=0.62, zorder=3)
    ax.axhline(100, color=fs.DARK, lw=1.4, ls="--", zorder=4)
    ax.text(4.42, 101.5, "expected 100", ha="right", va="bottom", fontsize=9.5, color=fs.DARK)
    for i, (o, c) in enumerate(zip(obs, contrib)):
        ax.text(i, o + 2, f"{o}", ha="center", va="bottom", fontsize=10, fontweight="bold")
        ax.text(i, 8, f"adds\n{c:.2f}", ha="center", va="bottom", fontsize=9.5, linespacing=1.2,
                color="white" if i == 0 else fs.DARK, zorder=5)
    ax.set_ylim(0, 150)
    ax.set_ylabel("tickets in 4 weeks", fontsize=10)
    fig.tight_layout()
    fs.save(fig, FOLDER, f"{SLUG}-tickets")


if __name__ == "__main__":
    distribution()
    tickets()
