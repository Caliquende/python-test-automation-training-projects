from unittest.mock import Mock, PropertyMock, call

import pytest
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.remote.webelement import WebElement

from ui.selenium_pytest.data.ui_texts import (
    CHECKOUT_STEP_ONE_TITLE,
    CHECKOUT_STEP_ONE_URL_PART,
)
from ui.selenium_pytest.pages.cart_page import CartPage
from ui.selenium_pytest.pages.inventory_page import InventoryPage


def test_cart_navigation_waits_for_delayed_render(driver, tmp_path):
    page = tmp_path / "inventory.html"
    page.write_text(
        """<!doctype html>
<html><body>
  <span class="title">Products</span>
  <a class="shopping_cart_link" href="#">Cart</a>
  <script>
    document.querySelector('.shopping_cart_link').addEventListener('click', (event) => {
      event.preventDefault();
      history.pushState({}, '', '?route=cart.html');
      setTimeout(() => {
        document.querySelector('.title').textContent = 'Your Cart';
        const cart = document.createElement('div');
        cart.className = 'cart_list';
        cart.textContent = 'Cart contents';
        document.body.appendChild(cart);
      }, 1200);
    });
  </script>
</body></html>""",
        encoding="utf-8",
    )
    driver.get(page.as_uri())

    InventoryPage(driver).go_to_cart()

    assert CartPage(driver).get_title_text() == "Your Cart"


def test_checkout_waits_for_the_form_after_the_url_changes(driver, tmp_path):
    page = tmp_path / "cart.html"
    page.write_text(
        """<!doctype html>
<html><body>
  <span class="title">Your Cart</span>
  <button id="checkout">Checkout</button>
  <script>
    document.querySelector('#checkout').addEventListener('click', () => {
      history.pushState({}, '', '?route=checkout-step-one.html');
      setTimeout(() => {
        const title = document.createElement('span');
        title.className = 'title';
        title.textContent = 'Checkout: Your Information';
        document.querySelector('.title').replaceWith(title);

        const firstName = document.createElement('input');
        firstName.id = 'first-name';
        document.body.appendChild(firstName);
      }, 1200);
    });
  </script>
</body></html>""",
        encoding="utf-8",
    )
    driver.get(page.as_uri())
    cart_page = CartPage(driver)

    cart_page.checkout(expected_url_part=CHECKOUT_STEP_ONE_URL_PART)

    assert cart_page.get_title_text() == CHECKOUT_STEP_ONE_TITLE
    assert CHECKOUT_STEP_ONE_URL_PART in cart_page.get_current_url()


@pytest.mark.parametrize("expected_text", [CHECKOUT_STEP_ONE_TITLE, ""])
def test_title_is_relocated_when_the_dom_replaces_it_during_the_read(expected_text):
    stale_title = Mock(spec=WebElement)
    stale_title.is_displayed.return_value = True
    type(stale_title).text = PropertyMock(side_effect=StaleElementReferenceException)
    current_title = Mock(spec=WebElement)
    current_title.is_displayed.return_value = True
    current_title.text = expected_text
    driver = Mock()
    driver.find_element.side_effect = [stale_title, current_title]
    cart_page = CartPage(driver)

    assert cart_page.get_title_text() == expected_text
    assert driver.find_element.call_args_list == [call(*CartPage.PAGE_TITLE)] * 2
