# Contributing

Thanks for helping improve `oss-impact-report`.

## Good First Contributions

- Add tests for edge cases in Git repositories.
- Improve report wording for maintainers.
- Add examples from real projects with permission.
- Build adapters for public package registries.
- Improve documentation for GitHub Actions usage.

## Development

```powershell
python -m pip install -e .
$env:PYTHONPATH="src"
python -m unittest discover -s tests
```

## Pull Request Checklist

- Keep changes small and explain the user problem.
- Add or update tests for behavior changes.
- Update README or docs when user-facing behavior changes.
- Avoid collecting private data by default.
- Make network calls opt-in and documented.

## Project Values

Reports should be truthful, reproducible, and useful. Do not add features that
inflate, fabricate, or obscure project impact.
