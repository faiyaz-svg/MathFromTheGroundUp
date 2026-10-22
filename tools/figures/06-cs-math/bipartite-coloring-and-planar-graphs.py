"""Figures for docs/06-cs-math/05-graphs/03-bipartite-coloring-and-planar-graphs.md."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import figstyle as fs  # noqa: E402

FOLDER = "06-cs-math"
SLUG = "bipartite-coloring-and-planar-graphs"


def draw(ax, pos, edges, color=None, labels=None):
    for u, v in edges:
        (x1, y1), (x2, y2) = pos[u], pos[v]
        ax.plot([x1, x2], [y1, y2], color=fs.DARK, lw=1.8, zorder=1)
    for v, (x, y) in pos.items():
        ax.scatter([x], [y], s=380, color="white", edgecolor=fs.DARK, linewidth=1.8, zorder=2)
        ax.text(x, y, v, ha="center", va="center", fontsize=12, zorder=3)
    ax.set_aspect("equal")
    ax.axis("off")


def k4_two_drawings():
    fig, (ax1, ax2) = fs.plt.subplots(1, 2, figsize=(7.2, 3.4))
    edges = ["ab", "bc", "cd", "da", "ac", "bd"]
    # Drawing 1: a square with both diagonals, which cross.
    pos1 = {"a": (0, 1), "b": (1, 1), "c": (1, 0), "d": (0, 0)}
    draw(ax1, pos1, edges)
    ax1.text(0.5, -0.35, "edges ac and bd cross", ha="center", color=fs.RED, fontsize=11)
    ax1.set_xlim(-0.3, 1.3)
    ax1.set_ylim(-0.5, 1.3)
    # Drawing 2: d inside the triangle abc, no crossing, four faces.
    pos2 = {"a": (0.5, 1.15), "b": (1.15, 0), "c": (-0.15, 0), "d": (0.5, 0.38)}
    draw(ax2, pos2, ["ab", "bc", "ca", "da", "db", "dc"])
    ax2.text(0.72, 0.52, "F1", ha="center", va="center", color=fs.GREEN, fontsize=12)
    ax2.text(0.28, 0.52, "F2", ha="center", va="center", color=fs.GREEN, fontsize=12)
    ax2.text(0.5, 0.14, "F3", ha="center", va="center", color=fs.GREEN, fontsize=12)
    ax2.text(1.1, 0.85, "F4 (outside)", ha="left", va="center", color=fs.BLUE, fontsize=11)
    ax2.set_xlim(-0.4, 1.9)
    ax2.set_ylim(-0.4, 1.3)
    fig.tight_layout()
    fs.save(fig, FOLDER, f"{SLUG}-k4")


if __name__ == "__main__":
    k4_two_drawings()
