import pytest
from selenium import webdriver

from ui.config.settings import HEADLESS


@pytest.fixture
def driver():
    """
    Pytest fixture to initialize and quit the Chrome WebDriver.
    Disables the password manager and credential service for a cleaner test environment.
    Supports headless execution for CI environments.
    """
    options = webdriver.ChromeOptions()

    if HEADLESS:
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")

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