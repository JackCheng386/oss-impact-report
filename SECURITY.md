# Security Policy

## Supported Versions

`oss-impact-report` is currently pre-1.0. Security fixes will target the latest
released version.

## Reporting A Vulnerability

Please do not open a public issue for sensitive security reports. Use GitHub
private vulnerability reporting when available, or contact the maintainers using
the repository's listed maintainer channel.

## Data Handling

The CLI is local-first. It does not make network calls in the initial release.
Future network-backed adapters must be opt-in, documented, and covered by tests.
