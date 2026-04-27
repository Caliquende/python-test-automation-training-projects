from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    """
    Page Object Model for the Cart page.
    """
    # Locators for elements on the Cart page
    PAGE_TITLE = (By.CSS_SELECTOR, ".title")
    CART_ITEMS = (By.CSS_SELECTOR, ".cart_item")
    FIRST_CART_ITEM_NAME = (By.CSS_SELECTOR, ".inventory_item_name")

    def __init__(self, driver):
        """
        Initialize the CartPage with a WebDriver instance and a wait object.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def get_title_text(self):
        """
        Wait for the page title to be visible and return its text.
        """
        title = self.wait.until(
            EC.visibility_of_element_located(self.PAGE_TITLE)
        )
        return title.text

    def get_cart_item_count(self):
        """
        Return the total number of items currently in the cart.
        """
        self.wait.until(
            EC.visibility_of_element_located(self.PAGE_TITLE)
        )
        return len(self.driver.find_elements(*self.CART_ITEMS))

    def get_first_cart_item_name(self):
        """
        Wait for the first item in the cart to be visible and return its name.
        """
        item_name = self.wait.until(
            EC.visibility_of_element_located(self.FIRST_CART_ITEM_NAME)
        )
        return item_name.text