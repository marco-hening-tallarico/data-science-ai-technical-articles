"""String helpers for article slug generation."""

from __future__ import annotations


def article_slug_from_title(article_title: str) -> str:
    """Create a simple URL-safe slug from a title."""
    lowered = article_title.lower().strip()
    cleaned = "".join(character if character.isalnum() else "-" for character in lowered)
    return "-".join(part for part in cleaned.split("-") if part)
