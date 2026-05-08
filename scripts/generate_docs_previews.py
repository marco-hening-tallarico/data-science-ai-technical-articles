"""Write docs/assets preview PNGs from committed project artifacts.

Priority sources (evidence-based, not invented):

- Data leakage: first matplotlib output embedded in
  ``articles/data-leakage-challenge/notebooks/Data_leaks.ipynb`` (correlation
  heatmap cell).
- NASA climate Pt. 1: ``articles/nasa-climate-data-pt1/figures/temperature_anomaly_grid.png``.
- Multiple testing: matplotlib output from the look-elsewhere Monte Carlo cell in
  ``articles/bonferroni-vs-benjamini-hochberg/notebooks/heavy-atom-p-val.ipynb``.

Also regenerates ``social-preview.png`` (text-only banner for GitHub).

Requires notebook outputs to retain ``image/png`` display_data (committed
execution results). Re-run the flagship notebooks if outputs were cleared.
"""

from __future__ import annotations

import base64
import json
import shutil
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

PROJECT_ROOT = Path(__file__).resolve().parents[1]
ASSETS_DIR = PROJECT_ROOT / "docs" / "assets"

DATA_LEAKS_NB = (
    PROJECT_ROOT
    / "articles"
    / "data-leakage-challenge"
    / "notebooks"
    / "Data_leaks.ipynb"
)
HEAVY_ATOM_NB = (
    PROJECT_ROOT
    / "articles"
    / "bonferroni-vs-benjamini-hochberg"
    / "notebooks"
    / "heavy-atom-p-val.ipynb"
)
NASA_PT1_FIGURE = (
    PROJECT_ROOT
    / "articles"
    / "nasa-climate-data-pt1"
    / "figures"
    / "temperature_anomaly_grid.png"
)

# Notebook cell indices align with current flagship notebooks (check after large edits).
_LEAKAGE_HEATMAP_CELL = 6
_BONFERRONI_MC_CELL = 1


def _pngs_in_cell(notebook_path: Path, cell_index: int) -> list[bytes]:
    """Decode every ``image/png`` in a code cell's outputs, in order."""
    payload = json.loads(notebook_path.read_text(encoding="utf-8"))
    cells = payload.get("cells", [])
    if cell_index >= len(cells):
        msg = f"{notebook_path.name}: cell index {cell_index} out of range"
        raise RuntimeError(msg)
    cell = cells[cell_index]
    decoded: list[bytes] = []
    for out in cell.get("outputs", []):
        data = out.get("data", {})
        b64 = data.get("image/png")
        if b64:
            decoded.append(base64.b64decode(b64))
    return decoded


def _write_png_from_notebook(
    notebook_path: Path,
    cell_index: int,
    png_index: int,
    dest: Path,
    *,
    description: str,
) -> None:
    pngs = _pngs_in_cell(notebook_path, cell_index)
    if not pngs:
        msg = (
            f"No embedded PNG in {notebook_path.relative_to(PROJECT_ROOT)} "
            f"cell {cell_index}; re-run the notebook to populate outputs "
            f"({description})."
        )
        raise RuntimeError(msg)
    if png_index >= len(pngs):
        msg = (
            f"{notebook_path.name} cell {cell_index}: "
            f"PNG index {png_index} but only {len(pngs)} image(s) present."
        )
        raise RuntimeError(msg)
    dest.write_bytes(pngs[png_index])


def _copy_nasa_climate_preview(dest: Path) -> None:
    if not NASA_PT1_FIGURE.is_file():
        msg = (
            f"Missing {NASA_PT1_FIGURE.relative_to(PROJECT_ROOT)}; "
            "generate it from the NASA Pt. 1 notebook pipeline."
        )
        raise RuntimeError(msg)
    shutil.copyfile(NASA_PT1_FIGURE, dest)


def write_social_preview(output_path: Path) -> None:
    """Minimal GitHub-style Open Graph asset (no external imagery)."""
    fig, ax = plt.subplots(figsize=(12, 6.3), dpi=100)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    fig.patch.set_facecolor("#0d1117")
    ax.text(
        0.5,
        0.72,
        "Technical Writing + Scientific Python",
        ha="center",
        va="center",
        fontsize=22,
        color="#f0f6fc",
        weight="bold",
    )
    ax.text(
        0.5,
        0.48,
        "technical writing  ·  scientific Python  ·  reproducible analysis",
        ha="center",
        va="center",
        fontsize=13,
        color="#8b949e",
    )
    ax.text(
        0.5,
        0.22,
        "Evidence-based portfolio · companion code & notebooks",
        ha="center",
        va="center",
        fontsize=11,
        color="#6e7681",
    )
    fig.savefig(output_path, facecolor=fig.get_facecolor(), bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    ASSETS_DIR.mkdir(parents=True, exist_ok=True)

    _write_png_from_notebook(
        DATA_LEAKS_NB,
        _LEAKAGE_HEATMAP_CELL,
        0,
        ASSETS_DIR / "data-leakage-preview.png",
        description="correlation heatmap",
    )

    _copy_nasa_climate_preview(ASSETS_DIR / "nasa-climate-preview.png")

    _write_png_from_notebook(
        HEAVY_ATOM_NB,
        _BONFERRONI_MC_CELL,
        0,
        ASSETS_DIR / "multiple-testing-preview.png",
        description="Monte Carlo / look-elsewhere plot",
    )

    write_social_preview(ASSETS_DIR / "social-preview.png")

    print(f"Wrote previews under {ASSETS_DIR.relative_to(PROJECT_ROOT)}/")
    print("  - data-leakage-preview.png  ← Data_leaks.ipynb embedded output")
    print("  - nasa-climate-preview.png   ← nasa-climate-data-pt1/figures/")
    print("  - multiple-testing-preview.png ← heavy-atom-p-val.ipynb embedded output")


if __name__ == "__main__":
    main()
