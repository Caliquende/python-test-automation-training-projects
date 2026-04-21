from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:
    PAGE_TITLE = (By.CSS_SELECTOR, ".title")
    INVENTORY_ITEMS = (By.CSS_SELECTOR, ".inventory_item")
    ADD_BACKPACK_TO_CART_BUTTON = (By.ID, "add-to-cart-sauce-labs-backpack")
    ADD_BIKE_LIGHT_TO_CART_BUTTON = (By.ID, "add-to-cart-sauce-labs-bike-light")
    CART_LINK = (By.CSS_SELECTOR, ".shopping_cart_link")
    CART_BADGE = (By.CSS_SELECTOR, ".shopping_cart_badge")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def get_title_text(self):
        title = self.wait.until(
            EC.visibility_of_element_located(self.PAGE_TITLE)
        )
        return title.text

    def get_product_count(self):
        self.wait.until(
            EC.visibility_of_all_elements_located(self.INVENTORY_ITEMS)
        )
        return len(self.driver.find_elements(*self.INVENTORY_ITEMS))

    def add_backpack_to_cart(self):
        add_button = self.wait.until(
            EC.element_to_be_clickable(self.ADD_BACKPACK_TO_CART_BUTTON)
        )
        add_button.click()

    def add_bike_light_to_cart(self):
        add_button = self.wait.until(
            EC.element_to_be_clickable(self.ADD_BIKE_LIGHT_TO_CART_BUTTON)
        )
        add_button.click()

    def get_cart_badge_text(self):
        badge = self.wait.until(
            EC.visibility_of_element_located(self.CART_BADGE)
        )
        return badge.text

    def go_to_cart(self):
        cart_link = self.wait.until(
            EC.element_to_be_clickable(self.CART_LINK)
        )
        cart_link.click()