"""Generate docs/portfolio_report.md — evidence-based portfolio roll-up."""

from __future__ import annotations

import json
import re
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
ARTICLES_DIR = PROJECT_ROOT / "articles"
OUTPUT_PATH = PROJECT_ROOT / "docs" / "portfolio_report.md"
NOTEBOOK_REPORT_PATH = PROJECT_ROOT / "docs" / "notebook_execution_report.json"
DEPENDENCY_PATH = PROJECT_ROOT / "docs" / "dependency_inventory.md"
STATUS_LABELS = ("runnable", "partial", "in progress", "pending migration")


def load_notebook_status() -> tuple[dict[str, str], dict[str, int], int]:
    """Load notebook status mapping and summary counts from JSON report."""
    if not NOTEBOOK_REPORT_PATH.exists():
        return {}, {}, 0

    report_payload = json.loads(NOTEBOOK_REPORT_PATH.read_text(encoding="utf-8"))
    per_notebook_status: dict[str, str] = {}
    summary_counts: dict[str, int] = {}
    for record in report_payload:
        notebook_path = str(record.get("notebook", ""))
        notebook_status = str(record.get("status", "unknown"))
        per_notebook_status[notebook_path] = notebook_status
        summary_counts[notebook_status] = summary_counts.get(notebook_status, 0) + 1
    return per_notebook_status, summary_counts, len(report_payload)


def extract_status(readme_text: str) -> str:
    """Extract first known status label from README text."""
    readme_lower = readme_text.lower()
    for status_label in STATUS_LABELS:
        if status_label in readme_lower:
            return status_label
    return "unknown"


def extract_data_availability(data_readme_text: str) -> str:
    """Classify data availability with conservative keyword rules."""
    lowered = data_readme_text.lower()
    if "pending migration" in lowered:
        return "pending migration"
    if "synthetic" in lowered:
        return "synthetic/generated"
    if "nasa power" in lowered or "public" in lowered:
        return "public source (documented)"
    if "external services" in lowered:
        return "external providers (see notes)"
    if "no local data pipeline is defined yet" in lowered:
        return "not yet defined"
    return "documented in article data notes"


def declared_libraries(article_dir: Path) -> str:
    """Return comma-separated requirement package names for one article."""
    requirements_path = article_dir / "requirements.txt"
    if not requirements_path.exists():
        return "-"

    packages: list[str] = []
    for raw_line in requirements_path.read_text(encoding="utf-8").splitlines():
        stripped = raw_line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        package_name = re.split(r"[<>=!~]", stripped, maxsplit=1)[0].strip()
        if package_name:
            packages.append(package_name)
    return ", ".join(packages) if packages else "-"


def main() -> None:
    """Write portfolio roll-up from article README metadata and JSON snapshots."""
    notebook_status_map, notebook_counts, notebook_total = load_notebook_status()

    dep_note = (
        f"`{DEPENDENCY_PATH.relative_to(PROJECT_ROOT).as_posix()}`"
        if DEPENDENCY_PATH.exists()
        else "`docs/dependency_inventory.md` (missing)"
    )

    report_lines: list[str] = [
        "# Portfolio report",
        "",
        "This document summarizes repository metadata and **existing** generated "
        "artifacts (article READMEs, `docs/notebook_execution_report.json`). "
        "It does **not** execute notebooks, refresh plots, or run CI.",
        "",
        "## Dependencies inventory",
        "",
        f"Pinned and declared dependency notes live in {dep_note}.",
        "",
        "## Article summary",
        "",
        "| Article | Status | Declared libraries | Data availability "
        "| Notebook status entries |",
        "| --- | --- | --- | --- | --- |",
    ]

    for article_dir in sorted(path for path in ARTICLES_DIR.iterdir() if path.is_dir()):
        readme_path = article_dir / "README.md"
        readme_text = (
            readme_path.read_text(encoding="utf-8") if readme_path.exists() else ""
        )
        data_readme_path = article_dir / "data" / "README.md"
        data_text = (
            data_readme_path.read_text(encoding="utf-8")
            if data_readme_path.exists()
            else ""
        )
        notebook_files = sorted(article_dir.glob("notebooks/*.ipynb"))
        notebook_states: list[str] = []
        for notebook_file in notebook_files:
            relative_notebook = notebook_file.relative_to(PROJECT_ROOT).as_posix()
            state = notebook_status_map.get(relative_notebook, "not listed")
            notebook_states.append(f"{notebook_file.name}: {state}")
        notebook_state_summary = "; ".join(notebook_states) if notebook_states else "-"

        report_lines.append(
            "| "
            f"`{article_dir.relative_to(PROJECT_ROOT).as_posix()}` | "
            f"{extract_status(readme_text)} | "
            f"{declared_libraries(article_dir)} | "
            f"{extract_data_availability(data_text)} | "
            f"{notebook_state_summary} |"
        )

    report_lines.extend(
        [
            "",
            "## Notebook execution snapshot",
            "",
        ]
    )
    if notebook_total == 0:
        report_lines.append(
            "- `docs/notebook_execution_report.json` not found; "
            "no notebook status snapshot available."
        )
    else:
        report_lines.append(
            f"- Source: `{NOTEBOOK_REPORT_PATH.relative_to(PROJECT_ROOT).as_posix()}`"
        )
        report_lines.append(f"- Notebook entries: {notebook_total}")
        for label, count in sorted(notebook_counts.items()):
            report_lines.append(f"- `{label}`: {count}")

    report_lines.extend(
        [
            "",
            "## Lint, tests, and local validation",
            "",
            "- Not captured automatically in this file.",
            "- Run `make check` in your active virtual environment for current "
            "Ruff + pytest results.",
        ]
    )

    OUTPUT_PATH.write_text("\n".join(report_lines) + "\n", encoding="utf-8")
    print(f"Wrote {OUTPUT_PATH.relative_to(PROJECT_ROOT)}")


if __name__ == "__main__":
    main()
