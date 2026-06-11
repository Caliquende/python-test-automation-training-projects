# TodoMVC Playwright Pytest

This project contains Playwright Python + Pytest practice tests for TodoMVC.

Back to the parent Playwright README: [../README.md](../README.md).

## Demo URL

```text
https://demo.playwright.dev/todomvc/
```

## Current Scenarios

The TodoMVC suite currently covers:

- opening the TodoMVC page
- adding a single todo
- adding multiple todos
- marking a todo as completed
- filtering active and completed todos
- updating the active todo count after completing items
- verifying filter navigation updates the URL and visible todos
- clearing completed todos
- controlled artifact debugging with trace, video, and screenshot capture

## Structure

```text
ui/playwright_pytest/todo_mvc/
  pages/
    todo_page.py
  tests/
    test_todomvc_basic.py
  debug_artifacts/
    trace_artifact_debugging_control_fail.py
  conftest.py
  README.md
```

## Page Object Model

`TodoPage` owns TodoMVC locators and user-focused actions:

- `open()`
- `add_todo(text)`
- `add_todos(todos)`
- `complete_todo(text)`
- `show_all_todos()`
- `show_active_todos()`
- `show_completed_todos()`
- `clear_completed_todos()`

Assertions stay in the test file.

## Locators

Stable locators are initialized once on `TodoPage`, for example:

- `new_todo_input`
- `todo_titles`
- `active_todo_count`
- filter links
- `clear_completed_button`

Dynamic locators are exposed as methods that depend on todo text:

- `todo_item(text)`
- `todo_checkbox(text)`

`active_todo_count` is the visible TodoMVC footer counter such as `1 item left` or `3 items left`. It is not the total number of todo title elements.

## Clear Completed

The clear completed scenario adds multiple todos, completes two of them, verifies total and active counts separately, clicks `Clear completed`, and then verifies that only the active todo remains.

## Setup

Install Python dependencies from the repository root:

```powershell
pip install -r requirements.txt
```

Install Playwright browsers when needed:

```powershell
playwright install
```

## Run From Repository Root

Run only TodoMVC tests:

```powershell
pytest ui/playwright_pytest/todo_mvc/tests
```

Run one test:

```powershell
pytest ui/playwright_pytest/todo_mvc/tests/test_todomvc_basic.py::test_user_can_add_single_todo
```

Run headed:

```powershell
pytest ui/playwright_pytest/todo_mvc/tests --headed
```

Run smoke tests:

```powershell
pytest ui/playwright_pytest/todo_mvc/tests -m smoke
```

Run regression tests:

```powershell
pytest ui/playwright_pytest/todo_mvc/tests -m regression
```

## Trace, Video, and Screenshot Artifacts

`debug_artifacts/trace_artifact_debugging_control_fail.py` is intentionally failing. It runs a real TodoMVC user flow and then uses a wrong final assertion so Playwright can produce debugging artifacts.

The file is separated from the normal `tests/` folder and does not start with `test_`, so standard commands such as `pytest ui/playwright_pytest` do not collect it.

Run it from the repository root:

```powershell
pytest ui/playwright_pytest/todo_mvc/debug_artifacts/trace_artifact_debugging_control_fail.py --tracing on --video on --screenshot on --output test-results
```

Expected result:

- the test fails by design
- trace, video, and screenshot artifacts are written under `test-results/`
- generated artifacts are ignored by Git
- this file is run directly only when artifact evidence is needed

Open a generated trace archive with:

```powershell
playwright show-trace .\test-results\<trace-file>.zip
```

The tests are part of the repository's Playwright suite and use the root `pytest.ini`.
