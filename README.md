# Python Test Automation Training Projects

This repository is a compact Python test automation training workspace with two tracks:

1. API automation for public demo APIs using Pytest, Requests, reusable clients, separated config, reusable payloads, markers, JUnit reports, and failure diagnostics.
2. UI automation for SauceDemo using Selenium WebDriver, Pytest, Page Object Model, shared fixtures, separated config, reusable test data, markers, JUnit reports, and failure diagnostics.

The repository is intentionally small. Its purpose is to practice maintainable automation structure, not to provide a production-scale test framework.

## Tech Stack

- Python
- Pytest
- Requests
- Selenium WebDriver
- Page Object Model
- API client layer
- JUnit XML reporting
- GitHub Actions CI
- CodeQL, Bandit, pip-audit, Dependabot, and pre-commit security checks

## Repository Structure

- `api/`
  - `clients/` - API client classes and shared HTTP request logic
  - `config/` - API base URLs and timeout configuration
  - `data/` - reusable API payloads and expected values
  - `tests/` - API test scenarios
  - `pytest.ini` - API-specific Pytest configuration
  - `README.md` - API track documentation

- `ui/`
  - `config/` - UI base URL, timeout, and headless configuration
  - `data/` - test users, expected UI texts, and product data
  - `pages/` - Page Object Model classes and BasePage abstraction
  - `tests/` - UI test scenarios
  - `conftest.py` - shared WebDriver and page object fixtures
  - `pytest.ini` - UI-specific Pytest configuration
  - `README.md` - UI track documentation

- `reports/`
  - local JUnit XML reports and failure artifacts
  - ignored by Git except for `reports/.gitkeep`

- `.github/workflows/`
  - API tests, UI tests, security scan, and CodeQL workflows

- `.github/dependabot.yml`
  - weekly pip and GitHub Actions dependency update checks

- `.pre-commit-config.yaml`
  - local commit-time quality and security hooks

- `.env.example`
  - example environment variables for local test credentials and test values

- `env_loader.py`
  - lightweight root `.env` loader used by config/test data modules

## Covered Areas

### API Automation

The API track covers:

- JSONPlaceholder
- DummyJSON

Main concepts:

- API client layer
- Shared base client
- Config separation
- Reusable payloads and expected values
- Authenticated and unauthenticated requests
- Positive and negative API checks
- Smoke and regression markers
- JUnit XML reports
- Failed request/response logging with sensitive field redaction

Expected current result:

```text
17 passed
```

### UI Automation

The UI track covers SauceDemo browser flows.

Main concepts:

- Selenium WebDriver
- Pytest fixtures
- Page Object Model
- BasePage abstraction
- Config separation
- Reusable users, products, and UI text constants
- Headless browser execution through `HEADLESS=true`
- Explicit waits and UI state validation
- Smoke and regression markers
- JUnit XML reports
- Failure screenshots and browser console logs

Expected current result:

```text
7 passed
```

## Setup

Create and activate a virtual environment:

```powershell
python -m venv .venv
.venv\Scripts\activate
```

Install dependencies:

```powershell
pip install -r requirements.txt
```

Create a local environment file:

```powershell
Copy-Item .env.example .env
```

Then fill the values in `.env`. The real `.env` file is ignored by Git and must not be committed.

Required local and CI values:

- `SAUCEDEMO_STANDARD_USERNAME`
- `SAUCEDEMO_STANDARD_PASSWORD`
- `JSONPLACEHOLDER_USER_ID`
- `DUMMYJSON_USERNAME`
- `DUMMYJSON_PASSWORD`
- `DUMMYJSON_EXPECTED_USERNAME`
- `DUMMYJSON_WRONG_ACCESS_TOKEN`

## Running Tests

Run these commands from the repository root. The repo also contains API/UI-specific `pytest.ini` files, so using the root commands keeps collection behavior predictable.

Run the full suite from the repository root:

```powershell
pytest
```

Run the full API suite:

```powershell
pytest api -v
```

Run API smoke tests:

```powershell
pytest api -m smoke -v
```

Run API regression tests:

```powershell
pytest api -m regression -v
```

Generate the API JUnit XML report:

```powershell
pytest api -v --junitxml=reports/api-junit.xml
```

Run the full UI suite:

```powershell
pytest ui -v
```

Run UI smoke tests:

```powershell
pytest ui -m smoke -v
```

Run UI regression tests:

```powershell
pytest ui -m regression -v
```

Generate the UI JUnit XML report:

```powershell
pytest ui -v --junitxml=reports/ui-junit.xml
```

Run UI tests in headless mode:

```powershell
$env:HEADLESS = "true"
pytest ui -v --junitxml=reports/ui-junit.xml
Remove-Item Env:HEADLESS
```

## Reports and Failure Artifacts

Generated files are written under `reports/` and should not be committed.

API failure diagnostics:

```text
reports/api/http-exchanges/
```

UI failure diagnostics:

```text
reports/ui/screenshots/
reports/ui/browser-console/
```

## Expected Marker Results

API smoke:

```text
5 passed, 12 deselected
```

API regression:

```text
17 passed
```

UI smoke:

```text
2 passed, 5 deselected
```

UI regression:

```text
7 passed
```

## CI

GitHub Actions runs on push and pull request targeting `main` or `master`, and can also be started manually.

Workflow jobs:

- `API Tests`
  - installs Python 3.11 dependencies
  - validates required API secrets
  - runs `pytest api -v --junitxml=reports/api-junit.xml`
  - uploads `api-test-artifacts`

- `UI Tests`
  - installs Python 3.11 dependencies
  - forces `HEADLESS=true`
  - validates required UI secrets
  - runs `pytest ui -v --junitxml=reports/ui-junit.xml`
  - uploads `ui-test-artifacts`

- `Security Scan`
  - installs Bandit and pip-audit
  - writes `reports/bandit-report.json`
  - writes `reports/pip-audit-report.json`
  - uploads `security-reports`
  - current scan commands are report-producing and non-blocking because the workflow uses `|| true`

- `CodeQL Analysis`
  - runs on push, pull request, and a weekly Monday schedule
  - uses the Python `security-extended` query pack
  - uploads findings to GitHub code scanning

Dependabot checks pip and GitHub Actions updates weekly.

## Security

Security guidance and vulnerability reporting are documented in [SECURITY.md](./SECURITY.md).

Current controls:

- `.env` and generated report artifacts are ignored by Git.
- Required secrets are validated in CI before API and UI jobs run.
- API failure logs redact sensitive fields before writing request/response diagnostics.
- CodeQL runs as a separate code scanning workflow.
- Bandit and pip-audit run in the CI security scan job and upload reports.
- Pre-commit hooks are configured for whitespace/YAML checks, large-file checks, private-key detection, Bandit, and detect-secrets.

Local pre-commit hooks are not automatic until installed:

```powershell
pip install pre-commit
pre-commit install
```

## Validation Notes

- API tests depend on public demo APIs. External outages or response changes can fail otherwise correct tests.
- UI tests depend on the live SauceDemo site and a local/CI Chrome installation.
- Selenium Manager is expected to handle ChromeDriver for recent Selenium versions.
- Real environment files such as `.env` must not be committed.
- Generated reports, screenshots, logs, caches, and browser driver folders should not be committed.
- When changing tests, clients, fixtures, or config, run the affected marker group and the full affected suite.

## Project Status

This is a beginner-friendly but structured test automation training repository.

It demonstrates:

- Layered test structure
- Page Object Model
- API client abstraction
- Shared fixtures
- Config separation
- Test data separation
- Marker-based execution
- JUnit reporting
- Failure diagnostics
- GitHub Actions CI
- Basic security scanning and dependency monitoring
