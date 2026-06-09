# Codex for Open Source Strategy

This document is a practical plan for growing `oss-impact-report` into a real
open source project that could eventually support a truthful Codex for Open
Source application.

Official references:

- https://openai.com/form/codex-for-oss/
- https://developers.openai.com/codex/codex-for-oss-terms

## Important Reality Check

The official program is aimed at maintainers of important open source projects.
Starting a new repository today does not automatically make it eligible. The
project needs real usefulness, public adoption, active maintenance, and honest
evidence that you are a maintainer.

Do not buy stars, fabricate downloads, invent users, or claim maintainer status
you do not have.

## Positioning

`oss-impact-report` helps maintainers create truthful, reproducible evidence
packs. That is useful beyond a single program:

- Maintainers can summarize project health for sponsors.
- Companies can review open source dependencies before adoption.
- Project leads can prepare handoffs and governance updates.
- Communities can publish transparent maintenance reports.

## 90-Day Plan

### Days 1-14: Ship A Useful Base

- Publish the repository with MIT license, README, tests, and CI.
- Create the first GitHub release.
- Add screenshots or sample output from 3 real repositories.
- Open 5 labeled starter issues.
- Ask 3 maintainers to review the output and report gaps.

### Days 15-45: Add Adoption Hooks

- Add a GitHub Action that commits or uploads `impact-report.md`.
- Add optional GitHub API metrics for stars, forks, issues, and PRs.
- Add PyPI packaging and installation docs.
- Write two short posts showing how maintainers use the report.
- Invite outside issues and small PRs.

### Days 46-90: Prove Maintenance

- Ship at least 3 tagged releases with changelogs.
- Keep issue response time visible and polite.
- Add registry adapters for PyPI and npm.
- Document privacy boundaries for network-backed metrics.
- Collect public examples from early users.

## Evidence To Track

- Repository URL and maintainer permissions.
- Commit history and release tags.
- Issue triage and merged pull requests.
- Stars, forks, watchers, and outside contributors.
- Package downloads after publishing.
- Public examples, mentions, or dependent workflows.
- Security policy and responsible disclosure process.

## Application Draft Inputs

When the project has real traction, prepare answers around:

- What problem the project solves and who uses it.
- Why the project matters to the open source ecosystem.
- Your concrete maintainer responsibilities.
- How ChatGPT Pro or Codex would help maintenance work.
- Links proving adoption, releases, and community usage.
