# SauceDemo UI Test Automation

A small UI test automation project built with Python, Selenium, and Pytest.

## Scope

This project covers a core end-to-end test set for the SauceDemo website:

- login and product list verification
- cart navigation
- add-to-cart flow
- cart badge update for multiple products

## Tech Stack

- Python
- Pytest
- Selenium
- Page Object Model

## Project Structure

\\\
├─ pages

│  ├─ __init__.py

│  ├─ login_page.py

│  ├─ inventory_page.py

│  └─ cart_page.py

├─ tests

│  ├─ __init__.py

│  └─ test_mini_project_core.py

├─ README.md

├─ requirements.txt

└─ .gitignore

\\\

## Installation

\\\bash

pip install -r requirements.txt

\\\

## Run Tests

\\\bash

pytest -v .\projects\tests\test_mini_project_core.py

\\\

## Notes

This project is intentionally kept small and readable.
The focus is on clean test structure, reusable page objects, and practical UI test coverage.
