# Alex Laroche's academic website

Jekyll site (AcademicPages fork) published by GitHub Pages from `master` at https://alexanderlaroche.github.io.

## Layout
- `_pages/`: about (homepage, `permalink: /`), research, publications, misc, sitemap, 404. Only one page may use `permalink: /`.
- `_data/navigation.yml`: top nav (Research, Publications, CV, Misc).
- `_config.yml`: site settings and sidebar author links (Email, ADS, arXiv, GitHub, ORCID). LinkedIn, INSPIRE and Google Scholar were removed on purpose.
- `_sass/_variables.scss` sets the dark palette; site-specific styles live in `_sass/_custom.scss`.
- `images/misc/`: figures for the Misc essays. `arxiv_submissions.png` is frozen at September 2026 to match the AI essay's text; rebuild it with `python scripts/make_arxiv_plot.py --through 2026-09 --out images/misc/arxiv_submissions.png`. A plain run of the script plots the latest complete month to `arxiv_submissions_<month>.png` in the current directory (needs `numpy` and `matplotlib`).
- `images/research/`: thumbnails for the research page blocks, plus `wordcloud.png`, built by `scripts/make_wordcloud.py` from the arXiv abstracts of all papers in `_data/publications.yml` (needs `pip install wordcloud`; rerun after a new paper).
- `images/profile.jpg`: sidebar photo (GitHub avatar). `_sass/_custom.scss` crops it square so it renders as a circle.
- `files/academic_cv.pdf`: CV, generated; do not edit it by hand. The source lives in an Overleaf project, and its publication list is written from `_data/publications.yml` by `scripts/make_cv_publications.py` (which overwrites the project's `publications.tex` at build time). `.github/workflows/update-cv.yml` clones it weekly over Overleaf's Git access (`OVERLEAF_TOKEN` repo secret), compiles it with latexmk and commits the PDF if it changed. Run it from the Actions tab after editing the CV.
- `googled42309bacdc49a3f.html`: Google Search Console verification. Do not delete.

## Publications
`_data/publications.yml` is generated; do not edit it by hand. `scripts/update_publications.py` builds it from ADS library 8zUtfV-GT9KVqGIFMyOYVw, and `.github/workflows/update-publications.yml` runs it weekly using the `ADS_TOKEN` repo secret. It also writes `_data/citations.yml` (citations per year from the ADS metrics API), which `_includes/citations_chart.html` draws on the publications page; the chart and the citation total are hidden until that file exists. Notes such as "Submitted to ApJ" go in `_data/publication_notes.yml`, keyed by bibcode or arXiv id. The page groups papers into First-author, Contributing author and Conference proceedings.

## Workflow
- Preview locally: `bundle exec jekyll serve`, then http://localhost:4000. It needs a UTF-8 locale (`LANG=en_US.UTF-8`), and changes to `_config.yml` need a restart.
- Make changes on a branch and open a PR. `.github/workflows/build-check.yml` runs the real GitHub Pages build on every PR.
- The `master` ruleset blocks force-pushes and deletion.

## Writing
Pages are in Alex's voice: plain, concise, first person, without em dashes or rhetorical flourishes. Credit collaborators by name.

## Planned
- AI essay (`_pages/ai_in_astro.md`): the JWST Cycle 6 figure (by Ian Crossfield) uses unofficial counts; update once STScI publishes official Cycle 6 numbers.
