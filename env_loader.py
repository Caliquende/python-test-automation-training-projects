"""
TR: Test konfigürasyonu için küçük .env yükleyici.
EN: Small .env loader for test configuration.
"""

import os
from pathlib import Path


ENV_FILE = Path(__file__).resolve().parent / ".env"
_ENV_LOADED = False


def _load_dotenv():
    """
    TR: Harici bağımlılık eklemeden kök .env dosyasını environment'a yükler.
    EN: Load the root .env file into the environment without adding a dependency.
    """
    global _ENV_LOADED

    if _ENV_LOADED:
        return

    _ENV_LOADED = True

    if not ENV_FILE.exists():
        return

    for raw_line in ENV_FILE.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()

        if not line or line.startswith("#") or "=" not in line:
            continue

        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")

        os.environ.setdefault(key, value)


def get_required_env(name):
    """
    TR: Zorunlu environment değerini döndürür; yoksa açık hata verir.
    EN: Return a required environment value; fail clearly when missing.
    """
    _load_dotenv()
    value = os.getenv(name)

    if value is None or value.strip() == "":
        raise RuntimeError(
            f"Required environment variable is missing: {name}. "
            "Create .env locally or configure the matching CI secret."
        )

    return value


def get_required_int_env(name):
    """
    TR: Zorunlu integer environment değerini döndürür.
    EN: Return a required integer environment value.
    """
    value = get_required_env(name)

    try:
        return int(value)
    except ValueError as exc:
        raise RuntimeError(f"Environment variable must be an integer: {name}") from exc
