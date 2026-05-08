"""Preprocessing helpers for NASA climate datasets."""

from __future__ import annotations

import pandas as pd


def normalize_nasa_columns(climate_records: pd.DataFrame) -> pd.DataFrame:
    """Normalize NASA column names to lowercase snake case."""
    renamed_columns = {
        column: column.strip().lower().replace(" ", "_")
        for column in climate_records.columns
    }
    return climate_records.rename(columns=renamed_columns)
