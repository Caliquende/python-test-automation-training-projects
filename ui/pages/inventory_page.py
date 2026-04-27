from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:
    """
    Page Object Model for the Inventory (Products) page.
    """
    # Locators for elements on the Inventory page
    PAGE_TITLE = (By.CSS_SELECTOR, ".title")
    INVENTORY_ITEMS = (By.CSS_SELECTOR, ".inventory_item")
    ADD_BACKPACK_TO_CART_BUTTON = (By.ID, "add-to-cart-sauce-labs-backpack")
    ADD_BIKE_LIGHT_TO_CART_BUTTON = (By.ID, "add-to-cart-sauce-labs-bike-light")
    CART_LINK = (By.CSS_SELECTOR, ".shopping_cart_link")
    CART_BADGE = (By.CSS_SELECTOR, ".shopping_cart_badge")

    def __init__(self, driver):
        """
        Initialize the InventoryPage with a WebDriver instance and a wait object.
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

    def get_product_count(self):
        """
        Return the total number of products displayed on the page.
        """
        self.wait.until(
            EC.visibility_of_all_elements_located(self.INVENTORY_ITEMS)
        )
        return len(self.driver.find_elements(*self.INVENTORY_ITEMS))

    def add_backpack_to_cart(self):
        """
        Wait for the Backpack "Add to Cart" button and click it.
        """
        add_button = self.wait.until(
            EC.element_to_be_clickable(self.ADD_BACKPACK_TO_CART_BUTTON)
        )
        add_button.click()

    def add_bike_light_to_cart(self):
        """
        Wait for the Bike Light "Add to Cart" button and click it.
        """
        add_button = self.wait.until(
            EC.element_to_be_clickable(self.ADD_BIKE_LIGHT_TO_CART_BUTTON)
        )
        add_button.click()

    def get_cart_badge_text(self):
        """
        Return the text (count) shown on the shopping cart badge.
        """
        badge = self.wait.until(
            EC.visibility_of_element_located(self.CART_BADGE)
        )
        return badge.text

    def go_to_cart(self):
        """
        Wait for the shopping cart link and click it to navigate to the Cart page.
        """
        cart_link = self.wait.until(
            EC.element_to_be_clickable(self.CART_LINK)
        )
        cart_link.click()