from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone
from pathlib import Path
import re
import subprocess
from typing import Any


@dataclass(frozen=True)
class Contributor:
    name: str
    email: str | None
    commits: int


@dataclass(frozen=True)
class GitMetrics:
    repository: str
    branch: str | None
    head: str | None
    since_days: int
    commit_count: int
    contributor_count: int
    top_contributors: list[Contributor] = field(default_factory=list)
    latest_tags: list[str] = field(default_factory=list)
    latest_commit_date: str | None = None
    status: str = "ok"
    warnings: list[str] = field(default_factory=list)


def collect_git_metrics(repo: str | Path, since_days: int = 90) -> GitMetrics:
    """Collect local Git signals for a repository."""
    repo_path = Path(repo).expanduser().resolve()
    warnings: list[str] = []

    if since_days <= 0:
        raise ValueError("since_days must be greater than zero")

    if not repo_path.exists():
        return GitMetrics(
            repository=str(repo_path),
            branch=None,
            head=None,
            since_days=since_days,
            commit_count=0,
            contributor_count=0,
            status="missing_repository",
            warnings=["Repository path does not exist."],
        )

    if not _is_git_repo(repo_path):
        return GitMetrics(
            repository=str(repo_path),
            branch=None,
            head=None,
            since_days=since_days,
            commit_count=0,
            contributor_count=0,
            status="not_git_repository",
            warnings=["Repository path is not a Git repository."],
        )

    since = datetime.now(timezone.utc) - timedelta(days=since_days)
    since_arg = since.date().isoformat()

    branch = _git_text(repo_path, ["branch", "--show-current"]) or None
    if not branch:
        branch = _git_text(repo_path, ["rev-parse", "--abbrev-ref", "HEAD"]) or None

    head = _git_text(repo_path, ["rev-parse", "--short", "HEAD"]) or None
    if head is None:
        return GitMetrics(
            repository=str(repo_path),
            branch=branch,
            head=None,
            since_days=since_days,
            commit_count=0,
            contributor_count=0,
            status="empty_repository",
            warnings=["Repository has no commits yet."],
        )

    latest_commit_date = _git_text(repo_path, ["log", "-1", "--format=%cI"]) or None
    commit_count = _git_int(
        repo_path,
        ["rev-list", "--count", f"--since={since_arg}", "HEAD"],
        warnings,
        "Could not count recent commits.",
    )

    contributors = _contributors(repo_path, since_arg, warnings)
    tags = _latest_tags(repo_path, warnings)

    return GitMetrics(
        repository=str(repo_path),
        branch=branch,
        head=head,
        since_days=since_days,
        commit_count=commit_count,
        contributor_count=len(contributors),
        top_contributors=contributors[:10],
        latest_tags=tags,
        latest_commit_date=latest_commit_date,
        status="ok",
        warnings=warnings,
    )


def contributor_to_dict(contributor: Contributor) -> dict[str, Any]:
    return {
        "name": contributor.name,
        "email": contributor.email,
        "commits": contributor.commits,
    }


def _run_git(repo: Path, args: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", "-C", str(repo), *args],
        capture_output=True,
        check=False,
        text=True,
    )


def _is_git_repo(repo: Path) -> bool:
    result = _run_git(repo, ["rev-parse", "--is-inside-work-tree"])
    return result.returncode == 0 and result.stdout.strip() == "true"


def _git_text(repo: Path, args: list[str]) -> str:
    result = _run_git(repo, args)
    if result.returncode != 0:
        return ""
    return result.stdout.strip()


def _git_int(repo: Path, args: list[str], warnings: list[str], message: str) -> int:
    text = _git_text(repo, args)
    if not text:
        return 0
    try:
        return int(text)
    except ValueError:
        warnings.append(message)
        return 0


def _contributors(repo: Path, since_arg: str, warnings: list[str]) -> list[Contributor]:
    result = _run_git(repo, ["shortlog", "-sne", f"--since={since_arg}", "HEAD"])
    if result.returncode != 0:
        warnings.append("Could not read contributor summary.")
        return []

    contributors: list[Contributor] = []
    for line in result.stdout.splitlines():
        contributor = _parse_shortlog_line(line)
        if contributor is not None:
            contributors.append(contributor)
    return contributors


def _parse_shortlog_line(line: str) -> Contributor | None:
    match = re.match(r"^\s*(\d+)\s+(.+?)(?:\s+<([^>]+)>)?\s*$", line)
    if not match:
        return None
    commits = int(match.group(1))
    name = match.group(2).strip()
    email = match.group(3).strip() if match.group(3) else None
    return Contributor(name=name, email=email, commits=commits)


def _latest_tags(repo: Path, warnings: list[str], limit: int = 5) -> list[str]:
    result = _run_git(repo, ["tag", "--sort=-creatordate", "--merged", "HEAD"])
    if result.returncode != 0:
        warnings.append("Could not read tags.")
        return []
    return [tag for tag in result.stdout.splitlines() if tag.strip()][:limit]
