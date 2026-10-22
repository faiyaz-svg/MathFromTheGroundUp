"""Figures for docs/05-university-core/07-probability/02-conditional-probability-and-bayes.md.

Run from the repo root:

    .venv/Scripts/python tools/figures/05-university-core/conditional-probability-and-bayes.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

import figstyle as fs  # noqa: E402

FOLDER = "05-university-core"
SLUG = "conditional-probability-and-bayes"


def bars():
    """10,000 people: who is sick, and who among the positives is sick."""
    fig, ax = plt.subplots(figsize=(8.0, 3.9))
    ax.set_xlim(0, 10000)
    ax.set_ylim(-0.2, 3.6)
    ax.axis("off")
    h = 0.7
    # top bar: everyone
    ax.barh(2.75, 100, height=h, left=0, color=fs.RED, alpha=0.85)
    ax.barh(2.75, 9900, height=h, left=100, color=fs.GREEN, alpha=0.35)
    ax.text(0, 3.4, "Everyone: 10,000 people", ha="left", va="center", fontsize=10.5)
    ax.text(0, 2.75 - 0.52, "100 sick", ha="left", va="center", fontsize=10, color=fs.RED)
    ax.text(5050, 2.75, "9,900 healthy", ha="center", va="center", fontsize=10.5, color=fs.DARK)
    # bottom bar: positives only, same horizontal scale
    ax.barh(0.95, 90, height=h, left=0, color=fs.RED, alpha=0.85)
    ax.barh(0.95, 495, height=h, left=90, color=fs.GREEN, alpha=0.35)
    ax.text(0, 1.6, "Test positive: 585 people (on the same scale)", ha="left", va="center",
            fontsize=10.5)
    ax.text(0, 0.95 - 0.52, "90 sick", ha="left", va="center", fontsize=10, color=fs.RED)
    ax.text(700, 0.95, "495 healthy: false positives", ha="left", va="center", fontsize=10.5,
            color=fs.DARK)
    ax.text(0, -0.1, "90 of the 585 positives are sick: about 15.4%", ha="left", va="center",
            fontsize=10.5, color=fs.RED)
    fs.save(fig, FOLDER, f"{SLUG}-bars")


def curves():
    """P(sick | positive) against prevalence for three tests."""
    fig, ax = plt.subplots(figsize=(5.8, 3.8))
    ax.grid(True)
    ax.set_axisbelow(True)
    p = np.logspace(-3, np.log10(0.5), 300)
    tests = [
        (0.90, 0.95, fs.BLUE, "specificity 95%", 0.30),
        (0.90, 0.99, fs.ORANGE, "specificity 99%", 0.20),
        (0.90, 0.999, fs.GREEN, "specificity 99.9%", 0.10),
    ]
    for se, sp, col, label, ly in tests:
        post = p * se / (p * se + (1 - p) * (1 - sp))
        ax.plot(p, post, color=col, lw=2.2)
        ax.text(0.45, ly, label, color=col, fontsize=10, ha="right", va="center")
    ax.text(0.45, 0.40, "sensitivity 90% for all three:", color=fs.DARK, fontsize=10,
            ha="right", va="center")
    ax.axvline(0.01, color=fs.GRAY, lw=1.0, ls="--")
    ax.plot([0.01], [0.9 * 0.01 / (0.9 * 0.01 + 0.99 * 0.05)], "o", color=fs.BLUE, zorder=5)
    ax.annotate("0.154 at 1% prevalence", xy=(0.01, 0.1538), xytext=(0.0115, 0.03),
                fontsize=9.5, color=fs.DARK,
                arrowprops=dict(arrowstyle="-", color=fs.DARK, lw=0.8))
    ax.set_xscale("log")
    ax.set_xlim(0.001, 0.5)
    ax.set_ylim(0, 1.02)
    ax.set_xticks([0.001, 0.01, 0.1, 0.5])
    ax.set_xticklabels(["0.1%", "1%", "10%", "50%"])
    ax.tick_params(labelsize=9, length=3)
    ax.set_xlabel("share of people who are sick (prevalence)", fontsize=10)
    ax.set_ylabel("P(sick given a positive test)", fontsize=9.5)
    fs.save(fig, FOLDER, f"{SLUG}-prevalence")


if __name__ == "__main__":
    bars()
    curves()
