import pytest

from ui.pages.login_page import LoginPage
from ui.pages.inventory_page import InventoryPage
from ui.pages.cart_page import CartPage

from ui.data.users import STANDARD_USER
from ui.data.products import (
    SAUCE_LABS_BACKPACK,
    EXPECTED_PRODUCT_COUNT,
    CART_BADGE_ONE_ITEM,
    CART_BADGE_TWO_ITEMS,
)
from ui.data.ui_texts import (
    PRODUCTS_PAGE_TITLE,
    CART_PAGE_TITLE,
    INVENTORY_URL_PART,
    CART_URL_PART,
)



def _login_as_standard_user(driver):
    """
    Helper function to perform a standard user login and return relevant page objects.
    """
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)

    login_page.open()
    login_page.login(STANDARD_USER["username"], STANDARD_USER["password"])

    return inventory_page, cart_page

@pytest.mark.smoke
@pytest.mark.regression
def test_logged_in_user_sees_product_list(driver):
    """
    Verify that a standard user can log in and see the product list.
    """
    inventory_page, _ = _login_as_standard_user(driver)

    # Verify page title and product count
    assert inventory_page.get_title_text() == PRODUCTS_PAGE_TITLE
    assert inventory_page.get_product_count() == EXPECTED_PRODUCT_COUNT
    assert INVENTORY_URL_PART in driver.current_url

@pytest.mark.smoke
@pytest.mark.regression
def test_user_can_open_cart_after_login(driver):
    """
    Verify that a logged-in user can navigate to the shopping cart page.
    """
    inventory_page, cart_page = _login_as_standard_user(driver)

    assert inventory_page.get_title_text() == PRODUCTS_PAGE_TITLE

    # Navigate to the cart
    inventory_page.go_to_cart()

    # Verify successful navigation to the cart
    assert cart_page.get_title_text() == CART_PAGE_TITLE
    assert CART_URL_PART in driver.current_url

@pytest.mark.regression
def test_user_can_add_backpack_to_cart_and_see_it_in_cart(driver):
    """
    Verify that adding an item to the cart updates the badge and shows the item in the cart page.
    """
    inventory_page, cart_page = _login_as_standard_user(driver)

    # Add a specific product
    inventory_page.add_backpack_to_cart()

    # Verify badge update
    assert inventory_page.get_cart_badge_text() == CART_BADGE_ONE_ITEM

    # Go to cart to verify item details
    inventory_page.go_to_cart()

    assert cart_page.get_title_text() == CART_PAGE_TITLE
    assert cart_page.get_cart_item_count() == 1
    assert cart_page.get_first_cart_item_name() == SAUCE_LABS_BACKPACK
    assert CART_URL_PART in driver.current_url


@pytest.mark.regression
def test_adding_two_products_updates_cart_badge_to_two(driver):
    """
    Verify that the cart badge count increments correctly when multiple items are added.
    """
    inventory_page, _ = _login_as_standard_user(driver)

    # Add multiple products
    inventory_page.add_backpack_to_cart()
    inventory_page.add_bike_light_to_cart()

    # Verify final badge count
    assert inventory_page.get_cart_badge_text() == CART_BADGE_TWO_ITEMS
