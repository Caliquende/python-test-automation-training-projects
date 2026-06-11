# API Pytest Automation

Python API automation practice using Pytest, Requests, reusable API clients, configuration, fixtures, and test data.

Back to the API overview: [../README.md](../README.md).

## Covered APIs

- JSONPlaceholder
- DummyJSON

## Current Scenarios

JSONPlaceholder coverage includes:

- retrieving a single post
- retrieving users
- creating a post
- updating a post
- deleting a post
- retrieving non-existing posts
- updating a non-existing post
- retrieving comments for a post

DummyJSON coverage includes:

- successful login
- retrieving the current user with a valid bearer token
- authorization errors with missing or invalid tokens
- retrieving a limited product list
- adding a cart
- deleting an existing cart
- deleting a non-existing cart

## Structure

```text
api/pytest/
  clients/
    base_client.py
    dummyjson_client.py
    jsonplaceholder_client.py
  config/
    settings.py
  data/
    dummyjson_payloads.py
    jsonplaceholder_payloads.py
  tests/
    test_dummyjson_client_suite.py
    test_jsonplaceholder_client_suite.py
  conftest.py
  README.md
```

## Fixtures and Test Data

`conftest.py` provides reusable API client fixtures:

- `jsonplaceholder_client`
- `dummyjson_client`

Reusable payloads and expected values live in `data/`. Environment-backed values are read at runtime through `env_loader.py`.

## Run From Repository Root

Run the API Pytest suite:

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

Run specific test files:

```powershell
pytest api/pytest/tests/test_jsonplaceholder_client_suite.py
pytest api/pytest/tests/test_dummyjson_client_suite.py
```

Create a JUnit report:

```powershell
pytest api/pytest/tests --junitxml=reports/api-junit.xml
```

## Reports

Generated report files are stored under `reports/` and should not be committed.

When an API test fails after making HTTP calls, request and response details are written under:

```text
reports/api/http-exchanges/
```

Sensitive fields such as authorization tokens and passwords are redacted before writing logs.
