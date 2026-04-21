from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    PAGE_TITLE = (By.CSS_SELECTOR, ".title")
    CART_ITEMS = (By.CSS_SELECTOR, ".cart_item")
    FIRST_CART_ITEM_NAME = (By.CSS_SELECTOR, ".inventory_item_name")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def get_title_text(self):
        title = self.wait.until(
            EC.visibility_of_element_located(self.PAGE_TITLE)
        )
        return title.text

    def get_cart_item_count(self):
        self.wait.until(
            EC.visibility_of_element_located(self.PAGE_TITLE)
        )
        return len(self.driver.find_elements(*self.CART_ITEMS))

    def get_first_cart_item_name(self):
        item_name = self.wait.until(
            EC.visibility_of_element_located(self.FIRST_CART_ITEM_NAME)
        )
        return item_name.text