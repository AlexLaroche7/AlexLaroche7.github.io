"""Build images/research/wordcloud.png from the titles and abstracts of all
my papers.

Reads the arXiv links of every paper in _data/publications.yml,
fetches their abstracts from the arXiv API and draws a word cloud in the
site's dark palette. Needs the `wordcloud` package:

    pip install wordcloud
    python scripts/make_wordcloud.py
"""
import re
import urllib.request
import xml.etree.ElementTree as ET
import zlib
from pathlib import Path

from wordcloud import STOPWORDS, WordCloud

ROOT = Path(__file__).resolve().parent.parent
PUBS = ROOT / "_data" / "publications.yml"
OUT = ROOT / "images" / "research" / "wordcloud.png"

# words that are common in abstracts but say nothing about the research
EXTRA_STOPWORDS = {
    "use", "used", "using", "show", "shows", "find", "found", "also", "can",
    "may", "well", "new", "one", "two", "three", "five", "eight", "first",
    "work", "paper", "present", "results", "result", "based", "however",
    "thus", "within", "without", "including", "allows", "make",
    "making", "provide", "provides", "suggest", "suggests", "demonstrate",
    "approach", "method", "methods", "model", "models", "data", "set",
    "number", "large", "small", "high", "low", "range", "known", "e", "g",
    "et", "al", "us", "will", "via", "order", "given", "per", "less", "much",
    "even", "still", "yet", "thereby", "remain", "remains", "require",
    "requires", "previously", "recently", "particular", "different",
    "aim", "refers", "relying", "comprise", "apply", "implemented",
    "account", "analyze", "consistent", "directly", "overall", "producing",
    "significant", "significantly", "viable", "impacts", "recent",
    "phenomena", "class", "relative", "associated", "generate", "function",
    "release", "sub", "surf", "object", "objects", "evidence", "image",
    "space", "theories", "properties", "sample", "learns", "parameter",
    "fraction", "amplitude", "predicted", "numerical", "distinguishes",
    "suppressing", "masquerade", "closing", "eleven", "inferences", "aspect",
    "likely", "due", "identify", "detected", "sources", "candidate",
    "framework", "system", "systems", "independent", "observations",
    "observational", "scale", "masses", "constraint", "pre", "post",
    "across", "highlight", "publicly", "available", "review", "unified",
    "common", "escape", "single",
}

# fold plurals the default normalization misses, so they don't double up
PLURALS = {"binaries": "binary", "stars": "star", "clusters": "cluster",
           "spectrum": "spectra", "halos": "halo", "haloes": "halo"}

# the site's dark palette: link blue, light grays and the warm accents
COLORS = ["#6cb6e6", "#6cb6e6", "#6cb6e6", "#e6edf3", "#c9d1d9", "#8b949e",
          "#f89406", "#62c462", "#ee5f5b"]


def arxiv_ids():
    ids = []
    for entry in PUBS.read_text().split("\n- ")[1:]:
        m = re.search(r'arxiv: "https://arxiv.org/abs/([^"]+)"', entry)
        if m:
            ids.append(m.group(1))
    return ids


def fetch_text(ids):
    url = ("https://export.arxiv.org/api/query?max_results=100&id_list="
           + ",".join(ids))
    with urllib.request.urlopen(url) as resp:
        root = ET.fromstring(resp.read())
    ns = {"a": "http://www.w3.org/2005/Atom"}
    parts = []
    for entry in root.findall("a:entry", ns):
        parts.append(entry.find("a:title", ns).text)
        parts.append(entry.find("a:summary", ns).text)
    text = " ".join(parts)
    # strip LaTeX markup such as $\textit{Gaia}$ and [$\alpha$/M]
    text = re.sub(r"\\[a-zA-Z]+", " ", text)
    text = re.sub(r"[${}\[\]_^]", " ", text)
    text = re.sub(r"[^\x00-\x7f]", " ", text)
    return re.sub(r"\b(" + "|".join(PLURALS) + r")\b",
                  lambda m: PLURALS[m.group(1).lower()], text,
                  flags=re.IGNORECASE)


def main():
    text = fetch_text(arxiv_ids())
    cloud = WordCloud(
        width=1600, height=800, scale=1,
        mode="RGBA", background_color=None,
        stopwords=STOPWORDS | EXTRA_STOPWORDS,
        collocations=True, min_word_length=3,
        # keep hyphenated terms such as post-interaction and ultra-light
        regexp=r"\w[\w'-]*\w",
        relative_scaling=0.3,
        max_words=70, prefer_horizontal=0.9,
        font_step=2, margin=6, random_state=7,
        # color by word, so reruns keep the same colors
        color_func=lambda word, **kwargs:
            COLORS[zlib.crc32(word.encode()) % len(COLORS)],
    ).generate(text)
    cloud.to_file(OUT)
    print(f"wrote {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
