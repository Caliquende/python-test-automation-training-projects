from selenium.webdriver.common.by import By

from ui.config.settings import BASE_URL
from ui.pages.base_page import BasePage


class LoginPage(BasePage):
    """
    Page Object Model for the Login page.
    """

    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "h3[data-test='error']")

    def open(self):
        """
        Navigate to the login page URL.
        """
        self.open_url(BASE_URL)

    def enter_username(self, username):
        """
        Enter the provided username into the username field.
        """
        self.type_text(self.USERNAME_INPUT, username)

    def enter_password(self, password):
        """
        Enter the provided password into the password field.
        """
        self.type_text(self.PASSWORD_INPUT, password)

    def click_login(self):
        """
        Click the login button.
        """
        self.click(self.LOGIN_BUTTON)

    def login(self, username, password):
        """
        Perform a full login flow with username and password.
        """
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def get_error_message_text(self):
        """
        Wait for an error message to appear and return its text.
        """
        return self.get_text(self.ERROR_MESSAGE)
