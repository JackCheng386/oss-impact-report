# GitHub Action

The repository includes an `Impact Report` workflow that can generate project
health reports on demand or every Monday.

## Run The Workflow

1. Open the repository on GitHub.
2. Go to **Actions**.
3. Select **Impact Report**.
4. Choose **Run workflow**.

The workflow uploads an artifact named `impact-report` with:

- `impact-report.md`
- `impact-report.json`

## Use In Another Repository

Copy `.github/workflows/impact-report.yml` into another Python project that can
install `oss-impact-report`, then adjust the command as needed:

```yaml
- run: python -m pip install git+https://github.com/JackCheng386/oss-impact-report.git
- run: oss-impact-report --repo . --format markdown --output reports/impact-report.md
```

For private repositories, review the report before publishing it. Local Git
history can contain names and email addresses from commit metadata.
