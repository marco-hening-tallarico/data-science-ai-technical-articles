# GitHub profile notes

Concise suggestions for repository metadata in the GitHub UI (description,
topics, social preview image). Adjust wording to match how you want the project
positioned publicly.

## Suggested repository description

Reproducible technical writing portfolio across scientific Python, statistics,
ML validation, and data analysis.

## Suggested topics

- technical-writing
- data-science
- scientific-computing
- machine-learning
- statistics
- reproducible-research
- python
- jupyter-notebook
- data-analysis
- ml-validation
- data-leakage
- climate-data

## Social preview

GitHub can show an Open Graph image on shares and some listings (repository
**Settings → General → Social preview**).

You can set **`docs/assets/social-preview.png`** as that image: it is a simple,
text-only banner (no copyrighted artwork) with three portfolio themes. If you
prefer a figure that reflects a specific article, use one of the selected output
previews under `docs/assets/` instead (for example `data-leakage-preview.png`,
`nasa-climate-preview.png`, or `multiple-testing-preview.png`).

Regenerate or adjust previews with `MPLBACKEND=Agg make preview-assets` from the
repository root, or `MPLBACKEND=Agg python scripts/generate_docs_previews.py`
(use `MPLBACKEND=Agg` in restricted or headless environments).
