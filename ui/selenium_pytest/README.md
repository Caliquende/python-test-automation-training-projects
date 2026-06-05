# Selenium Pytest UI Automation

SauceDemo UI automation practice using Selenium WebDriver, Pytest, and Page Object Model.

## Location

```text
ui/selenium_pytest/
```

## Structure

```text
config/
data/
pages/
tests/
conftest.py
pytest.ini
README.md
```

## Current Scope

The current UI suite covers basic SauceDemo user journeys:

* standard user login
* product list visibility
* cart navigation
* adding one or more products to cart
* removing a cart item
* opening checkout

## Run From Repository Root

Full UI suite:

```powershell
pytest ui/selenium_pytest -v
```

Smoke UI tests:

```powershell
pytest ui/selenium_pytest -m smoke -v
```

Regression UI tests:

```powershell
pytest ui/selenium_pytest -m regression -v
```

Specific test file:

```powershell
pytest ui/selenium_pytest/tests/test_mini_project_core.py -v
```

JUnit report:

```powershell
pytest ui/selenium_pytest -v --junitxml=reports/ui-junit.xml
```

## Headless Execution

Set this value for headless browser execution:

```powershell
$env:HEADLESS="true"
```

## Failure Artifacts

When a UI test fails, the Pytest hook writes diagnostics under:

```text
reports/ui/screenshots/
reports/ui/browser-console/
```

Generated report files should not be committed.

## Notes

This is a learning-focused Selenium/Pytest suite, not a production-scale framework. Page interactions belong in `pages/`, reusable test values belong in `data/`, and assertions should stay in the test files.
