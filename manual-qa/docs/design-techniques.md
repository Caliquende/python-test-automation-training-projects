# SauceDemo — Test Design Techniques Assessment

**Document:** `manual-qa/docs/design-techniques.md`  
**Assessment date:** 2026-11-18  
**Application under test (AUT):** https://www.saucedemo.com/  
**Techniques:** Equivalence Partitioning (EP); Boundary Value Analysis (BVA)  
**Document status:** **COMPLETE — design assessment only**  
**Execution status:** **NOT RUN** for the formal test cases in this report  
**Test basis:** [Requirements and Acceptance Criteria](https://github.com/Caliquende/python-test-automation-training-projects/blob/main/manual-qa/docs/requirements.md) (2026-11-17); [Scope and Coverage Baseline](https://github.com/Caliquende/python-test-automation-training-projects/blob/main/manual-qa/docs/scope.md) (2026-11-16)

## 1. Executive Summary

The assessment identifies EP classes for SauceDemo login credentials, special demo accounts, and required Checkout Information fields. It documents **17 test-design IDs representing 14 distinct input/action scenarios**, with direct links to the applicable exercise requirements or an explicit missing-criterion designation. Repeated positive scenarios are not counted multiple times.

A separate technique-applicability assessment covers **all 14 acceptance criteria (AC-001–AC-014)**, including Inventory, Cart, Checkout Overview, and Checkout Complete. This screening is not a claim that detailed test designs have been produced for all 14 criteria: the case register intentionally concentrates on Login and Checkout Information.

**BVA finding:** None of the five reviewed text fields has a documented minimum/maximum length or numeric range in the exercise acceptance criteria. Evidence-based 2-value and 3-value BVA data therefore cannot be derived. Missing boundary specifications are documented as test-basis gaps rather than replaced by arbitrary limits.

The reviewed UI observations are distinguished from expectations and formal execution results. **No formal manual case execution, production defect, or application fix is claimed by this report.**

## 2. Test Basis, Method, and Evidence Classification

### 2.1 Requirement authority

`REQ-001` through `REQ-006` and `AC-001` through `AC-014` are **training-exercise requirements**, approved in an exercise by ChatGPT acting as Product Owner. They are not official SauceDemo customer requirements. The 2026-11-17 requirements document includes recorded manual observations and an automation-coverage baseline.

### 2.2 Technique selection

- **EP:** Partition inputs or meaningful application states when different behavior is expected. Use representative members of each justified class; do not assume that all recognized demo users behave alike.
- **BVA:** Identify ordered input domains and their specified inclusive or exclusive limits. Derive adjacent boundary test values only when the actual limit and its semantics are supported by the test basis.
- **Other techniques:** Sorting invariants, shopping-cart state changes, arithmetic checks, and checkout completion may be better assessed with state-transition, decision-table, or calculation-focused tests. These are identified in the coverage assessment without relabeling them as BVA.

### 2.3 Evidence and status definitions

| Classification | Meaning |
|---|---|
| **EXERCISE AC** | Expected behavior in the approved training-exercise AC document |
| **SOURCE-CODE EXPECTED** | Expected behavior supported by the [Sauce Labs login implementation](https://github.com/saucelabs/sample-app-web/blob/main/src/pages/Login.jsx) |
| **USER-REPORTED OBSERVATION** | UI behavior reported during the assessment; not a complete formal case-execution record |
| **VISIBLE UI EVIDENCE** | A particular UI state and error text were visible in supplied images; no full step-by-step run log is inferred |
| **AC MISSING** | No approved exercise criterion defines the behavior sufficiently for a pass/fail oracle |
| **NOT RUN** | No independently documented formal execution under the corresponding DT ID |

The assessment records what is known about UI behavior; it does not claim verified back-end rules. Nonempty test-field values were not consistently retained and are therefore described as **nonempty, exact value not recorded** instead of being fabricated.

## 3. Equivalence Partition Analysis

### 3.1 Login — Username

**Precondition:** Open the login page and hold the Password value constant at the documented demo value `secret_sauce`.

| EP class | Representative Username | Expected outcome | Traceability |
|---|---|---|---|
| Recognized standard user | `standard_user` | Successful login; inventory page with `Products` | REQ-001 / AC-001 |
| Unrecognized user | `unknown_user` | Login rejected; credentials-mismatch error | REQ-001 / AC-002 |
| Empty username | `""` | Login rejected; `Username is required` | REQ-001 / AC-002; SOURCE-CODE EXPECTED |

The demo presents `standard_user`, `locked_out_user`, `problem_user`, `performance_glitch_user`, `error_user`, and `visual_user`. Membership in this list does **not** guarantee identical authentication or post-login behavior. For example, `standard_user` and `locked_out_user` belong to distinct behavioral classes.

Changing `standard_user` to `standart_user` crosses from a recognized to an unrecognized username class. This is an **EP** variation, not a BVA test.

### 3.2 Login — Password

**Precondition:** Keep Username fixed at `standard_user`.

| EP class | Representative Password | Expected / reported UI behavior | Traceability |
|---|---|---|---|
| Correct password | `secret_sauce` | Inventory is displayed | REQ-001 / AC-001 |
| Incorrect, nonempty password | `secret_sauc` | `Epic sadface: Username and password do not match any user in this service` | REQ-001 / AC-002 |
| Empty password | `""` | `Epic sadface: Password is required` | REQ-001 / AC-002 |

A single space (`" "`) was reported to produce the same credentials-mismatch response as `secret_sauc`. It is an **additional representative of the incorrect, nonempty partition**, not a fourth partition or a new test-design ID. The final reported behavior for an actual empty string is `Password is required`.

### 3.3 Special demo accounts

**Locked account (`locked_out_user`).** With valid demo credentials, the reported result was `Epic sadface: Sorry, this user has been locked out`; inventory access was blocked. This is a **recognized-but-locked** account class. The message does not demonstrate that the account has a separate administrative *suspended* status. `REQ-001` is relevant, but a dedicated locked-account AC is **MISSING**: AC-002 concerns invalid credentials, not a valid locked account.

**Special inventory presentation (`problem_user`).** The tester described a successful transition to an inventory page on which all six product cards displayed the same pug photograph, while product details differed. This identifies a **special post-login presentation** class. `REQ-002 / AC-003` addresses the presence of six product cards but does not define image correctness. An image-specific test oracle and AC are **MISSING**; the observation must not be labeled a confirmed product defect.

### 3.4 Checkout Information — required-field partitions

**UI test precondition:** At least one product is present in the cart and the Checkout Information page is open. Populate `First Name`, `Last Name`, and `Postal Code` as specified, and click **Continue**. When isolating the omission of one field, hold the other two fields nonempty. These are **UI-level test conditions**, not assertions about back-end validation.

| Field / EP condition | Other fields | Expected behavior | Traceability |
|---|---|---|---|
| First Name nonempty | Last Name and Postal Code nonempty | Checkout Overview; `checkout-step-two.html` | REQ-004 / AC-011 |
| First Name empty | Last Name and Postal Code nonempty | `Error: First Name is required`; no Overview transition | REQ-004 / AC-012 |
| Last Name nonempty | First Name and Postal Code nonempty | Checkout Overview; `checkout-step-two.html` | REQ-004 / AC-011 |
| Last Name empty | First Name and Postal Code nonempty | `Error: Last Name is required`; no Overview transition | REQ-004 / AC-012 |
| Postal Code nonempty | First Name and Last Name nonempty | Checkout Overview; `checkout-step-two.html` | REQ-004 / AC-011 |
| Postal Code empty | First Name and Last Name nonempty | `Error: Postal Code is required`; no Overview transition | REQ-004 / AC-012 |

**Recorded validation precedence:** The UI reports the **first empty required field** in the sequence `First Name → Last Name → Postal Code`. The following multi-field conditions preserve that rule:

| Empty fields | Other field | First error shown | Traceability |
|---|---|---|---|
| First Name + Last Name | Postal Code nonempty | `Error: First Name is required` | REQ-004 / AC-012 |
| Last Name + Postal Code | First Name nonempty | `Error: Last Name is required` | REQ-004 / AC-012 |
| First Name + Last Name + Postal Code | None | `Error: First Name is required` | REQ-004 / AC-012 |
| First Name + Postal Code (supplemental condition) | Last Name nonempty | `Error: First Name is required` | REQ-004 / AC-012 |

The last row is a **supplemental observed combination**, not an extra numbered DT case. The exact error wording above is consistent with the November 17 observation register. Earlier abbreviated messages omitting `is` are not treated as different product responses.

## 4. Detailed Test Design Register

**Execution procedure, Login (DT-001–DT-007):** Open `https://www.saucedemo.com/`, enter the specified credentials, click **Login**, and inspect the expected login outcome. For DT-008, inspect the product cards after a successful special-account login.

**Execution procedure, Checkout (DT-009–DT-017):** Sign in, place at least one product in the cart, open Checkout Information, supply fields as specified, click **Continue**, and verify either the Overview URL or the first required-field message. Nonempty values that were not recorded in the assessment are deliberately unspecified.

| Design ID | Technique / target partition | Test data and variation | Expected result / oracle | Requirement / AC | Evidence basis | Formal run |
|---|---|---|---|---|---|---|
| DT-001 | EP / recognized standard Username | `standard_user` + `secret_sauce` | Inventory / `Products`; URL contains `inventory.html` | REQ-001 / AC-001 | EXERCISE AC; USER-REPORTED OBSERVATION | NOT RUN |
| DT-002 | EP / unrecognized Username | `unknown_user` + `secret_sauce` | Rejected login; credentials-mismatch error | REQ-001 / AC-002 | SOURCE-CODE EXPECTED; design proposal | NOT RUN |
| DT-003 | EP / empty Username | `""` + `secret_sauce` | Rejected login; username-required error | REQ-001 / AC-002 | SOURCE-CODE EXPECTED; design proposal | NOT RUN |
| DT-004 | EP / valid Password | `standard_user` + `secret_sauce` | Successful login to Inventory | REQ-001 / AC-001 | USER-REPORTED OBSERVATION | NOT RUN |
| DT-005 | EP / invalid nonempty Password | `standard_user` + `secret_sauc`; equivalent input: `" "` | Credentials-mismatch error; login denied | REQ-001 / AC-002 | USER-REPORTED OBSERVATION | NOT RUN |
| DT-006 | EP / empty Password | `standard_user` + `""` | `Password is required`; login denied | REQ-001 / AC-002 | USER-REPORTED OBSERVATION; SOURCE-CODE EXPECTED | NOT RUN |
| DT-007 | EP / recognized but locked account | `locked_out_user` + valid demo password | Locked-out message; no Inventory access | REQ-001; **AC MISSING** | USER-REPORTED OBSERVATION; SOURCE-CODE EXPECTED | NOT RUN |
| DT-008 | EP / recognized special-behavior account | `problem_user` + valid demo password; inspect Inventory | Six product cards visible; same pug image across cards was observed; image correctness oracle **MISSING** | REQ-002 / AC-003 (partial); **AC MISSING** | USER-REPORTED OBSERVATION; VISIBLE UI EVIDENCE | NOT RUN |
| DT-009 | EP / First Name present | All three Checkout fields nonempty | Checkout Overview at `checkout-step-two.html` | REQ-004 / AC-011 | USER-REPORTED OBSERVATION | NOT RUN |
| DT-010 | EP / First Name absent | First Name `""`; Last Name and Postal Code nonempty | `Error: First Name is required`; remain on form | REQ-004 / AC-012 | EXERCISE AC; observation register | NOT RUN |
| DT-011 | EP / Last Name present | All three Checkout fields nonempty | Checkout Overview at `checkout-step-two.html` | REQ-004 / AC-011 | USER-REPORTED OBSERVATION | NOT RUN |
| DT-012 | EP / Last Name absent | Last Name `""`; First Name and Postal Code nonempty | `Error: Last Name is required`; remain on form | REQ-004 / AC-012 | EXERCISE AC; observation register | NOT RUN |
| DT-013 | EP / Postal Code present | All three Checkout fields nonempty | Checkout Overview at `checkout-step-two.html` | REQ-004 / AC-011 | USER-REPORTED OBSERVATION | NOT RUN |
| DT-014 | EP / Postal Code absent | Postal Code `""`; First Name and Last Name nonempty | `Error: Postal Code is required`; remain on form | REQ-004 / AC-012 | USER-REPORTED OBSERVATION; observation register | NOT RUN |
| DT-015 | EP / First + Last Name absent | First Name `""`; Last Name `""`; Postal Code nonempty | `Error: First Name is required`; remain on form | REQ-004 / AC-012 | VISIBLE UI EVIDENCE; observation register | NOT RUN |
| DT-016 | EP / Last Name + Postal Code absent | First Name nonempty; Last Name `""`; Postal Code `""` | `Error: Last Name is required`; remain on form | REQ-004 / AC-012 | VISIBLE UI EVIDENCE; observation register | NOT RUN |
| DT-017 | EP / all three Checkout fields absent | First Name `""`; Last Name `""`; Postal Code `""` | `Error: First Name is required`; remain on form | REQ-004 / AC-012 | VISIBLE UI EVIDENCE; observation register | NOT RUN |

**ID integrity:** User-specified DT-009–DT-014 IDs are retained as originally submitted. DT-009, DT-011, and DT-013 all describe the same all-fields-nonempty Checkout flow. DT-001 and DT-004 describe the same standard-login flow. These are separate partition viewpoints **but not additional independent executable scenarios**. Thus **17 design IDs − 1 redundant login row − 2 redundant Checkout rows = 14 distinct input/action scenarios**. This count excludes the unnumbered supplemental validation condition.

## 5. Boundary Value Analysis (BVA) Applicability

| Field | Potential ordered dimension | Documented lower limit | Documented upper limit | 2-value BVA derivable? | 3-value BVA derivable? | Missing test basis |
|---|---|---|---|---|---|---|
| Username | Character count | Not specified | Not specified | No | No | Approved minimum/maximum allowed length and inclusivity |
| Password | Character count | Not specified | Not specified | No | No | Approved minimum/maximum allowed length and inclusivity |
| First Name | Character count | Not specified | Not specified | No | No | Approved minimum/maximum allowed length and inclusivity |
| Last Name | Character count | Not specified | Not specified | No | No | Approved minimum/maximum allowed length and inclusivity |
| Postal Code | Character count; numeric range **only if required** | Not specified | Not specified | No | No | Approved format, length/range limits, and inclusivity |

The difference between an empty string and a nonempty string supports required-field **EP** classes. It does **not** establish a formally authorized character-length boundary for 2-value/3-value BVA. No fixed postal-code digit count, numeric limit, or arbitrary min/max threshold has been assumed. The lack of documented limits does not establish that the implementation itself has no technical limits.

## 6. EP/BVA Suitability Across All Acceptance Criteria

**Purpose:** Screen every exercise AC for technique suitability. Rows marked **NOT DESIGNED** do not have additional DT cases in this report. This classification addresses the previously omitted functional areas without inventing test requirements or changing the approved case IDs.

| AC | Function / requirement | EP applicability and concrete partition opportunity | BVA assessment | Design coverage / next action |
|---|---|---|---|---|
| AC-001 | Successful login (REQ-001) | **Direct:** recognized standard credentials versus other login classes | No documented Username/Password length boundaries | DT-001, DT-004; duplicates de-duplicated |
| AC-002 | Invalid login (REQ-001) | **Direct:** unknown Username, empty Username, invalid nonempty Password, empty Password | No documented credential-length boundaries | DT-002, DT-003, DT-005, DT-006 |
| AC-003 | Inventory display (REQ-002) | **Conditional:** standard vs special-account inventory presentation; visible vs absent product cards | Six expected product cards is an exact assertion, **not** a specified permitted quantity range | DT-008 partially; image-specific AC **MISSING** |
| AC-004 | Inventory price sort (REQ-002) | **Conditional:** sort mode as discrete selection class; prices with ties vs distinct prices could support data partitioning if defined | No allowed price-range boundary or sorting-limit specification; verify order invariant instead | **NOT DESIGNED**; sorting assertion and tie handling later |
| AC-005 | Cart navigation (REQ-003) | **Conditional:** inventory/cart navigation state rather than a natural input class | Not applicable to a numeric boundary under this AC | **NOT DESIGNED**; state-transition test better suited |
| AC-006 | Add one product (REQ-003) | **Direct:** zero items versus one named item; item identity classes if specified | Expected badge `1` is a scenario count, not a defined quantity limit | **NOT DESIGNED**; add/remove state checks later |
| AC-007 | Add two products (REQ-003) | **Direct:** one versus two selected products; distinct-item combinations | No cart maximum or permitted-count boundary specified | **NOT DESIGNED**; item-count classes can be extended |
| AC-008 | Remove one product (REQ-003) | **Conditional:** present versus removed product; cart empty/nonempty states | No permitted item-count maximum; removal is a transition | **NOT DESIGNED**; state transition better suited |
| AC-009 | Open Checkout with one item (REQ-004) | **Direct:** cart contains one item versus another count/state | One item is a defined precondition, not a numeric acceptance boundary | **NOT DESIGNED**; compare with AC-010 |
| AC-010 | Open Checkout with two items (REQ-004) | **Direct:** cart contains two items versus one item | Two items is a defined precondition, not a specified maximum | **NOT DESIGNED**; compare with AC-009 |
| AC-011 | Valid Checkout Information (REQ-004) | **Direct:** each required field nonempty, positive form class | No documented input length/format bounds | DT-009, DT-011, DT-013; same input flow |
| AC-012 | Missing Checkout Information (REQ-004) | **Direct:** individual and multiple missing fields; first-error precedence | No documented input length/format bounds | DT-010, DT-012, DT-014–DT-017 |
| AC-013 | Checkout Overview totals (REQ-005) | **Conditional:** one-item vs multi-item order, amounts with differing decimal fractions, if representative data is specified | No specified total, tax, or price validity range; use arithmetic consistency checks | **NOT DESIGNED**; subtotal + displayed tax = displayed total is the current AC oracle |
| AC-014 | Checkout Complete (REQ-006) | **Conditional:** pre-finish vs completed order states, but primarily a workflow transition | No specified quantitative completion boundary | **NOT DESIGNED**; state-transition/end-to-end check better suited |

**Scope interpretation:** The inventory, cart, and downstream Checkout ACs are **not universally inapplicable to EP**. Several support useful state/data classes, but the original November 18 case designs were focused on form and login input validation. This table records suitability, explicit gaps, and appropriate techniques for all 14 criteria. It does not misrepresent screening as completed detailed test design.

## 7. Evidence and Limitations

- The November 17 [requirements document](https://github.com/Caliquende/python-test-automation-training-projects/blob/main/manual-qa/docs/requirements.md) records the observed required-field precedence and the exact UI error wording. The November 18 responses report the positive and negative outcomes recorded above.
- Four provided UI states corroborated the field-order behavior: First Name present/Last Name missing/Postal Code missing; First Name missing/Last Name present/Postal Code missing; First and Last Name missing/Postal Code present; and all three missing. The same product-image observation was reported for the special `problem_user` demonstration. Neither observation set is treated as proof of all unrecorded steps or an independently complete execution session.
- In the November 17 Checkout Overview example, displayed `Item total: $39.98`, `Tax: $3.20`, and `Total: $43.18` satisfy the displayed arithmetic. The correctness of the underlying tax-rate rule was **NOT VERIFIED**. This is context for AC-013, not a new BVA test or a new DT case.
- No dedicated AC defines locked-account behavior or product-image correctness. No official numeric input or cart boundary specification was provided.
- This report does not include screenshots or external screenshot references in its source list. It contains no claims of an executed test suite, a discovered production defect, or a fixed bug.

## 8. Verification and Validation

### 8.1 Verification — documentation and internal consistency

| Check | Expected | Recorded result | Verdict |
|---|---|---|---|
| Design ID integrity | DT-001–DT-017 present once each | 17 defined rows; stable IDs preserved | **PASS** |
| Unique-scenario count | At least 10 distinct input/action scenarios | 14 distinct scenarios after 3 duplicate rows removed from count | **PASS** |
| Traceability | Each case mapped to REQ/AC or AC MISSING | Every DT row has a mapping or explicit gap | **PASS** |
| Technique classification | EP justified, no unsupported BVA cases | Login/Checkout partitions justified; BVA limits absent for all five fields | **PASS** |
| AC completeness of suitability assessment | AC-001–AC-014 screened | 14 criteria assessed, including 10 not originally targeted in the detailed register | **PASS** |
| Expected vs observed evidence | No formal case execution PASS without a run log | Reporter observations kept separate; 17 formal cases marked NOT RUN | **PASS** |
| Text and scope | Professional report; no study-dialogue or numbered-question sections | Report-based sections and design evidence only | **PASS** |

### 8.2 Validation — fitness for the intended deliverable

| Acceptance criterion | Expected | Recorded result | Verdict |
|---|---|---|---|
| November 18 design objective | EP for Login and Checkout inputs; 10+ unique scenarios; BVA feasibility analysis | 14 distinct scenarios; five-field BVA matrix; explicit case-to-AC linkage | **PASS — design deliverable** |
| Entire AC inventory considered | Technique suitability or reason for omission documented for all 14 ACs | Full AC-001–AC-014 screening table with gaps and next techniques | **PASS — screening only** |
| Executed manual test evidence | Formal run logs required before execution claims | No complete formal DT-specific run logs attached | **NOT RUN — outside design scope** |
| Boundary-based BVA design | Authoritative limits needed for actual boundary-value test data | No approved min/max or inclusion rule in the current test basis | **BLOCKED — missing specification** |
| Product defect assessment | Approved oracle and reproducible evidence needed | Special-account image behavior recorded; product defect not established | **NOT VERIFIED** |

**Final assessment:** **PASS for the November 18 EP/BVA test-design report and AC suitability screening.** The broader functional test suite has **not** been executed by this report, and BVA boundary cases remain blocked pending supported limits.

## 9. References

- [SauceDemo application](https://www.saucedemo.com/)
- [Exercise Requirements and Acceptance Criteria](https://github.com/Caliquende/python-test-automation-training-projects/blob/main/manual-qa/docs/requirements.md)
- [Manual QA Scope and Existing Automation Coverage](https://github.com/Caliquende/python-test-automation-training-projects/blob/main/manual-qa/docs/scope.md)
- [Sauce Labs sample application — Login implementation](https://github.com/saucelabs/sample-app-web/blob/main/src/pages/Login.jsx)
- [ISTQB Certified Tester Foundation Level](https://istqb.org/certifications/certified-tester-foundation-level/)
