"""Article-local tests for NASA Pt. 1 pipeline helpers."""

import importlib.util
from pathlib import Path

import pandas as pd

MODULE_PATH = Path(__file__).resolve().parents[1] / "src" / "nasa_pt1_pipeline.py"
SPEC = importlib.util.spec_from_file_location("article_nasa_pt1_pipeline", MODULE_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(MODULE)


def test_normalize_date_column_formats_dates() -> None:
    climate_frame = pd.DataFrame({"date": ["2025/01/01", "2025-01-02"]})
    normalized = MODULE.normalize_date_column(climate_frame, "date")
    assert list(normalized["date"]) == ["2025-01-01", "2025-01-02"]


def test_normalize_date_column_coerces_invalid_to_nan() -> None:
    climate_frame = pd.DataFrame({"date": ["not-a-date"]})
    normalized = MODULE.normalize_date_column(climate_frame, "date")
    assert pd.isna(normalized.loc[0, "date"])
