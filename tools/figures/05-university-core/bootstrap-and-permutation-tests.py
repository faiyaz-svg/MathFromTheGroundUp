"""Figures for docs/05-university-core/08-statistics/06-bootstrap-and-permutation-tests.md.

Run from the repo root:

    .venv/Scripts/python tools/figures/05-university-core/bootstrap-and-permutation-tests.py
"""

import itertools
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

import figstyle as fs  # noqa: E402

FOLDER = "05-university-core"
SLUG = "bootstrap-and-permutation-tests"
B = 10_000


def style(ax, grid="y"):
    ax.tick_params(labelsize=9, length=3)
    ax.grid(True, axis=grid)
    ax.set_axisbelow(True)


def bootstrap():
    """Bootstrap distributions of the mean and the median of 15 response times, with the 95% intervals."""
    times = np.array([82, 95, 101, 88, 110, 97, 240, 105, 92, 99, 130, 87, 104, 310, 94])
    n = len(times)
    rng = np.random.default_rng(1)
    res = times[rng.integers(0, n, size=(B, n))]
    means, medians = res.mean(axis=1), np.median(res, axis=1)
    m_lo, m_hi = np.percentile(means, [2.5, 97.5])
    d_lo, d_hi = np.percentile(medians, [2.5, 97.5])
    print("mean interval", round(m_lo, 1), round(m_hi, 1), "median interval", d_lo, d_hi)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8.8, 3.5), gridspec_kw={"width_ratios": [1.25, 1]})
    style(ax1)
    bins = np.arange(70, 215, 3)
    counts, _, _ = ax1.hist(means, bins=bins, color=fs.GRAY, alpha=0.7, zorder=2)
    ytop = counts.max() * 1.75
    ax1.set_ylim(0, ytop)
    ax1.axvline(times.mean(), color=fs.DARK, lw=1.3, ls="--", zorder=4)
    ax1.text(times.mean() + 2, ytop * 0.94, "sample mean 122.3", fontsize=9.5, ha="left", va="top")
    for y, lo, hi, color, label in (
        (ytop * 0.70, m_lo, m_hi, "#027a50", f"bootstrap, {m_lo:.1f} to {m_hi:.1f}"),
        (ytop * 0.58, 86.6, 157.9, fs.BLUE, "t interval, 86.6 to 157.9"),
    ):
        ax1.annotate("", xy=(lo, y), xytext=(hi, y), arrowprops=dict(arrowstyle="|-|", color=color, lw=1.8, mutation_scale=4))
        ax1.text(hi + 4, y, label, color=color, ha="left", va="center", fontsize=9.5)
    ax1.set_xlabel("mean of one resample (ms)", fontsize=10)
    ax1.set_ylabel("resamples (of 10,000)", fontsize=10)
    ax1.set_xlim(70, 215)

    style(ax2)
    vals, cnt = np.unique(medians, return_counts=True)
    colors = [fs.GREEN if d_lo <= v <= d_hi else fs.GRAY for v in vals]
    ax2.bar(vals, cnt, width=0.8, color=colors, alpha=0.85, zorder=2)
    ax2.axvline(np.median(times), color=fs.DARK, lw=1.3, ls="--", zorder=4)
    ax2.text(np.median(times) + 1, cnt.max() * 1.02, "sample median 99", fontsize=9.5, ha="left")
    ax2.set_ylim(0, cnt.max() * 1.12)
    ax2.set_xlim(80, 125)
    ax2.set_xlabel("median of one resample (ms)", fontsize=10)
    ax2.set_ylabel("resamples (of 10,000)", fontsize=10)
    ax2.text(113, cnt.max() * 0.55, f"interval\n{d_lo:.0f} to {d_hi:.0f}", color="#027a50", fontsize=9.5, ha="left")
    fig.tight_layout(w_pad=1.5)
    fs.save(fig, FOLDER, f"{SLUG}-bootstrap")


def permutation():
    """The exact permutation distribution of the difference of means for the two builds."""
    a = np.array([214, 202, 236, 228, 207, 245, 219, 231, 212, 290])
    b = np.array([201, 211, 189, 225, 205, 194, 210, 198, 238, 203])
    pooled = np.concatenate([a, b])
    observed = a.mean() - b.mean()
    combos = np.array(list(itertools.combinations(range(20), 10)))
    sums = pooled[combos].sum(axis=1)
    diffs = sums / 10 - (pooled.sum() - sums) / 10
    extreme = np.abs(diffs) >= abs(observed) - 1e-9
    print("arrangements", len(diffs), "extreme", extreme.sum(), "p", extreme.mean())

    fig, ax = plt.subplots(figsize=(7.0, 3.5))
    style(ax)
    bins = np.arange(-34, 34.1, 2)
    ax.hist(diffs, bins=bins, color=fs.GRAY, alpha=0.7, zorder=2)
    counts, edges = np.histogram(diffs, bins=bins)
    for lo, hi, c in zip(edges[:-1], edges[1:], counts):
        mid = (lo + hi) / 2
        if abs(mid) >= observed - 1:
            ax.bar(mid, c, width=hi - lo, color=fs.RED, alpha=0.8, zorder=3)
    ax.axvline(observed, color=fs.RED, lw=1.3, ls="--", zorder=4)
    ax.axvline(-observed, color=fs.RED, lw=1.3, ls="--", zorder=4)
    ytop = counts.max()
    ax.set_ylim(0, ytop * 1.18)
    ax.text(observed + 1, ytop * 0.5, "observed\ndifference 21.0", color=fs.RED, fontsize=9.5, ha="left")
    ax.text(-observed - 1, ytop * 0.5, "-21.0", color=fs.RED, fontsize=9.5, ha="right")
    ax.text(0, ytop * 1.07, "all 184,756 ways to label 10 of the 20 values A", fontsize=9.5, ha="center")
    ax.text(31.5, ytop * 0.2, "red: 4,850\nrelabelings,\n2.6%", color=fs.RED, fontsize=9, ha="right")
    ax.set_xlabel("mean of group A minus mean of group B, after relabeling (ms)", fontsize=10)
    ax.set_ylabel("number of relabelings", fontsize=10)
    ax.set_xlim(-34, 34)
    fig.tight_layout()
    fs.save(fig, FOLDER, f"{SLUG}-permutation")


def failures():
    """Left: the bootstrap distribution of a maximum. Right: spread of a mean for dependent data."""
    rng = np.random.default_rng(1)
    x = rng.uniform(0, 100, 20)
    max_boot = x[rng.integers(0, 20, (B, 20))].max(axis=1)
    print("max", x.max(), (max_boot == x.max()).mean())

    # the AR(1) experiment of the "In code" section
    rng = np.random.default_rng(5)
    reps, N, phi, L = 1000, 200, 0.7, 20
    e = rng.standard_normal((reps, N + 100))
    series = np.zeros_like(e)
    for t in range(1, N + 100):
        series[:, t] = phi * series[:, t - 1] + e[:, t]
    series = series[:, 100:]
    iid_se, block_se = [], []
    for s in series:
        m_iid = s[rng.integers(0, N, (500, N))].mean(axis=1)
        starts = rng.integers(0, N - L + 1, (500, N // L))
        m_block = s[(starts[:, :, None] + np.arange(L)).reshape(500, N)].mean(axis=1)
        iid_se.append(m_iid.std(ddof=1))
        block_se.append(m_block.std(ddof=1))
    true_sd = series.mean(axis=1).std(ddof=1)
    print("true", true_sd, "iid", np.mean(iid_se), "block", np.mean(block_se))

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8.8, 3.5), gridspec_kw={"width_ratios": [1.15, 1]})
    style(ax1)
    vals, cnt = np.unique(max_boot, return_counts=True)
    colors = [fs.RED if v == x.max() else fs.GRAY for v in vals]
    ax1.bar(vals, cnt, width=0.7, color=colors, alpha=0.85, zorder=3)
    ax1.axvline(100, color=fs.DARK, lw=1.4, ls="--", zorder=4)
    ax1.text(99.6, cnt.max() * 0.45, "true\nmaximum\n100", fontsize=9.5, ha="right")
    ax1.text(x.max() - 1.2, cnt.max() * 0.97, "64% of resamples have\nthe sample maximum, 95.0", color=fs.RED,
             fontsize=9.5, ha="right", va="top")
    ax1.set_xlim(70, 101.5)
    ax1.set_ylim(0, cnt.max() * 1.1)
    ax1.set_xlabel("maximum of one resample", fontsize=10)
    ax1.set_ylabel("resamples (of 10,000)", fontsize=10)

    style(ax2)
    labels = ["true spread\nof the mean", "ordinary\nbootstrap", "block\nbootstrap"]
    vals = [true_sd, np.mean(iid_se), np.mean(block_se)]
    bars = ax2.bar(labels, vals, color=[fs.DARK, fs.RED, fs.GREEN], width=0.6, zorder=3)
    for bar, v in zip(bars, vals):
        ax2.text(bar.get_x() + bar.get_width() / 2, v + 0.006, f"{v:.3f}", ha="center", fontsize=10, fontweight="bold")
    ax2.set_ylim(0, 0.29)
    ax2.set_ylabel("standard error of the mean", fontsize=10)
    ax2.tick_params(axis="x", labelsize=9)
    fig.tight_layout(w_pad=1.5)
    fs.save(fig, FOLDER, f"{SLUG}-failures")


if __name__ == "__main__":
    bootstrap()
    permutation()
    failures()
