from playwright.sync_api import Locator, Page


class InventoryPage:
    INVENTORY_URL_PART = "inventory.html"

    def __init__(self, page: Page) -> None:
        self.page = page

        self.page_title: Locator = page.locator("[data-test='title']")
        self.inventory_items: Locator = page.locator("[data-test='inventory-item']")
        self.cart_link: Locator = page.locator("[data-test='shopping-cart-link']")
        self.cart_badge: Locator = page.locator("[data-test='shopping-cart-badge']")

    def product_title(self, product_name: str) -> Locator:
        return self.page.get_by_text(product_name, exact=True)

    def add_product_button(self, product_name: str) -> Locator:
        product_item = self.inventory_items.filter(has_text=product_name)
        return product_item.get_by_role("button", name="Add to cart")

    def remove_product_button(self, product_name: str) -> Locator:
        product_item = self.inventory_items.filter(has_text=product_name)
        return product_item.get_by_role("button", name="Remove")

    def add_product_to_cart(self, product_name: str) -> None:
        self.add_product_button(product_name).click()

    def remove_product_from_cart(self, product_name: str) -> None:
        self.remove_product_button(product_name).click()

    def open_cart(self) -> None:
        self.cart_link.click()
