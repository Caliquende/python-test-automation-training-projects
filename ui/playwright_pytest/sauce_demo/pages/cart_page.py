from playwright.sync_api import Locator, Page


class CartPage:
    CART_URL_PART = "cart.html"
    CHECKOUT_STEP_ONE_URL_PART = "checkout-step-one.html"

    def __init__(self, page: Page) -> None:
        self.page = page

        self.page_title: Locator = page.locator("[data-test='title']")
        self.cart_items: Locator = page.locator("[data-test='inventory-item']")
        self.checkout_button: Locator = page.locator("[data-test='checkout']")

    def cart_item(self, product_name: str) -> Locator:
        return self.cart_items.filter(has_text=product_name)

    def remove_product_button(self, product_name: str) -> Locator:
        return self.cart_item(product_name).get_by_role("button", name="Remove")

    def remove_product_from_cart(self, product_name: str) -> None:
        self.remove_product_button(product_name).click()

    def checkout(self) -> None:
        self.checkout_button.click()
