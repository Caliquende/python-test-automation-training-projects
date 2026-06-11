# Selenium Pytest UI Automation

This package contains SauceDemo UI automation practice using Selenium WebDriver, Pytest, and Page Object Model.

See the Playwright implementation at [../playwright_pytest/README.md](../playwright_pytest/README.md).

## Tested Application

- SauceDemo: `https://www.saucedemo.com/`

## Current Scenarios

The Selenium suite currently covers:

- standard user login and product list visibility
- opening the cart after login
- adding the Sauce Labs Backpack to the cart and verifying it in the cart
- adding two products and verifying the cart badge
- removing an item from the cart
- proceeding to checkout with one item
- proceeding to checkout with two items

## Structure

```text
ui/selenium_pytest/
  config/
    settings.py
  data/
    products.py
    ui_texts.py
    users.py
  pages/
    base_page.py
    login_page.py
    inventory_page.py
    cart_page.py
  tests/
    test_mini_project_core.py
  conftest.py
  pytest.ini
  README.md
```

## Page Object Model

The Selenium page objects inherit from `BasePage`. `BasePage` centralizes WebDriver interaction helpers such as navigation, explicit waits, clicking, typing, text lookup, element counting, and URL checks.

Page-specific locators and actions are split across:

- `LoginPage`
- `InventoryPage`
- `CartPage`

Assertions remain in `tests/test_mini_project_core.py`.

## Fixtures

`conftest.py` provides:

- `driver`
- `login_page`
- `inventory_page`
- `cart_page`

The `driver` fixture creates and quits Chrome WebDriver for each test.

## Wait and Browser Mode

The suite uses Selenium explicit waits through `WebDriverWait` in `BasePage`.

Headless mode is controlled by the `HEADLESS` environment variable. The suite runs headless by default.

```powershell
pytest ui/selenium_pytest/tests
```

To run headed, set `HEADLESS` to `false`:

```powershell
$env:HEADLESS="false"
pytest ui/selenium_pytest/tests
```

When headed mode is enabled, the fixture maximizes the browser window.

## Run From Repository Root

Run the Selenium suite:

```powershell
pytest ui/selenium_pytest/tests
```

Run a specific test file:

```powershell
pytest ui/selenium_pytest/tests/test_mini_project_core.py
```

Run smoke tests:

```powershell
pytest ui/selenium_pytest/tests -m smoke
```

Run regression tests:

```powershell
pytest ui/selenium_pytest/tests -m regression
```

Create a JUnit report:

```powershell
pytest ui/selenium_pytest/tests --junitxml=reports/ui-junit.xml
```

## Failure Artifacts

When a Selenium UI test fails, the Pytest hook writes diagnostics under:

```text
reports/ui/screenshots/
reports/ui/browser-console/
```

Generated report files should not be committed.
