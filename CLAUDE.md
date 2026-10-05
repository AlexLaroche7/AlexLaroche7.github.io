# Alex Laroche's academic website

Jekyll site (AcademicPages fork) published by GitHub Pages from `master` at https://alexanderlaroche.github.io.

## Layout
- `_pages/`: about (homepage, `permalink: /`), research, publications, sitemap, 404. Only one page may use `permalink: /`.
- `_data/navigation.yml`: top nav (Research, Publications, CV).
- `_config.yml`: site settings and sidebar author links (Email, ADS, arXiv, GitHub, ORCID). LinkedIn, INSPIRE and Google Scholar were removed on purpose.
- `_sass/_variables.scss` sets the dark palette; site-specific styles live in `_sass/_custom.scss`.
- `images/research/`: thumbnails for the research page blocks.
- `files/academic_cv.pdf`: CV, built in Overleaf and replaced by hand for now.
- `googled42309bacdc49a3f.html`: Google Search Console verification. Do not delete.

## Publications
`_data/publications.yml` is generated; do not edit it by hand. `scripts/update_publications.py` builds it from ADS library 8zUtfV-GT9KVqGIFMyOYVw, and `.github/workflows/update-publications.yml` runs it weekly using the `ADS_TOKEN` repo secret. Notes such as "Submitted to ApJ" go in `_data/publication_notes.yml`, keyed by bibcode or arXiv id. The page groups papers into First-author, Contributing author and Conference proceedings.

## Workflow
- Preview locally: `bundle exec jekyll serve`, then http://localhost:4000.
- Make changes on a branch and open a PR. `.github/workflows/build-check.yml` runs the real GitHub Pages build on every PR.
- The `master` ruleset blocks force-pushes and deletion.

## Writing
Pages are in Alex's voice: plain, concise, first person, without em dashes or rhetorical flourishes. Credit collaborators by name.

## Planned
- A Misc page with a Running log. Drafts exist outside the repo (`cim_2025.md`, `running.md`).
- Building the CV from Overleaf into `files/academic_cv.pdf`.
