import pytest
from selenium import webdriver

from ui.config.settings import HEADLESS


@pytest.fixture
def driver():
    """
    Pytest fixture to initialize and quit the Chrome WebDriver.

    The fixture supports both local visible browser execution and
    headless execution for CI environments.
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