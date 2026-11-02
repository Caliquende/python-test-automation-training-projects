from types import SimpleNamespace

import pytest
from selenium.common.exceptions import WebDriverException

from ui.selenium_pytest import conftest


@pytest.mark.parametrize("failure", [False, WebDriverException("capture failed")])
def test_screenshot_failure_creates_log_not_fake_png(tmp_path, monkeypatch, failure):
    class Driver:
        current_url = "https://example.test/"
        title = "Demo"

        def save_screenshot(self, path):
            if isinstance(failure, Exception):
                raise failure
            return failure

        def get_log(self, name):
            return []

    monkeypatch.setattr(conftest, "UI_REPORTS_DIR", tmp_path)
    item = SimpleNamespace(funcargs={"driver": Driver()}, nodeid="test_demo")
    result = SimpleNamespace(get_result=lambda: SimpleNamespace(when="call", failed=True))
    hook = conftest.pytest_runtest_makereport(item, None)
    next(hook)
    with pytest.raises(StopIteration):
        hook.send(result)

    assert not (tmp_path / "screenshots" / "test_demo.png").exists()
    assert "Screenshot could not be captured" in (
        tmp_path / "browser-console" / "test_demo.log"
    ).read_text(encoding="utf-8")
