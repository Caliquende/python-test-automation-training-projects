# SauceDemo · Manual Software Testing Case Study

> **Status:** Test design reviewed · **CONDITIONAL PASS (19 Nov 2026)**  
> **Application under test:** [SauceDemo / Swag Labs](https://www.saucedemo.com/)  
> **Project:** [Python Test Automation Training Projects](https://github.com/Caliquende/python-test-automation-training-projects)  
> **Approval authority:** ChatGPT acting as Product Owner (PO) for this **training exercise only**; not official SauceDemo stakeholder approval.

This manual software testing case study connects scope, exercise-level requirements, test design techniques, decision tables, state transitions, manual execution results, defect triage, and the pre-existing Selenium/Playwright automation baseline. It covers the login-to-checkout journey, without claiming complete product coverage.

## Documentation

| Document | Contents | Status |
|---|---|---|
| [Scope & Coverage Assessment](docs/scope.md) | Six functional areas; 14 original baseline behaviors (`B01–B14`); automation gap assessment | Baseline: 16 Nov 2026 |
| [Requirements & Acceptance Criteria](docs/requirements.md) | Six requirement groups (`REQ-001–006`); **17** exercise-approved ACs (`AC-001–017`); traceability, manual observations, AC-016 defect candidate | Updated: 19 Nov 2026 |
| [Test Design Techniques](docs/design-techniques.md) | Equivalence Partitioning (EP), Boundary Value Analysis (BVA) feasibility, test-design screening | Reviewed: 18 Nov 2026 |
| [Decision Tables & State Transitions](docs/decision_tables_and_state_transitions.md) | Cart/Checkout decision tables, state transitions, test-case candidates, Q6 final quality gate | Reviewed: 19 Nov 2026; **CP** |

**Version note:** The original 14-behavior scope baseline remains historical; AC-015–017 extend the requirements beyond it. The 18 Nov `design-techniques.md` assessment predates AC-015–017 and must not be interpreted as having screened them.

## Functional coverage and outcomes

| Area | Scope and results |
|---|---|
| Login | Valid and invalid sign-in; invalid login manually observed |
| Inventory | Six-product inventory and price-low-to-high sorting |
| Cart | Cart navigation, one/two-item add/remove, two-to-one removal (AC-015), duplicate-add policy (AC-017: manual PASS) |
| Checkout Information | One/two-item entry, required-field combinations, **empty-cart checkout restriction (AC-016: manual FAIL)** |
| Checkout Overview | Items and displayed totals; arithmetic checked for a two-item example; tax-rate correctness unverified |
| Checkout Complete | Finish navigation and visible confirmation |

### Automation baseline — historical, not new execution

The [16 Nov 2026 scope assessment](docs/scope.md) cites [GitHub Actions run #56](https://github.com/Caliquende/python-test-automation-training-projects/actions/runs/43870142191):

| Evidence | Recorded result | Interpretation |
|---|---|---|
| Selenium / Pytest | **10/10 PASS** | 7 SauceDemo functional tests plus 3 supporting tests |
| Playwright / Pytest | **15/15 PASS** | 7 SauceDemo functional tests plus 8 TodoMVC tests |
| Original SauceDemo behavior coverage | **8/14** behaviors asserted by both reviewed suites | Baseline behavior mappings, not unique tests per behavior |
| Original automation gaps | **6/14** behaviors without matching assertions | Invalid login, sorting, checkout form/validation, overview and completion |
| AC-015–017 automation | **NOT VERIFIED / no matching assertion identified** | New exercise ACs were not part of the 14-behavior baseline |
| Firefox / WebKit | **NOT VERIFIED** | No matching execution evidence in the cited run |

Existing SauceDemo automation reaches Checkout Information; the cited run does not establish automated completion of checkout or execution of the newly designed decision-table scenarios.

### Defect candidate — AC-016: Empty cart allows checkout

**Status:** OPEN — manually observed; **Severity/Priority:** Not assigned; **Type:** Functional behavior against an exercise-level acceptance criterion.

| Field | Detail |
|---|---|
| Application | [SauceDemo](https://www.saucedemo.com/) |
| Test environment | Windows 11, Brave (Chromium-based); browser version not recorded |
| Preconditions | Signed in; shopping cart contains **zero products** |
| Reproduction steps | 1. Open the empty cart. 2. Select **Checkout**. |
| Expected result (AC-016) | Checkout is blocked and the user remains on the Cart page (`cart.html`). |
| Actual result | Checkout proceeds to `https://www.saucedemo.com/checkout-step-one.html`. |
| Result | **FAIL** against AC-016; reported as a defect candidate by the Software Test Engineer |
| Additional observation | A separately provided Checkout Overview screenshot displays `Item total: $0`, `Tax: $0.00`, and `Total: $0.00`. The screenshot does **not**, by itself, establish the navigation sequence from the empty cart to that page. |
| Reproducibility | Observed during manual testing on 19 Nov 2026; repeated-run count not recorded |
| Supporting evidence | Tester observation and screenshot reviewed in the study conversation; image not embedded or linked here |

**Upstream GitHub Issue:** [saucelabs/sample-app-web#201 — Empty cart allows users to proceed to checkout](https://github.com/saucelabs/sample-app-web/issues/201)  
**Issue status (verified 19 Nov 2026):** OPEN; no maintainer response recorded at verification time.

**Upstream issue caveat:** AC-016 was defined by the Product Owner **for this training exercise**, not by Sauce Labs. The upstream issue has been submitted; maintainers have not yet confirmed whether empty-cart checkout is intended behavior. The observed navigation is factual; violation of official product requirements is **NOT VERIFIED**.

### Manual execution and defect triage

Manual checks were executed by the **Software Test Engineer**. Recorded outcomes are part of the test documentation; screenshot distribution is not required for a manual execution PASS. The documents distinguish **manual execution**, **candidate test-case design**, and **historical CI**.

- **17 Nov:** AC-002, AC-004, AC-011, AC-012 (seven blank-field combinations), AC-013 and AC-014 have recorded manual observations.
- **19 Nov:** AC-015 (remove one of two cart items) **PASS**; AC-016 (empty-cart Checkout restriction) **FAIL**; AC-017 (same product not added twice) **PASS** under the exercise PO policy.
- **AC-016 defect candidate:** With an empty cart, selecting Checkout navigated to `checkout-step-one.html` instead of remaining on Cart. A separate screenshot shows a zero-total Checkout Overview, but does not independently prove its navigation path. This is a failure **against the exercise-level AC**, not confirmation of a violation of official SauceDemo requirements.
- **AC-017 policy:** The exercise PO specified at most one instance of a product. The observed refusal to add a duplicate matches that criterion. Detailed interaction sequence was not separately recorded.

**Evidence boundary:** Screenshots and screenshot filenames are intentionally excluded from these exported documents. No independent screenshot review, tax-formula verification, backend order-persistence check, or new automation run is claimed.

## Final Quality Gate — Q6/6

**Decision: CONDITIONAL PASS (CP) for the test-design handoff.** Requirements traceability and selected design coverage passed review. Manual execution is **PASS as an activity**, while individual application results retain their own PASS/FAIL verdicts. The open AC-016 defect candidate and remaining unverified conditions prevent a blanket application PASS.

**Residual risks:** Three-or-more-product cart/checkout behavior, cancel/back navigation and recovery, malformed/whitespace-only/length-boundary inputs without approved limits, tax-rate correctness, and backend persistence. These are **NOT VERIFIED**, not assumed defects.

## Repository layout

```text
manual-qa/
├── README.md
└── docs/
    ├── scope.md
    ├── requirements.md
    ├── design-techniques.md
    └── decision_tables_and_state_transitions.md
```

The documentation files shown above are present in the repository following PR #30. The updated README with the upstream Issue #201 reference is prepared for a separate commit. Formal standalone test-case files and a test plan are not claimed to exist.

## Abbreviations and status legend

| Term | Meaning |
|---|---|
| AC | Acceptance Criterion |
| AUT | Application Under Test |
| BVA | Boundary Value Analysis |
| CHST / ST | Checkout / Cart State Transition |
| CI | Continuous Integration |
| CP | Conditional Pass |
| DT | Decision Table |
| EP | Equivalence Partitioning |
| PO | Product Owner (exercise role) |
| REQ | Requirement |
| TC | Test Case; IDs in the design document are **proposed**, not formal execution records |
| UI | User Interface |
| PASS / FAIL | Outcome for the explicitly named check or application criterion |
| NOT VERIFIED | Evidence or approved expected behavior is insufficient for the named condition |

**Next actions:** Track the upstream response to [Issue #201](https://github.com/saucelabs/sample-app-web/issues/201); verify the remaining risk scenarios if they enter scope; create formal test cases/execution logs or automation assertions separately when requested. Do not treat the design CP as an application release sign-off.
