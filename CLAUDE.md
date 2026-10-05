# Alex Laroche's academic website

Jekyll site (AcademicPages fork) published by GitHub Pages from `master` at https://alexanderlaroche.github.io.

## Layout
- `_pages/`: about (homepage, `permalink: /`), research, publications, misc, sitemap, 404. Only one page may use `permalink: /`.
- `_data/navigation.yml`: top nav (Research, Publications, CV, Misc).
- `_config.yml`: site settings and sidebar author links (Email, ADS, arXiv, GitHub, ORCID). LinkedIn, INSPIRE and Google Scholar were removed on purpose.
- `_sass/_variables.scss` sets the dark palette; site-specific styles live in `_sass/_custom.scss`.
- `images/misc/`: figures for the Misc essays. `arxiv_submissions.png` is drawn from arXiv's monthly and per-category submission statistics.
- `images/research/`: thumbnails for the research page blocks, plus `wordcloud.png`, built by `scripts/make_wordcloud.py` from the arXiv abstracts of all papers in `_data/publications.yml` (needs `pip install wordcloud`; rerun after a new paper).
- `images/profile.jpg`: sidebar photo (GitHub avatar). `_sass/_custom.scss` crops it square so it renders as a circle.
- `files/academic_cv.pdf`: CV, built in Overleaf and replaced by hand for now.
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
- Running log on the Misc page. A draft (`_pages/cim_2025.md`, `published: false`) is stored locally only and excluded from git via `.git/info/exclude`; it is not in the repo.
- AI essay (`_pages/ai_in_astro.md`): the JWST Cycle 6 figure (by Ian Crossfield) uses unofficial counts; update once STScI publishes official Cycle 6 numbers.
- Building the CV from Overleaf into `files/academic_cv.pdf`.
