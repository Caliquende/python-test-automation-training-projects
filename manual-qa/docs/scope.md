# SauceDemo — Manual QA Scope & Automation Coverage Assessment

**Document:** `manual-qa/docs/scope.md`  
**Assessment date:** 2026-11-16  
**Application under test (AUT):** https://www.saucedemo.com/  
**Repository:** https://github.com/Caliquende/python-test-automation-training-projects  
**Reviewed commit:** `78825f13eda1f4f23b2c7b464bf19c1ea550d589`  
**Document status:** Baseline assessment; manual execution evidence is not available.

## 1. Purpose and Test Objective

Assess which **observed SauceDemo behaviors** are verified by existing Selenium/Pytest and Playwright/Pytest assertions, identify missing automation coverage, and record separate CI execution evidence. This is a **coverage assessment**, not a claim that all SauceDemo functionality has been validated or that defects have been found.

## 2. Test Basis and Evidence Hierarchy

1. **Application observation:** The tester reports manually exploring Login, Inventory, Cart, Checkout Information, Checkout Overview, and Checkout Complete in SauceDemo. These observations are user-reported, without saved screenshots, videos, or execution logs.
2. **Source code:** The Selenium and Playwright test functions and their assertions at the reviewed repository commit establish **implemented automation coverage**.
3. **CI execution:** [GitHub Actions — Test Automation, run #56](https://github.com/Caliquende/python-test-automation-training-projects/actions/runs/43870142191) establishes the execution results for the tests run at that commit.

**Important:** Observed behavior is not an official customer requirement or acceptance criterion. A Page Object action alone does not constitute test coverage: a relevant test assertion is required. A passing CI test does not imply coverage of unasserted downstream behavior.

## 3. Assessment Scope

### In Scope — Functional Behavior

- **Login:** successful and unsuccessful login behavior.
- **Inventory / Products:** product list display and sorting.
- **Cart:** navigation, adding one or two products, badge updates, item visibility, and item removal.
- **Checkout Information:** reaching the form, entering customer information, and input validation.
- **Checkout Overview:** reaching and reviewing the order summary and displayed totals.
- **Checkout Complete:** finishing the demo order and viewing confirmation.

### Additional Assessment Only — Non-functional Coverage

Check whether the existing **SauceDemo test suites** contain dedicated assertions for security, performance, accessibility, and usability. Do not implement or execute new tests for these categories during this assessment.

### Out of Scope for This Assessment

- Implementing new Selenium/Playwright tests, fixing application code, or making claims about real defects.
- Formal requirement verification, detailed EP/BVA, decision tables, and full manual case execution reporting (separate planned activities).
- Testing TodoMVC, unrelated APIs, databases, `can-landing`, or TestForge.
- Executing Firefox/WebKit tests today. Their evidence status is tracked as a gap only.

## 4. Environment and Evidence

| Assessment type | Environment | Evidence | Result |
|---|---|---|---|
| Manual exploration | Windows 11; Brave (Chromium-based); Brave 1.100.58 / Chromium 158.0.8127.42 (version recorded 2026-11-20) | Tester statement; no saved manual artifacts | **OBSERVED — USER-REPORTED**, not independently validated |
| Selenium CI | GitHub Actions, Ubuntu 24.04 runner; headless Chrome via Selenium; Python 3.11.18 / pytest 9.0.3 per shared logs | Run #56, Selenium UI Tests job log and JUnit artifact | **PASS: 10/10** (7 SauceDemo functional, 3 supporting tests) |
| Playwright CI | GitHub Actions, Ubuntu 24.04 runner; Chromium; Python 3.11.18 / pytest 9.0.3 per shared logs | Run #56, Playwright UI Tests job log and JUnit artifact | **PASS: 15/15** (7 SauceDemo, 8 TodoMVC) |
| Playwright Firefox/WebKit | Not evidenced for this run | No matching execution results in reviewed run | **NOT VERIFIED** |

**CI run:** https://github.com/Caliquende/python-test-automation-training-projects/actions/runs/43870142191  
**CI date:** 2026-11-16  
**Commit:** `78825f13eda1f4f23b2c7b464bf19c1ea550d589`  
**Artifacts recorded for this run:** `ui-test-artifacts`, `playwright-ui-test-artifacts` (JUnit reports). Artifact presence was verified; the XML contents were not separately inspected.  
**Manual observation date / detailed expected-vs-actual logs:** Not recorded. No manual PASS verdict is assigned.

## 5. Coverage Classification Rules

- **COVERED:** A test function and an assertion for the specific behavior were identified in the reviewed source.
- **NOT COVERED:** Review of the identified SauceDemo test suites found no assertion for the behavior.
- **NOT VERIFIED:** Available evidence is insufficient to determine coverage or execution status.
- **PASS / FAIL:** Execution verdict for an identified test, based on a specific recorded run; not a label for application features as a whole.
- **NO TEST:** No matching automated test exists in the reviewed suites, so there is no CI verdict for that behavior.
- **USER-REPORTED:** Manual behavior was explored according to the tester, but no independent execution artifact is retained.

## 6. Selenium vs. Playwright — Behavior-level Coverage Matrix

`S1–S7` and `P1–P7` refer to the test functions in Section 7. Code coverage and CI execution results are displayed in separate columns for each framework. A repeated test ID indicates **one test asserting multiple behaviors**, not an additional distinct test. All `PASS` entries refer specifically to CI run #56.

| ID | Assessed behavior | Selenium code | Selenium CI | Playwright code | Playwright CI | Coverage gap |
| --- | --- | --- | --- | --- | --- | --- |
| **B01** | Valid login leads to product listing | COVERED (S1) | PASS | COVERED (P1) | PASS | None identified for this behavior |
| **B02** | Invalid login / rejected credentials | NOT COVERED | NO TEST | NOT COVERED | NO TEST | Negative login assertions missing |
| **B03** | Inventory page title and product count | COVERED (S1) | PASS | COVERED (P1) | PASS | No gap for these assertions |
| **B04** | Inventory sorting behavior | NOT COVERED | NO TEST | NOT COVERED | NO TEST | Sorting assertions missing |
| **B05** | Navigate from inventory to cart | COVERED (S2) | PASS | COVERED (P2) | PASS | No gap for navigation |
| **B06** | Add one item; check badge and cart content | COVERED (S3) | PASS | COVERED (P3) | PASS | No gap for tested product/flow |
| **B07** | Add two items; check badge count | COVERED (S4) | PASS | COVERED (P4) | PASS | No gap for tested two-item flow |
| **B08** | Remove a cart item; check empty state | COVERED (S5) | PASS | COVERED (P5) | PASS | No gap for tested removal flow |
| **B09** | Open Checkout Information with one item | COVERED (S6) | PASS | COVERED (P6) | PASS | Only navigation and page identity checked |
| **B10** | Open Checkout Information with two items | COVERED (S7) | PASS | COVERED (P7) | PASS | Only navigation and page identity checked |
| **B11** | Enter valid customer information and continue | NOT COVERED | NO TEST | NOT COVERED | NO TEST | Checkout form submission missing |
| **B12** | Reject missing/invalid checkout information | NOT COVERED | NO TEST | NOT COVERED | NO TEST | Negative checkout validation missing |
| **B13** | Verify Checkout Overview items and totals | NOT COVERED | NO TEST | NOT COVERED | NO TEST | Order review and amount assertions missing |
| **B14** | Finish order and verify completion | NOT COVERED | NO TEST | NOT COVERED | NO TEST | Full end-to-end purchase assertion missing |

**Interpretation:** Seven SauceDemo functional tests exist in each framework, covering the same seven test scenarios. The matrix has **14 assessed behavior entries**, not 14 independent automated scenarios. Passing tests stop at the first Checkout Information screen; reaching that screen is **not** equivalent to submitting or completing checkout.

## 7. Source-code Traceability

**Selenium test file:** [test_mini_project_core.py](https://github.com/Caliquende/python-test-automation-training-projects/blob/78825f13eda1f4f23b2c7b464bf19c1ea550d589/ui/selenium_pytest/tests/test_mini_project_core.py)  
**Playwright test file:** [test_sauce_demo_core.py](https://github.com/Caliquende/python-test-automation-training-projects/blob/78825f13eda1f4f23b2c7b464bf19c1ea550d589/ui/playwright_pytest/sauce_demo/tests/test_sauce_demo_core.py)

### Selenium traceability

| Ref | Selenium test function |
| --- | --- |
| S1 | `test_logged_in_user_sees_product_list` |
| S2 | `test_user_can_open_cart_after_login` |
| S3 | `test_user_can_add_backpack_to_cart_and_see_it_in_cart` |
| S4 | `test_adding_two_products_updates_cart_badge_to_two` |
| S5 | `test_user_can_add_backpack_to_cart_and_remove_it_from_cart` |
| S6 | `test_user_can_add_backpack_to_cart_and_checkout` |
| S7 | `test_user_can_add_two_items_to_cart_and_checkout` |

### Playwright traceability

| Ref | Playwright test function |
| --- | --- |
| P1 | `test_standard_user_sees_product_list_after_login` |
| P2 | `test_logged_in_user_can_open_cart` |
| P3 | `test_user_can_add_backpack_to_cart_and_see_it_in_cart` |
| P4 | `test_adding_two_products_updates_cart_badge_to_two` |
| P5 | `test_user_can_add_backpack_to_cart_and_remove_it_from_cart` |
| P6 | `test_user_can_add_backpack_to_cart_and_checkout` |
| P7 | `test_user_can_add_two_items_to_cart_and_checkout` |

**Not counted as SauceDemo functional scenarios:** The Selenium suite also has one [delayed-render cart navigation test](https://github.com/Caliquende/python-test-automation-training-projects/blob/78825f13eda1f4f23b2c7b464bf19c1ea550d589/ui/selenium_pytest/tests/test_cart_navigation_timing.py) using a temporary **local HTML fixture**, and two parametrized [failure-evidence tests](https://github.com/Caliquende/python-test-automation-training-projects/blob/78825f13eda1f4f23b2c7b464bf19c1ea550d589/ui/selenium_pytest/tests/test_failure_evidence.py). These three passed in CI but do not provide additional SauceDemo business-flow coverage.

## 8. Manual Observation Register

The tester reports performing **10 exploratory activities** without noticing unexpected behavior: successful login, unsuccessful login, product listing, product sorting, add to cart, remove from cart, checkout information entry, checkout input validation, checkout overview review, and checkout completion.

- **Source:** Tester statement only.
- **Evidence:** No screenshots, videos, formal test cases, expected-vs-actual execution log, or defect records supplied.
- **Assessment:** `USER-REPORTED / NOT DOCUMENTED` for each activity.
- **Restriction:** Do **not** convert these observations into ten `PASS` manual test cases or claim that a defect was discovered or fixed.

## 9. Non-functional Coverage Assessment

| Category | Reviewed evidence / coverage | Assessment |
| --- | --- | --- |
| Security | Bandit and pip-audit cover repository code/dependencies. No dedicated SauceDemo application-security assertions identified. | NOT COVERED in SauceDemo UI suites |
| Performance | No load, timing or performance-threshold assertions identified. | NOT COVERED |
| Accessibility | No dedicated accessibility assertions or audit integration identified. | NOT COVERED |
| Usability | No formal usability criteria or user-task evaluation assertions identified. | NOT COVERED |

**Security limitation:** The repository security-scan commands use `|| true`; a successful job does **not** prove a clean security scan or application-level security coverage.

These findings concern the **reviewed SauceDemo UI test suites**, not every possible test or quality attribute of the application.

## 10. Cross-browser Evidence Gap

| Browser / engine | Existing run evidence | Status |
|---|---|---|
| Selenium Chrome (headless) | Functional SauceDemo tests in run #56 | PASS (7/7) |
| Playwright Chromium | Functional SauceDemo tests in run #56 | PASS (7/7) |
| Playwright Firefox | Not present in run #56 | NOT VERIFIED |
| Playwright WebKit | Not present in run #56 | NOT VERIFIED |

Brave was used for **manual exploration** only; the CI results must not be represented as Brave runs. Firefox and WebKit execution is deferred, not claimed as failed.

## 11. Qualitative Coverage-gap Priorities

Priority reflects **business impact**, a **qualitative view of plausible failure exposure** (not a measured defect probability), and **current assertion coverage**. **Failure likelihood is unknown and has not been measured for any listed gap.** Levels are provisional; no numerical scoring or unverified defect claims are made.

| Gap | Business impact | Existing coverage | Priority | Reason |
| --- | --- | --- | --- | --- |
| B14 — Checkout completion | High | No matching assertions | **HIGH** | Core purchase flow has no end-to-end completion check |
| B11 / B13 — Form submission and order review | High | No matching assertions | **HIGH** | The checkout path is only checked up to step one |
| B12 — Checkout input validation | High | No matching assertions | **HIGH** | Invalid or missing required information is not automatically checked |
| B02 — Invalid login | Medium | No matching assertions | **MEDIUM** | Authentication rejection behavior is untested |
| B04 — Inventory sorting | Medium | No matching assertions | **MEDIUM** | User-facing sorting behavior is untested |
| Firefox / WebKit evidence | Medium | No matching CI runs | **MEDIUM** | Cross-browser behavior is not yet established |

**Risk note:** These are **coverage priorities**, not confirmed product defects, and the failure likelihood is unknown. Security, performance, accessibility, and usability require separate acceptance criteria before assigning defensible product-risk severity.

## 12. Verification

| Checked output | Expected | Actual evidence | Verdict |
|---|---|---|---|
| Reviewed Selenium coverage | Source-backed functional assertions | Seven SauceDemo test functions mapped to S1–S7 | PASS |
| Reviewed Playwright coverage | Source-backed functional assertions | Seven SauceDemo test functions mapped to P1–P7 | PASS |
| CI run and job results | Independently accessible run evidence | Run #56: 10/10 Selenium and 15/15 Playwright test results | PASS |
| CI report artifacts | JUnit artifacts recorded | Two named UI artifacts present in run metadata; contents not separately inspected | PASS (presence only) |
| Manual exploration evidence | Repeatable manual execution logs or screenshots | No saved manual execution evidence supplied | BLOCKED |
| Firefox/WebKit execution | Browser-specific run results | No corresponding results in reviewed run | NOT RUN / NOT VERIFIED |

## 13. Validation and Limitations

- **PASS — Document fit:** The assessment includes all six selected functional areas, a comparative behavior-level coverage matrix, separate code and execution statuses, non-functional gap review, and a qualitative priority list.
- **PASS — Claim discipline:** CI success applies only to the tests that actually executed; manual statements remain user-reported; neither missing tests nor potential risks are represented as actual defects.
- **BLOCKED — Independent manual validation:** Screenshots, dated case-by-case logs, and reproducible actual-vs-expected records were not supplied.
- **NOT VERIFIED — Unexecuted platforms:** Firefox/WebKit outcomes and any unreviewed integration outside the identified SauceDemo suites.
- **Open work:** Future requirement/acceptance-criteria design, detailed manual test cases and execution logs, extended checkout automation, and cross-browser verification are separate activities; none is marked complete here.

## 14. Assessment Summary

The reviewed repository has **7 SauceDemo Selenium** and **7 SauceDemo Playwright** functional tests, all passing in the verified CI run. These two suites exercise largely equivalent **login → inventory → cart → first checkout screen** scenarios. No automated assertions were found in these suites for **invalid login, inventory sorting, customer-information submission/validation, checkout overview totals, or completed purchase**. Manual exploration of these areas is reported but lacks independent evidence. The document therefore records the current **baseline and gaps**, rather than certifying the whole application as tested.

## Post-baseline coordination — 2026-11-20

This 2026-11-16 automation coverage baseline is preserved as historical evidence. AC-004 price sorting is included in the separate 2026-11-23–27 manual execution plan; the original B04 automation gap remains unchanged. The browser version was subsequently recorded: Brave 1.100.58 / Chromium 158.0.8127.42.

**Cross-document PO approval note (AC-016):** `Issue #201 expected behaviour (Development comment)`. AC-016 retains its exercise-level expectation and historical FAIL. The upstream issue was closed on 2026-11-20 as intentional behaviour; this 16 November automation baseline is unchanged.
