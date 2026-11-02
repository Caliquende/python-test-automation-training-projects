# Python Test Automation Training Projects

Structured QA automation practice repository for API, Selenium UI, Playwright UI, and exported Newman examples.

This repository is intended for learning and portfolio practice, not as a production-scale test framework.

## Documentation

* [API overview](api/README.md)
* [API Pytest suite](api/pytest/README.md)
* [Newman collection](api/newman/README.md)
* [UI overview](ui/README.md)
* [Selenium Pytest suite](ui/selenium_pytest/README.md)
* [Playwright Pytest suite](ui/playwright_pytest/README.md)
* [TodoMVC Playwright project](ui/playwright_pytest/todo_mvc/README.md)
* [SauceDemo Playwright project](ui/playwright_pytest/sauce_demo/README.md)

## Structure

```text
api/
  pytest/
    clients/
    config/
    data/
    tests/
    conftest.py
    README.md
  newman/
    collection/
    environment/
    README.md
ui/
  selenium_pytest/
    config/
    data/
    pages/
    tests/
    conftest.py
    README.md
  playwright_pytest/
    todo_mvc/
    sauce_demo/
    README.md
reports/
  .gitkeep
test-results/
  .gitkeep
.github/
  workflows/
    codeql.yml
    newman-ci.yml
    test-automation.yml
pytest.ini
requirements.txt
```

## Active Practice Areas

* API automation with Python, Pytest, and Requests under `api/pytest/`
* API collection execution with exported Postman files and Newman under `api/newman/`
* UI automation with Selenium and Pytest under `ui/selenium_pytest/`
* UI automation with Playwright Python and Pytest under `ui/playwright_pytest/`

## Local Setup

Install Python dependencies:

```powershell
python -m pip install -r requirements.txt
```

Install Chromium for the Playwright suite:

```powershell
python -m playwright install chromium
```

Create a local environment file for environment-backed API and UI test data:

```powershell
Copy-Item .env.example .env
```

The real `.env` file is ignored by Git.

## Run Tests

Run all Pytest tests from the repository root:

```powershell
pytest
```

Run API Pytest tests:

```powershell
pytest api/pytest/tests
```

Run Selenium UI tests:

```powershell
pytest ui/selenium_pytest/tests
```

Run TodoMVC Playwright tests:

```powershell
pytest ui/playwright_pytest/todo_mvc/tests
```

Run SauceDemo Playwright tests:

```powershell
pytest ui/playwright_pytest/sauce_demo/tests
```

Run the full Playwright suite:

```powershell
pytest ui/playwright_pytest
```

Run Playwright tests headed:

```powershell
pytest ui/playwright_pytest --headed
```

## Markers

The root `pytest.ini` defines:

* `smoke`
* `regression`

Examples:

```powershell
pytest -m smoke
pytest -m regression
```

## Newman Collection

The Newman assets are under `api/newman/`.

Run them from the repository root when Newman is installed:

```powershell
newman run ".\api\newman\collection\collection.json" -e ".\api\newman\environment\environment.json"
```

## GitHub Actions

[![Test Automation](https://github.com/Caliquende/python-test-automation-training-projects/actions/workflows/test-automation.yml/badge.svg?branch=main)](https://github.com/Caliquende/python-test-automation-training-projects/actions/workflows/test-automation.yml)
[![Newman API Tests](https://github.com/Caliquende/python-test-automation-training-projects/actions/workflows/newman-ci.yml/badge.svg?branch=main)](https://github.com/Caliquende/python-test-automation-training-projects/actions/workflows/newman-ci.yml)
[![CodeQL Analysis](https://github.com/Caliquende/python-test-automation-training-projects/actions/workflows/codeql.yml/badge.svg?branch=main)](https://github.com/Caliquende/python-test-automation-training-projects/actions/workflows/codeql.yml)

The badges show the latest workflow status on `main`; open a run to inspect its jobs and commit. Example runs for the 28 October 2026 merge: [Test Automation](https://github.com/Caliquende/python-test-automation-training-projects/actions/runs/40674984557), [Newman](https://github.com/Caliquende/python-test-automation-training-projects/actions/runs/40674984563), and [CodeQL](https://github.com/Caliquende/python-test-automation-training-projects/actions/runs/40674984614).

The repository uses the following workflows:

* `.github/workflows/test-automation.yml`

  * API Pytest tests
  * Selenium Pytest UI tests
  * Playwright Pytest UI tests
  * Python security scans
* `.github/workflows/newman-ci.yml`

  * Exported Postman collection execution with Newman
* `.github/workflows/codeql.yml`

  * GitHub CodeQL analysis for Python

The Playwright CI job installs Python dependencies, installs Chromium with its required Linux dependencies, and runs the TodoMVC and SauceDemo Playwright suites headlessly.

It generates a JUnit XML test result and retains Playwright trace and screenshot evidence only for failed tests.

Detailed Playwright CI and artifact documentation is available in:

```text
ui/playwright_pytest/README.md
```

## Reports and Failure Evidence

To inspect CI results, open a completed run from its workflow page or the examples above, then download an artifact from the run's **Artifacts** section. Downloading requires a GitHub account signed in with read access. Artifacts expire; availability depends on the repository's retention settings. The Playwright artifacts have a 14-day retention period.

| Artifact | Contents |
| --- | --- |
| `api-test-artifacts` | API JUnit XML and any API failure evidence |
| `ui-test-artifacts` | Selenium JUnit XML and any UI failure evidence |
| `playwright-ui-test-artifacts` | Playwright JUnit XML |
| `playwright-failure-artifacts-ubuntu-chromium` | Playwright traces and screenshots when generated on failure |
| `newman-reports` | Newman HTML and JUnit XML |
| `security-reports` | Bandit and pip-audit JSON reports |

Failure-only artifacts can be absent from a successful run. Upload steps run even on failure, but an artifact can still be absent if no matching file was produced. The security scan is **informational**: Bandit and pip-audit exit codes are suppressed, so a green job does not establish that there are no vulnerabilities or scan errors. Inspect `security-reports` for findings.

Generated output paths include:

```text
reports/api-junit.xml
reports/ui-junit.xml
reports/playwright-ui-junit.xml
reports/newman-report.html
reports/newman-report.xml
reports/api/http-exchanges/
reports/ui/screenshots/
reports/ui/browser-console/
test-results/playwright/
```

JUnit XML files contain structured test results.

Playwright traces and screenshots contain failure-debugging evidence.

Only the placeholder files under `reports/` and `test-results/` should be committed. Generated reports and browser artifacts are ignored by Git.

## Notes

The tests use public demo applications and APIs.

Failures can be caused by external service changes, network issues, browser startup problems, missing environment values, or actual test and application defects.