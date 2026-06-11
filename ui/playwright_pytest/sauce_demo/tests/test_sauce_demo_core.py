import re

import pytest
from playwright.sync_api import Page, expect

from ui.playwright_pytest.sauce_demo.data.products import (
    CART_BADGE_ONE_ITEM,
    CART_BADGE_TWO_ITEMS,
    EXPECTED_PRODUCT_COUNT,
    SAUCE_LABS_BACKPACK,
    SAUCE_LABS_BIKE_LIGHT,
)
from ui.playwright_pytest.sauce_demo.data.ui_texts import (
    CART_PAGE_TITLE,
    CHECKOUT_STEP_ONE_TITLE,
    PRODUCTS_PAGE_TITLE,
)
from ui.playwright_pytest.sauce_demo.pages.cart_page import CartPage
from ui.playwright_pytest.sauce_demo.pages.inventory_page import InventoryPage
from ui.playwright_pytest.sauce_demo.pages.login_page import LoginPage


def _login_as_standard_user(
    login_page: LoginPage,
    standard_user_credentials: dict[str, str],
) -> None:
    login_page.open()
    login_page.login_with(
        standard_user_credentials["username"],
        standard_user_credentials["password"],
    )


@pytest.mark.smoke
@pytest.mark.regression
def test_standard_user_sees_product_list_after_login(
    page: Page,
    login_page: LoginPage,
    inventory_page: InventoryPage,
    standard_user_credentials: dict[str, str],
) -> None:
    """
    TR: Standart kullanıcının giriş yapıp ürün listesini gördüğünü doğrular.
    EN: Verifies that a standard user can log in and see the product list.

    Learning focus:
    - Using a Page Object fixture with pytest-playwright's page fixture
    - Performing login through a user-focused action method
    - Verifying URL and user-visible inventory results together
    - Keeping assertions inside the test
    """
    _login_as_standard_user(login_page, standard_user_credentials)

    expect(page).to_have_url(re.compile(InventoryPage.INVENTORY_URL_PART))
    expect(inventory_page.page_title).to_have_text(PRODUCTS_PAGE_TITLE)
    expect(inventory_page.inventory_items).to_have_count(EXPECTED_PRODUCT_COUNT)
    expect(inventory_page.product_title(SAUCE_LABS_BACKPACK)).to_be_visible()


@pytest.mark.smoke
@pytest.mark.regression
def test_logged_in_user_can_open_cart(
    page: Page,
    login_page: LoginPage,
    inventory_page: InventoryPage,
    cart_page: CartPage,
    standard_user_credentials: dict[str, str],
) -> None:
    """
    TR: Giriş yapmış kullanıcının alışveriş sepetine gidebildiğini doğrular.
    EN: Verifies that a logged-in user can navigate to the shopping cart page.

    Learning focus:
    - Reusing page object fixtures without hiding the login flow
    - Navigating through a user-focused action method
    - Verifying URL and cart page title together
    - Keeping navigation assertions inside the test
    """
    _login_as_standard_user(login_page, standard_user_credentials)

    expect(inventory_page.page_title).to_have_text(PRODUCTS_PAGE_TITLE)

    inventory_page.open_cart()

    expect(page).to_have_url(re.compile(CartPage.CART_URL_PART))
    expect(cart_page.page_title).to_have_text(CART_PAGE_TITLE)


@pytest.mark.regression
def test_user_can_add_backpack_to_cart_and_see_it_in_cart(
    login_page: LoginPage,
    inventory_page: InventoryPage,
    cart_page: CartPage,
    standard_user_credentials: dict[str, str],
) -> None:
    """
    TR: Sepete ürün eklemenin rozeti güncellediğini ve ürünün sepette göründüğünü doğrular.
    EN: Verifies that adding an item updates the cart badge and shows the item in the cart.

    Learning focus:
    - Using dynamic product locators inside the page object
    - Adding a product through a user-focused action method
    - Verifying badge text and cart content in the test
    - Keeping cart state isolated per test
    """
    _login_as_standard_user(login_page, standard_user_credentials)

    inventory_page.add_product_to_cart(SAUCE_LABS_BACKPACK)

    expect(inventory_page.cart_badge).to_have_text(CART_BADGE_ONE_ITEM)
    expect(inventory_page.remove_product_button(SAUCE_LABS_BACKPACK)).to_be_visible()

    inventory_page.open_cart()

    expect(cart_page.page_title).to_have_text(CART_PAGE_TITLE)
    expect(cart_page.cart_items).to_have_count(1)
    expect(cart_page.cart_item(SAUCE_LABS_BACKPACK)).to_be_visible()


@pytest.mark.regression
def test_adding_two_products_updates_cart_badge_to_two(
    login_page: LoginPage,
    inventory_page: InventoryPage,
    standard_user_credentials: dict[str, str],
) -> None:
    """
    TR: Birden fazla ürün eklendiğinde sepet rozetinin doğru şekilde arttığını doğrular.
    EN: Verifies that the cart badge increments correctly when multiple items are added.

    Learning focus:
    - Reusing one dynamic action method for different products
    - Verifying visible cart badge state after each user action
    - Avoiding duplicate tests that only vary by product data
    - Keeping assertions inside the test
    """
    _login_as_standard_user(login_page, standard_user_credentials)

    inventory_page.add_product_to_cart(SAUCE_LABS_BACKPACK)

    expect(inventory_page.cart_badge).to_have_text(CART_BADGE_ONE_ITEM)

    inventory_page.add_product_to_cart(SAUCE_LABS_BIKE_LIGHT)

    expect(inventory_page.cart_badge).to_have_text(CART_BADGE_TWO_ITEMS)


@pytest.mark.regression
def test_user_can_add_backpack_to_cart_and_remove_it_from_cart(
    login_page: LoginPage,
    inventory_page: InventoryPage,
    cart_page: CartPage,
    standard_user_credentials: dict[str, str],
) -> None:
    """
    TR: Sepete eklenen bir ürünün sepet sayfasından silinebildiğini doğrular.
    EN: Verifies that an item added to the cart can be removed from the cart page.

    Learning focus:
    - Moving from inventory to cart through page object actions
    - Removing a product through a dynamic cart locator
    - Verifying the empty cart state with locator count
    - Relying on Playwright expect retry instead of explicit waits
    """
    _login_as_standard_user(login_page, standard_user_credentials)

    inventory_page.add_product_to_cart(SAUCE_LABS_BACKPACK)
    expect(inventory_page.cart_badge).to_have_text(CART_BADGE_ONE_ITEM)

    inventory_page.open_cart()
    expect(cart_page.cart_items).to_have_count(1)

    cart_page.remove_product_from_cart(SAUCE_LABS_BACKPACK)

    expect(cart_page.cart_items).to_have_count(0)
    expect(cart_page.cart_item(SAUCE_LABS_BACKPACK)).not_to_be_visible()


@pytest.mark.regression
def test_user_can_add_backpack_to_cart_and_checkout(
    page: Page,
    login_page: LoginPage,
    inventory_page: InventoryPage,
    cart_page: CartPage,
    standard_user_credentials: dict[str, str],
) -> None:
    """
    TR: Ürün ekledikten sonra checkout sayfasına ilerlenebildiğini doğrular.
    EN: Verifies that a user can proceed to checkout after adding an item.

    Learning focus:
    - Building a complete user flow with small page object actions
    - Verifying cart content before checkout
    - Verifying checkout URL and visible page title together
    - Keeping expected outcomes in the test
    """
    _login_as_standard_user(login_page, standard_user_credentials)

    inventory_page.add_product_to_cart(SAUCE_LABS_BACKPACK)
    inventory_page.open_cart()

    expect(cart_page.cart_items).to_have_count(1)
    expect(cart_page.cart_item(SAUCE_LABS_BACKPACK)).to_be_visible()

    cart_page.checkout()

    expect(page).to_have_url(re.compile(CartPage.CHECKOUT_STEP_ONE_URL_PART))
    expect(cart_page.page_title).to_have_text(CHECKOUT_STEP_ONE_TITLE)


@pytest.mark.regression
def test_user_can_add_two_items_to_cart_and_checkout(
    page: Page,
    login_page: LoginPage,
    inventory_page: InventoryPage,
    cart_page: CartPage,
    standard_user_credentials: dict[str, str],
) -> None:
    """
    TR: İki ürün ekledikten sonra checkout sayfasına ilerlenebildiğini doğrular.
    EN: Verifies that a user can proceed to checkout with multiple items in the cart.

    Learning focus:
    - Reusing product actions for a multi-item cart flow
    - Verifying cart item count before checkout
    - Verifying navigation and user-visible checkout state
    - Keeping tests independent from previous cart state
    """
    _login_as_standard_user(login_page, standard_user_credentials)

    inventory_page.add_product_to_cart(SAUCE_LABS_BACKPACK)
    inventory_page.add_product_to_cart(SAUCE_LABS_BIKE_LIGHT)
    inventory_page.open_cart()

    expect(cart_page.cart_items).to_have_count(2)
    expect(cart_page.cart_item(SAUCE_LABS_BACKPACK)).to_be_visible()
    expect(cart_page.cart_item(SAUCE_LABS_BIKE_LIGHT)).to_be_visible()

    cart_page.checkout()

    expect(page).to_have_url(re.compile(CartPage.CHECKOUT_STEP_ONE_URL_PART))
    expect(cart_page.page_title).to_have_text(CHECKOUT_STEP_ONE_TITLE)
