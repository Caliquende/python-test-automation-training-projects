from playwright.sync_api import Locator, Page

from ui.playwright_pytest.sauce_demo.config.settings import SAUCEDEMO_BASE_URL


class LoginPage:
    URL = SAUCEDEMO_BASE_URL

    def __init__(self, page: Page) -> None:
        self.page = page

        self.username_input: Locator = page.locator("[data-test='username']")
        self.password_input: Locator = page.locator("[data-test='password']")
        self.login_button: Locator = page.locator("[data-test='login-button']")
        self.error_message: Locator = page.locator("[data-test='error']")

    def open(self) -> None:
        self.page.goto(self.URL)

    def login_with(self, username: str, password: str) -> None:
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()
