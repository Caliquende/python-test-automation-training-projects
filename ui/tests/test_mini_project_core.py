import pytest

# Test verilerini ve sabitleri içe aktarıyoruz.
# Importing test data and constants.
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
    CHECKOUT_STEP_ONE_TITLE,
    INVENTORY_URL_PART,
    CART_URL_PART,
    CHECKOUT_STEP_ONE_URL_PART,
)


def _login_as_standard_user(login_page, inventory_page):
    """
    TR: Standart kullanıcı ile giriş yapar. 
    Sayfa nesneleri artık fixture olarak otomatik gelir.
    
    EN: Performs a standard user login. 
    Page objects are now automatically provided as fixtures.
    """
    login_page.open()
    login_page.login(STANDARD_USER["username"], STANDARD_USER["password"])


@pytest.mark.smoke
@pytest.mark.regression
def test_logged_in_user_sees_product_list(driver, login_page, inventory_page):
    """
    TR: Standart kullanıcının giriş yapıp ürün listesini gördüğünü doğrular.
    EN: Verify that a standard user can log in and see the product list.
    """
    _login_as_standard_user(login_page, inventory_page)

    assert inventory_page.get_title_text() == PRODUCTS_PAGE_TITLE
    assert inventory_page.get_product_count() == EXPECTED_PRODUCT_COUNT
    assert INVENTORY_URL_PART in driver.current_url


@pytest.mark.smoke
@pytest.mark.regression
def test_user_can_open_cart_after_login(driver, login_page, inventory_page, cart_page):
    """
    TR: Giriş yapmış kullanıcının alışveriş sepetine gidebildiğini doğrular.
    EN: Verify that a logged-in user can navigate to the shopping cart page.
    """
    _login_as_standard_user(login_page, inventory_page)

    assert inventory_page.get_title_text() == PRODUCTS_PAGE_TITLE

    inventory_page.go_to_cart()

    assert cart_page.get_title_text() == CART_PAGE_TITLE
    assert CART_URL_PART in driver.current_url


@pytest.mark.regression
def test_user_can_add_backpack_to_cart_and_see_it_in_cart(login_page, inventory_page, cart_page):
    """
    TR: Sepete ürün eklemenin sepet ikonundaki sayıyı güncellediğini ve ürünün sepette göründüğünü doğrular.
    EN: Verify that adding an item to the cart updates the badge and shows the item in the cart page.
    """
    _login_as_standard_user(login_page, inventory_page)

    inventory_page.add_backpack_to_cart()
    inventory_page.wait_until_cart_badge_text_is(CART_BADGE_ONE_ITEM)

    assert inventory_page.get_cart_badge_text() == CART_BADGE_ONE_ITEM

    inventory_page.go_to_cart()

    assert cart_page.get_title_text() == CART_PAGE_TITLE
    assert cart_page.get_cart_item_count() == 1
    assert cart_page.get_first_cart_item_name() == SAUCE_LABS_BACKPACK


@pytest.mark.regression
def test_adding_two_products_updates_cart_badge_to_two(login_page, inventory_page):
    """
    TR: Birden fazla ürün eklendiğinde sepet sayısının doğru şekilde arttığını doğrular.
    EN: Verify that the cart badge count increments correctly when multiple items are added.
    """
    _login_as_standard_user(login_page, inventory_page)

    inventory_page.add_backpack_to_cart()
    inventory_page.wait_until_cart_badge_text_is(CART_BADGE_ONE_ITEM)

    inventory_page.add_bike_light_to_cart()
    inventory_page.wait_until_cart_badge_text_is(CART_BADGE_TWO_ITEMS)

    assert inventory_page.get_cart_badge_text() == CART_BADGE_TWO_ITEMS


@pytest.mark.regression
def test_user_can_add_backpack_to_cart_and_remove_it_from_cart(login_page, inventory_page, cart_page):
    """
    TR: Sepete eklenen bir ürünün sepet sayfasından silinebildiğini doğrular.
    EN: Verify that an item added to the cart can be removed from the cart page.
    """
    _login_as_standard_user(login_page, inventory_page)

    inventory_page.add_backpack_to_cart()
    inventory_page.wait_until_cart_badge_text_is(CART_BADGE_ONE_ITEM)

    inventory_page.go_to_cart()

    assert cart_page.get_cart_item_count() == 1

    cart_page.remove_first_cart_item()
    cart_page.wait_until_cart_item_count_is(0)

    assert cart_page.get_cart_item_count() == 0
    assert cart_page.is_cart_empty()


@pytest.mark.regression
def test_user_can_add_backpack_to_cart_and_checkout(driver, login_page, inventory_page, cart_page):
    """
    TR: Ürün ekledikten sonra ödeme (checkout) sayfasına ilerlenebildiğini doğrular.
    EN: Verify that a user can proceed to the checkout page after adding an item.
    """
    _login_as_standard_user(login_page, inventory_page)

    inventory_page.add_backpack_to_cart()
    inventory_page.go_to_cart()

    assert cart_page.get_cart_item_count() == 1

    cart_page.checkout()

    # TR: Checkout sayfasına geçildiğini doğrularız.
    # EN: Verify that we have navigated to the checkout page.
    assert cart_page.get_title_text() == CHECKOUT_STEP_ONE_TITLE
    assert CHECKOUT_STEP_ONE_URL_PART in driver.current_url


@pytest.mark.regression
def test_user_can_add_two_items_to_cart_and_checkout(driver, login_page, inventory_page, cart_page):
    """
    TR: İki ürün ekledikten sonra ödeme sayfasına ilerlenebildiğini doğrular.
    EN: Verify that a user can proceed to checkout with multiple items in the cart.
    """
    _login_as_standard_user(login_page, inventory_page)

    inventory_page.add_backpack_to_cart()
    inventory_page.add_bike_light_to_cart()
    inventory_page.go_to_cart()

    assert cart_page.get_cart_item_count() == 2

    cart_page.checkout()

    assert cart_page.get_title_text() == CHECKOUT_STEP_ONE_TITLE
    assert CHECKOUT_STEP_ONE_URL_PART in driver.current_url