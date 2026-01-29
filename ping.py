import time
import requests
import os
from datetime import datetime
from threading import Thread
from flask import Flask

PING_INTERVAL = int(os.getenv("PING_INTERVAL", 60))
SELF_URL = os.getenv("RENDER_EXTERNAL_URL")
PORT = int(os.getenv("PORT", 10000))

URLS_TO_PING = [
    "https://navine-compressor.onrender.com/",
    "https://navine-file-sharer.onrender.com",
    "https://website-pinger-w81z.onrender.com",
    "example.com",
    "example.com",
]

def ping(url):
    try:
        r = requests.get(url, timeout=10)
        print(f"{datetime.utcnow()} {url} {r.status_code}")
    except Exception as e:
        print(f"{datetime.utcnow()} {url} {e}")

def ping_loop():
    while True:
        for url in URLS_TO_PING:
            ping(url)
        if SELF_URL:
            ping(SELF_URL)
        time.sleep(PING_INTERVAL)

app = Flask(__name__)

@app.route("/")
def health():
    return "Pinging Sites", 200

if __name__ == "__main__":
    Thread(target=ping_loop, daemon=True).start()
    app.run(host="0.0.0.0", port=PORT)
