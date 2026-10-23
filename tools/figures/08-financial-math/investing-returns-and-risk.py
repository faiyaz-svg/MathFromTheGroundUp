"""Figure for investing-returns-and-risk: 10,000 made-up 30-year paths, shown as percentile bands."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import numpy as np

import figstyle as fs

rng = np.random.default_rng(2026)
paths_n, years = 10000, 30
r = np.maximum(rng.normal(0.07, 0.15, size=(paths_n, years)), -0.95)
paths = 10000 * np.cumprod(1 + r, axis=1)
paths = np.hstack([np.full((paths_n, 1), 10000.0), paths])
x = np.arange(years + 1)

p5, p25, p50, p75, p95 = np.percentile(paths, [5, 25, 50, 75, 95], axis=0)

fig, ax = fs.figure(6.2, 4.0)
ax.fill_between(x, p5, p95, color=fs.GREEN, alpha=0.15, linewidth=0)
ax.fill_between(x, p25, p75, color=fs.GREEN, alpha=0.30, linewidth=0)
for i in range(5):
    ax.plot(x, paths[i], color=fs.GRAY, linewidth=0.8, alpha=0.9)
ax.plot(x, p50, color=fs.GREEN, linewidth=2.2)
ax.plot(x, 10000 * 1.07**x, color=fs.ORANGE, linewidth=1.6, linestyle="--")
ax.set_yscale("log")
ax.set_xlabel("Years")
ax.set_ylabel("Value of \\$10,000 (log scale, dollars)")
ax.set_xlim(0, 33.5)
ax.text(30.4, p50[-1], "median", color=fs.GREEN, va="center", fontsize=9)
ax.text(30.4, 10000 * 1.07**30 * 1.25, "steady 7%", color=fs.ORANGE, va="center", fontsize=9)
ax.text(30.4, p95[-1], "95th", color=fs.DARK, va="center", fontsize=9)
ax.text(30.4, p5[-1], "5th", color=fs.DARK, va="center", fontsize=9)
ax.text(3.0, 150000, "light band: 5th to 95th percentile\nmedium band: 25th to 75th\ngray lines: five single paths", fontsize=8.5, va="center")
ax.set_ylim(3000, 500000)
fs.save(fig, "08-financial-math", "investing-returns-and-risk-fan")
