"""
TR: UI otomasyon paketi için konfigürasyon değerleri.
Bu modül, ortam düzeyindeki değerleri (URL, zaman aşımı vb.) test ve sayfa nesnesi kodundan ayrı tutar.

EN: Configuration values for the UI automation suite.
This module keeps environment-level values away from test and page object code.
"""

import os

# Test edilecek web sitesinin ana adresi.
# The main address of the website to be tested.
BASE_URL = "https://www.saucedemo.com/"

# Elementlerin bulunması için beklenecek varsayılan saniye (Explicit Wait).
# Default seconds to wait for elements (Explicit Wait).
DEFAULT_TIMEOUT = 10

# 'Headless' modun aktif olup olmadığını ortam değişkenlerinden (environment variables) kontrol eder.
# Varsayılan olarak headless çalışır; headed çalışma için HEADLESS=false kullanılabilir.
# Checks if 'Headless' mode is active from environment variables.
# Runs headless by default; use HEADLESS=false for headed execution.
HEADLESS = os.getenv("HEADLESS", "true").lower() == "true"
