"""Figures for docs/05-university-core/03-applications-of-derivatives/05-optimization.md.

Run from the repo root:

    .venv/Scripts/python tools/figures/05-university-core/optimization.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
from matplotlib.patches import Rectangle  # noqa: E402

import figstyle as fs  # noqa: E402

FOLDER = "05-university-core"
SLUG = "optimization"
BOX = dict(facecolor="white", edgecolor="none", pad=0.4, alpha=0.9)


def grid(ax, size=9):
    ax.tick_params(labelsize=size, length=3)
    ax.grid(True)
    ax.set_axisbelow(True)


def box():
    """The net of a box cut from a 30 by 20 sheet, and its volume."""
    fig, (a, b) = plt.subplots(1, 2, figsize=(9.4, 3.8), gridspec_kw={"width_ratios": [1.1, 1]})
    a.set_aspect("equal")
    a.axis("off")
    s = 4.0
    a.add_patch(Rectangle((0, 0), 30, 20, fill=False, ec=fs.DARK, lw=2.2))
    for cx, cy in [(0, 0), (30 - s, 0), (0, 20 - s), (30 - s, 20 - s)]:
        a.add_patch(Rectangle((cx, cy), s, s, fc="#f6d5d7", ec=fs.RED, lw=1.5))
    a.plot([s, s], [0, s], color=fs.DARK, lw=1.0, ls="--")
    a.plot([30 - s, 30 - s], [0, s], color=fs.DARK, lw=1.0, ls="--")
    a.plot([0, s], [s, s], color=fs.DARK, lw=1.0, ls="--")
    a.plot([0, s], [20 - s, 20 - s], color=fs.DARK, lw=1.0, ls="--")
    a.plot([s, s], [20 - s, 20], color=fs.DARK, lw=1.0, ls="--")
    a.plot([30 - s, 30 - s], [20 - s, 20], color=fs.DARK, lw=1.0, ls="--")
    a.plot([30 - s, 30], [s, s], color=fs.DARK, lw=1.0, ls="--")
    a.plot([30 - s, 30], [20 - s, 20 - s], color=fs.DARK, lw=1.0, ls="--")
    a.text(s / 2, s / 2, "x", color=fs.RED, fontsize=11, ha="center", va="center")
    a.text(15, 10, "base: (30 − 2x) by (20 − 2x)", color=fs.GREEN, fontsize=10.5, ha="center", va="center")
    a.text(15, -1.2, "30 cm", color=fs.DARK, fontsize=10, ha="center", va="top")
    a.text(-1.0, 10, "20 cm", color=fs.DARK, fontsize=10, ha="right", va="center")
    a.text(15, 22.2, "cut a square of side x from each corner", color=fs.DARK, fontsize=9.5, ha="center", va="bottom")
    a.set_xlim(-6, 31)
    a.set_ylim(-4, 25)

    grid(b)
    x = np.linspace(0, 10, 300)
    v = x * (30 - 2 * x) * (20 - 2 * x)
    b.plot(x, v, color=fs.GREEN, lw=2.4)
    xs = (200 - 11200**0.5) / 24
    vs = xs * (30 - 2 * xs) * (20 - 2 * xs)
    b.plot([xs, xs], [0, vs], color=fs.GRAY, lw=1.1, ls="--")
    b.plot([xs], [vs], "o", color=fs.RED, ms=7, zorder=5)
    b.text(xs + 0.35, vs + 40, "x ≈ 3.92, V ≈ 1056 cm³", color=fs.RED, fontsize=10, ha="left", va="bottom")
    b.plot([0, 10], [0, 0], "o", color=fs.DARK, ms=5.5, zorder=5)
    b.set_xlim(-0.3, 10.4)
    b.set_ylim(-60, 1300)
    b.set_xlabel("cut size x (cm)")
    b.set_ylabel("volume V (cm³)")
    fs.save(fig, FOLDER, f"{SLUG}-box")


def fence():
    """Fence along a river: the layout, and the area with and without a limit on the river side."""
    fig, (a, b) = plt.subplots(1, 2, figsize=(9.0, 3.6), gridspec_kw={"width_ratios": [1, 1.25]})
    a.set_aspect("equal")
    a.axis("off")
    a.add_patch(Rectangle((0, 0), 10, 5, fc="#e6f2fb", ec="none"))
    a.text(5, 2.5, "river", color=fs.BLUE, fontsize=11, ha="center", va="center")
    a.add_patch(Rectangle((1.5, 5), 7, 4, fc="#eaf6f0", ec="none"))
    a.plot([1.5, 1.5, 8.5, 8.5], [5, 9, 9, 5], color=fs.GREEN, lw=3.2)
    a.text(5, 7, "A = x y", color=fs.GREEN, fontsize=11, ha="center", va="center")
    a.text(5, 9.4, "y (fenced)", color=fs.GREEN, fontsize=10, ha="center", va="bottom")
    a.text(1.2, 7, "x", color=fs.GREEN, fontsize=10.5, ha="right", va="center")
    a.text(8.8, 7, "x", color=fs.GREEN, fontsize=10.5, ha="left", va="center")
    a.text(5, 4.6, "y = 200 − 2x\nof the river bank", color=fs.DARK, fontsize=9, ha="center", va="top")
    a.set_xlim(-0.5, 10.5)
    a.set_ylim(-0.2, 11)

    grid(b)
    x = np.linspace(0, 100, 300)
    b.plot(x, x * (200 - 2 * x), color=fs.GREEN, lw=2.4)
    b.axvspan(60, 100, color="#eef0f2", zorder=0)
    b.plot([50], [5000], "o", color=fs.RED, ms=7, zorder=5)
    b.text(50, 5000 + 250, "no limit: x = 50, A = 5000", color=fs.RED, fontsize=10, ha="center", va="bottom")
    b.plot([60], [4800], "o", color=fs.BLUE, ms=7, zorder=5)
    b.annotate("river side at most 80 m:\nx ≥ 60, best at the\nendpoint, A = 4800", xy=(60, 4800), xytext=(8, 1500), color=fs.BLUE,
               fontsize=9.5, ha="left", va="center", arrowprops=dict(arrowstyle="->", color=fs.BLUE, lw=1.2))
    b.set_xlim(0, 100)
    b.set_ylim(0, 5900)
    b.set_xlabel("x (m)")
    b.set_ylabel("area A (m²)")
    fs.save(fig, FOLDER, f"{SLUG}-fence")


def can():
    """Surface area of a 355 cm^3 can against its radius."""
    fig, ax = fs.figure(5.6, 3.8)
    grid(ax)
    r = np.linspace(2.2, 6.2, 300)
    s = 2 * np.pi * r**2 + 2 * 355 / r
    ax.plot(r, s, color=fs.GREEN, lw=2.4)
    r0 = (355 / (2 * np.pi)) ** (1 / 3)
    s0 = 2 * np.pi * r0**2 + 2 * 355 / r0
    ax.plot([r0, r0], [250, s0], color=fs.GRAY, lw=1.1, ls="--")
    ax.plot([r0], [s0], "o", color=fs.RED, ms=7, zorder=5)
    ax.text(r0 + 0.12, 265, "r ≈ 3.84 cm, h = 2r ≈ 7.67 cm", color=fs.RED, fontsize=10, ha="left", va="center")
    ax.text(r0 - 0.12, 266, "S ≈ 277.5 cm²", color=fs.RED, fontsize=10, ha="right", va="center")
    ax.text(2.4, 395, "S(r) = 2πr² + 710/r", color=fs.GREEN, fontsize=10.5, ha="left", va="center")
    ax.set_xlim(2.2, 6.2)
    ax.set_ylim(250, 420)
    ax.set_xlabel("radius r (cm)")
    ax.set_ylabel("surface area S (cm²)")
    fs.save(fig, FOLDER, f"{SLUG}-can")


def closest():
    """The point on y = sqrt(x) closest to (4, 0)."""
    fig, ax = fs.figure(5.6, 4.2)
    ax.set_aspect("equal")
    grid(ax)
    ax.spines["left"].set_position("zero")
    ax.spines["bottom"].set_position("zero")
    x = np.linspace(0, 7.6, 300)
    ax.plot(x, np.sqrt(x), color=fs.GREEN, lw=2.4, zorder=3)
    r = 3.75**0.5
    th = np.linspace(0, 2 * np.pi, 400)
    ax.plot(4 + r * np.cos(th), r * np.sin(th), color=fs.GRAY, lw=1.2, ls="--", zorder=1)
    px, py = 3.5, 3.5**0.5
    ax.plot([4, px], [0, py], color=fs.RED, lw=2.0, zorder=4)
    ax.plot([4], [0], "o", color=fs.DARK, ms=6.5, zorder=6)
    ax.plot([px], [py], "o", color=fs.RED, ms=7, zorder=6)
    ax.text(4.12, -0.3, "(4, 0)", color=fs.DARK, fontsize=10, ha="left", va="top")
    ax.text(px - 0.15, py + 0.15, "(3.5, √3.5)", color=fs.RED, fontsize=10, ha="right", va="bottom")
    ax.text(4.12, 1.0, "distance\n√3.75 ≈ 1.94", color=fs.RED, fontsize=9.5, ha="left", va="center")
    ax.text(7.0, 2.85, "y = √x", color=fs.GREEN, fontsize=10.5, ha="right", va="bottom")
    ax.set_xlim(-0.5, 7.8)
    ax.set_ylim(-2.4, 3.2)
    ax.set_xticks([1, 2, 3, 4, 5, 6, 7])
    ax.set_yticks([-2, -1, 1, 2, 3])
    fs.save(fig, FOLDER, f"{SLUG}-closest")


def profit():
    """Revenue and cost for p = 100 - 2q and C = 200 + 20q + 2q^2: parallel tangents at q = 10."""
    fig, ax = fs.figure(6.0, 4.2)
    grid(ax)
    q = np.linspace(0, 24, 300)
    R = 100 * q - 2 * q**2
    C = 200 + 20 * q + 2 * q**2
    ax.plot(q, R, color=fs.GREEN, lw=2.4)
    ax.plot(q, C, color=fs.RED, lw=2.4)
    lx = np.array([5, 15])
    ax.plot(lx, 800 + 60 * (lx - 10), color=fs.GREEN, lw=1.3, ls="--")
    ax.plot(lx, 600 + 60 * (lx - 10), color=fs.RED, lw=1.3, ls="--")
    ax.plot([10, 10], [600, 800], color=fs.DARK, lw=2.4)
    ax.plot([10], [800], "o", color=fs.GREEN, ms=6.5, zorder=5)
    ax.plot([10], [600], "o", color=fs.RED, ms=6.5, zorder=5)
    ax.text(10.4, 700, "maximum gap = profit \\$200\nat q = 10", color=fs.DARK, fontsize=9.5, ha="left", va="center", bbox=BOX)
    ax.text(3.0, 1135, "revenue R(q)", color=fs.GREEN, fontsize=10.5, ha="left", va="center")
    ax.text(18.3, 1450, "cost C(q)", color=fs.RED, fontsize=10.5, ha="right", va="center")
    ax.text(1.0, 1560, "both dashed tangents have slope 60:\nMR = MC = \\$60", color=fs.DARK, fontsize=9.5, ha="left", va="center")
    ax.set_xlim(0, 24)
    ax.set_ylim(0, 1700)
    ax.set_xlabel("quantity q")
    ax.set_ylabel("dollars")
    fs.save(fig, FOLDER, f"{SLUG}-profit")


def gradient_descent():
    """One-variable gradient descent on (w - 3)^2 + 1 for several learning rates."""
    fig, (a, b) = plt.subplots(1, 2, figsize=(9.4, 3.8), gridspec_kw={"width_ratios": [1, 1.15]})
    grid(a)
    w = np.linspace(-0.6, 6.6, 300)
    a.plot(w, (w - 3) ** 2 + 1, color=fs.GREEN, lw=2.4, zorder=2)
    eta = 0.1
    cur = 0.0
    xs = [cur]
    for _ in range(8):
        cur -= eta * 2 * (cur - 3)
        xs.append(cur)
    xs = np.array(xs)
    ys = (xs - 3) ** 2 + 1
    a.plot(xs, ys, "o-", color=fs.BLUE, ms=5, lw=1.0, zorder=4)
    a.text(0.0, 11.4, "start w = 0", color=fs.BLUE, fontsize=9.5, ha="left", va="bottom")
    a.text(3.0, 0.55, "minimum at w = 3", color=fs.GREEN, fontsize=9.5, ha="center", va="top")
    a.text(6.4, 11.2, "η = 0.1", color=fs.BLUE, fontsize=10.5, ha="right", va="center")
    a.set_xlim(-0.6, 6.6)
    a.set_ylim(0, 13)
    a.set_xlabel("w")
    a.set_ylabel("f(w)")

    grid(b)
    n = np.arange(0, 11)
    for eta, col, name in [(0.1, fs.GREEN, "η = 0.1"), (0.9, fs.BLUE, "η = 0.9"), (1.0, fs.ORANGE, "η = 1.0"), (1.1, fs.RED, "η = 1.1")]:
        cur = 0.0
        seq = [cur]
        for _ in range(10):
            cur -= eta * 2 * (cur - 3)
            seq.append(cur)
        b.plot(n, seq, "o-", color=col, ms=4, lw=1.4)
    b.axhline(3, color=fs.GRAY, lw=1.0, ls="--")
    b.text(0.3, -8.0, "η = 1.1 diverges", color=fs.RED, fontsize=9.5, ha="left", va="center")
    b.text(0.3, -10.5, "η = 1.0 bounces, 0 and 6", color=fs.ORANGE, fontsize=9.5, ha="left", va="center")
    b.text(0.3, -13.0, "η = 0.9 spirals in slowly", color=fs.BLUE, fontsize=9.5, ha="left", va="center")
    b.text(0.3, -15.5, "η = 0.1 creeps up to 3", color=fs.GREEN, fontsize=9.5, ha="left", va="center")
    b.text(10.2, 3.0, "target 3", color=fs.GRAY, fontsize=9, ha="left", va="center")
    b.set_xlim(0, 11.8)
    b.set_ylim(-17, 21)
    b.set_xlabel("step n")
    b.set_ylabel("w after n steps")
    fs.save(fig, FOLDER, f"{SLUG}-gradient-descent")


if __name__ == "__main__":
    box()
    fence()
    can()
    closest()
    profit()
    gradient_descent()
