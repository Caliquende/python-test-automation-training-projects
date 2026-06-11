# API Test Automation

This folder contains API automation practice for public demo APIs.

The active Python API suite is under [pytest/](pytest/README.md). The `newman/` folder contains exported Postman/Newman assets and has its own README.

## Tools and Libraries

- Python
- Pytest
- Requests

## Current Pytest Scope

The Pytest API suite covers:

- JSONPlaceholder posts, users, comments, create, update, delete, and negative lookup/update cases
- DummyJSON login, current user authorization, products, cart creation, cart deletion, and negative cart deletion cases

## Structure

```text
api/
  pytest/
    clients/
    config/
    data/
    tests/
    conftest.py
    README.md
  newman/
    collection/
    environment/
    README.md
```

## Setup

Install Python dependencies from the repository root:

```powershell
pip install -r requirements.txt
```

Create a local `.env` file from the example when environment-backed test data is needed:

```powershell
Copy-Item .env.example .env
```

## Run API Tests

Run only the Python API tests from the repository root:

```powershell
pytest api/pytest/tests
```

Run smoke API tests:

```powershell
pytest api/pytest/tests -m smoke
```

Run regression API tests:

```powershell
pytest api/pytest/tests -m regression
```

## Fixtures and Test Data

`api/pytest/conftest.py` provides API client fixtures for JSONPlaceholder and DummyJSON.

Reusable payloads and expected values live in `api/pytest/data/`. Some values are read from `.env` at runtime through `env_loader.py`.

When an API test fails after making HTTP calls, request and response details are written under `reports/api/http-exchanges/`. Sensitive values are redacted by the base client before writing diagnostic data.
