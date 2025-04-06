# src/utils/encryption.py
from cryptography.fernet import Fernet
from src.config import KEY

cipher = Fernet(KEY)


def encrypt(data: str) -> str:
    return cipher.encrypt(data.encode()).decode()


def decrypt(data: str) -> str:
    return cipher.decrypt(data.encode()).decode()
