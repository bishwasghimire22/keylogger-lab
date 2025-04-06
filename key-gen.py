## Run this once and paste the output in config.py

from cryptography.fernet import Fernet

print(Fernet.generate_key().decode())
