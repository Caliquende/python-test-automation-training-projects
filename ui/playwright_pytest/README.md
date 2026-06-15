# Playwright Python Pytest UI Automation

This folder contains Playwright Python + Pytest UI automation practice.

## Current Projects

* [TodoMVC](todo_mvc/README.md)
* [SauceDemo](sauce_demo/README.md)

## Structure

```text
ui/playwright_pytest/
  todo_mvc/
    pages/
    tests/
    debug_artifacts/
    conftest.py
    README.md
  sauce_demo/
    config/
    data/
    pages/
    tests/
    conftest.py
    README.md
  README.md
```

## Pytest Playwright Fixtures

The tests use the `page` fixture provided by `pytest-playwright`.

Project-level `conftest.py` files wrap that page in small page object fixtures such as:

* `todo_page`
* `login_page`
* `inventory_page`
* `cart_page`

Fixtures do not hide full user scenarios. Login and other user actions stay visible in the test body.

## Playwright Approach

Playwright locators, actionability checks, auto-waiting, and retrying `expect` assertions are used instead of manual sleeps or explicit waits.

The Playwright examples do not use a shared `BasePage`. The current pages are small enough that inheritance would add indirection without removing meaningful duplication.

Compared with the Selenium suite, the Playwright suite keeps page objects focused on locators and user actions while assertions remain in the tests.

## Run From Repository Root

Run only TodoMVC tests:

```powershell
pytest ui/playwright_pytest/todo_mvc/tests
```

Run only SauceDemo tests:

```powershell
pytest ui/playwright_pytest/sauce_demo/tests
```

Run the full Playwright suite:

```powershell
pytest ui/playwright_pytest
```

Run Playwright tests headed:

```powershell
pytest ui/playwright_pytest --headed
```

Run the full repository Pytest suite:

```powershell
pytest
```

## Controlled Artifact Debugging

The intentionally failing TodoMVC debugging file is:

```text
ui/playwright_pytest/todo_mvc/debug_artifacts/trace_artifact_debugging_control_fail.py
```

Run it directly from the repository root:

```powershell
pytest ui/playwright_pytest/todo_mvc/debug_artifacts/trace_artifact_debugging_control_fail.py --tracing on --video on --screenshot on --output test-results
```

This command is expected to fail.

The file creates trace, screenshot, and video evidence for a controlled assertion failure.

It is outside the normal TodoMVC `tests/` folder and its filename does not start with `test_`. Normal commands such as `pytest`, `pytest ui/playwright_pytest`, and the GitHub Actions Playwright job do not collect it.

The detailed controlled failure scenario is documented in [todo_mvc/README.md](todo_mvc/README.md).

## GitHub Actions CI

The Playwright suite runs inside:

```text
.github/workflows/test-automation.yml
```

The job name is:

```text
Playwright UI Tests
```

The workflow runs on:

* push to `main` or `master`
* pull requests targeting `main` or `master`
* manual `workflow_dispatch`

The Playwright job:

1. Checks out the repository.
2. Sets up Python 3.11.
3. Installs the dependencies from `requirements.txt`.
4. Installs Chromium and its required Linux dependencies.
5. Validates the SauceDemo GitHub Actions secrets.
6. Runs the normal TodoMVC and SauceDemo test directories headlessly.
7. Generates a JUnit XML result.
8. Retains trace and screenshot evidence only for failed tests.
9. Uploads the JUnit result and failure evidence as separate GitHub Actions artifacts.

Python package installation and browser installation are separate steps.

Installing `pytest-playwright` provides the Python plugin and Playwright package. The following command installs the Chromium browser binary and its required Linux dependencies on the CI runner:

```bash
python -m playwright install --with-deps chromium
```

## CI Test Command

```bash
pytest \
  ui/playwright_pytest/todo_mvc/tests \
  ui/playwright_pytest/sauce_demo/tests \
  -v \
  --browser=chromium \
  --tracing=retain-on-failure \
  --screenshot=only-on-failure \
  --video=off \
  --output=test-results/playwright \
  --junitxml=reports/playwright-ui-junit.xml
```

Playwright runs headlessly by default. The CI command does not use `--headed`.

The controlled failing debugging file is not included in this command.

## CI Artifact Strategy

The default Playwright CI artifact strategy is:

```text
Trace: retain-on-failure
Screenshot: only-on-failure
Video: off
```

Trace is retained only when a test fails because it provides detailed debugging evidence such as:

* actions and locator calls
* before and after DOM snapshots
* assertion and action call logs
* source locations
* console output
* network activity

Screenshots are also retained only for failed tests. They provide a quick view of the visible browser state at failure time, but they do not replace the additional evidence available in a trace.

Video is disabled by default because it increases file size, upload time, and artifact storage.

Video can be enabled temporarily when investigating timing-sensitive behavior such as:

* flicker
* redirects
* animations
* short-lived UI states
* elements that appear and disappear rapidly

## Test Results and Debugging Evidence

The Playwright job creates two different output groups.

Structured test result:

```text
reports/playwright-ui-junit.xml
```

Playwright failure evidence:

```text
test-results/playwright/
```

Pytest terminal output shows the live execution result.

JUnit XML contains structured test case results.

Trace and screenshot files contain debugging evidence.

GitHub Actions artifacts are the mechanism used to retain and download these files after the workflow has finished.

This Python/Pytest project does not use the HTML reporter from the Node.js Playwright Test runner.

## GitHub Actions Artifacts

The JUnit artifact is named:

```text
playwright-ui-test-artifacts
```

The failure evidence artifact is named:

```text
playwright-failure-artifacts-ubuntu-chromium
```

Both artifacts use a 14-day retention period.

The artifact upload steps run even when the Pytest step fails.

A successful run may not contain any Playwright failure evidence. Missing fail-only trace or screenshot files do not cause an additional workflow failure.

To inspect a failed GitHub Actions run:

1. Open the failed workflow run.
2. Download `playwright-failure-artifacts-ubuntu-chromium`.
3. Extract the downloaded archive.
4. Locate the generated `trace.zip`.
5. Open it locally:

```powershell
playwright show-trace .\path\to\trace.zip
```

The screenshot files can be opened directly after extracting the artifact.

## Sensitive Data Warning

Playwright traces, screenshots, and videos can contain:

* visible form values
* application URLs
* test data rendered in the DOM
* console messages
* network request and response details
* headers, cookies, or tokens exposed by the tested application

Real production credentials and customer data should not be used in artifact-producing portfolio tests.
