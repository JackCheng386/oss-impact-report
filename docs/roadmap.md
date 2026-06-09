# Roadmap

`oss-impact-report` is focused on helping maintainers publish clear, repeatable
project health summaries.

## 0.2.0

- Add a GitHub Action for scheduled report generation.
- Add example reports from public repositories.
- Improve empty-repository and detached-HEAD handling.
- Document recommended report fields for release notes and sponsorship updates.

## 0.3.0

- Add optional GitHub API metrics for stars, forks, issues, and pull requests.
- Support GitHub token configuration through environment variables.
- Add privacy notes for network-backed metrics.
- Export compact summary badges for README files.

## 0.4.0

- Add registry adapters for PyPI and npm package download counts.
- Add dependency health summaries.
- Add report templates for maintainers, teams, and foundations.

## Principles

- Prefer local-first data collection by default.
- Make network-backed metrics explicit and optional.
- Keep reports reproducible and easy to review.
- Avoid vanity metrics when they do not help maintainers make decisions.
