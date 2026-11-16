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
