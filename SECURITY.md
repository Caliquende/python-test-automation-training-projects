# Security Policy

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| latest  | :white_check_mark: |

## Reporting a Vulnerability

1. **DO NOT** open a public GitHub issue for security vulnerabilities.
2. Report via [GitHub Security Advisory](https://github.com/Caliquende/python-test-automation-training-projects/security/advisories/new).
3. Include a detailed description, steps to reproduce, and any potential impact.
4. We will acknowledge your report within 48 hours.

## Security Measures

- **Dependabot:** Monitors pip and GitHub Actions dependencies for known vulnerabilities.
- **CodeQL:** Static analysis scans Python code for security patterns on every push/PR.
- **Bandit:** SAST tool scans for common Python security issues in CI.
- **pip-audit:** Checks installed packages against CVE databases.
- **Pre-commit Hooks:** detect-secrets, detect-private-key, and Bandit run before every commit.
- **Environment Variables:** `.env` files are gitignored. Never commit credentials.
