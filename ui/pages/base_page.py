from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from ui.config.settings import DEFAULT_TIMEOUT


class BasePage:
    """
    Base class for all Page Object classes.

    This class keeps common WebDriver interactions in one place.
    Page classes should use these helper methods instead of repeating
    wait, click, type, and get text logic.
    """

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, DEFAULT_TIMEOUT)

    def open_url(self, url):
        """
        Navigate to the given URL.
        """
        self.driver.get(url)

    def find_visible_element(self, locator):
        """
        Wait until an element is visible and return it.
        """
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )

    def find_all_visible_elements(self, locator):
        """
        Wait until all matching elements are visible and return them.
        """
        return self.wait.until(
            EC.visibility_of_all_elements_located(locator)
        )

    def find_clickable_element(self, locator):
        """
        Wait until an element is clickable and return it.
        """
        return self.wait.until(
            EC.element_to_be_clickable(locator)
        )

    def click(self, locator):
        """
        Wait until an element is clickable and click it.
        """
        self.find_clickable_element(locator).click()

    def type_text(self, locator, text):
        """
        Type text into an input field.
        """
        element = self.find_visible_element(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        """
        Wait until an element is visible and return its text.
        """
        return self.find_visible_element(locator).text

    def count_elements(self, locator):
        """
        Return the number of matching elements after waiting for them to be visible.
        """
        self.find_all_visible_elements(locator)
        return len(self.driver.find_elements(*locator))
