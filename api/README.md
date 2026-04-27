# API Test Automation Project

This sub-project focuses on REST API automation testing using Python and the `requests` library. It covers two different public APIs to demonstrate various testing techniques.

## Features

- **JSONPlaceholder Integration**: Tests for basic CRUD operations (GET, POST, PUT, DELETE).
- **DummyJSON Integration**: Tests for authenticated endpoints, Bearer token management, and complex data structures (Products, Carts).
- **Validation**: Strict status code checks, schema validation, and data integrity verification.

## Project Structure

```text
api/
├── tests/
│   └── test_api_core_suite.py  # Main test suite for API core functionality
├── .gitignore                  # API specific ignore rules
├── pytest.ini                  # API specific pytest configuration
└── README.md                   # This file
```

## Setup

Ensure you have the required dependencies installed:

```bash
pip install requests pytest
```

## Running Tests

From the `api` directory:

```bash
pytest
```

To see detailed output:

```bash
pytest -v
```

## Test Coverage

- **JSONPlaceholder**:
    - GET posts and users
    - POST (create) new posts
    - PUT (update) existing posts
    - DELETE posts
- **DummyJSON**:
    - User login and token retrieval
    - Authenticated profile access (`/user/me`)
    - Error handling for missing or invalid tokens
    - Product list retrieval and validation
    - Shopping cart operations (add, delete)
