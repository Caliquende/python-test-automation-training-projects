"""
TR: SauceDemo UI testleri için test kullanıcıları.
Bu modül, kullanıcı bilgilerini test senaryolarından ayrı tutarak yönetilebilirliği artırır.

EN: Test users for SauceDemo UI tests.
This module keeps user credentials away from test case code for better maintainability.
"""

from env_loader import get_required_env


# Standart kullanıcı giriş bilgileri.
# Standard user credentials.
STANDARD_USER = {
    "username": get_required_env("SAUCEDEMO_STANDARD_USERNAME"),
    "password": get_required_env("SAUCEDEMO_STANDARD_PASSWORD"),
}
