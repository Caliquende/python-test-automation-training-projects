# Test Automation Projects

This directory contains two main test automation sub-projects:

1.  **[API Automation](api/README.md)**: REST API tests for JSONPlaceholder and DummyJSON using Python and Requests.
2.  **[UI Automation](ui/README.md)**: Web UI tests for SauceDemo using Python, Selenium, and the Page Object Model (POM).

## General Structure

```text
projects/
├── api/                # API Test Automation project
│   ├── tests/          # API test cases
│   └── pytest.ini      # API specific configuration
├── ui/                 # UI Test Automation project
│   ├── pages/          # Page Object Model classes
│   ├── tests/          # UI test cases
│   └── pytest.ini      # UI specific configuration
├── README.md           # Root projects documentation
├── pytest.ini          # Root configuration to run all tests
└── .gitignore          # Root git ignore file
```

## Prerequisites

- Python 3.x
- pip (Python package manager)

## Installation

It is recommended to use a virtual environment:

```bash
# Create a virtual environment
python -m venv venv

# Activate it (Windows)
.\venv\Scripts\activate

# Install dependencies
pip install requests selenium pytest
```

## Running Tests

You can run all tests from this root directory:

```bash
pytest
```

Or run specific sub-projects:

```bash
# Run API tests
pytest api/

# Run UI tests
pytest ui/
```
