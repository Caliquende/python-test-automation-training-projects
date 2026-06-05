# API Pytest Automation

Python API automation practice using Pytest, Requests, reusable API clients, config, and test data.

## Location

```text
api/pytest/
```

## Structure

```text
clients/
config/
data/
tests/
conftest.py
pytest.ini
README.md
```

## Covered APIs

* JSONPlaceholder
* DummyJSON

## Run From Repository Root

Full API suite:

```powershell
pytest api/pytest -v
```

Smoke API tests:

```powershell
pytest api/pytest -m smoke -v
```

Regression API tests:

```powershell
pytest api/pytest -m regression -v
```

Specific test files:

```powershell
pytest api/pytest/tests/test_jsonplaceholder_client_suite.py -v
pytest api/pytest/tests/test_dummyjson_client_suite.py -v
```

JUnit report:

```powershell
pytest api/pytest -v --junitxml=reports/api-junit.xml
```

## Reports

Generated report files are stored under `reports/` and should not be committed.

When an API test fails after making HTTP calls, request/response details are written under:

```text
reports/api/http-exchanges/
```

Sensitive fields such as authorization tokens and passwords are redacted before writing logs.

## Notes

This is a junior-level practice suite. Test logic should stay in `tests/`, request logic should stay in `clients/`, and reusable values should stay in `data/` or `config/`.
