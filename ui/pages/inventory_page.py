from selenium.webdriver.common.by import By

from ui.pages.base_page import BasePage


class InventoryPage(BasePage):
    """
    Page Object Model for the Inventory Products page.
    """

    PAGE_TITLE = (By.CSS_SELECTOR, ".title")
    INVENTORY_ITEMS = (By.CSS_SELECTOR, ".inventory_item")
    ADD_BACKPACK_TO_CART_BUTTON = (By.ID, "add-to-cart-sauce-labs-backpack")
    ADD_BIKE_LIGHT_TO_CART_BUTTON = (By.ID, "add-to-cart-sauce-labs-bike-light")
    CART_LINK = (By.CSS_SELECTOR, ".shopping_cart_link")
    CART_BADGE = (By.CSS_SELECTOR, ".shopping_cart_badge")
    CART_URL_PART = "cart.html"

    def get_title_text(self):
        """
        Wait for the page title to be visible and return its text.
        """
        return self.get_text(self.PAGE_TITLE)

    def get_product_count(self):
        """
        Return the total number of products displayed on the page.
        """
        return self.count_elements(self.INVENTORY_ITEMS)

    def add_backpack_to_cart(self):
        """
        Wait for the Backpack Add to Cart button and click it.
        """
        self.click(self.ADD_BACKPACK_TO_CART_BUTTON)

    def add_bike_light_to_cart(self):
        """
        Wait for the Bike Light Add to Cart button and click it.
        """
        self.click(self.ADD_BIKE_LIGHT_TO_CART_BUTTON)

    def get_cart_badge_text(self):
        """
        Return the text count shown on the shopping cart badge.
        """
        return self.get_text(self.CART_BADGE)

    def wait_until_cart_badge_text_is(self, expected_text):
        """
        Wait until the shopping cart badge shows the expected text.
        """
        self.wait_for_text(self.CART_BADGE, expected_text)

    def go_to_cart(self):
        """
        Click the shopping cart link and wait until the Cart page URL is loaded.
        """
        self.click_and_wait_for_url(self.CART_LINK, self.CART_URL_PART)