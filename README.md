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

CI uses Python 3.11. Install Python 3.11 and the project dependencies from the repository root:

```powershell
python -m pip install -r requirements.txt
```

Direct Python packages are pinned in `requirements.txt`; transitive dependencies are not locked, so a future installation may resolve different transitive versions. CI uses Ubuntu 24.04 for all three workflows, Python 3.11 for Pytest, and Node.js 20 for Newman.

Install Chromium for the Playwright suite:

```powershell
python -m playwright install chromium
```

The Selenium suite uses Chrome separately from Playwright's Chromium installation. Install Chrome or Chrome for Testing; Selenium Manager can discover or download a compatible ChromeDriver when needed. Driver discovery and downloads may require network access. See the [Selenium Manager documentation](https://www.selenium.dev/documentation/selenium_manager/).

Create a local environment file for environment-backed API and UI test data if one does not already exist:

```powershell
Copy-Item .env.example .env
```

Then fill in the values below in `.env` or provide them as environment variables. Existing environment variables take precedence over `.env` values. The `.env` file is ignored by Git; do not commit credentials.

| Suite | Required variables | How to choose values |
| --- | --- | --- |
| Selenium and SauceDemo Playwright | `SAUCEDEMO_STANDARD_USERNAME`, `SAUCEDEMO_STANDARD_PASSWORD` | Use the standard-user credentials displayed on the [SauceDemo login page](https://www.saucedemo.com/). |
| API Pytest: JSONPlaceholder | `JSONPLACEHOLDER_USER_ID` | Integer user ID; `1` is used in the [JSONPlaceholder examples](https://jsonplaceholder.typicode.com/). This is read during test collection. |
| API Pytest: DummyJSON | `DUMMYJSON_USERNAME`, `DUMMYJSON_PASSWORD`, `DUMMYJSON_EXPECTED_USERNAME`, `DUMMYJSON_WRONG_ACCESS_TOKEN` | Use a demo username and password from [DummyJSON's authentication documentation](https://dummyjson.com/docs/auth); set the expected username to the same username and the wrong token to a non-empty invalid token for the negative test. |

The TodoMVC Playwright tests and Newman collection do not require these `.env` values. A full `pytest` run collects the JSONPlaceholder module, so it needs `JSONPLACEHOLDER_USER_ID` even when running only another suite through a marker filter. The tests access public demo services and need network access.

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

The badges show the latest workflow status on `main`; open a run to inspect its jobs and commit. For a historical example, see the [2 November 2026 CI evidence snapshot](docs/ci-evidence.md) and its linked original runs. The snapshot is not a live status report.

CodeQL results are available under **Security > Code scanning**. A successful analysis means the job completed; check alerts separately before drawing conclusions about findings.

### Running CI in your own repository

Configure repository Actions secrets before running the Pytest jobs. API Tests requires `JSONPLACEHOLDER_USER_ID`, `DUMMYJSON_USERNAME`, `DUMMYJSON_PASSWORD`, `DUMMYJSON_EXPECTED_USERNAME`, and `DUMMYJSON_WRONG_ACCESS_TOKEN`. Selenium and Playwright require `SAUCEDEMO_STANDARD_USERNAME` and `SAUCEDEMO_STANDARD_PASSWORD`. The jobs validate these settings and fail before testing if any are absent. GitHub may not provide repository secrets to workflows triggered by forked pull requests; see [GitHub's secrets documentation](https://docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/use-secrets). Newman needs no repository secrets. Use demo data only and never commit secret values.

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
