import pytest
from selenium import webdriver

from projects.ui.pages.login_page import LoginPage
from projects.ui.pages.inventory_page import InventoryPage
from projects.ui.pages.cart_page import CartPage


@pytest.fixture
def driver():
    """
    Pytest fixture to initialize and quit the Chrome WebDriver.
    Disables the password manager and credential service for a cleaner test environment.
    """
    options = webdriver.ChromeOptions()
    options.add_experimental_option(
        "prefs",
        {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
        },
    )

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()


def _login_as_standard_user(driver):
    """
    Helper function to perform a standard user login and return relevant page objects.
    """
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    return inventory_page, cart_page


def test_logged_in_user_sees_product_list(driver):
    """
    Verify that a standard user can log in and see the product list.
    """
    inventory_page, _ = _login_as_standard_user(driver)

    # Verify page title and product count
    assert inventory_page.get_title_text() == "Products"
    assert inventory_page.get_product_count() == 6
    assert "inventory.html" in driver.current_url


def test_user_can_open_cart_after_login(driver):
    """
    Verify that a logged-in user can navigate to the shopping cart page.
    """
    inventory_page, cart_page = _login_as_standard_user(driver)

    assert inventory_page.get_title_text() == "Products"

    # Navigate to the cart
    inventory_page.go_to_cart()

    # Verify successful navigation to the cart
    assert cart_page.get_title_text() == "Your Cart"
    assert "cart.html" in driver.current_url


def test_user_can_add_backpack_to_cart_and_see_it_in_cart(driver):
    """
    Verify that adding an item to the cart updates the badge and shows the item in the cart page.
    """
    inventory_page, cart_page = _login_as_standard_user(driver)

    # Add a specific product
    inventory_page.add_backpack_to_cart()

    # Verify badge update
    assert inventory_page.get_cart_badge_text() == "1"

    # Go to cart to verify item details
    inventory_page.go_to_cart()

    assert cart_page.get_title_text() == "Your Cart"
    assert cart_page.get_cart_item_count() == 1
    assert cart_page.get_first_cart_item_name() == "Sauce Labs Backpack"
    assert "cart.html" in driver.current_url


def test_adding_two_products_updates_cart_badge_to_two(driver):
    """
    Verify that the cart badge count increments correctly when multiple items are added.
    """
    inventory_page, _ = _login_as_standard_user(driver)

    # Add multiple products
    inventory_page.add_backpack_to_cart()
    inventory_page.add_bike_light_to_cart()

    # Verify final badge count
    assert inventory_page.get_cart_badge_text() == "2"
