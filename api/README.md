# API Test Automation Project

This sub-project contains automated REST API tests using Python, Pytest, Requests, and a simple API client layer.

The goal of this project is not only to send API requests, but also to practice a maintainable API automation structure with separate layers for configuration, reusable clients, test data, assertions, markers, reporting, and CI execution.

## Tech Stack

- Python
- Pytest
- Requests
- API client layer
- Pytest markers
- JUnit XML reporting
- Request/response logging on failed API tests
- GitHub Actions CI

## Project Structure

- `clients/`
  - `base_client.py` — Shared HTTP request logic
  - `jsonplaceholder_client.py` — JSONPlaceholder endpoint client
  - `dummyjson_client.py` — DummyJSON endpoint client

- `config/`
  - `settings.py` — Base URLs and timeout configuration

- `data/`
  - `jsonplaceholder_payloads.py` — JSONPlaceholder payloads and expected values
  - `dummyjson_payloads.py` — DummyJSON payloads and expected values

- `tests/`
  - `test_jsonplaceholder_client_suite.py` — JSONPlaceholder API tests
  - `test_dummyjson_client_suite.py` — DummyJSON API tests

- `pytest.ini` — API-specific Pytest configuration
- `README.md` — API project documentation

## Covered APIs

This project covers two public demo APIs:

- JSONPlaceholder
- DummyJSON

## Covered Flows

### JSONPlaceholder

- Get a single post
- Get users
- Create a post
- Update a post
- Delete a post

### DummyJSON

- Successful login
- Access current user with a valid Bearer token
- Reject current user request without token
- Reject current user request with invalid token
- Get limited product list
- Add cart
- Delete cart

## Test Architecture Notes

This project uses a small but layered API test automation structure.

- `tests/` contains test scenarios and assertions
- `clients/` contains API interaction logic
- `config/` contains base URLs and timeout values
- `data/` contains reusable payloads and expected values
- `pytest.ini` contains test discovery and marker configuration

Test files should describe API behavior. Raw `requests.get`, `requests.post`, `requests.put`, and `requests.delete` calls should stay inside client classes, not directly inside test scenarios.

## Key Design Decisions

### Base Client

`BaseClient` centralizes shared HTTP methods such as GET, POST, PUT, and DELETE.

This avoids repeating raw Requests logic across test files.

### Service-Specific Clients

Each API has its own client class:

- `JsonPlaceholderClient`
- `DummyJsonClient`

This keeps endpoint logic organized and makes tests easier to read.

### Configuration Layer

Base URLs and timeout values are stored in `config/settings.py`.

### Test Data Layer

Payloads, IDs, usernames, token-related values, and expected values are stored under the `data/` folder.

### Marker-Based Execution

The project uses Pytest markers to separate fast smoke checks from broader regression checks.

## Setup

Install the required dependencies:

    pip install pytest requests

Create a local environment file from the example:

    Copy-Item .env.example .env

Required API values:

- `JSONPLACEHOLDER_USER_ID`
- `DUMMYJSON_USERNAME`
- `DUMMYJSON_PASSWORD`
- `DUMMYJSON_EXPECTED_USERNAME`
- `DUMMYJSON_WRONG_ACCESS_TOKEN`

The real `.env` file is ignored by Git. CI must receive these values through GitHub Actions secrets with the same names.

## Running Tests

Run these commands from the repository root. This avoids confusion from the API-specific `pytest.ini` when invoking pytest from inside `api/`.

From the repository root, run the full API suite:

    pytest api -v

Run only smoke API tests:

    pytest api -m smoke -v

Run API regression tests:

    pytest api -m regression -v

Run a specific JSONPlaceholder test file:

    pytest api/tests/test_jsonplaceholder_client_suite.py -v

Run a specific DummyJSON test file:

    pytest api/tests/test_dummyjson_client_suite.py -v

## Test Reports

Generate a JUnit XML report for the API suite:

    pytest api -v --junitxml=reports/api-junit.xml

Generated report files are stored under the `reports/` folder and should not be committed to version control.

When an API test fails after making HTTP calls, request and response details are written as JSON under:

    reports/api/http-exchanges/

Sensitive fields such as authorization tokens and passwords are redacted before writing logs.

## Pytest Markers

The project uses the following markers:

- `smoke` — Fast critical API checks
- `regression` — Broader API tests used to verify existing behavior after changes

## Expected Results

Full API suite:

    17 passed

Smoke API suite:

    5 passed, 12 deselected

Regression API suite:

    17 passed

## CI

GitHub Actions runs the API test suite automatically on push and pull request.

The workflow generates test artifacts and uploads them:

- `api-test-artifacts`

The artifact includes the JUnit XML report and API request/response logs when failures occur.

## Notes

This is a beginner-friendly API automation project.

It is intentionally small, but it demonstrates important automation architecture concepts such as client abstraction, config separation, reusable test data, marker-based execution, JUnit reporting, and CI integration.
