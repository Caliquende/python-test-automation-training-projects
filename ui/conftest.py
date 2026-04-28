import pytest
from selenium import webdriver


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
