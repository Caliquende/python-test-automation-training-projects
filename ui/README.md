# SauceDemo UI Test Automation Project

This sub-project contains automated UI tests for the SauceDemo website using Python, Selenium WebDriver, Pytest, and the Page Object Model pattern.

The goal of this project is not only to write UI tests, but also to practice a maintainable test automation structure with separate layers for configuration, test data, page interactions, fixtures, and test execution strategy.

## Tech Stack

- Python
- Selenium WebDriver
- Pytest
- Page Object Model
- BasePage abstraction
- Pytest markers
- Headless mode through `HEADLESS=true`
- Screenshot capture on failed UI tests
- Browser console logging on failed UI tests
- GitHub Actions CI

## Project Structure

- `config/`
  - `settings.py` — Base URL and timeout configuration

- `data/`
  - `users.py` — Test user data
  - `products.py` — Product-related test data
  - `ui_texts.py` — Expected UI texts and URL parts

- `pages/`
  - `base_page.py` — Shared wait, click, type, text, and navigation helpers
  - `login_page.py` — Login page locators and actions
  - `inventory_page.py` — Inventory page locators and actions
  - `cart_page.py` — Cart page locators and actions

- `tests/`
  - `test_mini_project_core.py` — UI test scenarios

- `conftest.py` — Shared Pytest fixtures
- `pytest.ini` — UI-specific Pytest configuration
- `README.md` — Project documentation

## Covered Flows

The current UI suite covers the following core user journeys:

- Standard user can log in and see the product list
- Logged-in user can open the cart page
- User can add a backpack product to the cart and verify it in the cart
- User can add two products and verify the cart badge count

## Test Architecture Notes

This project uses a small but layered UI test automation structure.

- `tests/` contains test scenarios and assertions
- `pages/` contains UI interaction logic and locators
- `config/` contains environment-level configuration
- `data/` contains reusable test data and expected values
- `conftest.py` contains shared setup fixtures
- `pytest.ini` contains test discovery and marker configuration

The test files should describe user behavior. Locator details, test users, expected UI texts, URL values, and timeout configuration should not be hardcoded directly inside test scenarios.

## Key Design Decisions

### Page Object Model

Page Object classes keep locators and page-specific actions away from test cases. This improves readability and reduces maintenance cost when the UI changes.

### Shared Fixture Setup

The WebDriver setup is stored in `conftest.py` as a shared Pytest fixture. Test functions receive the `driver` fixture automatically instead of creating browser setup logic inside each test.

### Configuration Layer

Base URL and timeout values are stored in `config/settings.py`. This keeps environment-level values separate from page objects and tests.

### Test Data Layer

Reusable test users, expected product values, page titles, URL parts, and badge values are stored under the `data/` folder. This helps keep test scenarios cleaner and easier to maintain.

### Marker-Based Execution

The project uses Pytest markers to separate fast smoke checks from broader regression checks.

## Setup

Install the required dependencies:

```bash
pip install selenium pytest
```

Chrome must be installed on the machine. Recent Selenium versions can handle ChromeDriver automatically through Selenium Manager.

Create a local environment file from the example:

```powershell
Copy-Item .env.example .env
```

Required UI values:

- `SAUCEDEMO_STANDARD_USERNAME`
- `SAUCEDEMO_STANDARD_PASSWORD`

The real `.env` file is ignored by Git. CI must receive these values through GitHub Actions secrets with the same names.

## Running Tests

Run these commands from the repository root. This avoids confusion from the UI-specific `pytest.ini` when invoking pytest from inside `ui/`.

From the repository root, run the UI suite:

```bash
pytest ui -v
```

Run only smoke tests:

```bash
pytest ui -m smoke -v
```

Run regression tests:

```bash
pytest ui -m regression -v
```

Run a specific UI test file:

```bash
pytest ui/tests/test_mini_project_core.py -v
```

Run all tests from the full workspace:

```bash
pytest -v
```

## Failure Artifacts

When a UI test fails, the shared Pytest hook in `conftest.py` writes diagnostic artifacts under:

```text
reports/ui/screenshots/
reports/ui/browser-console/
```

Screenshots help inspect the browser state at the failure point. Browser console logs help diagnose JavaScript or UI runtime problems.

## Pytest Markers

The project uses the following markers:

- `smoke` — Fast critical checks for core functionality
- `regression` — Broader tests used to verify existing behavior after changes

Example:

```bash
pytest ui -m smoke -v
```

## Current Test Cases

- `test_logged_in_user_sees_product_list`
  - Verifies that a standard user can log in and see the product list

- `test_user_can_open_cart_after_login`
  - Verifies that a logged-in user can navigate to the cart page

- `test_user_can_add_backpack_to_cart_and_see_it_in_cart`
  - Verifies that a user can add a backpack product to the cart and see it on the cart page

- `test_adding_two_products_updates_cart_badge_to_two`
  - Verifies that adding two products updates the cart badge count correctly

- `test_user_can_add_backpack_to_cart_and_remove_it_from_cart`
  - Verifies that an item added to the cart can be removed from the cart page

- `test_user_can_add_backpack_to_cart_and_checkout`
  - Verifies that a user can proceed to checkout after adding one item

- `test_user_can_add_two_items_to_cart_and_checkout`
  - Verifies that a user can proceed to checkout with multiple items

## Current Scope

This is a beginner-friendly UI automation project. It is intentionally small, but it already demonstrates important automation architecture concepts:

- Page Object Model
- BasePage abstraction
- Shared Pytest fixtures
- Config separation
- Reusable test data
- Expected value constants
- Marker-based test execution
- Headless browser support through configuration
- GitHub Actions CI

## Future Improvements

Planned improvements:

- Add optional rich HTML or Allure reporting
- Add more negative login scenarios
- Add more cart and checkout flow coverage

## Notes

This project should be treated as a learning-focused automation suite, not as a large-scale production framework. The current goal is to understand clean test automation structure and gradually improve it with maintainable architecture practices.
