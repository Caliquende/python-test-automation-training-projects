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
  README.md
```

The suite uses the [repository-root pytest.ini](../../pytest.ini).

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

The `driver` fixture creates and quits Chrome WebDriver for each test. Install Chrome or Chrome for Testing separately from Playwright's Chromium. If no driver is supplied, [Selenium Manager](https://www.selenium.dev/documentation/selenium_manager/) can discover or download a compatible driver; this can require network access. See the [root setup instructions](../../README.md#local-setup) for SauceDemo test data.

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

When a Selenium test fails during its test call and a driver is available, the Pytest hook attempts to write diagnostics under:

```text
reports/ui/screenshots/
reports/ui/browser-console/
```

Driver setup failures may not produce these diagnostics. Screenshot or console capture can also fail; review artifacts before sharing and use demo credentials only. Generated report files should not be committed.

## CI results

The [Test Automation workflow](../../.github/workflows/test-automation.yml) uploads `ui-test-artifacts`, including `reports/ui-junit.xml` and any generated Selenium failure evidence. Open a completed run in [Actions](https://github.com/Caliquende/python-test-automation-training-projects/actions/workflows/test-automation.yml) and download it from **Artifacts**. See the [root README](../../README.md#reports-and-failure-evidence) for access and retention details.
