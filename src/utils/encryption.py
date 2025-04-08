# src/utils/encryption.py
from cryptography.fernet import Fernet
import os
import sys


# Add parent directory to path to find config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import KEY

cipher = Fernet(KEY)


def encrypt(data: str) -> str:
    return cipher.encrypt(data.encode()).decode()


def decrypt(data: str) -> str:
    return cipher.decrypt(data.encode()).decode()
