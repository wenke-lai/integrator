import requests


def get_my_ip() -> str:
    response = requests.get("https://checkip.amazonaws.com/", timeout=5)
    response.raise_for_status()
    return response.text.strip()
