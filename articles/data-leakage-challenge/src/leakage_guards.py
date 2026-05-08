"""Reusable leakage guard helpers for tabular ML workflows."""

from __future__ import annotations

import pandas as pd


def has_entity_overlap(
    training_frame: pd.DataFrame,
    testing_frame: pd.DataFrame,
    entity_column: str,
) -> bool:
    """Return True when entity IDs appear in both training and testing frames."""
    training_entities = set(training_frame[entity_column])
    testing_entities = set(testing_frame[entity_column])
    return bool(training_entities.intersection(testing_entities))


def is_sorted_chronologically(data_frame: pd.DataFrame, date_column: str) -> bool:
    """Return True when date column is sorted ascending without reordering."""
    parsed_dates = pd.to_datetime(data_frame[date_column], errors="coerce")
    return parsed_dates.is_monotonic_increasing


def entity_overlap_ratio(
    training_frame: pd.DataFrame,
    testing_frame: pd.DataFrame,
    entity_column: str,
) -> float:
    """Return overlap ratio based on unique entities in the testing frame."""
    testing_entities = set(testing_frame[entity_column])
    if not testing_entities:
        return 0.0
    training_entities = set(training_frame[entity_column])
    overlap_count = len(training_entities.intersection(testing_entities))
    return overlap_count / float(len(testing_entities))
