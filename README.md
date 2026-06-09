# oss-impact-report

Generate practical health reports for open source maintainers.

`oss-impact-report` is a small CLI that reads a local Git repository and turns
maintenance signals into Markdown or JSON. It summarizes activity, contributor
breadth, release cadence, and maintenance gaps so maintainers can prepare
release notes, sponsorship updates, project handoffs, and internal open source
reviews without rebuilding the same report by hand.

## Features

- Local-first Git metrics with no network access required.
- Markdown and JSON output for humans and automation.
- Recent commit and contributor activity over a configurable window.
- Latest tag summary for release cadence evidence.
- Plain maintenance recommendations based on observable project signals.
- Standard-library Python implementation.

## Install From Source

```powershell
git clone https://github.com/JackCheng386/oss-impact-report.git
cd oss-impact-report
python -m pip install -e .
```

## Usage

Generate a Markdown report for the current repository:

```powershell
oss-impact-report --repo . --format markdown
```

Write a JSON report:

```powershell
oss-impact-report --repo . --format json --output impact.json
```

Change the activity window:

```powershell
oss-impact-report --repo . --since-days 180 --project-name "My Project"
```

## Example Output

```markdown
# My Project Open Source Impact Report

| Signal | Value |
| --- | --- |
| Repository | C:\work\my-project |
| Branch | main |
| HEAD | a1b2c3d |
| Activity window | 90 days |
| Commits in window | 42 |
| Contributors in window | 5 |
| Latest commit | 2026-06-07T18:33:21+00:00 |

## Maintenance Notes

- Activity is strong for the selected window.
- Contributor breadth is healthy for a small or medium project.
- Recent tags are available; keep release notes easy to find.
```

## Roadmap

- GitHub API integration for stars, forks, issues, PRs, and dependents.
- Registry adapters for npm, PyPI, crates.io, RubyGems, and Docker Hub.
- GitHub Action that publishes `impact-report.md` on a schedule.
- OpenSSF Scorecard and dependency health summaries.
- Templates for sponsorship pages and project governance docs.

See [`docs/roadmap.md`](docs/roadmap.md) for the current project plan.

## Contributing

Contributions are welcome. Start with
[`CONTRIBUTING.md`](CONTRIBUTING.md), then open an issue describing the use case
you want this project to support.

## License

MIT. See [`LICENSE`](LICENSE).
