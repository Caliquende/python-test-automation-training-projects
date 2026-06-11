import pytest
from playwright.sync_api import Page

from ui.playwright_pytest.todo_mvc.pages.todo_page import TodoPage


@pytest.fixture
def todo_page(page: Page) -> TodoPage:
    return TodoPage(page)