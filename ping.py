import time
import requests
import os
from datetime import datetime

PING_INTERVAL = int(os.getenv("PING_INTERVAL", 60))
SELF_URL = os.getenv("RENDER_EXTERNAL_URL")

URLS_TO_PING = [
    "https://example.com",
    "https://another-site.com",
]

def ping(url):
    try:
        r = requests.get(url, timeout=10)
        print(f"{datetime.utcnow()} {url} {r.status_code}")
    except Exception as e:
        print(f"{datetime.utcnow()} {url} {e}")

while True:
    for url in URLS_TO_PING:
        ping(url)
    if SELF_URL:
        ping(SELF_URL)
    time.sleep(PING_INTERVAL)
