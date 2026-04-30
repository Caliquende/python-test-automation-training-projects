import pytest
from selenium import webdriver

from ui.config.settings import HEADLESS
from ui.pages.login_page import LoginPage
from ui.pages.inventory_page import InventoryPage
from ui.pages.cart_page import CartPage


@pytest.fixture
def driver():
    """
    TR: Chrome WebDriver'ı başlatan ve test bittikten sonra kapatan Pytest fixture'ı.
    EN: Pytest fixture to initialize and quit the Chrome WebDriver.
    """
    options = webdriver.ChromeOptions()

    if HEADLESS:
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-extensions")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--log-level=3")

    options.add_experimental_option(
        "prefs",
        {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
        },
    )

    driver = webdriver.Chrome(options=options)

    if HEADLESS:
        driver.set_window_size(1920, 1080)
    else:
        driver.maximize_window()

    yield driver

    driver.quit()


@pytest.fixture
def login_page(driver):
    """
    TR: Giriş sayfası nesnesini (Page Object) sağlar.
    EN: Provides the Login page object.
    """
    return LoginPage(driver)


@pytest.fixture
def inventory_page(driver):
    """
    TR: Ürün listesi sayfası nesnesini sağlar.
    EN: Provides the Inventory page object.
    """
    return InventoryPage(driver)


@pytest.fixture
def cart_page(driver):
    """
    TR: Sepet sayfası nesnesini sağlar.
    EN: Provides the Cart page object.
    """
    return CartPage(driver)