import re
from pathlib import Path

import pytest
from selenium import webdriver
from selenium.common.exceptions import WebDriverException

from ui.config.settings import HEADLESS
from ui.pages.login_page import LoginPage
from ui.pages.inventory_page import InventoryPage
from ui.pages.cart_page import CartPage


UI_REPORTS_DIR = Path("reports") / "ui"


def _safe_artifact_name(nodeid):
    """
    TR: Pytest nodeid değerini dosya adı olarak güvenli hale getirir.
    EN: Convert a Pytest nodeid into a safe artifact file name.
    """
    return re.sub(r"[^A-Za-z0-9_.-]+", "_", nodeid).strip("_")


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    TR: UI testi başarısız olduğunda screenshot ve browser console log üretir.
    EN: Capture screenshot and browser console logs when a UI test fails.
    """
    outcome = yield
    report = outcome.get_result()

    if report.when != "call" or not report.failed:
        return

    driver = item.funcargs.get("driver")

    if driver is None:
        return

    artifact_name = _safe_artifact_name(item.nodeid)
    screenshots_dir = UI_REPORTS_DIR / "screenshots"
    console_logs_dir = UI_REPORTS_DIR / "browser-console"
    screenshots_dir.mkdir(parents=True, exist_ok=True)
    console_logs_dir.mkdir(parents=True, exist_ok=True)

    screenshot_path = screenshots_dir / f"{artifact_name}.png"
    console_log_path = console_logs_dir / f"{artifact_name}.log"

    try:
        driver.save_screenshot(str(screenshot_path))
    except WebDriverException as exc:
        screenshot_path.write_text(
            f"Screenshot could not be captured: {exc}\n",
            encoding="utf-8",
        )

    log_lines = []

    try:
        log_lines.append(f"URL: {driver.current_url}")
        log_lines.append(f"Title: {driver.title}")
        log_lines.append("")

        browser_logs = driver.get_log("browser")

        if browser_logs:
            for entry in browser_logs:
                log_lines.append(
                    f"{entry.get('level', 'UNKNOWN')} "
                    f"{entry.get('timestamp', '')} "
                    f"{entry.get('message', '')}"
                )
        else:
            log_lines.append("No browser console entries were captured.")
    except WebDriverException as exc:
        log_lines.append(f"Browser console log could not be captured: {exc}")

    console_log_path.write_text("\n".join(log_lines) + "\n", encoding="utf-8")


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
    options.set_capability("goog:loggingPrefs", {"browser": "ALL"})

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
