# Playwright Python Pytest UI Automation

This folder contains Playwright Python + Pytest UI automation practice.

## Current Projects

- [TodoMVC](todo_mvc/README.md)
- [SauceDemo](sauce_demo/README.md)

## Structure

```text
ui/playwright_pytest/
  todo_mvc/
    pages/
    tests/
    conftest.py
    README.md
  sauce_demo/
    pages/
    tests/
    conftest.py
    README.md
  README.md
```

## Pytest Playwright Fixtures

The tests use the `page` fixture provided by `pytest-playwright`. Project-level `conftest.py` files wrap that page in small page object fixtures such as `todo_page`, `login_page`, `inventory_page`, and `cart_page`.

Fixtures do not hide full user scenarios. Login and other user actions stay visible in the test body.

## Playwright Approach

Playwright locators, actionability checks, auto-waiting, and `expect` retry assertions are used instead of manual sleeps or explicit waits.

The Playwright examples do not use a shared `BasePage`. The current pages are small enough that inheritance would add indirection without removing meaningful duplication.

Compared with the Selenium suite, the Playwright suite keeps page objects focused on user actions and locators while assertions stay in the tests.

## Run From Repository Root

Run all Playwright tests:

```powershell
pytest ui/playwright_pytest
```

Run Playwright tests headed:

```powershell
pytest ui/playwright_pytest --headed
```

Run the full repository Pytest suite:

```powershell
pytest
```
