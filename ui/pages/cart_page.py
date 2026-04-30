from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from ui.pages.base_page import BasePage


class CartPage(BasePage):
    """
    TR: Alışveriş Sepeti sayfası için Sayfa Nesnesi Modeli (Page Object Model).
    EN: Page Object Model for the Cart page.
    """

    # Element konumlandırıcıları (Locators)
    PAGE_TITLE = (By.CSS_SELECTOR, ".title")
    CART_ITEMS = (By.CSS_SELECTOR, ".cart_item")
    FIRST_CART_ITEM_NAME = (By.CSS_SELECTOR, ".inventory_item_name")
    REMOVE_ITEM_BUTTON = (By.CSS_SELECTOR, ".cart_button")
    CHECKOUT_BUTTON = (By.ID, "checkout")
    CART_BADGE = (By.CSS_SELECTOR, ".shopping_cart_badge")

    def get_title_text(self):
        return self.get_text(self.PAGE_TITLE)

    def get_cart_item_count(self):
        # TR: find_elements kullanarak o anki listeyi döner (beklemez).
        # EN: Returns the current list using find_elements (does not wait).
        return len(self.driver.find_elements(*self.CART_ITEMS))

    def get_first_cart_item_name(self):
        return self.get_text(self.FIRST_CART_ITEM_NAME)

    def remove_first_cart_item(self):
        self.click(self.REMOVE_ITEM_BUTTON)

    def checkout(self):
        self.click(self.CHECKOUT_BUTTON)

    def wait_until_cart_item_count_is(self, expected_count):
        """
        TR: Sepetteki ürün sayısı beklenen değere ulaşana kadar bekler.
        EN: Waits until the number of items in the cart matches the expected count.
        """
        if expected_count == 0:
            # TR: Eğer 0 bekliyorsak, tüm elemanların DOM'dan kaybolmasını beklemek daha güvenlidir.
            # EN: If expecting 0, it's safer to wait for all elements to be absent from the DOM.
            self.wait.until(
                EC.invisibility_of_element_located(self.CART_ITEMS)
            )
        else:
            self.wait.until(
                lambda driver: len(driver.find_elements(*self.CART_ITEMS)) == expected_count
            )
            
    def is_cart_empty(self):
        """
        TR: Sepetin tamamen boş olduğunu (badge'in olmadığını) kontrol eder.
        EN: Checks if the cart is completely empty (no badge present).
        """
        return len(self.driver.find_elements(*self.CART_BADGE)) == 0
