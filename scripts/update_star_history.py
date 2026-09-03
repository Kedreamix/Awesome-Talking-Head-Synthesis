#!/usr/bin/env python3
"""Rebuild docs/star-history.json from GitHub stargazer timestamps.

GitHub has no date-filtered star-count API. The public total is live; the
daily curve is reconstructed from GraphQL `starredAt` values (available to
repository admins/collaborators, including Actions' GITHUB_TOKEN).
"""

from __future__ import annotations

import argparse
import json
import os
import urllib.error
import urllib.request
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

DEFAULT_REPO = "Kedreamix/Awesome-Talking-Head-Synthesis"
DEFAULT_OUTPUT = Path("docs/star-history.json")
GRAPHQL_URL = "https://api.github.com/graphql"
SHANGHAI = ZoneInfo("Asia/Shanghai")
QUERY = """
query($owner: String!, $name: String!, $after: String) {
  repository(owner: $owner, name: $name) {
    stargazerCount
    stargazers(first: 100, after: $after, orderBy: {field: STARRED_AT, direction: ASC}) {
      pageInfo { hasNextPage endCursor }
      edges { starredAt }
    }
  }
}
"""


def github_token() -> str:
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if not token:
        raise SystemExit("GITHUB_TOKEN is required to read stargazer timestamps")
    return token


def graphql(token: str, variables: dict) -> dict:
    request = urllib.request.Request(
        GRAPHQL_URL,
        data=json.dumps({"query": QUERY, "variables": variables}).encode(),
        headers={
            "Accept": "application/json",
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "User-Agent": "awesome-talking-head-star-history",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=60) as response:
            payload = json.load(response)
    except urllib.error.HTTPError as error:
        detail = error.read().decode("utf-8", errors="replace")
        raise SystemExit(f"GitHub GraphQL HTTP {error.code}: {detail}") from error
    if payload.get("errors"):
        raise SystemExit(f"GitHub GraphQL errors: {payload['errors']}")
    return payload["data"]


def fetch_starred_at(repo: str, token: str) -> tuple[int, list[str]]:
    owner, name = repo.split("/", 1)
    timestamps: list[str] = []
    after = None
    total = 0
    while True:
        data = graphql(token, {"owner": owner, "name": name, "after": after})
        repository = data["repository"]
        if repository is None:
            raise SystemExit(f"Repository {repo} was not found")
        total = int(repository["stargazerCount"])
        stargazers = repository["stargazers"]
        timestamps.extend(edge["starredAt"] for edge in stargazers["edges"])
        page = stargazers["pageInfo"]
        if not page["hasNextPage"]:
            break
        after = page["endCursor"]
    return total, timestamps


def shanghai_date(value: str) -> str:
    return datetime.fromisoformat(value.replace("Z", "+00:00")).astimezone(SHANGHAI).date().isoformat()


def build_history(timestamps: list[str]) -> list[dict]:
    added = Counter(shanghai_date(item) for item in timestamps)
    cumulative = 0
    history = []
    for date in sorted(added):
        cumulative += added[date]
        history.append({"date": date, "added": added[date], "stars": cumulative})
    return history


def write_history(path: Path, count: int, history: list[dict], now: datetime) -> None:
    payload = {
        "updated_at": now.isoformat(timespec="seconds").replace("+00:00", "Z"),
        "timezone": "Asia/Shanghai",
        "count": count,
        "history": history,
    }
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", default=os.environ.get("GITHUB_REPOSITORY", DEFAULT_REPO))
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()

    count, timestamps = fetch_starred_at(args.repo, github_token())
    history = build_history(timestamps)
    if history and history[-1]["stars"] != len(timestamps):
        raise SystemExit("Reconstructed history does not match fetched timestamps")
    write_history(args.output, count, history, datetime.now(timezone.utc))
    last = history[-1] if history else {"date": "none", "stars": 0, "added": 0}
    print(
        f"Wrote {len(history)} days ({last['stars']} stars, last {last['date']} +{last['added']}) to {args.output}"
    )


if __name__ == "__main__":
    main()
