#!/usr/bin/env python3
"""Record one daily GitHub star-count snapshot for the Pages site."""

import argparse
import json
import os
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

DEFAULT_REPO = "Kedreamix/Awesome-Talking-Head-Synthesis"
DEFAULT_OUTPUT = Path("docs/star-history.json")


def fetch_stars(repo: str) -> int:
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "awesome-talking-head-star-tracker",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"

    request = urllib.request.Request(
        f"https://api.github.com/repos/{repo}",
        headers=headers,
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        payload = json.load(response)
    return int(payload["stargazers_count"])


def load_history(path: Path) -> dict:
    if not path.exists():
        return {"updated_at": "", "history": []}
    with path.open(encoding="utf-8") as handle:
        payload = json.load(handle)
    if not isinstance(payload.get("history"), list):
        raise ValueError(f"{path} has an invalid history field")
    return payload


def update_history(path: Path, stars: int, now: datetime) -> None:
    payload = load_history(path)
    today = now.astimezone(ZoneInfo("Asia/Shanghai")).date().isoformat()
    history = [
        item
        for item in payload["history"]
        if isinstance(item, dict) and item.get("date") != today
    ]
    history.append({"date": today, "stars": stars})
    history.sort(key=lambda item: item["date"])

    output = {
        "updated_at": now.isoformat(timespec="seconds").replace("+00:00", "Z"),
        "history": history,
    }
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(output, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(f"Recorded {stars} stars for {today} in {path}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", default=os.environ.get("GITHUB_REPOSITORY", DEFAULT_REPO))
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--stars", type=int, help="Use a supplied count instead of calling GitHub")
    args = parser.parse_args()

    stars = args.stars if args.stars is not None else fetch_stars(args.repo)
    update_history(args.output, stars, datetime.now(timezone.utc))


if __name__ == "__main__":
    main()
