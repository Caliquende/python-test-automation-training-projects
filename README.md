# Python Test Automation Training Projects

Structured QA automation practice repository for API, Selenium UI, Playwright UI, and exported Newman examples.

This repository is intended for learning and portfolio practice, not as a production-scale test framework.

## Documentation

- [API overview](api/README.md)
- [API Pytest suite](api/pytest/README.md)
- [UI overview](ui/README.md)
- [Selenium Pytest suite](ui/selenium_pytest/README.md)
- [Playwright Pytest suite](ui/playwright_pytest/README.md)
- [TodoMVC Playwright project](ui/playwright_pytest/todo_mvc/README.md)
- [SauceDemo Playwright project](ui/playwright_pytest/sauce_demo/README.md)

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
pytest.ini
requirements.txt
```

## Active Practice Areas

- API automation with Python, Pytest, and Requests under `api/pytest/`
- API collection execution with exported Postman files and Newman under `api/newman/`
- UI automation with Selenium and Pytest under `ui/selenium_pytest/`
- UI automation with Playwright Python and Pytest under `ui/playwright_pytest/`

## Local Setup

Install Python dependencies:

```powershell
pip install -r requirements.txt
```

Install Playwright browsers when needed:

```powershell
playwright install
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

Run Playwright UI tests:

```powershell
pytest ui/playwright_pytest
```

Run Playwright tests headed:

```powershell
pytest ui/playwright_pytest --headed
```

## Markers

The root `pytest.ini` defines:

- `smoke`
- `regression`

Examples:

```powershell
pytest -m smoke
pytest -m regression
```

## Newman Collection

The Newman assets are under `api/newman/`. Run them from the repository root when Newman is installed:

```powershell
newman run ".\api\newman\collection\collection.json" -e ".\api\newman\environment\environment.json"
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

The tests use public demo applications and APIs. Failures can be caused by external service changes, network issues, browser startup problems, or missing local environment values.
