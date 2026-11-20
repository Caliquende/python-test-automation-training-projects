# SauceDemo — Manual Test Plan

**Date:** 2026-11-20  
**Status:** S1–S5 planning decisions PASS; S6 document review completed with recorded limitations  
**AUT:** https://www.saucedemo.com/  
**Nature:** Educational test plan; not an official Sauce Labs specification or release approval.

## 1. Purpose

Plan manual functional tests for the exercise-approved AC-001–AC-017 across Login, Inventory, Cart, Checkout Information, Checkout Overview and Checkout Complete. Separate test-design completion from execution outcomes and release decisions.

## 2. Scope

**In:** Login; Inventory listing and Add/Remove; Cart; Checkout Information; Checkout Overview; Checkout Complete.

**Out:** Product detail page; performance; load/stress; security/penetration testing. **AC-004 (price sorting) is IN SCOPE** for 23–27 November 2026. No potentially disruptive tests against the public third-party demo.

## 3. Test Basis

- Exercise-approved acceptance criteria AC-001–AC-017 from `requirements.md`, not official Sauce Labs requirements.
- Existing cart/checkout decision tables and state transitions in `decision_tables_and_state_transitions.md`.
- Prior manual observations are historical evidence, not new execution during 23–27 November.
- [Sauce Labs Issue #201](https://github.com/saucelabs/sample-app-web/issues/201): **CLOSED on 2026-11-20**. Maintainer `diemol` explicitly confirmed empty-cart checkout is **intentional** to support testing/validation flows. GitHub displays closure as `completed`; this is not evidence of a code fix. AC-016 remains FAIL **against the exercise-only AC** until the simulated PO revises that AC; it is **not an open upstream defect**.

## 4. Risks and Priorities

All probabilities: **Unknown — insufficient historical data**. These are hypothetical risks, not observed failures.

| Risk | Description | Impact | Priority | Probability |
|---|---|---|---|---|
| R-004 | Product cannot be added to cart | High | P0 | Unknown |
| R-005 | User cannot proceed to checkout with items | High | P0 | Unknown |
| R-006 | Checkout Overview financial total is wrong | High | P0 | Unknown |
| R-007 | Finish fails to reach Checkout Complete | High | P1 | Unknown |

AC-016 is a separately observed discrepancy with an **exercise-only** expectation. The official maintainer has classified the actual behavior as intentional.

## 5. Environment and Test Data

| Field | Recorded value |
|---|---|
| Operating system | Windows 11 (tester-reported) |
| Manual browser | Brave **1.100.58** |
| Browser engine | Chromium **158.0.8127.42** |
| AUT | https://www.saucedemo.com/ |
| Demo users | `standard_user`, `locked_out_user`, `problem_user`, `performance_glitch_user`, `error_user`, `visual_user` |
| Demo password | `secret_sauce` (public demo credential; no personal secrets) |
| Positive login data | `standard_user` / `secret_sauce` |
| Negative login data | `standart_user` / `secret_sauce`; `standard_user` / `secret_sauc` (intentional invalid values) |
| Product examples | Sauce Labs Backpack ($29.99), Sauce Labs Bike Light ($9.99); empty, one-item and two-item cart states |
| Checkout data | First Name, Last Name, Postal Code; eight filled/blank combinations for three required fields |
| Reset procedure | Hamburger menu → Reset App State; check initial cart state before each test; Logout/Login when changing users |

Reset effectiveness is not independently retested in this planning session; this does not block plan completion. Avoid real personal data and private credentials.

### Checkout calculation evidence

Historical manual observation for Backpack + Bike Light: subtotal `$39.98`, displayed tax `$3.20`, displayed total `$43.18`. Arithmetic `$39.98 + $3.20 = $43.18` **PASS**. The observed tax is consistent with **8%**, because `$39.98 × 0.08 = $3.1984`, rounded to `$3.20`. **Source-code formula: VERIFIED** against Sauce Labs `sample-app-web` at commit `d5cd655fa8a974f4ddb6fde2868586e0084211d2`, `src/utils/orderCalculations.js`: `orderTax = (orderTotal * 0.08).toFixed(2)` and `orderGrandTotal = (orderTotal + parseFloat(orderTax)).toFixed(2)`. `src/pages/CheckOutStepTwo.jsx` calls `calculateOrderTotals` and displays its returned values. The repository also contains `src/utils/__tests__/orderCalculations.tests.js` covering subtotal, tax and grand total. The recorded manual figures agree with this implementation; no new AUT run or repository test execution is claimed. Source: https://github.com/saucelabs/sample-app-web/blob/d5cd655fa8a974f4ddb6fde2868586e0084211d2/src/utils/orderCalculations.js

## 6. Entry and Exit Criteria

### Entry — E1–E5

- **E1:** AC-001–017 approved for this exercise.
- **E2:** AUT accessible and demo accounts/test data available.
- **E3:** Test cases mapped to applicable ACs before execution; unimplemented formal cases flagged.
- **E4:** Scope, environment and reset procedure documented.
- **E5:** Known blockers and open issues recorded before execution; upstream Issue #201 is **closed**, not open.

### Exit — X1–X6

- **X1:** Each planned case recorded as PASS, FAIL, BLOCKED or NOT RUN.
- **X2:** All P0 cases executed and evaluated.
- **X3:** Remaining defects, risks and limitations documented.
- **X4:** Every executed case has an actual result and sufficient evidence record.
- **X5:** AC–TC traceability and test summary completed.
- **X6:** Every test PASS and no open defects — **strict completion criterion**, not a prerequisite for a conditional test-design handoff.

**Release decision:** Conditional release may be evaluated by the authorized decision-maker after explicit risk acceptance; no release PASS is asserted by this plan. **Test-design handoff:** CONDITIONAL PASS with documented limitations.

## 7. Execution Strategy and Schedule

**23–27 November 2026:** Smoke → risk-prioritized cases (P0, then P1) → remaining in-scope end-to-end flows, **including AC-004 price-low-to-high sorting** (verify nondecreasing numerical prices). Functional flow: Login → Inventory → Cart → Checkout Information → Checkout Overview → Checkout Complete. Daily case counts and exact assignments are **not specified**; do not invent them.

**Execution verdicts:**

| Status | Decision rule |
|---|---|
| PASS | Executed actual result meets the exercise expected result |
| FAIL | Executed actual result contradicts the exercise expected result |
| BLOCKED | Prerequisite/dependency prevents completion of the case |
| NOT RUN | Case not executed |

## 8. Evidence and Defect Policy

For every executed case, record written observations. For FAIL and critical cases, capture screenshots when feasible; evidence can remain private and need not be embedded in a public repository. A mismatch against an exercise-approved AC is a **defect candidate against that exercise specification**, not automatically an official Sauce Labs defect. Behavior without an approved expected result is a **clarification**. Issue #201 is **reference only**, closed as intentional; do not reopen or present it as unresolved.

**Execution log fields (10):** `id`, `ac`, `date`, `environment`, `data`, `expected`, `actual`, `status`, `evidence`, `defect`.

## 9. Roles

- **Software Test Engineer:** Test planning, case design, manual execution, recording and triage.
- **Simulated Product Owner (ChatGPT, exercise only):** Exercise-level AC acceptance and clarification; no authority over official Sauce Labs product requirements or release.
- **Actual Sauce Labs maintainer:** Upstream product behavior clarification, as recorded in Issue #201; not the exercise PO.

## 10. Traceability

The table distinguishes **existing candidate IDs** from **formal executable test cases**. No invented TC IDs are assigned to the four uncovered requirements. AC-004 is in execution scope; its formal TC has not yet been authored.

| AC | Existing candidate TC ID(s) | Design source | Plan status |
|---|---|---|---|
| AC-001 | **MISSING** | Login | Formal TC design needed |
| AC-002 | **MISSING** | Login | Formal TC design needed |
| AC-003 | **MISSING** | Inventory | Formal TC design needed |
| AC-004 | **MISSING formal TC**; historical manual AC-004 PASS recorded | Inventory sorting; nondecreasing price order | IN SCOPE; formal TC needed |
| AC-005 | TC-005–TC-007 | ST-05–07 | Candidate |
| AC-006 | TC-001 | DT-001 R01 / ST-01 | Candidate |
| AC-007 | TC-002 | DT-001 R02 / ST-02 | Candidate |
| AC-008 | TC-004 | DT-001 R04 / ST-04 | Candidate |
| AC-009 | TC-CHK-009 | CHST-01 | Candidate |
| AC-010 | TC-CHK-010 | CHST-02 | Candidate |
| AC-011 | TC-CHK-001 | DT-002 R01 / CHST-03 | Candidate |
| AC-012 | TC-CHK-002–008 | DT-002 R02–R08 / CHST-04 | Candidate |
| AC-013 | TC-CHK-011 | CHST-05 | Candidate |
| AC-014 | TC-CHK-012 | CHST-06 | Candidate |
| AC-015 | TC-003 | DT-001 R03 / ST-03 | Candidate |
| AC-016 | TC-CHK-013 | DT-003 E01 / CHST-07 | Exercise AC FAIL; upstream intentional |
| AC-017 | TC-008 | DT-003 D01 / ST-08 | Candidate; prior manual PASS |

**Traceability assessment:** All 17 AC IDs accounted for. **13/17** have pre-existing candidate TC mappings in the cart/checkout design; **4/17** lack formal TC IDs in that mapping (login EP design IDs DT-001–007 exist separately), all **4 in current execution scope**. Full formal TC specification and execution log remain to be authored; they are not represented as completed.

## 11. Assumptions, Limitations and Quality Gate

- No test probability percentages invented; all four risks have Unknown probability.
- Official product requirements and official release authority unavailable.
- Source-level tax calculation verified in the cited Sauce Labs repository revision; historical two-item UI figures match. This does not establish a new live AUT execution or correctness for every possible input.
- Manual reset behavior has not been separately rechecked during plan authoring.
- Formal executable cases and AC–TC mapping for AC-001–004 are not complete; AC-004 is in current execution scope.
- Three-plus-product, navigation recovery, unsupported field boundaries and backend persistence are not established as tested.
- Historical screenshots and manual observations are not new 23–27 November executions.

**Final plan quality gate: CONDITIONAL PASS.** All requested plan sections are present and S1–S5 decisions incorporated; the remaining **formal case-design gaps** are explicit. This is a design/handoff verdict, **not** an application PASS, release PASS or proof of new execution.

## Verification and Validation Record

| Check | Expected | Actual | Verdict |
|---|---|---|---|
| Document structure | Purpose, Scope, Test Basis, Risks, Environment/Data, Entry/Exit, Strategy, Evidence/Defects, Roles, Schedule, Limitations, Traceability | All included | PASS |
| Approved S1–S5 decisions | No invented or omitted user choices | Risk P0/P0/P0/P1; Smoke→Risk→E2E; E1–E5; X1–X6; evidence and issue reference policy included | PASS |
| Browser version | User-reported exact versions | Brave 1.100.58 / Chromium 158.0.8127.42 | PASS |
| Issue #201 | Reflect maintainer decision | Closed, intentional; exercise AC discrepancy separate | PASS |
| AC coverage | All 17 ACs represented without invented IDs | 17 listed; four mapping gaps disclosed | PASS for inventory; CONDITIONAL for executable design |
| Tax source-code review | Authoritative code confirmation and comparison to historical observation | Sauce Labs `orderCalculations.js` uses 8% tax and two-decimal rounding; `CheckOutStepTwo.jsx` displays calculated totals; $39.98 / $3.20 / $43.18 matches | PASS — source review and recorded example; no new execution |
| Execution | No claim of new test run | No new run claimed | PASS (reporting integrity) |
| GitHub push | Only claim if performed | Not performed | NOT RUN |

## 12. PO decision update — 2026-11-20

**PO approval note (AC-016):** `Issue #201 expected behaviour (Development comment)`. The exercise-approved AC-016 expectation is unchanged; the historical manual verdict remains FAIL against this exercise AC. Upstream [Issue #201](https://github.com/saucelabs/sample-app-web/issues/201) was closed on 2026-11-20 as intentional/expected behaviour, not fixed; no open upstream product defect is asserted.

AC-004 sorting is explicitly included in the 23–27 November manual execution scope. Its historical manual PASS and absence of a formal TC are recorded separately.
