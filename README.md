# Python Test Automation Training Projects

Structured junior-level QA automation practice repository.

This repository contains small API, UI, and Postman/Newman automation examples. It is intended for learning and portfolio practice, not as a production-scale test framework.

## Structure

```text
api/
  pytest/
    clients/
    config/
    data/
    tests/
    conftest.py
    pytest.ini
    README.md
  newman/
    collection/
      collection.json
    environment/
      environment.json
    README.md
ui/
  selenium_pytest/
    config/
    data/
    pages/
    tests/
    conftest.py
    pytest.ini
    README.md
  playwright_pytest/
    README.md
    .gitkeep
reports/
  .gitkeep
.github/workflows/
```

## Active Practice Areas

* API automation with Python, Pytest, and Requests under `api/pytest/`.
* API collection execution with exported Postman files and Newman under `api/newman/`.
* UI automation with Selenium and Pytest under `ui/selenium_pytest/`.
* Future Playwright/Pytest placeholder under `ui/playwright_pytest/`.

## Local Setup

Install Python dependencies:

```powershell
pip install -r requirements.txt
```

Create a local environment file if you want to run the Python API/UI suites with local values:

```powershell
Copy-Item .env.example .env
```

The real `.env` file is ignored by Git.

## Run API Pytest Suite

```powershell
pytest api/pytest -v
```

JUnit report:

```powershell
pytest api/pytest -v --junitxml=reports/api-junit.xml
```

## Run Selenium Pytest UI Suite

```powershell
pytest ui/selenium_pytest -v
```

JUnit report:

```powershell
pytest ui/selenium_pytest -v --junitxml=reports/ui-junit.xml
```

Set `HEADLESS=true` for headless UI execution.

## Run Newman Collection

CLI only:

```powershell
newman run ".\api\newman\collection\collection.json" -e ".\api\newman\environment\environment.json"
```

CLI, HTML, and JUnit XML:

```powershell
newman run ".\api\newman\collection\collection.json" -e ".\api\newman\environment\environment.json" -r "cli,html,junit" --reporter-html-export ".\reports\newman-report.html" --reporter-junit-export ".\reports\newman-report.xml"
```

Generated reports are written under `reports/` and should not be committed.

## GitHub Actions

Current workflows:

* `Test Automation`: runs API Tests, UI Tests, and Security Scan jobs.
* `Newman API Tests`: runs the exported Postman collection with Newman.
* `CodeQL`: runs GitHub code scanning for Python.

The API workflow command is:

```bash
pytest api/pytest -v --junitxml=reports/api-junit.xml
```

The UI workflow command is:

```bash
pytest ui/selenium_pytest -v --junitxml=reports/ui-junit.xml
```

The Newman workflow uses:

```bash
api/newman/collection/collection.json
api/newman/environment/environment.json
```

## Reports

Generated report paths include:

```text
reports/api-junit.xml
reports/ui-junit.xml
reports/newman-report.html
reports/newman-report.xml
reports/api/http-exchanges/
reports/ui/screenshots/
reports/ui/browser-console/
```

Only `reports/.gitkeep` should be committed.

## Notes

The tests use public demo applications and APIs, so failures can be caused by external service changes, network issues, or missing local environment values.
