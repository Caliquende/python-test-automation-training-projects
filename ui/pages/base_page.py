from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from ui.config.settings import DEFAULT_TIMEOUT


class BasePage:
    """
    Base class for all Page Object classes.

    This class keeps common WebDriver interactions in one place.
    Page classes should use these helper methods instead of repeating
    wait, click, type, get text, and navigation wait logic.
    """

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, DEFAULT_TIMEOUT)

    def open_url(self, url):
        """
        Navigate to the given URL.
        """
        self.driver.get(url)

    def get_current_url(self):
        """
        Return the current browser URL.
        """
        return self.driver.current_url

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

    def scroll_to_element(self, element):
        """
        Scroll the element into the center of the viewport.
        """
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            element,
        )

    def javascript_click(self, locator):
        """
        Click an element using JavaScript as a fallback.
        """
        element = self.find_clickable_element(locator)
        self.scroll_to_element(element)
        self.driver.execute_script("arguments[0].click();", element)

    def click(self, locator):
        """
        Wait until an element is clickable, scroll it into view, and click it.

        If the normal Selenium click fails, JavaScript click is used as a fallback.
        """
        element = self.find_clickable_element(locator)
        self.scroll_to_element(element)

        try:
            element.click()
        except WebDriverException:
            self.driver.execute_script("arguments[0].click();", element)

    def click_and_wait_for_url(self, locator, expected_url_part):
        """
        Click an element and wait until the current URL contains the expected text.

        If navigation does not happen after the first click, the method retries
        once with JavaScript click.
        """
        self.click(locator)

        try:
            return self.wait_for_url_contains(expected_url_part)
        except TimeoutException:
            self.javascript_click(locator)
            return self.wait_for_url_contains(expected_url_part)

    def click_and_wait_for_visible_element(self, click_locator, expected_visible_locator):
        """
        Click an element and wait until another expected element becomes visible.

        This is useful when a click causes a UI state change, such as an
        Add to Cart button turning into a Remove button.
        """
        self.click(click_locator)

        try:
            return self.find_visible_element(expected_visible_locator)
        except TimeoutException:
            self.javascript_click(click_locator)
            return self.find_visible_element(expected_visible_locator)

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

    def wait_for_url_contains(self, expected_url_part):
        """
        Wait until the current URL contains the expected text.
        """
        return self.wait.until(
            EC.url_contains(expected_url_part)
        )

    def wait_for_text(self, locator, expected_text):
        """
        Wait until the given element contains the expected text.
        """
        return self.wait.until(
            EC.text_to_be_present_in_element(locator, expected_text)
        )