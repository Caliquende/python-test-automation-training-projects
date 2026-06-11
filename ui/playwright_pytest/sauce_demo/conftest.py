import pytest
from playwright.sync_api import Page

from ui.playwright_pytest.sauce_demo.data.users import get_standard_user
from ui.playwright_pytest.sauce_demo.pages.cart_page import CartPage
from ui.playwright_pytest.sauce_demo.pages.inventory_page import InventoryPage
from ui.playwright_pytest.sauce_demo.pages.login_page import LoginPage


@pytest.fixture
def login_page(page: Page) -> LoginPage:
    return LoginPage(page)


@pytest.fixture
def inventory_page(page: Page) -> InventoryPage:
    return InventoryPage(page)


@pytest.fixture
def cart_page(page: Page) -> CartPage:
    return CartPage(page)


@pytest.fixture
def standard_user_credentials() -> dict[str, str]:
    return get_standard_user()
