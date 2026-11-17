# SauceDemo · Manual QA Case Study

> **Status:** Working draft · Documentation in progress  
> **Application under test:** [SauceDemo / Swag Labs](https://www.saucedemo.com/)  
> **Project:** [Python Test Automation Training Projects](https://github.com/Caliquende/python-test-automation-training-projects)

A practical software testing case study that connects **test scope**, **requirements**, **acceptance criteria**, **existing automation coverage**, and **manual observations**. The current documentation covers the login-to-checkout journey in SauceDemo.

This project separates what has been **specified**, **asserted in automation**, **observed manually**, and **verified by CI**. A passing test run is not treated as proof of behavior that its tests do not assert.

## Documentation

| Document | Purpose | Current state |
|:--|:--|:--|
| [**Scope & Coverage Assessment**](docs/scope.md) | Defines six functional areas, maps 14 behaviors (`B01–B14`) to existing Selenium/Playwright assertions, and identifies coverage gaps. | Baseline assessment · **16 Nov 2026** |
| [**Requirements & Acceptance Criteria**](docs/requirements.md) | Defines six candidate requirements (`REQ-001–006`), 14 acceptance criteria (`AC-001–014`), a traceability matrix, and six manual observation records. | Exercise-level PO approval · **17 Nov 2026** |

**Approval context:** The 14 ACs are marked `APPROVED (by ChatGPT as PO)` **for this training exercise only**. They are not official requirements or approvals from Sauce Labs or the SauceDemo product owner.

## Functional coverage

| Area | Behaviors reviewed |
|:--|:--|
| **Login** | Valid and invalid sign-in |
| **Inventory** | Product listing and price sorting |
| **Cart** | Navigation, add/remove operations, item count and badge |
| **Checkout Information** | Entry into checkout, valid information and required-field validation |
| **Checkout Overview** | Item details and displayed financial summary |
| **Checkout Complete** | Checkout completion screen and confirmation |

### Automation baseline

The [scope assessment](docs/scope.md) reviews the **16 Nov 2026** CI baseline, [GitHub Actions run #56](https://github.com/Caliquende/python-test-automation-training-projects/actions/runs/43870142191).

| Evidence | Recorded result | Interpretation |
|:--|:--|:--|
| Selenium / Pytest | **10/10 PASS** in the referenced run | Includes **7 SauceDemo functional tests** and 3 supporting tests |
| Playwright / Pytest | **15/15 PASS** in the referenced run | Includes **7 SauceDemo functional tests** and 8 TodoMVC tests |
| SauceDemo behavior coverage | **8/14 behaviors** have matching assertions in both reviewed suites | These are behavior mappings, **not** eight distinct test functions per suite |
| Remaining automation gaps | **6/14 behaviors** lack matching assertions in the reviewed suites | Invalid login, sorting, checkout form submission/validation, overview and completion |
| Firefox / WebKit | **NOT VERIFIED** | No corresponding execution evidence in the referenced run |

The existing SauceDemo functional tests reach **Checkout Information**; they do not establish automated coverage of the full checkout journey.

### Manual review

The [requirements document](docs/requirements.md) records observations from **17 Nov 2026** for six behaviors outside the reviewed automation coverage:

- **AC-002:** Invalid sign-in rejection
- **AC-004:** Price-low-to-high sorting
- **AC-011:** Continue with customer information
- **AC-012:** Required-field validation (seven blank-field combinations)
- **AC-013:** Checkout overview and displayed totals
- **AC-014:** Checkout completion confirmation

The observations are recorded as text with their outcomes and limitations. **Screenshots, screenshot filenames and image links are deliberately excluded for privacy.** The exported documents therefore do not provide independently inspectable screenshot evidence. Tax-rate correctness and backend order persistence are not claimed as verified.

## Repository layout

```text
manual-qa/
├── README.md
└── docs/
    ├── scope.md
    └── requirements.md
```

## Current boundaries and next steps

This is a **documentation-first, work-in-progress case study**, not a claim of complete SauceDemo test coverage.

The planned manual QA work continues with test design techniques (EP/BVA and decision tables), a test plan, manual test cases, execution records, and traceability. Missing automated behaviors are tracked separately for later Playwright regression work.

For details, see [the scope assessment](docs/scope.md) and [the acceptance criteria and observation log](docs/requirements.md).
