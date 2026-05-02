# Security Policy

## Supported Versions

| Version | Supported |
| ------- | --------- |
| latest  | yes       |

This is a training repository. Security fixes are handled against the current default branch.

## Reporting a Vulnerability

Do not open a public GitHub issue for security vulnerabilities.

Report privately through GitHub Security Advisories:

```text
https://github.com/Caliquende/python-test-automation-training-projects/security/advisories/new
```

Include:

- affected file, workflow, dependency, or test path
- steps to reproduce
- expected and actual impact
- any logs or proof of concept needed to verify the issue

The target acknowledgement time is 48 hours.

## Secret Handling

- Do not commit `.env` or any other real environment file.
- Use `.env.example` only for variable names and empty example values.
- Configure CI credentials as GitHub Actions secrets.
- Required CI secrets are validated before the API and UI jobs run.
- API failure diagnostics redact sensitive fields before writing request/response logs.

Required secret names:

- `SAUCEDEMO_STANDARD_USERNAME`
- `SAUCEDEMO_STANDARD_PASSWORD`
- `JSONPLACEHOLDER_USER_ID`
- `DUMMYJSON_USERNAME`
- `DUMMYJSON_PASSWORD`
- `DUMMYJSON_EXPECTED_USERNAME`
- `DUMMYJSON_WRONG_ACCESS_TOKEN`

## Current Security Controls

- Dependabot checks pip and GitHub Actions dependencies weekly.
- CodeQL runs for Python on push, pull request, and a weekly schedule.
- Bandit runs in the CI security scan job and uploads a JSON report.
- pip-audit runs in the CI security scan job and uploads a JSON report.
- Pre-commit hooks are configured for basic file hygiene, private-key detection, Bandit, and detect-secrets.
- `.gitignore` excludes local secrets, caches, virtual environments, generated reports, screenshots, console logs, request/response logs, and driver folders.

## Important Limitations

- The CI Bandit and pip-audit commands are currently non-blocking because the workflow uses `|| true`; treat their uploaded reports as findings to review, not as a merge gate.
- Local pre-commit checks only run after a developer installs and enables them with `pre-commit install`.
- The current pre-commit configuration references `pyproject.toml` for Bandit and `.secrets.baseline` for detect-secrets. Add those files or adjust `.pre-commit-config.yaml` before treating local pre-commit as a reliable gate.
- This repository tests public demo services, so external service changes can affect test results and generated diagnostics.

## Local Security Checks

Install and enable pre-commit hooks:

```powershell
pip install pre-commit
pre-commit install
```

Run the configured hooks manually:

```powershell
pre-commit run --all-files
```

Run CI-equivalent security scans locally:

```powershell
pip install bandit[toml] pip-audit
bandit -r . -f screen --severity-level medium --confidence-level medium -x ./.venv,./venv,./env,./.pytest_cache
pip-audit
```

## Report Artifacts

Security scan outputs are generated under `reports/` and should not be committed:

```text
reports/bandit-report.json
reports/pip-audit-report.json
```
