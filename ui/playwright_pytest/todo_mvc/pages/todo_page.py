from playwright.sync_api import Locator, Page


class TodoPage:
    URL = "https://demo.playwright.dev/todomvc/"

    def __init__(self, page: Page) -> None:
        self.page = page

        self.new_todo_input: Locator = page.get_by_placeholder(
            "What needs to be done?"
        )
        self.todo_titles: Locator = page.get_by_test_id("todo-title")
        self.active_todo_count: Locator = page.get_by_test_id("todo-count")

        self.all_filter: Locator = page.get_by_role("link", name="All")
        self.active_filter: Locator = page.get_by_role("link", name="Active")
        self.completed_filter: Locator = page.get_by_role(
            "link",
            name="Completed",
        )
        self.clear_completed_button: Locator = page.get_by_role(
            "button",
            name="Clear completed",
        )

    def todo_item(self, text: str) -> Locator:
        return self.page.get_by_role("listitem").filter(has_text=text)

    def todo_checkbox(self, text: str) -> Locator:
        return self.todo_item(text).get_by_label("Toggle Todo")

    def open(self) -> None:
        self.page.goto(self.URL)

    def add_todo(self, text: str) -> None:
        self.new_todo_input.fill(text)
        self.new_todo_input.press("Enter")

    def add_todos(self, todos: list[str]) -> None:
        for todo in todos:
            self.add_todo(todo)

    def complete_todo(self, text: str) -> None:
        self.todo_checkbox(text).check()

    def show_all_todos(self) -> None:
        self.all_filter.click()

    def show_active_todos(self) -> None:
        self.active_filter.click()

    def show_completed_todos(self) -> None:
        self.completed_filter.click()

    def clear_completed_todos(self) -> None:
        self.clear_completed_button.click()