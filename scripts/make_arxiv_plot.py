"""Build images/misc/arxiv_submissions.png for the "On AI in astronomy" essay.

Left panel: all arXiv submissions per month since 1991, from arXiv's monthly
submission statistics (a CSV). Right panel: monthly submissions since 2022 for
computer science, cs.AI and astrophysics, read from the data embedded in
arXiv's "Submissions by Category" report page. Needs numpy and matplotlib:

    pip install numpy matplotlib
    python scripts/make_arxiv_plot.py                  # latest complete month
    python scripts/make_arxiv_plot.py --through 2026-09 --out images/misc/arxiv_submissions.png

The essay's figure is frozen at September 2026 to match its text, so a plain
run writes arxiv_submissions_<month>.png in the current directory instead of
overwriting it. The second command above rebuilds the essay's figure.
"""
import argparse
import base64
import csv
import datetime as dt
import io
import json
import re
import urllib.request
from collections import defaultdict
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parent.parent
MONTHLY_CSV = "https://arxiv.org/stats/get_monthly_submissions"
CATEGORY_PAGE = "https://info.arxiv.org/about/reports/submission_category_by_year.html"

# the site's dark palette
TEXT, GRID, BLUE, ORANGE = "#c9d1d9", "#30363d", "#6cb6e6", "#f89406"


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": "alexanderlaroche.github.io plot script"})
    with urllib.request.urlopen(req) as r:
        return r.read().decode("utf-8")


def to_date(month):
    return dt.date(int(month[:4]), int(month[5:7]), 1)


def monthly_totals(through):
    rows = csv.DictReader(io.StringIO(fetch(MONTHLY_CSV)))
    return [(to_date(r["month"]), int(r["submissions"])) for r in rows if r["month"] <= through]


def decode(values):
    """Plotly stores numeric arrays as {"dtype", "bdata"} base64 blobs."""
    if isinstance(values, dict) and "bdata" in values:
        return np.frombuffer(base64.b64decode(values["bdata"]), dtype=values["dtype"]).tolist()
    return list(values)


def category_totals(through):
    """Monthly submissions for cs (all), cs.AI and astro-ph, from the first chart on the page."""
    html = fetch(CATEGORY_PAGE)
    start = html.index("Plotly.newPlot(")
    start = html.index("[", start)
    traces, _ = json.JSONDecoder().raw_decode(html[start:])
    out = defaultdict(lambda: {"cs": 0, "cs.AI": 0, "astro-ph": 0})
    for t in traces:
        cat = re.search(r"Category=([^<]+)", t.get("hovertemplate", ""))
        if not cat:
            continue
        cat = cat.group(1)
        keys = (["cs", "cs.AI"] if cat == "cs.AI" else ["cs"] if cat.startswith("cs.")
                else ["astro-ph"] if cat.startswith("astro-ph") else [])
        for x, y in zip(decode(t["x"]), decode(t["y"])):
            month = x[:7]
            if month <= through:
                for k in keys:
                    out[month][k] += int(y)
    months = sorted(out)
    return [to_date(m) for m in months], [out[m] for m in months]


def main():
    first_of_month = dt.date.today().replace(day=1)
    last_complete = (first_of_month - dt.timedelta(days=1)).strftime("%Y-%m")
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("--through", default=last_complete,
                   help="last month to include, YYYY-MM (default: last complete month)")
    p.add_argument("--out", type=Path, help="output PNG (default: arxiv_submissions_<month>.png)")
    args = p.parse_args()
    out = args.out or Path(f"arxiv_submissions_{args.through}.png")

    totals = monthly_totals(args.through)
    tc, cats = category_totals(args.through)

    plt.rcParams.update({"text.color": TEXT, "axes.labelcolor": TEXT, "xtick.color": TEXT,
                         "ytick.color": TEXT, "axes.edgecolor": GRID, "font.size": 14,
                         "font.family": "DejaVu Sans"})
    fig, (a, b) = plt.subplots(1, 2, figsize=(12, 4.4))

    t, n = zip(*totals)
    a.plot(t, [x / 1000 for x in n], color=BLUE, lw=1.4)
    a.set_title("All arXiv submissions per month", color=TEXT)
    a.set_ylabel("Submissions (thousands)")
    a.xaxis.set_major_locator(mdates.YearLocator(8))
    a.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
    a.annotate(f"{t[-1]:%b %Y}: ~{round(n[-1], -3):,}", (t[-1], n[-1] / 1000), xytext=(-150, -6),
               textcoords="offset points", color=TEXT, fontsize=12,
               arrowprops=dict(arrowstyle="-", color=TEXT, lw=0.8))

    l1, = b.plot(tc, [c["cs"] / 1000 for c in cats], color=BLUE, lw=1.6,
                 label="Computer science (all), left axis")
    b.set_title("Submissions per month by primary category", color=TEXT)
    b.set_ylabel("Computer science (thousands)", color=BLUE)
    b.tick_params(axis="y", colors=BLUE)
    # cs.AI and astro-ph are ~10x smaller, so they get their own axis on the right
    r = b.twinx()
    l2, = r.plot(tc, [c["cs.AI"] / 1000 for c in cats], color=ORANGE, lw=1.6, label="cs.AI, right axis")
    l3, = r.plot(tc, [c["astro-ph"] / 1000 for c in cats], color=ORANGE, lw=1.6, ls="--",
                 label="Astrophysics (all), right axis")
    r.set_ylabel("cs.AI and astrophysics (thousands)", color=ORANGE)
    r.tick_params(axis="y", colors=ORANGE)
    r.set_ylim(bottom=0)
    for sp in ("top", "left"):
        r.spines[sp].set_visible(False)
    b.legend(handles=[l1, l2, l3], frameon=False, loc="upper left", fontsize=11)

    for ax in (a, b):
        ax.set_facecolor("none")
        ax.grid(color=GRID, lw=0.6)
        ax.set_axisbelow(True)
        ax.spines["top"].set_visible(False)
        ax.set_ylim(bottom=0)
    a.spines["right"].set_visible(False)

    fig.tight_layout()
    fig.savefig(out, dpi=160, transparent=True)
    print(f"wrote {out} (data through {t[-1]:%b %Y})")


if __name__ == "__main__":
    main()
