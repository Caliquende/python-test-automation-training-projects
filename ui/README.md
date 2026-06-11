# UI Test Automation

This folder contains browser-based UI automation practice for public demo applications.

The repository currently uses two UI automation approaches:

- [Selenium + Pytest](selenium_pytest/README.md)
- [Playwright Python + Pytest](playwright_pytest/README.md)

## Structure

```text
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
```

## Selenium and Playwright

The Selenium suite uses Chrome WebDriver, explicit waits, and page objects for SauceDemo flows.

The Playwright suite uses pytest-playwright's `page` fixture, Playwright locators, actionability checks, auto-waiting, and `expect` retry assertions. It does not use a shared `BasePage`.

## Run UI Tests

Run all UI tests from the repository root:

```powershell
pytest ui
```

Run only Selenium UI tests:

```powershell
pytest ui/selenium_pytest/tests
```

Run only Playwright UI tests:

```powershell
pytest ui/playwright_pytest
```

Run smoke UI tests:

```powershell
pytest ui -m smoke
```

Run regression UI tests:

```powershell
pytest ui -m regression
```

The repository root `pytest.ini` is the global Pytest configuration for UI and API tests. It defines the collected test paths, markers, Python path, and import mode.
