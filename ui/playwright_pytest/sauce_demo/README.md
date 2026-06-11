# SauceDemo Playwright Pytest

This project contains Playwright Python + Pytest coverage for the SauceDemo user flows already present in the Selenium suite.

Back to the parent Playwright README: [../README.md](../README.md).

## Application URL

```text
https://www.saucedemo.com/
```

## Ported Selenium Scenarios

The Playwright suite covers the SauceDemo scenarios found in `ui/selenium_pytest/tests/test_mini_project_core.py`:

- standard user login and product list visibility
- opening the cart after login
- adding the Sauce Labs Backpack to the cart and verifying it in the cart
- adding two products and verifying the cart badge
- removing an item from the cart
- proceeding to checkout with one item
- proceeding to checkout with two items

No extra SauceDemo scenarios are added beyond the current Selenium coverage.

## Structure

```text
ui/playwright_pytest/sauce_demo/
  pages/
    __init__.py
    login_page.py
    inventory_page.py
    cart_page.py
  config/
    __init__.py
    settings.py
  data/
    __init__.py
    products.py
    ui_texts.py
    users.py
  tests/
    __init__.py
    test_sauce_demo_core.py
  conftest.py
  README.md
```

## Page Object Responsibilities

`LoginPage` owns login URL, login form locators, and the `login_with(username, password)` action.

`InventoryPage` owns the inventory title, product list, cart link, cart badge, product-specific add/remove button locators, and cart navigation.

`CartPage` owns cart items, product-specific cart item locators, remove buttons, and checkout navigation.

Page objects do not contain assertions. Expected results are visible in the test file.

## Config and Test Data

`config/settings.py` stores the SauceDemo base URL.

`data/products.py` stores product names, expected product count, and cart badge text values.

`data/ui_texts.py` stores expected page titles.

`data/users.py` reads the standard SauceDemo credentials from the local environment.

## Fixtures

`conftest.py` provides:

- `login_page`
- `inventory_page`
- `cart_page`
- `standard_user_credentials`

The page object fixtures wrap pytest-playwright's `page` fixture. The credentials fixture reads `SAUCEDEMO_STANDARD_USERNAME` and `SAUCEDEMO_STANDARD_PASSWORD` from the local environment through `env_loader.py`.

Fixtures do not perform automatic login. Each test shows:

```python
login_page.open()
login_page.login_with(username, password)
```

through the shared helper in the test file.

## Locator Choices

The tests prefer user-facing Playwright locators where they fit. SauceDemo exposes stable `data-test` attributes for several controls, so the page objects use explicit CSS locators such as:

```python
page.locator("[data-test='username']")
```

Product-specific controls are resolved from the product card text and then use role-based button locators.

## Setup

Install Python dependencies from the repository root:

```powershell
pip install -r requirements.txt
```

Install Playwright browsers when needed:

```powershell
playwright install
```

Create a local `.env` file when SauceDemo credentials are not already available in the environment:

```powershell
Copy-Item .env.example .env
```

## Run From Repository Root

Run only SauceDemo Playwright tests:

```powershell
pytest ui/playwright_pytest/sauce_demo/tests
```

Run the SauceDemo test file:

```powershell
pytest ui/playwright_pytest/sauce_demo/tests/test_sauce_demo_core.py
```

Run headed:

```powershell
pytest ui/playwright_pytest/sauce_demo/tests --headed
```

Run smoke tests:

```powershell
pytest ui/playwright_pytest/sauce_demo/tests -m smoke
```

Run regression tests:

```powershell
pytest ui/playwright_pytest/sauce_demo/tests -m regression
```

Run the full repository Pytest suite:

```powershell
pytest
```

## Selenium POM vs Playwright POM

The Selenium implementation uses a shared `BasePage`, explicit waits, and WebDriver helper methods.

The Playwright implementation uses direct Playwright locators, built-in actionability checks, auto-waiting, and retrying `expect` assertions. It does not use `BasePage`, sleep calls, or explicit wait wrappers.
