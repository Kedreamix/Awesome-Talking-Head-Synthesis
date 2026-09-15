#!/usr/bin/env python3
"""Render the README open-source projects table from docs/projects.json."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "docs" / "projects.json"
README_PATH = ROOT / "README.md"
START = "<!-- OPEN_SOURCE_PROJECTS:START -->"
END = "<!-- OPEN_SOURCE_PROJECTS:END -->"

RESOURCE_LABELS = {
    "weights": "Weights",
    "apks": "APKs",
    "site": "Site",
    "docs": "Docs",
    "demo": "Demo",
    "gallery": "Gallery",
    "successor": "Successor",
    "page": "Page",
}


def render_table(data: dict) -> str:
    projects = data.get("projects", [])
    if data.get("count") != len(projects):
        raise ValueError("projects.json count does not match the projects array")

    lines = [
        "| Year | Project | Code | Resources | Description |",
        "| ---- | ---- | ---- | ---- | ---- |",
    ]
    for project in projects:
        resources = " · ".join(
            f"[{RESOURCE_LABELS.get(item['label'], item['label'].title())}]({item['url']})"
            for item in project.get("links", [])
        )
        description = project.get("description", {}).get("en", "")
        lines.append(
            f"| {project['year']} | [{project['name']}]({project['url']}) "
            f"| [Code]({project['url']}) | {resources} | {description} |"
        )
    return "\n".join(lines)


def update_readme(readme: str, table: str) -> str:
    if readme.count(START) != 1 or readme.count(END) != 1:
        raise ValueError("README project table markers are missing or duplicated")
    before, remainder = readme.split(START, 1)
    _, after = remainder.split(END, 1)
    return f"{before}{START}\n{table}\n{END}{after}"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--check",
        action="store_true",
        help="fail if README.md is not synchronized with docs/projects.json",
    )
    args = parser.parse_args()

    data = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    current = README_PATH.read_text(encoding="utf-8")
    expected = update_readme(current, render_table(data))

    if args.check:
        if current != expected:
            print("README.md project table is out of date; run scripts/sync_projects.py")
            return 1
        print("README.md project table is synchronized")
        return 0

    README_PATH.write_text(expected, encoding="utf-8")
    print(f"Updated {README_PATH.relative_to(ROOT)} from {DATA_PATH.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
