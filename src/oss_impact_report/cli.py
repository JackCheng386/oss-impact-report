from __future__ import annotations

import argparse
from pathlib import Path
import sys

from .git_metrics import collect_git_metrics
from .report import render_json, render_markdown


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="oss-impact-report",
        description="Generate local-first open source impact reports.",
    )
    parser.add_argument(
        "--repo",
        default=".",
        help="Path to the Git repository to inspect. Defaults to current directory.",
    )
    parser.add_argument(
        "--since-days",
        type=int,
        default=90,
        help="Activity window in days. Defaults to 90.",
    )
    parser.add_argument(
        "--format",
        choices=["markdown", "json"],
        default="markdown",
        help="Output format. Defaults to markdown.",
    )
    parser.add_argument(
        "--output",
        help="Optional file path. Prints to stdout when omitted.",
    )
    parser.add_argument(
        "--project-name",
        help="Optional display name for Markdown output.",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    try:
        metrics = collect_git_metrics(args.repo, since_days=args.since_days)
    except ValueError as exc:
        parser.error(str(exc))

    if args.format == "json":
        output = render_json(metrics)
    else:
        output = render_markdown(metrics, project_name=args.project_name)

    if args.output:
        Path(args.output).write_text(output, encoding="utf-8")
    else:
        sys.stdout.write(output)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
