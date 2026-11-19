# SauceDemo — Requirements and Acceptance Criteria

**Document:** `manual-qa/docs/requirements.md`  
**Assessment date:** 2026-11-17; updated 2026-11-19  
**Application under test:** https://www.saucedemo.com/  
**Repository:** https://github.com/Caliquende/python-test-automation-training-projects  
**Scope baseline:** [scope.md](scope.md)  
**Source baseline reviewed:** `a2942f72d1b57ee7705d2da2d2c0181bd013527d`  
**CI reference for existing assertions:** [Test Automation — run #56](https://github.com/Caliquende/python-test-automation-training-projects/actions/runs/43870142191) at commit `78825f13eda1f4f23b2c7b464bf19c1ea550d589`  
**Document status:** AC-001–017 APPROVED (exercise PO only); manual execution recorded; AC-016 FAIL (open defect candidate); Final Quality Gate CONDITIONAL PASS for design deliverables. These are not official SauceDemo customer requirements.

## 1. Purpose and Boundaries

Create testable, uniquely identified acceptance criteria for the six functional areas selected in the SauceDemo scope assessment: Login, Inventory, Cart, Checkout Information, Checkout Overview and Checkout Complete. The objective is to define observable expected behavior and map it to the existing automated assertions or a documented coverage gap. All 17 acceptance criteria have exercise-level approval from ChatGPT acting as Product Owner (PO); this does not constitute official SauceDemo stakeholder approval. Manual behavior observations made during the 2026-11-17 interactive review are recorded below; screenshots and screenshot references are intentionally excluded from this deliverable for user security.

**Test environment (reported):** Windows 11; Brave (Chromium-based); version not supplied.  
**Manual evidence:** Six previously unautomated behaviors were reviewed interactively on 2026-11-17, and actual results were recorded in Section 4. Screenshots and their filenames are withheld from this document for user security; this limits independent review by anyone who only receives this file.  
**CI evidence:** 7 SauceDemo Selenium and 7 SauceDemo Playwright tests passed in run #56, with overlap in the scenarios covered. Run #56 does not validate the proposed criteria that lack corresponding assertions.

### Terminology and evidence rules

- **REQ**: a candidate functional requirement derived for this exercise.
- **AC**: a measurable, scenario-specific acceptance criterion; each uses Given / When / Then.
- **CODE ASSERTED**: reviewed test code contains an assertion for that behavior; the relevant tests passed in the referenced run. Code coverage is separate from approval; the exercise-level PO approval documented here does not constitute official SauceDemo stakeholder acceptance.
- **SESSION-OBSERVED**: observed or reported during the 2026-11-17 interactive manual review; the textual actual result is recorded, but image evidence is withheld from the deliverable for user security.
- **NOT VERIFIED**: a particular condition (for example, backend processing, tax-rate correctness or a URL not shown in the available observation) was not independently established.
- **APPROVED (by ChatGPT as PO)**: exercise-level acceptance of the AC by ChatGPT in the Product Owner role. Applies to all 17 ACs; it is not official SauceDemo product-owner approval, and it does not imply automation coverage or execution PASS.

## 2. Candidate Requirements and Acceptance Criteria

### REQ-001 — Login
**Candidate requirement:** The application should accept valid demo credentials and reject invalid login attempts with an observable result.

**AC-001 — Successful sign-in**  
**Given** the login page is open and valid standard-user credentials are available,  
**When** the user submits those credentials,  
**Then** the product inventory page is shown, the URL contains `inventory.html`, and the page title is `Products`.  
**Basis:** CODE ASSERTED (`S1`, `P1`, coverage behavior `B01`). **AC status:** APPROVED (by ChatGPT as PO).

**AC-002 — Invalid sign-in is rejected**  
**Given** the login page is open,  
**When** the user submits incorrect credentials,  
**Then** access to the inventory is not granted and an observable login error is shown.  
**Basis:** SESSION-OBSERVED (`B02`); exact message recorded in Section 4; no matching automated assertion identified. **AC status:** APPROVED (by ChatGPT as PO).

### REQ-002 — Inventory / Products
**Candidate requirement:** An authenticated user should be able to inspect the product inventory and use its sorting control.

**AC-003 — Product inventory is displayed**  
**Given** a standard user has signed in,  
**When** the inventory page loads,  
**Then** the title `Products` and six product cards are displayed.  
**Basis:** CODE ASSERTED (`S1`, `P1`, `B03`). **AC status:** APPROVED (by ChatGPT as PO).

**AC-004 — Price sorting**  
**Given** the inventory is displayed,  
**When** the user chooses the price-low-to-high sorting option,  
**Then** the visible product prices are in nondecreasing numerical order.  
**Basis:** SESSION-OBSERVED (`B04`); the selected sorting mode and six displayed prices are recorded in Section 4; no matching automated assertion identified. **AC status:** APPROVED (by ChatGPT as PO).

### REQ-003 — Cart
**Candidate requirement:** A signed-in user should be able to navigate to the cart, add products, inspect cart quantity, and remove products.

**AC-005 — Cart navigation**  
**Given** the product inventory is displayed,  
**When** the user selects the shopping-cart link,  
**Then** the cart page is displayed, its URL contains `cart.html`, and its title is `Your Cart`.  
**Basis:** CODE ASSERTED (`S2`, `P2`, `B05`). **AC status:** APPROVED (by ChatGPT as PO).

**AC-006 — Add one product**  
**Given** a signed-in user is viewing the inventory,  
**When** the user adds `Sauce Labs Backpack` to the cart and opens the cart,  
**Then** the cart badge displays `1` before navigation and the cart shows one item named `Sauce Labs Backpack`.  
**Basis:** CODE ASSERTED (`S3`, `P3`, `B06`). **AC status:** APPROVED (by ChatGPT as PO).

**AC-007 — Add two products**  
**Given** a signed-in user is viewing the inventory,  
**When** the user adds `Sauce Labs Backpack` and `Sauce Labs Bike Light`,  
**Then** the cart badge displays `2`.  
**Basis:** CODE ASSERTED (`S4`, `P4`, `B07`). **AC status:** APPROVED (by ChatGPT as PO).

**AC-008 — Remove a product from the cart**  
**Given** the cart contains one `Sauce Labs Backpack`,  
**When** the user removes that product on the cart page,  
**Then** the cart contains zero cart-item rows and the removed product is no longer visible.  
**Basis:** CODE ASSERTED (`S5`, `P5`, `B08`). **AC status:** APPROVED (by ChatGPT as PO).

**AC-015 — Remove one product from a multi-item cart**  
**Given** the Cart page contains `Sauce Labs Backpack` and `Sauce Labs Bike Light`,  
**When** the user removes `Sauce Labs Bike Light` on the Cart page,  
**Then** `Sauce Labs Bike Light` is absent, `Sauce Labs Backpack` remains, the numeric cart badge displays `1`, and the user remains on the Cart page.  
**Basis:** USER-REPORTED manual test (2026-11-19; `DT-001/R03`, `ST-03`, `TC-003` in local `decision-tables.md`). No matching automated assertion established. **AC status:** APPROVED (by ChatGPT as PO) on 2026-11-19 for this training exercise only.

**AC-017 — Prevent duplicate product addition**  
**Given** a product is already present in the cart,  
**When** the user attempts to add that same product again,  
**Then** the cart retains one instance of that product and its quantity remains `1`.  
**Basis:** Manual test observation on 2026-11-19: the same product was not added a second time. **AC status:** APPROVED (by ChatGPT as exercise PO) on 2026-11-19; the precise attempted UI interaction was not recorded. This is a single-instance cart policy for the training exercise, not an official SauceDemo requirement.

### REQ-004 — Checkout Information
**Candidate requirement:** A user with a populated cart should be able to open the information form, provide required information and receive an observable response to missing information.

**AC-016 — Prevent checkout with an empty cart**  
**Given** the cart contains zero products,  
**When** the user selects Checkout,  
**Then** checkout does not advance and the user remains on the Cart page.  
**Basis:** Manual test on 2026-11-19: empty-cart Checkout navigated to `checkout-step-one.html`, contrary to this newly approved exercise-level requirement. **AC status:** APPROVED (by ChatGPT as exercise PO) on 2026-11-19. **Test verdict:** FAIL — defect candidate; official SauceDemo intended behavior is not established.

**AC-009 — Open checkout with one item**  
**Given** the cart contains one product,  
**When** the user selects Checkout,  
**Then** the URL contains `checkout-step-one.html` and the page title is `Checkout: Your Information`.  
**Basis:** CODE ASSERTED (`S6`, `P6`, `B09`). **AC status:** APPROVED (by ChatGPT as PO).

**AC-010 — Open checkout with two items**  
**Given** the cart contains two products,  
**When** the user selects Checkout,  
**Then** the URL contains `checkout-step-one.html` and the page title is `Checkout: Your Information`.  
**Basis:** CODE ASSERTED (`S7`, `P7`, `B10`). **AC status:** APPROVED (by ChatGPT as PO).

**AC-011 — Continue after supplying customer information**  
**Given** the Checkout Information page is open,  
**When** the user enters nonempty first name, last name and postal code fields and selects Continue,  
**Then** the Checkout Overview page is displayed. The exact URL and page title must be recorded during verification.  
**Basis:** SESSION-OBSERVED (`B11`); the Continue transition was observed and recorded in Section 4; no matching automated assertion identified. **AC status:** APPROVED (by ChatGPT as PO).

**AC-012 — Required information validation**  
**Given** the Checkout Information page is open,  
**When** the user leaves one required information field empty and selects Continue,  
**Then** an observable validation error is shown and the user does not advance to Checkout Overview. The tested field and exact error text must be recorded.  
**Basis:** SESSION-OBSERVED (`B12`); seven empty-field combinations and their error priority are recorded in Section 4; no matching automated assertion identified. **AC status:** APPROVED (by ChatGPT as PO).

### REQ-005 — Checkout Overview
**Candidate requirement:** Before a demo purchase is finished, the user should be able to review selected items and the financial summary.

**AC-013 — Review items and totals**  
**Given** a user has reached Checkout Overview with one or more selected products,  
**When** the order summary is displayed,  
**Then** the selected item names and quantities can be inspected, and subtotal, tax, and total are visible. The displayed total should equal the displayed subtotal plus displayed tax at the display precision; any difference must be logged rather than presumed to be a defect.  
**Basis:** SESSION-OBSERVED (`B13`); order-summary fields and a two-product example recorded in Section 4; no corresponding assertions in the reviewed test suites. **AC status:** APPROVED (by ChatGPT as PO).

### REQ-006 — Checkout Complete
**Candidate requirement:** The demo checkout flow should produce an observable completion state after the user confirms the order.

**AC-014 — Finish checkout**  
**Given** a user has reached Checkout Overview,  
**When** the user selects Finish,  
**Then** a distinct checkout-complete state and a user-visible completion confirmation are displayed. The exact title, confirmation text and URL must be recorded during verification.  
**Basis:** SESSION-OBSERVED (`B14`); visible completion confirmation recorded in Section 4; browser URL `saucedemo.com/checkout-complete.html` observed; no corresponding assertions in the reviewed test suites. **AC status:** APPROVED (by ChatGPT as PO).

## 3. AC-to-Coverage Traceability

`S1–S7` and `P1–P7` refer to the mapping in `scope.md`. The table distinguishes existing automation assertions from manual observations. All 17 ACs have exercise-level PO approval, which does not imply execution coverage.

| AC | Requirement | Scope behavior | Selenium assertion | Playwright assertion | Existing CI result | Review need |
|---|---|---|---|---|---|---|
| AC-001 | REQ-001 | B01 | S1 | P1 | Both PASS | Exercise PO-approved; code-asserted |
| AC-002 | REQ-001 | B02 | None identified | None identified | NO TEST | Manual result recorded; screenshot withheld |
| AC-003 | REQ-002 | B03 | S1 | P1 | Both PASS | Exercise PO-approved; code-asserted |
| AC-004 | REQ-002 | B04 | None identified | None identified | NO TEST | Manual result recorded; screenshot withheld |
| AC-005 | REQ-003 | B05 | S2 | P2 | Both PASS | Exercise PO-approved; code-asserted |
| AC-006 | REQ-003 | B06 | S3 | P3 | Both PASS | Exercise PO-approved; code-asserted |
| AC-007 | REQ-003 | B07 | S4 | P4 | Both PASS | Exercise PO-approved; code-asserted |
| AC-008 | REQ-003 | B08 | S5 | P5 | Both PASS | Exercise PO-approved; code-asserted |
| AC-009 | REQ-004 | B09 | S6 | P6 | Both PASS | Exercise PO-approved; code-asserted |
| AC-010 | REQ-004 | B10 | S7 | P7 | Both PASS | Exercise PO-approved; code-asserted |
| AC-011 | REQ-004 | B11 | None identified | None identified | NO TEST | Manual result recorded; screenshot withheld |
| AC-012 | REQ-004 | B12 | None identified | None identified | NO TEST | 7 combinations recorded; screenshot withheld |
| AC-013 | REQ-005 | B13 | None identified | None identified | NO TEST | Manual result recorded; screenshot withheld |
| AC-014 | REQ-006 | B14 | None identified | None identified | NO TEST | Confirmation and `checkout-complete.html` URL recorded; screenshot withheld |
| AC-015 | REQ-003 | Not included in B01–B14 baseline | None identified | None identified | NO TEST | Manual two-to-one cart removal on 2026-11-19; exercise PO-approved; `DT-001/R03`, `ST-03`, `TC-003` |
| AC-016 | REQ-004 | Outside B01–B14 baseline | None identified | None identified | NO TEST | Manual FAIL: empty cart navigates to checkout information; defect candidate, 2026-11-19 |
| AC-017 | REQ-003 | Outside B01–B14 baseline | None identified | None identified | NO TEST | Manual PASS against exercise PO policy: same product not added twice; interaction detail not recorded |

## 4. Requirements Review and Testability Checklist

Assess each criterion against the application observations or source-backed assertions. The 17 ACs are APPROVED (by ChatGPT as PO) within this training exercise; CODE ASSERTED indicates existing automation coverage, not official stakeholder approval.

- [ ] Each AC has a unique ID and links to one REQ.
- [ ] Every AC identifies an actionable trigger and an observable expected result.
- [ ] Any exact URL, UI text, quantity or calculation is backed by the reviewed code or a recorded observation.
- [ ] Behavior taken only from recollection is labeled USER-REPORTED, not independently validated.
- [ ] Proposed rules without sufficient evidence remain NOT VERIFIED.
- [ ] No missing automation test is reported as an actual application defect.
- [ ] No CI result is reused as proof of manual exploratory execution.

### Manual observation log — 2026-11-17

The following entries are textual records of the interactive manual-review session. The source screenshots and their names are intentionally not included in this deliverable. Observation times were not separately logged; dates are known.

| AC ID | Observation date/time | Preconditions / Test Data | Action | Expected Result | Actual Result | Evidence | Observation Status |
|---|---|---|---|---|---|---|---|
| AC-002 | 2026-11-17; time not recorded | Login page; incorrect credentials (exact values not retained) | Submit the login form | Inventory access is refused; a login error appears | Login page remained visible; `Epic sadface: Username and password do not match any user in this service` was displayed | Evidence: (Screenshot was not shared due to the users's security) | PASS — observed login rejection |
| AC-004 | 2026-11-17; time not recorded | Signed-in user; six inventory products | Select `Price (low to high)` | Displayed product prices are in nondecreasing order | The six displayed prices were `$7.99`, `$9.99`, `$15.99`, `$15.99`, `$29.99`, `$49.99`, in that order | Evidence: (Screenshot was not shared due to the users's security) | PASS — observed six-product sorting |
| AC-011 | 2026-11-17; time not recorded | Checkout Information page; nonempty First Name, Last Name and Postal Code (values withheld) | Select `Continue` | Checkout Overview is displayed | Checkout Overview was displayed with title `Checkout: Overview`; `checkout-step-two.html` was observed | Evidence: (Screenshot was not shared due to the users's security) | PASS — observed navigation |
| AC-012 | 2026-11-17; time not recorded | Checkout Information page; all seven nonempty subsets of the three required fields left blank in separate checks | Select `Continue` for each blank-field combination | A required-field error appears; user does not advance | Validation messages reflected the priority `First Name`, then `Last Name`, then `Postal Code`; all seven blank-field combinations were checked (details below) | Evidence: (Screenshot was not shared due to the users's security) | PASS — observed missing-field validation; see detail table |
| AC-013 | 2026-11-17; time not recorded | Checkout Overview with Backpack (`$29.99`) and Bike Light (`$9.99`) | Inspect selected items and financial summary | Items, quantities, `Item total`, `Tax` and `Total` are visible; displayed arithmetic is consistent | Two items visible; `Item total: $39.98`, `Tax: $3.20`, `Total: $43.18`; displayed values satisfy `$39.98 + $3.20 = $43.18`. Independent tax-rate correctness was not verified | Evidence: (Screenshot was not shared due to the users's security) | PASS — item display/arithmetic; tax formula NOT VERIFIED |
| AC-014 | 2026-11-17; time not recorded | Checkout Overview reached with items in cart | Select `Finish` | Distinct completion state and visible confirmation appear | `Thank you for your order!` was displayed, with the order-dispatched explanatory text and `Back Home` control; browser address bar displayed `saucedemo.com/checkout-complete.html` | Evidence: (Screenshot was not shared due to the users's security) | PASS — visible confirmation and browser URL observed |

**Seven blank-field combinations (AC-012)**

| Blank fields | Observed message |
|---|---|
| First Name | `Error: First Name is required` |
| Last Name | `Error: Last Name is required` |
| Postal Code | `Error: Postal Code is required` |
| First Name + Last Name | `Error: First Name is required` |
| First Name + Postal Code | `Error: First Name is required` |
| Last Name + Postal Code | `Error: Last Name is required` |
| First Name + Last Name + Postal Code | `Error: First Name is required` |

**Evidence privacy:** Screenshots were used in the interactive review but are deliberately not embedded, linked, named or distributed with this document. An external reviewer cannot independently reproduce the screenshot-based verification from the document alone. No backend-order proof or independent tax-rate rule is asserted.

### Additional manual observation — 2026-11-19

| AC ID | Observation date/time | Preconditions / Test Data | Action | Expected Result | Actual Result | Evidence | Observation Status |
|---|---|---|---|---|---|---|---|
| AC-015 | 2026-11-19; time not recorded | Cart page with Backpack and Bike Light | Remove Bike Light | Backpack remains, Bike Light disappears, badge `1`, remain on Cart | Software Test Engineer executed the two-to-one removal check during Cart decision-table and state-transition review | Software Test Engineer manual execution record; screenshot not embedded | PASS — manual execution; independent replay not claimed |
| AC-016 | 2026-11-19; time not recorded | Empty cart | Select Checkout | Stay on Cart; checkout blocked | Navigated to `checkout-step-one.html` | Test engineer execution record; separate screenshot shows a zero-total Checkout Overview, but its navigation path is not independently established | FAIL — defect candidate against exercise PO AC |
| AC-017 | 2026-11-19; time not recorded | Product already in cart | Attempt to add same product again | One instance; quantity remains `1` | Same product was not added a second time | Test engineer execution record; detailed action sequence not supplied | PASS — observed behavior matches exercise PO policy; detailed reproduction NOT VERIFIED |

## 5. Verification and Validation Record

| Stage | Output checked | Expected result | Actual evidence | Verdict |
|---|---|---|---|---|
| Verification — authoring | Requirement and AC structure | Six requirement groups; at least 10 unique AC IDs; traceable scenarios | Six REQ sections, 17 unique AC entries and 17 corresponding traceability rows verified in the draft | PASS (structure only) |
| Verification — source | Existing automation baseline | Identified assertions and relevant run link | Source reviewed in GitHub; 7 Selenium + 7 Playwright SauceDemo tests in successful run #56 | PASS (baseline only) |
| Verification — observations | Six manual observation entries; test data, action, expected, actual, evidence privacy and status recorded | Every targeted AC has a complete textual observation entry | AC-002, AC-004, AC-011, AC-012, AC-013, AC-014 recorded; no screenshot material or filenames included | PASS (textual records only) |
| Validation — observed behavior | Match six draft ACs to the session's observable behavior | Explicit actual results for each targeted behavior | Observed login rejection, sorting, form advancement, empty-field rejection, overview and completion confirmation; unverified tax rule clearly scoped; completion URL recorded | PASS for stated UI observations; exceptions NOT VERIFIED |
| Validation — external evidence reproducibility | Independent reviewer can inspect underlying screenshot evidence | Screenshots are intentionally withheld for user security | Not independently inspectable from the exported document alone | BLOCKED (privacy restriction) |
| Validation — exercise PO approval | All 17 ACs receive explicit exercise-level approval from the assigned PO role | ChatGPT acting as PO approved AC-001 through AC-017 within this training exercise | APPROVED (by ChatGPT as PO) — 17/17 | PASS (exercise approval only) |
| Validation — stakeholder requirements | Official product requirements are approved by an authorized product owner | Explicit official requirement authority | Not available; exercise role-play does not confer official SauceDemo approval | BLOCKED |

## 6. Known Limitations and Next Action

- Source code and CI demonstrate **assertion coverage**, not official authorization of business requirements; exercise-level PO approval is recorded separately.
- This document contains six manual observation entries from 2026-11-17 and three additional manual test records (AC-015–017) from 2026-11-19. Source screenshots remain withheld for the user's security; external independent screenshot verification is therefore unavailable.
- No new SauceDemo test run, code change, defect report or fix is claimed by this file.
- The six original targeted observation gaps and AC-015–017 manual results are recorded in Section 4. Empty-cart checkout fails the newly approved exercise AC-016 and is a defect candidate; duplicate-add behavior meets exercise AC-017. The attached zero-total Overview screenshot is not proof of the exact navigation sequence. `Tax` formula correctness remains NOT VERIFIED. The checkout-complete URL was observed in the browser address bar during the interactive review.
- The AC-015–017 amendments are local only; no GitHub update is claimed. Final design review Q6/6: CONDITIONAL PASS; AC-016 remains an open defect candidate against the exercise PO criterion. Do not require or attach screenshots: the evidence column uses the user-specified privacy statement.

### Final Quality Gate — 2026-11-19

| Gate | Expected | Actual | Result |
|---|---|---|---|
| Requirements | All AC-001–017 unique and traceable | 17 AC entries and 17 traceability rows; six REQ groups | PASS |
| Manual execution | Results recorded without requiring screenshot distribution | Software Test Engineer performed the manual tests; AC-016 FAIL, AC-017 PASS; earlier observations preserved | PASS — execution; outcomes vary |
| Design consistency | AC-015–017 reflected in decision/state models | See local `decision_tables_and_state_transitions.md` (DT-001/DT-003, ST-03/ST-08, CHST-07) | PASS — local design |
| Residual risk | Unverified behavior explicit | 3+ products, navigation recovery, input limits, tax rule and backend persistence remain unverified | CONDITIONAL PASS |
| Application acceptance | No untriaged failed AC | AC-016 is an open defect candidate relative to exercise PO rule; official product policy not confirmed | FAIL — AC-016; triage open |

**Overall:** CONDITIONAL PASS for design-document handoff, not a PASS for all application behavior. No new automation execution, defect fix or GitHub synchronization is claimed.

## 7. Sources

- [Current scope baseline](scope.md)
- [Existing Selenium SauceDemo tests](https://github.com/Caliquende/python-test-automation-training-projects/blob/main/ui/selenium_pytest/tests/test_mini_project_core.py)
- [Existing Playwright SauceDemo tests](https://github.com/Caliquende/python-test-automation-training-projects/blob/main/ui/playwright_pytest/sauce_demo/tests/test_sauce_demo_core.py)
- [Sauce Labs official sample-app-web repository](https://github.com/saucelabs/sample-app-web)
- [ISTQB Foundation Level](https://istqb.org/certifications/certified-tester-foundation-level/)
