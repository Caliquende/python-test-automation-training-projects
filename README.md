# SauceDemo UI Test Automation

A small UI test automation project built with Python, Selenium, and Pytest.

## Scope

This project covers a core end-to-end test set for the SauceDemo website.

Covered flows:
- login and product list verification
- cart navigation
- add-to-cart flow
- cart badge update for multiple products

## Tech Stack

- Python
- Pytest
- Selenium WebDriver
- Page Object Model

## Project Structure

```text
.
├── pages
│   ├── __init__.py
│   ├── login_page.py
│   ├── inventory_page.py
│   └── cart_page.py
├── tests
│   └── test_mini_project_core.py
├── pytest.ini
├── README.md
├── requirements.txt
└── .gitignore
```

## Installation

```bash
pip install -r requirements.txt
```

## Run Tests

Run the core suite:

```bash
pytest -q
```

Or run the test file directly:

```bash
pytest -v .\tests\test_mini_project_core.py
```

## Test Cases

The current core suite includes:

- `test_logged_in_user_sees_product_list`
- `test_user_can_open_cart_after_login`
- `test_user_can_add_backpack_to_cart_and_see_it_in_cart`
- `test_adding_two_products_updates_cart_badge_to_two`

## Notes

This project is intentionally kept small and readable.

The focus is on:
- clean test structure
- reusable page objects
- practical UI coverage
- simple and understandable pytest usage

## Future Improvement Ideas

- negative login scenarios in a separate suite
- cart empty-state checks
- CI integration
- separating test data from test logic