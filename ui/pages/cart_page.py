from selenium.webdriver.common.by import By

from ui.pages.base_page import BasePage


class CartPage(BasePage):
    """
    Page Object Model for the Cart page.
    """

    PAGE_TITLE = (By.CSS_SELECTOR, ".title")
    CART_ITEMS = (By.CSS_SELECTOR, ".cart_item")
    FIRST_CART_ITEM_NAME = (By.CSS_SELECTOR, ".inventory_item_name")

    def get_title_text(self):
        """
        Wait for the page title to be visible and return its text.
        """
        return self.get_text(self.PAGE_TITLE)

    def get_cart_item_count(self):
        """
        Return the total number of items currently in the cart.
        """
        return self.count_elements(self.CART_ITEMS)

    def get_first_cart_item_name(self):
        """
        Wait for the first item in the cart to be visible and return its name.
        """
        return self.get_text(self.FIRST_CART_ITEM_NAME)
