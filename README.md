# Python Test Automation Training Projects

Training repository with two focused Python automation tracks:

1. **[API automation](api/README.md)**: REST API tests against JSONPlaceholder and DummyJSON with `requests` and `pytest`.
2. **[UI automation](ui/README.md)**: SauceDemo browser tests with Selenium WebDriver, `pytest`, and Page Object Model classes.

## Repository Structure

```text
.
├── api/
│   ├── tests/              # API test cases
│   ├── pytest.ini          # API-specific pytest settings
│   └── README.md           # API track notes
├── ui/
│   ├── pages/              # Page Object Model classes
│   ├── tests/              # UI test cases
│   ├── pytest.ini          # UI-specific pytest settings
│   └── README.md           # UI track notes
├── pytest.ini              # Root pytest configuration
├── requirements.txt        # Shared Python dependencies
└── README.md
```

## Requirements

- Python 3.10+ recommended
- Chrome or another Selenium-supported browser for UI tests
- Network access to the public demo APIs and `https://www.saucedemo.com`

## Setup

```powershell
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Running Tests

Run the full suite from the repository root:

```powershell
pytest
```

Run one track only:

```powershell
pytest api/
pytest ui/
```

## Validation Notes

- API tests depend on external demo services; failures can be caused by service outages or response changes.
- UI tests depend on a local browser driver managed by Selenium and the current SauceDemo behavior.
- Keep locators in `ui/pages/` aligned with the live UI before treating test failures as application defects.
