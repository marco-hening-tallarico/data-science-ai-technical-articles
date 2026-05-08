"""Generate lightweight PNG previews for docs/assets from repo-local fixtures.

Figures are illustrative only: leakage panel uses the same toy frames as
article tests; NASA panel uses the shared NASA POWER JSON schema test fixture;
multiple-testing panel uses p-values from article unit tests for BH helpers.
"""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
ASSETS_DIR = PROJECT_ROOT / "docs" / "assets"

sys.path.insert(0, str(PROJECT_ROOT))

from shared.nasa.data_access import power_json_to_frame  # noqa: E402


def _configure_axes_style() -> None:
    plt.rcParams.update(
        {
            "figure.facecolor": "white",
            "axes.facecolor": "white",
            "axes.grid": True,
            "grid.alpha": 0.25,
            "font.size": 10,
        }
    )


def write_leakage_preview(output_path: Path) -> None:
    """Overlap illustration matching ``test_entity_overlap_ratio_for_partial_overlap``."""
    training_frame = pd.DataFrame({"tail_id": ["A", "B", "C"]})
    testing_frame = pd.DataFrame({"tail_id": ["C", "D"]})
    train_set = set(training_frame["tail_id"])
    test_set = set(testing_frame["tail_id"])
    overlap = train_set.intersection(test_set)

    fig, ax = plt.subplots(figsize=(6, 3.5), dpi=120)
    categories = sorted(train_set.union(test_set))
    train_counts = [1 if c in train_set else 0 for c in categories]
    test_counts = [1 if c in test_set else 0 for c in categories]
    x = np.arange(len(categories))
    width = 0.35
    ax.bar(x - width / 2, train_counts, width, label="Train split", color="#4c72b0")
    ax.bar(x + width / 2, test_counts, width, label="Test split", color="#55a868")
    for idx, cat in enumerate(categories):
        if cat in overlap:
            ax.annotate(
                "overlap",
                xy=(idx, 1.05),
                ha="center",
                fontsize=8,
                color="#c44e52",
            )
    ax.set_xticks(x)
    ax.set_xticklabels(categories)
    ax.set_ylim(0, 1.35)
    ax.set_ylabel("Present in split (toy IDs)")
    ax.set_title("Entity overlap toy example (article test scenario)")
    ax.legend(loc="upper right", fontsize=8)
    fig.tight_layout()
    fig.savefig(output_path, bbox_inches="tight")
    plt.close(fig)


def write_nasa_preview(output_path: Path) -> None:
    """Two-day T2M series from ``tests/test_nasa_data_access_shared.py`` fixture."""
    payload = {
        "properties": {
            "parameter": {
                "T2M": {"20250101": 10.0, "20250102": 11.0},
                "PRECTOTCORR": {"20250101": 0.1, "20250102": 0.2},
            }
        }
    }
    frame = power_json_to_frame(payload)
    fig, ax = plt.subplots(figsize=(6, 3.5), dpi=120)
    ax.plot(
        frame["date"],
        frame["T2M"],
        marker="o",
        color="#4c72b0",
        label="T2M (fixture payload)",
    )
    ax.set_xlabel("Date")
    ax.set_ylabel("T2M")
    ax.set_title("NASA POWER schema → frame (compact test fixture, not live API)")
    ax.legend(fontsize=8)
    fig.autofmt_xdate()
    fig.tight_layout()
    fig.savefig(output_path, bbox_inches="tight")
    plt.close(fig)


def write_multiple_testing_preview(output_path: Path) -> None:
    """BH thresholds vs sorted p-values; Bonferroni α/m line for comparison."""
    import importlib.util

    module_path = (
        PROJECT_ROOT
        / "articles"
        / "bonferroni-vs-benjamini-hochberg"
        / "src"
        / "multiple_testing.py"
    )
    spec = importlib.util.spec_from_file_location("article_mt", module_path)
    module = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(module)

    p_values = np.array([0.001, 0.02, 0.03, 0.4])
    q_level = 0.05
    m = len(p_values)
    sorted_indices = np.argsort(p_values)
    sorted_p = p_values[sorted_indices]
    thresholds = module.benjamini_hochberg_thresholds(m, q_level)
    bonf_line = 0.05 / m

    fig, ax = plt.subplots(figsize=(6, 3.8), dpi=120)
    ranks = np.arange(1, m + 1)
    ax.scatter(ranks, sorted_p, color="#4c72b0", label="Sorted p-values", zorder=3)
    ax.plot(ranks, thresholds, color="#55a868", label=f"BH thresholds (q={q_level})")
    ax.axhline(bonf_line, color="#c44e52", linestyle="--", label="Bonferroni α/m")
    ax.set_xlabel("Rank (sorted p-values)")
    ax.set_ylabel("p")
    ax.set_title("Multiple testing: BH vs Bonferroni (article test p-values)")
    ax.legend(fontsize=8, loc="upper left")
    fig.tight_layout()
    fig.savefig(output_path, bbox_inches="tight")
    plt.close(fig)


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
    _configure_axes_style()
    ASSETS_DIR.mkdir(parents=True, exist_ok=True)
    write_leakage_preview(ASSETS_DIR / "data-leakage-preview.png")
    write_nasa_preview(ASSETS_DIR / "nasa-climate-preview.png")
    write_multiple_testing_preview(ASSETS_DIR / "multiple-testing-preview.png")
    write_social_preview(ASSETS_DIR / "social-preview.png")
    print(f"Wrote previews under {ASSETS_DIR.relative_to(PROJECT_ROOT)}/")


if __name__ == "__main__":
    main()
