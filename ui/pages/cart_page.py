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
    REMOVE_ITEM_BUTTON = (By.XPATH, "//button[text()='Remove']")
    CHECKOUT_BUTTON = (By.ID, "checkout")
    CART_BADGE = (By.CSS_SELECTOR, ".shopping_cart_badge")

    def get_title_text(self):
        return self.get_text(self.PAGE_TITLE)

    def get_cart_item_count(self):
        # TR: find_elements kullanarak o anki listeyi döner.
        # EN: Returns the current list using find_elements.
        return len(self.driver.find_elements(*self.CART_ITEMS))

    def get_first_cart_item_name(self):
        return self.get_text(self.FIRST_CART_ITEM_NAME)

    def remove_first_cart_item(self):
        # TR: Direkt JS click ile tıklamayı garantiye alıyoruz (Headless CI ortamları için daha güvenilir)
        # EN: Using JS click to ensure it clicks in Headless CI environments.
        self.javascript_click(self.REMOVE_ITEM_BUTTON)

    def checkout(self, expected_url_part=None):
        """
        TR: Checkout butonuna tıklar. Eğer bir URL parçası verilirse o sayfaya geçene kadar bekler.
        EN: Click checkout button. If a URL part is provided, wait until navigation.
        """
        if expected_url_part:
            self.click_and_wait_for_url(self.CHECKOUT_BUTTON, expected_url_part)
        else:
            self.click(self.CHECKOUT_BUTTON)

    def wait_until_cart_item_count_is(self, expected_count):
        """
        TR: Sepetteki ürün sayısı beklenen değere ulaşana kadar bekler.
        EN: Waits until the number of items in the cart matches the expected count.
        """
        if expected_count == 0:
            self.wait.until(EC.invisibility_of_element_located(self.CART_ITEMS))
        else:
            self.wait.until(
                lambda driver: len(driver.find_elements(*self.CART_ITEMS)) == expected_count
            )
            
    def is_cart_empty(self):
        return self.get_cart_item_count() == 0
