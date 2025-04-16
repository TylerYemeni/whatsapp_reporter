import random

def rotate_proxy():
    try:
        with open("proxies.txt", "r") as f:
            proxies = [line.strip() for line in f.readlines() if line.strip()]
        return random.choice(proxies) if proxies else None
    except FileNotFoundError:
        return None
