from env_loader import get_required_env


def get_standard_user() -> dict[str, str]:
    return {
        "username": get_required_env("SAUCEDEMO_STANDARD_USERNAME"),
        "password": get_required_env("SAUCEDEMO_STANDARD_PASSWORD"),
    }
