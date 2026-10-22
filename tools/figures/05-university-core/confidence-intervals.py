"""Figures for docs/05-university-core/08-statistics/02-confidence-intervals.md.

Run from the repo root:

    .venv/Scripts/python tools/figures/05-university-core/confidence-intervals.py
"""

import math
import random
import statistics as st
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

import figstyle as fs  # noqa: E402

FOLDER = "05-university-core"
SLUG = "confidence-intervals"


def style(ax, grid="y"):
    ax.tick_params(labelsize=9, length=3)
    ax.grid(True, axis=grid)
    ax.set_axisbelow(True)


def t_pdf(x, df):
    c = math.exp(math.lgamma((df + 1) / 2) - math.lgamma(df / 2)) / math.sqrt(df * math.pi)
    return c * (1 + x * x / df) ** (-(df + 1) / 2)


def t_cdf(x, df, steps=4000):
    """P(T <= x) by Simpson's rule on the density from 0 to |x|."""
    a = abs(x)
    h = a / steps
    total = t_pdf(0, df) + t_pdf(a, df)
    for i in range(1, steps):
        total += (4 if i % 2 else 2) * t_pdf(i * h, df)
    area = total * h / 3
    return 0.5 + area if x >= 0 else 0.5 - area


def t_ppf(p, df):
    lo, hi = 0.0, 100.0
    for _ in range(60):
        mid = (lo + hi) / 2
        if t_cdf(mid, df) < p:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def tcurves():
    """t densities against the normal, and the 97.5th percentile against df."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8.6, 3.4), gridspec_kw={"width_ratios": [1.15, 1]})
    style(ax1)
    xs = np.linspace(-4.5, 4.5, 400)
    normal = np.exp(-xs**2 / 2) / math.sqrt(2 * math.pi)
    ax1.plot(xs, normal, color=fs.DARK, lw=2, zorder=4)
    ax1.plot(xs, [t_pdf(x, 2) for x in xs], color=fs.RED, lw=2, zorder=3)
    ax1.plot(xs, [t_pdf(x, 5) for x in xs], color=fs.ORANGE, lw=2, zorder=3)
    ax1.text(-0.35, 0.405, "normal", color=fs.DARK, ha="right", fontsize=10)
    ax1.text(1.05, 0.285, "t, 5 df", color=fs.ORANGE, ha="left", fontsize=10)
    ax1.text(-2.3, 0.115, "t, 2 df", color=fs.RED, ha="right", fontsize=10)
    ax1.set_xlabel("value", fontsize=10)
    ax1.set_ylabel("density", fontsize=10)
    ax1.set_xlim(-4.5, 4.5)
    style(ax2)
    ax2.grid(True, axis="x")
    dfs = list(range(2, 61))
    ax2.plot(dfs, [t_ppf(0.975, d) for d in dfs], color=fs.GREEN, lw=2, zorder=4)
    ax2.axhline(1.96, color=fs.DARK, ls="--", lw=1.2)
    ax2.text(60, 1.93, "z* = 1.96", ha="right", va="top", fontsize=10)
    for d in (4, 9, 29):
        v = t_ppf(0.975, d)
        ax2.plot([d], [v], "o", color=fs.GREEN, ms=5, zorder=5)
        ax2.text(d + 1.2, v + 0.04, f"{v:.3f}", fontsize=9.5, ha="left", va="bottom")
    ax2.set_xlabel("degrees of freedom", fontsize=10)
    ax2.set_ylabel("t* for 95% confidence", fontsize=10)
    ax2.set_ylim(1.7, 4.6)
    fig.tight_layout(w_pad=1.5)
    fs.save(fig, FOLDER, f"{SLUG}-t")


def coverage():
    """Fifty 95% t intervals from fifty samples of 25 values."""
    rng = np.random.default_rng(11)
    mu, sigma, n, reps = 50.0, 10.0, 25, 50
    tstar = t_ppf(0.975, n - 1)
    fig, ax = plt.subplots(figsize=(7.2, 5.2))
    style(ax, "x")
    misses = 0
    for i in range(reps):
        sample = rng.normal(mu, sigma, n)
        xbar = sample.mean()
        half = tstar * sample.std(ddof=1) / math.sqrt(n)
        hit = xbar - half <= mu <= xbar + half
        misses += not hit
        color = fs.GREEN if hit else fs.RED
        ax.plot([xbar - half, xbar + half], [i, i], color=color, lw=2, zorder=3)
        ax.plot([xbar], [i], "o", color=color, ms=3.5, zorder=4)
    print("intervals missing mu:", misses, "of", reps)
    ax.axvline(mu, color=fs.DARK, lw=1.4, ls="--", zorder=2)
    ax.text(mu + 0.3, reps + 0.2, "true mean 50", ha="left", va="bottom", fontsize=10)
    ax.set_ylim(-1, reps + 2.2)
    ax.set_yticks([])
    ax.spines["left"].set_visible(False)
    ax.set_xlabel("95% interval from one sample of 25 values", fontsize=10)
    fig.tight_layout()
    fs.save(fig, FOLDER, f"{SLUG}-coverage")


def margin():
    """Margin of error of a poll against the sample size, for p = 0.5."""
    fig, ax = plt.subplots(figsize=(6.2, 3.6))
    style(ax)
    ax.grid(True, axis="x")
    ns = np.linspace(50, 10500, 600)
    ax.plot(ns, 100 * 1.96 * 0.5 / np.sqrt(ns), color=fs.BLUE, lw=2, zorder=3)
    for n in (100, 400, 1000, 2401, 10000):
        m = 100 * 1.96 * 0.5 / math.sqrt(n)
        ax.plot([n], [m], "o", color=fs.BLUE, ms=5, zorder=4)
        dy = 0.45 if n < 3000 else 0.7
        ax.text(n + 150, m + dy, f"n = {n}: ±{m:.1f}", fontsize=9.5, ha="left", va="center")
    ax.set_xlabel("sample size n", fontsize=10)
    ax.set_ylabel("margin of error (percentage points)", fontsize=10)
    ax.set_xlim(0, 11800)
    ax.set_ylim(0, 11.5)
    fig.tight_layout()
    fs.save(fig, FOLDER, f"{SLUG}-margin")


def bootstrap():
    """Bootstrap distribution of the median of 15 response times."""
    times = [82, 95, 101, 88, 110, 97, 240, 105, 92, 99, 130, 87, 104, 310, 94]
    random.seed(1)
    boots = sorted(st.median(random.choices(times, k=len(times))) for _ in range(10_000))
    lo, hi = boots[int(0.025 * 10_000)], boots[int(0.975 * 10_000)]
    print("bootstrap median interval:", lo, hi, "sample median", st.median(times))
    fig, ax = plt.subplots(figsize=(6.6, 3.4))
    style(ax)
    values = sorted(set(boots))
    counts = [boots.count(v) / len(boots) for v in values]
    colors = [fs.GREEN if lo <= v <= hi else fs.GRAY for v in values]
    ax.bar(values, counts, width=1.6, color=colors, zorder=3)
    ax.axvline(st.median(times), color=fs.DARK, ls="--", lw=1.2, zorder=4)
    ax.text(st.median(times) + 1.5, max(counts) * 1.02, "sample median 99", ha="left", va="bottom", fontsize=9.5)
    far = sum(1 for v in boots if v > 140)
    ax.text(139, max(counts) * 0.3, f"{far} resamples above 140\nnot shown", ha="right", fontsize=9,
            color=fs.GRAY)
    ax.set_xlim(80, 140)
    ax.text(lo - 1, max(counts) * 0.55, f"{lo}", ha="right", fontsize=10, color=fs.GREEN)
    ax.text(hi + 1, max(counts) * 0.55, f"{hi}", ha="left", fontsize=10, color=fs.GREEN)
    ax.set_ylim(0, max(counts) * 1.2)
    ax.set_xlabel("median of one resample of the 15 times (ms)", fontsize=10)
    ax.set_ylabel("share of 10,000 resamples", fontsize=10)
    fig.tight_layout()
    fs.save(fig, FOLDER, f"{SLUG}-bootstrap")


if __name__ == "__main__":
    tcurves()
    coverage()
    margin()
    bootstrap()
