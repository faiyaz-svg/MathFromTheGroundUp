"""Figure for index-funds-fees-and-dollar-cost-averaging: growth of $10,000 at three fee levels."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import numpy as np

import figstyle as fs

x = np.arange(0, 31)
gross = 0.06

fig, ax = fs.figure(6.0, 3.8)
series = [
    (0.0, "no fee, 6.0%", fs.GRAY),
    (0.002, "MER 0.2%, net 5.8%", fs.GREEN),
    (0.015, "MER 1.5%, net 4.5%", fs.RED),
]
for m, label, colour in series:
    y = 10000 * (1 + gross - m) ** x
    ax.plot(x, y, color=colour, linewidth=2.0)
    shift = {0.0: 3800, 0.002: -2200, 0.015: 0}[m]
    ax.text(30.6, y[-1] + shift, f"{label}\n\\${y[-1]:,.0f}", color=colour, va="center", fontsize=8.5)

ax.annotate(
    "",
    xy=(30, 10000 * 1.045**30),
    xytext=(30, 10000 * 1.058**30),
    arrowprops=dict(arrowstyle="<->", color=fs.DARK, linewidth=1.0),
)
ax.set_xlim(0, 42)
ax.set_xlabel("Years")
ax.set_ylabel("Value of \\$10,000 (dollars)")
fs.save(fig, "08-financial-math", "index-funds-fees-and-dollar-cost-averaging-fees")
