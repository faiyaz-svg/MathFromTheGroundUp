"""Number-line drawing helpers for the algebra foundations figures.

Used by compound-inequalities-and-interval-notation.py and
absolute-value-equations-and-inequalities.py in this folder. Import it with:

    sys.path.insert(0, str(Path(__file__).resolve().parent))
    import algebra_numberline as nl

Call figstyle.save through the module (fs.save), never `from figstyle import save`,
so that the PNG preview tool can swap it out.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import figstyle as fs  # noqa: E402

MINUS = "−"


def tick_label(v, decimals=0):
    """A tick label with a true minus sign."""
    if decimals == 0 and float(v).is_integer():
        s = f"{int(v)}"
    else:
        s = f"{v:.{decimals}f}"
    return s.replace("-", MINUS)


def canvas(width, height, xlim, ylim):
    """A bare axes in data coordinates, with no frame."""
    fig, ax = fs.figure(width, height)
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.axis("off")
    return fig, ax


def axis_line(ax, y, lo, hi, ticks, decimals=0, size=9, tick_h=0.09, label_gap=0.16, show_labels=True):
    """A horizontal number line from lo to hi with arrowheads and labelled ticks."""
    ax.annotate(
        "",
        xy=(hi, y),
        xytext=(lo, y),
        arrowprops=dict(arrowstyle="<|-|>", color=fs.DARK, lw=1.2, shrinkA=0, shrinkB=0, mutation_scale=9),
    )
    for t in ticks:
        ax.plot([t, t], [y - tick_h, y + tick_h], color=fs.DARK, lw=1.0, solid_capstyle="butt")
        if show_labels:
            ax.text(t, y - label_gap, tick_label(t, decimals), ha="center", va="top", fontsize=size)


def dot(ax, x, y, closed, colour=fs.GREEN, size=7.5):
    """A closed (filled) or open (white-filled) dot."""
    ax.plot(
        [x],
        [y],
        "o",
        ms=size,
        mfc=colour if closed else "white",
        mec=colour,
        mew=1.8,
        zorder=5,
        clip_on=False,
    )


def segment(ax, y, a, b, closed_a, closed_b, colour=fs.GREEN, lw=4.5):
    """A bounded solution set on the line, with a dot at each end."""
    ax.plot([a, b], [y, y], color=colour, lw=lw, solid_capstyle="butt", zorder=3)
    dot(ax, a, y, closed_a, colour)
    dot(ax, b, y, closed_b, colour)


def ray(ax, y, start, direction, closed, hi, lo, colour=fs.GREEN, lw=4.5):
    """A solution set that runs off the end of the line.

    direction is +1 for a ray to the right and -1 for a ray to the left. The ray
    stops at the arrowhead of the line (hi on the right, lo on the left).
    """
    end = hi if direction > 0 else lo
    ax.annotate(
        "",
        xy=(end, y),
        xytext=(start, y),
        arrowprops=dict(arrowstyle="-|>", color=colour, lw=lw, shrinkA=0, shrinkB=0, mutation_scale=7),
        zorder=3,
    )
    dot(ax, start, y, closed, colour)


def whole_line(ax, y, lo, hi, colour=fs.GREEN, lw=4.5):
    """The whole line shaded."""
    ax.annotate(
        "",
        xy=(hi, y),
        xytext=(lo, y),
        arrowprops=dict(arrowstyle="<|-|>", color=colour, lw=lw, shrinkA=0, shrinkB=0, mutation_scale=7),
        zorder=3,
    )


def guide(ax, x, y_top, y_bottom, colour=fs.GRAY):
    """A light dashed vertical guide at a boundary value."""
    ax.plot([x, x], [y_bottom, y_top], color=colour, lw=0.9, ls=(0, (3, 3)), zorder=1)
