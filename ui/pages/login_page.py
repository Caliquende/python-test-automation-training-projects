from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    """
    Page Object Model for the Login page.
    """
    # Base URL for the application
    URL = "https://www.saucedemo.com/"

    # Locators for elements on the Login page
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "h3[data-test='error']")

    def __init__(self, driver):
        """
        Initialize the LoginPage with a WebDriver instance and a wait object.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        """
        Navigate to the login page URL.
        """
        self.driver.get(self.URL)

    def enter_username(self, username):
        """
        Enter the provided username into the username field.
        """
        self.driver.find_element(*self.USERNAME_INPUT).send_keys(username)

    def enter_password(self, password):
        """
        Enter the provided password into the password field.
        """
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)

    def click_login(self):
        """
        Click the login button.
        """
        self.driver.find_element(*self.LOGIN_BUTTON).click()

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
        error_message = self.wait.until(
            EC.visibility_of_element_located(self.ERROR_MESSAGE)
        )
        return error_message.text