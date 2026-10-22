"""Figures for docs/05-university-core/08-statistics/03-hypothesis-testing.md.

Run from the repo root:

    .venv/Scripts/python tools/figures/05-university-core/hypothesis-testing.py
"""

import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

import figstyle as fs  # noqa: E402

FOLDER = "05-university-core"
SLUG = "hypothesis-testing"


def style(ax, grid="y"):
    ax.tick_params(labelsize=9, length=3)
    ax.grid(True, axis=grid)
    ax.set_axisbelow(True)


def phi(x):
    return np.exp(-np.asarray(x) ** 2 / 2) / math.sqrt(2 * math.pi)


def norm_sf(x):
    return 0.5 * math.erfc(x / math.sqrt(2))


def pvalue():
    """Left: the p-value of z = 2.53 as a tail area. Right: p-values under H0 and under a real effect."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8.8, 3.4), gridspec_kw={"width_ratios": [1.1, 1]})
    style(ax1)
    xs = np.linspace(-4, 4, 500)
    ax1.plot(xs, phi(xs), color=fs.DARK, lw=2, zorder=4)
    z0 = 2.53
    for sign in (1, -1):
        xx = np.linspace(z0, 4, 100) * sign
        ax1.fill_between(xx, 0, phi(xx), color=fs.RED, alpha=0.65, zorder=3)
    ax1.axvline(z0, color=fs.RED, lw=1.2, ls="--")
    ax1.axvline(-z0, color=fs.RED, lw=1.2, ls="--")
    ax1.text(z0 + 0.1, 0.2, "z = 2.53", color=fs.RED, ha="left", fontsize=10)
    ax1.text(3.2, 0.03, "0.0057", color=fs.RED, ha="center", fontsize=9.5)
    ax1.text(-3.2, 0.03, "0.0057", color=fs.RED, ha="center", fontsize=9.5)
    ax1.text(-4.1, 0.31, "area outside the\ndashed lines:\n0.0114 = p-value", ha="left", fontsize=10)
    ax1.set_xlabel("test statistic if H0 is true", fontsize=10)
    ax1.set_ylabel("density", fontsize=10)
    ax1.set_ylim(0, 0.43)
    # simulated p-values
    rng = np.random.default_rng(5)
    n, reps = 20, 10_000

    def pvals(shift):
        x = rng.normal(shift, 1, (reps, n))
        z = x.mean(axis=1) * math.sqrt(n)  # known sigma = 1, so a z test
        return np.array([2 * norm_sf(abs(v)) for v in z])

    p0 = pvals(0.0)
    p1 = pvals(0.5)
    print("share of p < 0.05 under H0:", (p0 < 0.05).mean(), "under shift 0.5:", (p1 < 0.05).mean())
    style(ax2)
    bins = np.linspace(0, 1, 21)
    ax2.hist(p0, bins=bins, color=fs.GRAY, alpha=0.8, zorder=3, label="no effect")
    ax2.hist(p1, bins=bins, color=fs.GREEN, histtype="step", lw=2.2, zorder=4)
    ax2.text(0.97, 1500, "no effect: flat", color=fs.DARK, ha="right", fontsize=10)
    ax2.text(0.22, 4700, "a real effect:\npiles up near 0", color="#027a50", ha="left", fontsize=10)
    ax2.set_xlabel("p-value of one test", fontsize=10)
    ax2.set_ylabel("number of tests (of 10,000)", fontsize=10)
    ax2.set_xlim(0, 1)
    fig.tight_layout(w_pad=1.5)
    fs.save(fig, FOLDER, f"{SLUG}-pvalue")


def power():
    """The null and alternative distributions of a z statistic, with alpha, beta and power shaded."""
    fig, ax = plt.subplots(figsize=(7.4, 3.6))
    style(ax)
    xs = np.linspace(-4, 7.5, 600)
    delta = 2.8
    crit = 1.96
    ax.plot(xs, phi(xs), color=fs.DARK, lw=2, zorder=5)
    ax.plot(xs, phi(xs - delta), color=fs.BLUE, lw=2, zorder=5)
    x1 = np.linspace(crit, 7.5, 200)
    ax.fill_between(x1, 0, phi(x1), color=fs.RED, alpha=0.75, zorder=4)
    x2 = np.linspace(-4, crit, 200)
    ax.fill_between(x2, 0, phi(x2 - delta), color=fs.ORANGE, alpha=0.55, zorder=3)
    x3 = np.linspace(crit, 7.5, 200)
    ax.fill_between(x3, 0, phi(x3 - delta), color=fs.GREEN, alpha=0.4, zorder=3)
    ax.axvline(crit, color=fs.DARK, lw=1.2, ls="--", zorder=6)
    ax.text(crit + 0.1, 0.455, "reject H0 to the right of the line", ha="left", fontsize=9.5, va="bottom")
    ax.text(-0.1, 0.405, "H0 true", color=fs.DARK, ha="right", fontsize=10)
    ax.text(delta + 0.15, 0.405, "effect is real", color=fs.BLUE, ha="left", fontsize=10)
    ax.annotate("alpha = 0.025 (type I error)", (2.5, 0.012), (3.9, 0.07), color=fs.RED, fontsize=9,
                arrowprops=dict(arrowstyle="-", color=fs.RED, lw=1))
    ax.annotate("beta = 0.20 (type II error)", (1.2, 0.03), (-3.8, 0.17), color="#a35a00", fontsize=9.5,
                arrowprops=dict(arrowstyle="-", color="#a35a00", lw=1))
    ax.text(4.3, 0.2, "power = 0.80", color="#027a50", ha="left", fontsize=10)
    ax.set_xlabel("test statistic", fontsize=10)
    ax.set_ylabel("density", fontsize=10)
    ax.set_ylim(0, 0.5)
    ax.set_xlim(-4, 7.5)
    fig.tight_layout()
    fs.save(fig, FOLDER, f"{SLUG}-power")


def multiple():
    """Chance of at least one false positive among m independent tests at alpha = 0.05."""
    fig, ax = plt.subplots(figsize=(6.2, 3.5))
    style(ax)
    ms = np.arange(1, 101)
    ax.plot(ms, 1 - 0.95**ms, color=fs.RED, lw=2, zorder=3)
    for m in (1, 5, 20, 100):
        v = 1 - 0.95**m
        ax.plot([m], [v], "o", color=fs.RED, ms=5, zorder=4)
        label = f"{m} test: {100 * v:.0f}%" if m == 1 else f"{m} tests: {100 * v:.0f}%"
        ax.text(m + 2, v + (0.07 if m == 1 else -0.045), label, fontsize=9.5, ha="left", va="center")
    ax.set_xlabel("number of independent tests, each at the 5% level", fontsize=10)
    ax.set_ylabel("P(at least one false positive)", fontsize=10)
    ax.set_ylim(0, 1.05)
    ax.set_xlim(0, 108)
    fig.tight_layout()
    fs.save(fig, FOLDER, f"{SLUG}-multiple")


if __name__ == "__main__":
    pvalue()
    power()
    multiple()
