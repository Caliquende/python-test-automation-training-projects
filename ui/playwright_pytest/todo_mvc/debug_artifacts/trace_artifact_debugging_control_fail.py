import re

import pytest
from playwright.sync_api import Page, expect

from ui.playwright_pytest.todo_mvc.pages.todo_page import TodoPage


@pytest.mark.regression
def test_completed_filter_state_for_artifact_debugging(
    page: Page,
    todo_page: TodoPage,
) -> None:
    """
    TR:
    Completed filtresi sonrasındaki UI durumunu artifact kanıtlarıyla
    incelemek için kontrollü bir failure üretir.

    EN:
    Produces a controlled failure for inspecting the UI state after using
    the Completed filter through artifact evidence.

    Learning focus:
    - Running a real user flow through the existing Page Object
    - Capturing trace, screenshot, and video evidence
    - Comparing the terminal symptom with the recorded UI state
    - Keeping assertions inside the test
    """
    completed_todo = "Review trace"
    active_todos = ["Inspect screenshot", "Watch video"]

    todo_page.open()
    todo_page.add_todos([completed_todo, *active_todos])
    todo_page.complete_todo(completed_todo)
    todo_page.show_completed_todos()

    expect(page).to_have_url(re.compile(r"#/completed$"))
    expect(todo_page.todo_item(completed_todo)).to_be_visible()

    for active_todo in active_todos:
        expect(todo_page.todo_item(active_todo)).not_to_be_visible()

    expect(todo_page.active_todo_count).to_have_text("1 item left")
