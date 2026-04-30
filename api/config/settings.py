"""
TR: API otomasyon paketi için konfigürasyon değerleri.
Bu modül, temel URL'leri ve zaman aşımı değerlerini test kodundan ayrı tutar.

EN: Configuration values for the API automation suite.
This module keeps base URLs and timeout values away from test code.
"""

# API servislerinin ana adresleri.
# Base URLs for the API services.
JSONPLACEHOLDER_BASE_URL = "https://jsonplaceholder.typicode.com"
DUMMYJSON_BASE_URL = "https://dummyjson.com"

# HTTP istekleri için varsayılan bekleme süresi (Saniye).
# Default timeout for HTTP requests (Seconds).
DEFAULT_TIMEOUT = 5