from __future__ import annotations

from dataclasses import asdict
import json
from typing import Any

from .git_metrics import GitMetrics, contributor_to_dict


def metrics_to_dict(metrics: GitMetrics) -> dict[str, Any]:
    data = asdict(metrics)
    data["top_contributors"] = [
        contributor_to_dict(contributor) for contributor in metrics.top_contributors
    ]
    return data


def render_json(metrics: GitMetrics) -> str:
    return json.dumps(metrics_to_dict(metrics), indent=2, sort_keys=True) + "\n"


def render_markdown(metrics: GitMetrics, project_name: str | None = None) -> str:
    title = project_name or _project_name(metrics.repository)
    lines = [
        f"# {title} Open Source Impact Report",
        "",
        "## Summary",
        "",
        "| Signal | Value |",
        "| --- | --- |",
        f"| Repository | `{metrics.repository}` |",
        f"| Status | `{metrics.status}` |",
        f"| Branch | `{metrics.branch or 'unknown'}` |",
        f"| HEAD | `{metrics.head or 'unknown'}` |",
        f"| Activity window | {metrics.since_days} days |",
        f"| Commits in window | {metrics.commit_count} |",
        f"| Contributors in window | {metrics.contributor_count} |",
        f"| Latest commit | {metrics.latest_commit_date or 'unknown'} |",
        "",
    ]

    lines.extend(_render_contributors(metrics))
    lines.extend(_render_tags(metrics))
    lines.extend(_render_notes(metrics))
    lines.extend(_render_warnings(metrics))

    return "\n".join(lines).rstrip() + "\n"


def _render_contributors(metrics: GitMetrics) -> list[str]:
    lines = ["## Recent Contributors", ""]
    if not metrics.top_contributors:
        return lines + ["No contributors found in the selected window.", ""]

    lines.extend(["| Contributor | Commits |", "| --- | ---: |"])
    for contributor in metrics.top_contributors:
        display = contributor.name
        if contributor.email:
            display = f"{display} <{contributor.email}>"
        lines.append(f"| {display} | {contributor.commits} |")
    lines.append("")
    return lines


def _render_tags(metrics: GitMetrics) -> list[str]:
    lines = ["## Release Signals", ""]
    if not metrics.latest_tags:
        return lines + ["No tags found on the current branch.", ""]

    lines.extend(f"- `{tag}`" for tag in metrics.latest_tags)
    lines.append("")
    return lines


def _render_notes(metrics: GitMetrics) -> list[str]:
    notes = ["## Maintenance Notes", ""]

    if metrics.status == "empty_repository":
        notes.append("- Create an initial commit before collecting activity metrics.")
    elif metrics.status != "ok":
        notes.append("- Collect metrics from a valid Git repository.")
    elif metrics.commit_count >= 20:
        notes.append("- Activity is strong for the selected window.")
    elif metrics.commit_count >= 5:
        notes.append("- Activity is visible; keep shipping small improvements.")
    else:
        notes.append("- Activity is quiet; publish a roadmap and resume regular commits.")

    if metrics.contributor_count >= 4:
        notes.append("- Contributor breadth is healthy for a small or medium project.")
    elif metrics.contributor_count >= 2:
        notes.append("- Contributor breadth is emerging; document starter issues clearly.")
    else:
        notes.append("- Contributor breadth is narrow; invite review and outside issues.")

    if metrics.latest_tags:
        notes.append("- Recent tags are available; keep release notes easy to find.")
    else:
        notes.append("- No tags were found; create versioned releases for users.")

    notes.append("")
    return notes


def _render_warnings(metrics: GitMetrics) -> list[str]:
    if not metrics.warnings:
        return []
    lines = ["## Warnings", ""]
    lines.extend(f"- {warning}" for warning in metrics.warnings)
    lines.append("")
    return lines


def _project_name(repository: str) -> str:
    cleaned = repository.rstrip("/\\")
    if not cleaned:
        return "Project"
    return cleaned.replace("\\", "/").split("/")[-1] or "Project"
