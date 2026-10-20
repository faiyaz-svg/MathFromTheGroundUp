"""Figures for docs/04-proofs-and-logic/02-logic-and-sets/06-sets-and-set-operations.md.

Run from the repo root:

    .venv/Scripts/python tools/figures/04-proofs-and-logic/sets-and-set-operations.py

Figures: how two sets can sit (relations), the four basic operations (operations),
three sets with a worked example (three-sets), De Morgan's law for sets (de-morgan)
and a Cartesian product (product).
"""

import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import figstyle as fs  # noqa: E402
from matplotlib.patches import Circle, Rectangle  # noqa: E402

FOLDER = "04-proofs-and-logic"
SLUG = "sets-and-set-operations"
FILL = fs.GREEN


def tint(colour, amount=0.55):
    """The colour mixed with white, as an opaque hex string (overlaps stay one shade)."""
    from matplotlib.colors import to_hex, to_rgb

    return to_hex(tuple(amount * c + (1 - amount) for c in to_rgb(colour)))


def universe(ax, ox, oy, w, h, label="U"):
    ax.add_patch(Rectangle((ox, oy), w, h, fill=False, ec=fs.DARK, lw=1.4, zorder=5))
    ax.text(ox + 0.12, oy + h - 0.12, label, ha="left", va="top", fontsize=11, color=fs.DARK)


def venn2_panel(ax, ox, oy, mode, colour=FILL, w=4.2, h=2.9, r=0.95, sep=0.62):
    """One two-set Venn diagram with the region for `mode` shaded."""
    universe(ax, ox, oy, w, h)
    shade = tint(colour)
    cy = oy + h / 2 - 0.05
    ax_c = ox + w / 2 - sep
    bx_c = ox + w / 2 + sep
    rect = Rectangle((ox, oy), w, h, fc=shade, ec="none", zorder=1)
    white_a = Circle((ax_c, cy), r, fc="white", ec="none", zorder=3)
    white_b = Circle((bx_c, cy), r, fc="white", ec="none", zorder=3)
    ca = Circle((ax_c, cy), r, fc=shade, ec="none", zorder=2)
    cb = Circle((bx_c, cy), r, fc=shade, ec="none", zorder=2)
    if mode == "union":
        ax.add_patch(ca)
        ax.add_patch(cb)
    elif mode == "inter":
        ax.add_patch(ca)
        ca.set_clip_path(Circle((bx_c, cy), r, transform=ax.transData))
    elif mode == "diff":
        ax.add_patch(ca)
        ax.add_patch(white_b)
    elif mode == "comp":
        ax.add_patch(rect)
        ax.add_patch(white_a)
    elif mode == "comp_union":
        ax.add_patch(rect)
        ax.add_patch(white_a)
        ax.add_patch(white_b)
    elif mode == "comp_b":
        ax.add_patch(rect)
        ax.add_patch(white_b)
    for cx in (ax_c, bx_c):
        ax.add_patch(Circle((cx, cy), r, fc="none", ec=fs.DARK, lw=1.4, zorder=6))
    ax.text(ax_c - 0.55, cy + 0.05, "A", ha="center", va="center", fontsize=12, zorder=7)
    ax.text(bx_c + 0.55, cy + 0.05, "B", ha="center", va="center", fontsize=12, zorder=7)


def canvas(width, height, xlim, ylim):
    fig, ax = fs.figure(width, height)
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.set_aspect("equal")
    ax.axis("off")
    return fig, ax


def relations():
    """Three ways two sets can sit: A inside B, disjoint, overlapping."""
    w, h = 4.2, 2.9
    gap = 0.5
    fig, ax = canvas(9.2, 2.6, (-0.1, 3 * w + 2 * gap + 0.1), (-0.65, h + 0.1))
    for i in range(3):
        universe(ax, i * (w + gap), 0, w, h)
    cy = h / 2 - 0.05
    # A inside B
    ox = 0
    for c, r in ((w / 2, 1.1), (w / 2 - 0.1, 0.55)):
        ax.add_patch(Circle((ox + c, cy), r, fc="none", ec=fs.DARK, lw=1.4, zorder=6))
    ax.add_patch(Circle((ox + w / 2 - 0.1, cy), 0.55, fc=tint(FILL), ec="none", zorder=2))
    ax.text(ox + w / 2 - 0.1, cy, "A", ha="center", va="center", fontsize=12, zorder=7)
    ax.text(ox + w / 2, cy + 0.83, "B", ha="center", va="center", fontsize=12, zorder=7)
    ax.text(ox + w / 2, -0.35, r"$A \subseteq B$", ha="center", va="center", fontsize=12)
    # disjoint
    ox = w + gap
    for cx, name in ((ox + w / 2 - 0.95, "A"), (ox + w / 2 + 0.95, "B")):
        ax.add_patch(Circle((cx, cy), 0.75, fc="none", ec=fs.DARK, lw=1.4, zorder=6))
        ax.text(cx, cy, name, ha="center", va="center", fontsize=12, zorder=7)
    ax.text(ox + w / 2, -0.35, r"$A \cap B = \emptyset$", ha="center", va="center", fontsize=12)
    # overlapping
    ox = 2 * (w + gap)
    for cx, name, dx in ((ox + w / 2 - 0.55, "A", -0.55), (ox + w / 2 + 0.55, "B", 0.55)):
        ax.add_patch(Circle((cx, cy), 0.95, fc="none", ec=fs.DARK, lw=1.4, zorder=6))
        ax.text(cx + dx, cy, name, ha="center", va="center", fontsize=12, zorder=7)
    ax.text(ox + w / 2, -0.35, r"$A \cap B \neq \emptyset$", ha="center", va="center", fontsize=12)
    fs.save(fig, FOLDER, f"{SLUG}-relations")


def operations():
    """Union, intersection, difference and complement on a two-set Venn diagram."""
    w, h = 4.2, 2.9
    gapx, gapy = 0.6, 0.85
    fig, ax = canvas(7.4, 5.4, (-0.1, 2 * w + gapx + 0.1), (-(h + gapy) - 0.6, h + 0.1))
    specs = [
        ("union", r"$A \cup B$", 0, 0),
        ("inter", r"$A \cap B$", w + gapx, 0),
        ("diff", r"$A \setminus B$", 0, -(h + gapy)),
        ("comp", r"$A^c = U \setminus A$", w + gapx, -(h + gapy)),
    ]
    for mode, label, ox, oy in specs:
        venn2_panel(ax, ox, oy, mode)
        ax.text(ox + w / 2, oy - 0.33, label, ha="center", va="center", fontsize=12)
    fs.save(fig, FOLDER, f"{SLUG}-operations")


def de_morgan():
    """(A union B) complement equals (A complement) intersect (B complement)."""
    w, h = 4.2, 2.9
    gap = 0.5
    fig, ax = canvas(11.6, 2.5, (-0.1, 4 * w + 3 * gap + 0.1), (-0.65, h + 0.1))
    specs = [
        ("comp", r"$A^c$", fs.BLUE, 0),
        ("comp_b", r"$B^c$", fs.ORANGE, 1),
        ("comp_union", r"$A^c \cap B^c$", fs.GREEN, 2),
        ("comp_union", r"$(A \cup B)^c$", fs.GREEN, 3),
    ]
    for mode, label, colour, i in specs:
        ox = i * (w + gap)
        venn2_panel(ax, ox, 0, mode, colour=colour)
        ax.text(ox + w / 2, -0.35, label, ha="center", va="center", fontsize=12)
    fs.save(fig, FOLDER, f"{SLUG}-de-morgan")


def three_sets():
    """Three sets with a worked example: A multiples of 2, B multiples of 3, C at most 6."""
    r = 1.55
    centres = {"A": (-0.85, 0.5), "B": (0.85, 0.5), "C": (0.0, -0.95)}
    fig, ax = canvas(5.6, 5.0, (-3.4, 3.4), (-3.2, 2.9))
    universe(ax, -3.3, -3.1, 6.6, 5.9)
    for name, (cx, cy) in centres.items():
        ax.add_patch(Circle((cx, cy), r, fc="none", ec=fs.DARK, lw=1.4, zorder=6))
    # label the sets outside the circles
    ax.text(-2.55, 1.9, "A", fontsize=13, ha="center", va="center", color=fs.DARK)
    ax.text(2.55, 1.9, "B", fontsize=13, ha="center", va="center", color=fs.DARK)
    ax.text(1.55, -2.45, "C", fontsize=13, ha="center", va="center", color=fs.DARK)

    def inside(name, x, y):
        cx, cy = centres[name]
        return (x - cx) ** 2 + (y - cy) ** 2 < r**2

    region_text = {
        (1, 0, 0): "8, 10",
        (0, 1, 0): "9",
        (0, 0, 1): "1, 5",
        (1, 1, 0): "12",
        (1, 0, 1): "2, 4",
        (0, 1, 1): "3",
        (1, 1, 1): "6",
    }
    xs = np.linspace(-3.0, 3.0, 400)
    ys = np.linspace(-2.8, 2.5, 400)
    gx, gy = np.meshgrid(xs, ys)
    for key, text in region_text.items():
        mask = np.ones_like(gx, dtype=bool)
        for flag, name in zip(key, "ABC"):
            cx, cy = centres[name]
            inside_mask = (gx - cx) ** 2 + (gy - cy) ** 2 < r**2
            mask &= inside_mask if flag else ~inside_mask
        px, py = gx[mask].mean(), gy[mask].mean()
        ax.text(px, py, text, ha="center", va="center", fontsize=11, zorder=7)
    ax.text(-2.55, -2.6, "7, 11", ha="center", va="center", fontsize=11, zorder=7)
    fs.save(fig, FOLDER, f"{SLUG}-three-sets")


def product():
    """The Cartesian product {1, 2, 3} x {a, b} as a grid of six ordered pairs."""
    fig, ax = fs.figure(4.6, 2.9)
    xs = [1, 2, 3]
    ys = [0, 1]
    names = ["a", "b"]
    for x in xs:
        for yi, y in enumerate(ys):
            ax.plot(x, y, "o", color=fs.GREEN, markersize=9, zorder=3)
            ax.text(x, y + 0.22, f"({x}, {names[yi]})", ha="center", va="bottom", fontsize=11)
    ax.set_xlim(0.4, 3.6)
    ax.set_ylim(-0.5, 1.7)
    ax.set_xticks(xs)
    ax.set_yticks(ys)
    ax.set_yticklabels(names)
    ax.set_xlabel(r"first coordinate, from $A = \{1, 2, 3\}$")
    ax.set_ylabel(r"second coordinate, from $B = \{a, b\}$")
    ax.grid(True)
    ax.set_axisbelow(True)
    fs.save(fig, FOLDER, f"{SLUG}-product")


if __name__ == "__main__":
    relations()
    operations()
    de_morgan()
    three_sets()
    product()
