# SauceDemo UI Test Automation Project

This sub-project contains automated UI tests for the SauceDemo website using Python, Selenium WebDriver, Pytest, and the Page Object Model pattern.

The goal of this project is not only to write UI tests, but also to practice a maintainable test automation structure with separate layers for configuration, test data, page interactions, fixtures, and test execution strategy.

## Tech Stack

- Python
- Selenium WebDriver
- Pytest
- Page Object Model
- Pytest markers

## Project Structure

- `config/`
  - `settings.py` — Base URL and timeout configuration

- `data/`
  - `users.py` — Test user data
  - `products.py` — Product-related test data
  - `ui_texts.py` — Expected UI texts and URL parts

- `pages/`
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

## Running Tests

From the repository root, run the UI suite:

```bash
pytest projects/ui -v
```

Run only smoke tests:

```bash
pytest projects/ui -m smoke -v
```

Run regression tests:

```bash
pytest projects/ui -m regression -v
```

Run a specific UI test file:

```bash
pytest projects/ui/tests/test_mini_project_core.py -v
```

Run all tests from the full workspace:

```bash
pytest -v
```

## Pytest Markers

The project uses the following markers:

- `smoke` — Fast critical checks for core functionality
- `regression` — Broader tests used to verify existing behavior after changes

Example:

```bash
pytest projects/ui -m smoke -v
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

## Current Scope

This is a beginner-friendly UI automation project. It is intentionally small, but it already demonstrates important automation architecture concepts:

- Page Object Model
- Shared Pytest fixtures
- Config separation
- Reusable test data
- Expected value constants
- Marker-based test execution

## Future Improvements

Planned improvements:

- Add a `BasePage` class
- Move common wait, click, type, and get text actions into `BasePage`
- Add reporting support with JUnit XML, pytest-html, or Allure
- Add GitHub Actions CI
- Add more negative login scenarios
- Add more cart and checkout flow coverage
- Add headless browser support through configuration

## Notes

This project should be treated as a learning-focused automation suite, not as a large-scale production framework. The current goal is to understand clean test automation structure and gradually improve it with maintainable architecture practices.