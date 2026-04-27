# SauceDemo UI Test Automation Project

This sub-project implements automated UI tests for the [SauceDemo](https://www.saucedemo.com/) website using Python, Selenium WebDriver, and the Page Object Model (POM) design pattern.

## Features

- **Page Object Model (POM)**: Separates page-specific logic from test cases for better maintainability.
- **End-to-End Flows**: Covers essential user journeys from login to cart management.
- **Robustness**: Uses Explicit Waits (WebDriverWait) to handle dynamic elements.

## Project Structure

```text
ui/
├── pages/                      # Page Object Model classes
│   ├── login_page.py           # Login page locators and actions
│   ├── inventory_page.py       # Product listing page locators and actions
│   └── cart_page.py            # Shopping cart page locators and actions
├── tests/                      # UI test cases
│   └── test_mini_project_core.py
├── .gitignore                  # UI specific ignore rules
├── pytest.ini                  # UI specific pytest configuration
└── README.md                   # This file
```

## Setup

Ensure you have the required dependencies installed:

```bash
pip install selenium pytest
```

Note: You must have a compatible version of Chrome and ChromeDriver installed on your system.

## Running Tests

From the `ui` directory:

```bash
pytest
```

To run the core suite with detailed logs:

```bash
pytest -v tests/test_mini_project_core.py
```

## Test Cases

The current suite includes:

- `test_logged_in_user_sees_product_list`: Verifies successful login and product count.
- `test_user_can_open_cart_after_login`: Verifies navigation to the cart.
- `test_user_can_add_backpack_to_cart_and_see_it_in_cart`: Verifies the add-to-cart flow.
- `test_adding_two_products_updates_cart_badge_to_two`: Verifies multiple items in the cart badge.