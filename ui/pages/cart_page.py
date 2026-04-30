from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from ui.pages.base_page import BasePage


class CartPage(BasePage):
    """
    TR: Alışveriş Sepeti sayfası için Sayfa Nesnesi Modeli (Page Object Model).
    Bu sayfa, sepete eklenen ürünlerin listelendiği sayfadır.
    
    EN: Page Object Model for the Cart page.
    This page lists the items that have been added to the shopping cart.
    """

    # Element konumlandırıcıları (Locators)
    PAGE_TITLE = (By.CSS_SELECTOR, ".title")
    CART_ITEMS = (By.CSS_SELECTOR, ".cart_item")
    FIRST_CART_ITEM_NAME = (By.CSS_SELECTOR, ".inventory_item_name")
    
    # Yeni eklenen locatorlar
    REMOVE_ITEM_BUTTON = (By.CSS_SELECTOR, ".cart_button")
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def get_title_text(self):
        """
        TR: Sayfa başlığının görünmesini bekler ve metnini döndürür.
        EN: Wait for the page title to be visible and return its text.
        """
        return self.get_text(self.PAGE_TITLE)

    def get_cart_item_count(self):
        """
        TR: Sepette o an bulunan toplam ürün sayısını döndürür.
        EN: Return the total number of items currently in the cart.
        """
        return len(self.driver.find_elements(*self.CART_ITEMS))

    def get_first_cart_item_name(self):
        """
        TR: Sepetteki ilk ürünün ismini döndürür.
        EN: Wait for the first item in the cart to be visible and return its name.
        """
        return self.get_text(self.FIRST_CART_ITEM_NAME)

    def remove_first_cart_item(self):
        """
        TR: Sepetteki ilk ürünü kaldırır.
        EN: Removes the first item from the cart.
        """
        self.click(self.REMOVE_ITEM_BUTTON)

    def checkout(self):
        """
        TR: Ödeme (Checkout) işlemini başlatır.
        EN: Starts the checkout process.
        """
        self.click(self.CHECKOUT_BUTTON)

    def wait_until_cart_item_count_is(self, expected_count):
        """
        TR: Sepetteki ürün sayısı beklenen değere ulaşana kadar bekler.
        EN: Waits until the number of items in the cart matches the expected count.
        """
        self.wait.until(
            lambda driver: len(driver.find_elements(*self.CART_ITEMS)) == expected_count
        )
