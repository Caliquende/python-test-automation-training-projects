# Python Test Automation Training Projects

This repository contains two focused Python test automation tracks:

1. API automation with Pytest, Requests, API client classes, config separation, reusable test data, JUnit reporting, and GitHub Actions CI.
2. UI automation with Selenium WebDriver, Pytest, Page Object Model, BasePage abstraction, config separation, reusable test data, JUnit reporting, and GitHub Actions CI.

The goal of this repository is not only to write test scripts, but also to practice maintainable test automation architecture.

## Tech Stack

- Python
- Pytest
- Requests
- Selenium WebDriver
- Page Object Model
- API client layer
- JUnit XML reporting
- GitHub Actions CI

## Repository Structure

- `api/`
  - `clients/` — API client classes and shared HTTP request logic
  - `config/` — API base URLs and timeout configuration
  - `data/` — Reusable API payloads and expected values
  - `tests/` — API test scenarios
  - `pytest.ini` — API-specific Pytest configuration
  - `README.md` — API project documentation

- `ui/`
  - `config/` — UI base URL, timeout, and headless configuration
  - `data/` — Test users, expected UI texts, and product data
  - `pages/` — Page Object Model classes and BasePage abstraction
  - `tests/` — UI test scenarios
  - `conftest.py` — Shared WebDriver fixture
  - `pytest.ini` — UI-specific Pytest configuration
  - `README.md` — UI project documentation

- `reports/`
  - Stores generated JUnit XML reports locally
  - Report files are ignored by Git

- `.github/workflows/`
  - GitHub Actions workflow for API and UI test execution

- `pytest.ini`
  - Root-level Pytest configuration

- `requirements.txt`
  - Shared Python dependencies

## Covered Areas

### API Automation

The API track covers public demo APIs:

- JSONPlaceholder
- DummyJSON

Main concepts practiced:

- API client layer
- Base client abstraction
- Config separation
- Reusable test data
- Authenticated requests
- Positive and negative API checks
- Smoke and regression markers
- JUnit XML reporting
- GitHub Actions CI

Expected result:

    12 passed

### UI Automation

The UI track covers SauceDemo browser tests.

Main concepts practiced:

- Selenium WebDriver
- Pytest fixtures
- Page Object Model
- BasePage abstraction
- Config separation
- Reusable test data
- Headless browser execution for CI
- Explicit waits and UI state validation
- Smoke and regression markers
- JUnit XML reporting
- GitHub Actions CI

Expected result:

    4 passed

## Setup

Create and activate a virtual environment:

    python -m venv .venv
    .venv\Scripts\activate

Install dependencies:

    pip install -r requirements.txt

## Running All Tests

Run the full test suite from the repository root:

    pytest

## Running API Tests

Run the full API suite:

    pytest api -v

Run API smoke tests:

    pytest api -m smoke -v

Run API regression tests:

    pytest api -m regression -v

Generate API JUnit XML report:

    pytest api -v --junitxml=reports/api-junit.xml

## Running UI Tests

Run the full UI suite:

    pytest ui -v

Run UI smoke tests:

    pytest ui -m smoke -v

Run UI regression tests:

    pytest ui -m regression -v

Generate UI JUnit XML report:

    pytest ui -v --junitxml=reports/ui-junit.xml

## Running UI Tests in Headless Mode

For CI-like local execution:

    $env:HEADLESS="true"
    pytest ui -v --junitxml=reports/ui-junit.xml
    Remove-Item Env:HEADLESS

## Expected Marker Results

API smoke:

    5 passed, 7 deselected

API regression:

    12 passed

UI smoke:

    2 passed, 2 deselected

UI regression:

    4 passed

## CI

GitHub Actions runs both API and UI tests automatically on push and pull request.

The workflow includes two jobs:

- API Tests
- UI Tests

Each job generates and uploads a JUnit XML artifact:

- api-junit-report
- ui-junit-report

## Validation Notes

- API tests use public demo APIs, so failures may sometimes be caused by external service outages or response changes.
- UI tests use SauceDemo, so failures may sometimes be caused by live UI behavior changes.
- UI tests run in headless Chrome on GitHub Actions.
- Test reports are generated under `reports/` and should not be committed.
- Cache folders such as `.pytest_cache` and `__pycache__` should not be committed.

## Security

This project implements the following security measures:

- **Dependabot:** Automatically monitors and updates dependencies and GitHub Actions.
- **CodeQL:** Performs Static Application Security Testing (SAST) to identify potential vulnerabilities.
- **Security Policy:** Responsible disclosure and security guidelines are defined in [SECURITY.md](./SECURITY.md).
- **SAST & Auditing:** Bandit and pip-audit are integrated into the CI/CD pipeline.
- **Pre-commit Hooks:** Local checks for secrets, private keys, and code quality before every commit.

## Project Status


This is a beginner-friendly but structured test automation training repository.

It is intentionally small, but it demonstrates important QA automation architecture concepts:

- Layered test structure
- Page Object Model
- API client abstraction
- Shared fixtures
- Config separation
- Test data separation
- Marker-based execution
- JUnit reporting
- GitHub Actions CI