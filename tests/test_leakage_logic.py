"""Basic guardrails against train/test leakage."""

import pandas as pd


def has_entity_overlap(
    train_frame: pd.DataFrame, test_frame: pd.DataFrame, entity_column: str
) -> bool:
    """Return True when entities appear in both train and test sets."""
    train_entities = set(train_frame[entity_column])
    test_entities = set(test_frame[entity_column])
    return bool(train_entities.intersection(test_entities))


def test_entity_overlap_detection() -> None:
    train_frame = pd.DataFrame({"tail_id": ["A", "B"]})
    test_frame = pd.DataFrame({"tail_id": ["C", "B"]})
    assert has_entity_overlap(train_frame, test_frame, "tail_id")
