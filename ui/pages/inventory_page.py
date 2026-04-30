from selenium.webdriver.common.by import By

from ui.pages.base_page import BasePage


class InventoryPage(BasePage):
    """
    TR: Ürün listesi sayfası (Inventory) için Sayfa Nesnesi Modeli (Page Object Model).
    Bu sayfa, giriş yaptıktan sonra açılan ürünlerin listelendiği ana sayfadır.
    
    EN: Page Object Model for the Inventory Products page.
    This is the main page that opens after login, listing all available products.
    """

    # Element konumlandırıcıları (Locators)
    PAGE_TITLE = (By.CSS_SELECTOR, ".title")
    INVENTORY_ITEMS = (By.CSS_SELECTOR, ".inventory_item")

    # Ürün ekleme ve çıkarma butonları
    # Add to cart and remove buttons
    ADD_BACKPACK_TO_CART_BUTTON = (By.ID, "add-to-cart-sauce-labs-backpack")
    REMOVE_BACKPACK_FROM_CART_BUTTON = (By.ID, "remove-sauce-labs-backpack")

    ADD_BIKE_LIGHT_TO_CART_BUTTON = (By.ID, "add-to-cart-sauce-labs-bike-light")
    REMOVE_BIKE_LIGHT_FROM_CART_BUTTON = (By.ID, "remove-sauce-labs-bike-light")

    # Sepet ikonu ve üzerindeki sayı rozeti (badge)
    # Cart link and the badge showing item count
    CART_LINK = (By.CSS_SELECTOR, ".shopping_cart_link")
    CART_BADGE = (By.CSS_SELECTOR, ".shopping_cart_badge")
    CART_URL_PART = "cart.html"

    def get_title_text(self):
        """
        TR: Sayfa başlığının görünmesini bekler ve metnini döndürür.
        EN: Wait for the page title to be visible and return its text.
        """
        return self.get_text(self.PAGE_TITLE)

    def get_product_count(self):
        """
        TR: Sayfada görüntülenen toplam ürün sayısını döndürür.
        EN: Return the total number of products displayed on the page.
        """
        return self.count_elements(self.INVENTORY_ITEMS)

    def add_backpack_to_cart(self):
        """
        TR: Sırt çantasını sepete ekler ve UI'ın güncellendiğini doğrular (Remove butonu görünene kadar bekler).
        EN: Add the Backpack product to the cart and wait until the UI confirms it.
        """
        self.click_and_wait_for_visible_element(
            self.ADD_BACKPACK_TO_CART_BUTTON,
            self.REMOVE_BACKPACK_FROM_CART_BUTTON,
        )

    def add_bike_light_to_cart(self):
        """
        TR: Bisiklet ışığını sepete ekler ve UI'ın güncellendiğini doğrular.
        EN: Add the Bike Light product to the cart and wait until the UI confirms it.
        """
        self.click_and_wait_for_visible_element(
            self.ADD_BIKE_LIGHT_TO_CART_BUTTON,
            self.REMOVE_BIKE_LIGHT_FROM_CART_BUTTON,
        )

    def get_cart_badge_text(self):
        """
        TR: Sepet ikonundaki ürün sayısını döndürür.
        EN: Return the text count shown on the shopping cart badge.
        """
        return self.get_text(self.CART_BADGE)

    def wait_until_cart_badge_text_is(self, expected_text):
        """
        TR: Sepet ikonundaki sayının beklenen değere ulaşmasını bekler.
        EN: Wait until the shopping cart badge shows the expected text.
        """
        self.wait_for_text(self.CART_BADGE, expected_text)

    def go_to_cart(self):
        """
        TR: Sepet ikonuna tıklar ve sepet sayfasının URL'i yüklenene kadar bekler.
        EN: Click the shopping cart link and wait until the Cart page URL is loaded.
        """
        self.click_and_wait_for_url(self.CART_LINK, self.CART_URL_PART)