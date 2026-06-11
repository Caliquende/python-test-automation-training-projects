import re

import pytest
from playwright.sync_api import Page, expect

from ui.playwright_pytest.todo_mvc.pages.todo_page import TodoPage


@pytest.mark.smoke
@pytest.mark.regression
def test_todomvc_page_opens(page: Page, todo_page: TodoPage) -> None:
    """
    TR: TodoMVC sayfasının açılışını test eder.
    EN: Tests the opening of the TodoMVC page.

    Learning focus:
    - Opening the page through the Page Object method
    - Page title verification
    - Page URL verification
    - Visibility validation of the main todo input
    """
    todo_page.open()

    expect(page).to_have_title("React • TodoMVC")
    expect(page).to_have_url("https://demo.playwright.dev/todomvc/#/")
    expect(todo_page.new_todo_input).to_be_visible()


@pytest.mark.smoke
@pytest.mark.regression
def test_user_can_add_single_todo(todo_page: TodoPage) -> None:
    """
    TR: Kullanıcının tek bir görev eklemesini test eder.
    EN: Tests the user's ability to add a single todo item.

    Learning focus:
    - Using a Page Object fixture
    - Calling a user-focused action method
    - Keeping the expected result assertion in the test
    - Separating page logic from test intent
    """
    todo_text = "Buy milk"

    todo_page.open()
    todo_page.add_todo(todo_text)

    expect(todo_page.todo_titles).to_have_text(todo_text)


@pytest.mark.regression
def test_user_can_add_multiple_todos(todo_page: TodoPage) -> None:
    """
    TR: Kullanıcının birden fazla görev eklemesini test eder.
    EN: Tests the user's ability to add multiple todo items.

    Learning focus:
    - Using a Page Object fixture
    - Adding multiple todo items through an action method
    - Using dynamic locator methods
    - Verifying multiple elements with count and text assertions
    - Keeping assertions inside the test
    """
    todos = ["Read docs", "Write test", "Refactor later"]

    todo_page.open()
    todo_page.add_todos(todos)

    expect(todo_page.todo_titles).to_have_count(3)
    expect(todo_page.todo_titles).to_have_text(todos)
    expect(todo_page.active_todo_count).to_have_text("3 items left")
    expect(todo_page.todo_item("Write test")).to_be_visible()


@pytest.mark.regression
def test_user_can_mark_todo_as_completed(todo_page: TodoPage) -> None:
    """
    TR: Kullanıcının bir görevi tamamlandı olarak işaretlemesini test eder.
    EN: Tests the user's ability to mark a todo item as completed.

    Learning focus:
    - Using a Page Object fixture
    - Adding and completing a todo through action methods
    - Using dynamic locator methods
    - Verifying checkbox state and CSS class
    - Keeping assertions inside the test
    """
    todo_text = "Buy milk"

    todo_page.open()
    todo_page.add_todo(todo_text)
    todo_page.complete_todo(todo_text)

    expect(todo_page.todo_checkbox(todo_text)).to_be_checked()
    expect(todo_page.todo_item(todo_text)).to_have_class("completed")


@pytest.mark.regression
def test_user_can_filter_active_and_completed_todos(
    todo_page: TodoPage,
) -> None:
    """
    TR: Active ve Completed filtrelerinin doğru todo listesini gösterdiğini doğrular.
    EN: Verifies that Active and Completed filters display the correct todo items.

    Learning focus:
    - Using a Page Object fixture and reusable action methods
    - Using dynamic locator methods for todo items and checkboxes
    - Filtering todo items through Page Object methods
    - Keeping state and visibility assertions inside the test
    """
    completed_todo = "Buy milk"
    active_todo = "Buy eggs"

    todo_page.open()
    todo_page.add_todos([completed_todo, active_todo])

    completed_todo_item = todo_page.todo_item(completed_todo)
    active_todo_item = todo_page.todo_item(active_todo)
    completed_todo_checkbox = todo_page.todo_checkbox(completed_todo)

    todo_page.complete_todo(completed_todo)

    expect(completed_todo_checkbox).to_be_checked()
    expect(completed_todo_item).to_have_class("completed")

    todo_page.show_completed_todos()

    expect(completed_todo_item).to_be_visible()
    expect(active_todo_item).not_to_be_visible()

    todo_page.show_active_todos()

    expect(active_todo_item).to_be_visible()
    expect(completed_todo_item).not_to_be_visible()


@pytest.mark.regression
def test_todo_count_updates_after_completing_items(
    todo_page: TodoPage,
) -> None:
    """
    TR: Bir görev tamamlandığında öğe sayısının güncellendiğini test eder.
    EN: Tests that the item count updates when todo items are completed.

    Learning focus:
    - Using Page Object action methods to add and complete todos
    - Using dynamic locator methods for todo items and checkboxes
    - Verifying dynamic active todo count updates
    - Filtering todos through Page Object methods
    - Keeping state, count and visibility assertions inside the test
    """
    completed_todo = "Pay rent"
    completed_todo_2 = "Buy bread"
    active_todo = "Call doctor"

    todo_page.open()
    todo_page.add_todos(
        [completed_todo, completed_todo_2, active_todo]
    )

    expect(todo_page.active_todo_count).to_have_text("3 items left")

    completed_todo_item = todo_page.todo_item(completed_todo)
    completed_todo_checkbox = todo_page.todo_checkbox(completed_todo)

    todo_page.complete_todo(completed_todo)

    expect(completed_todo_checkbox).to_be_checked()
    expect(completed_todo_item).to_have_class("completed")

    completed_todo_item_2 = todo_page.todo_item(completed_todo_2)
    completed_todo_checkbox_2 = todo_page.todo_checkbox(
        completed_todo_2
    )

    todo_page.complete_todo(completed_todo_2)

    expect(completed_todo_checkbox_2).to_be_checked()
    expect(completed_todo_item_2).to_have_class("completed")
    expect(todo_page.active_todo_count).to_have_text("1 item left")

    todo_page.show_completed_todos()

    expect(completed_todo_item).to_be_visible()
    expect(completed_todo_item_2).to_be_visible()
    expect(todo_page.todo_item(active_todo)).not_to_be_visible()

    todo_page.show_active_todos()

    expect(todo_page.todo_item(active_todo)).to_be_visible()
    expect(completed_todo_item).not_to_be_visible()
    expect(completed_todo_item_2).not_to_be_visible()

    todo_page.show_all_todos()

    expect(todo_page.todo_item(active_todo)).to_be_visible()
    expect(completed_todo_item).to_be_visible()
    expect(completed_todo_item_2).to_be_visible()


@pytest.mark.smoke
@pytest.mark.regression
def test_filter_navigation_updates_url_and_visible_todos(
    page: Page,
    todo_page: TodoPage,
) -> None:
    """
    TR: Filtre navigasyonunun URL'yi ve görünür todo'ları güncellediğini test eder.
    EN: Tests that filter navigation updates the URL and visible todos.

    Learning focus:
    - Using Page Object action methods for adding, completing and filtering todos
    - Using dynamic locator methods for todo items and checkboxes
    - Verifying hash route navigation with regex
    - Verifying the user-visible result after navigation
    - Keeping URL and visibility assertions inside the test
    """
    active_todo = "Learn Playwright"
    completed_todo = "Practice test automation"

    todo_page.open()
    todo_page.add_todos([active_todo, completed_todo])
    todo_page.complete_todo(completed_todo)

    expect(todo_page.todo_checkbox(completed_todo)).to_be_checked()
    expect(todo_page.todo_item(completed_todo)).to_have_class(
        "completed"
    )

    todo_page.show_completed_todos()

    expect(page).to_have_url(re.compile(r"#/completed$"))
    expect(todo_page.todo_item(completed_todo)).to_be_visible()
    expect(todo_page.todo_item(active_todo)).not_to_be_visible()

    todo_page.show_active_todos()

    expect(page).to_have_url(re.compile(r"#/active$"))
    expect(todo_page.todo_item(active_todo)).to_be_visible()
    expect(todo_page.todo_item(completed_todo)).not_to_be_visible()

    todo_page.show_all_todos()

    expect(page).to_have_url(re.compile(r"#/$"))
    expect(todo_page.todo_item(active_todo)).to_be_visible()
    expect(todo_page.todo_item(completed_todo)).to_be_visible()


@pytest.mark.smoke
@pytest.mark.regression
def test_user_can_clear_completed_todos(todo_page: TodoPage) -> None:
    """
    TR: Kullanıcının tamamlanmış görevleri temizleyebildiğini test eder.
    EN: Tests the user's ability to clear completed todos.

    Learning focus:
    - Using Page Object action methods to add and complete todos
    - Using dynamic locator methods for todo items and checkboxes
    - Verifying total and active todo counts separately
    - Clicking the "Clear completed" button through the Page Object method
    - Keeping state, count and visibility assertions inside the test
    """
    completed_todos = ["Pay rent", "Buy bread"]
    active_todo = "Call doctor"

    todo_page.open()
    todo_page.add_todos(completed_todos)
    todo_page.add_todo(active_todo)

    expect(todo_page.todo_titles).to_have_count(3)
    expect(todo_page.active_todo_count).to_have_text("3 items left")

    for completed_todo in completed_todos:
        todo_page.complete_todo(completed_todo)

    expect(todo_page.todo_titles).to_have_count(3)
    expect(todo_page.active_todo_count).to_have_text("1 item left")
    expect(
        todo_page.todo_item(completed_todos[0])
    ).to_be_visible()
    expect(
        todo_page.todo_item(completed_todos[1])
    ).to_be_visible()
    expect(todo_page.todo_item(active_todo)).to_be_visible()

    todo_page.clear_completed_todos()

    expect(todo_page.todo_titles).to_have_count(1)
    expect(todo_page.active_todo_count).to_have_text("1 item left")
    expect(
        todo_page.todo_item(completed_todos[0])
    ).not_to_be_visible()
    expect(
        todo_page.todo_item(completed_todos[1])
    ).not_to_be_visible()
    expect(todo_page.todo_item(active_todo)).to_be_visible()
    expect(todo_page.clear_completed_button).not_to_be_visible()