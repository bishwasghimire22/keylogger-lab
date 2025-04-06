# Lab Keylogger Project (Ethical Use)

This project is for security research in a sandbox environment. It records keystrokes, encrypts them, and runs in the background stealthily.

## ⚠️ Ethical Use Only

Run only in a lab or with consent. Never deploy on personal or production systems without authorization.

## Features

- Stealth execution (no console window)
- Encrypted keystroke logs
- PyInstaller build support
- Auto-start setup ready

## How to Run

1. Install dependencies
2. Run or build the executable
3. Logs are stored in `/logs/encrypted_log.txt`

## Overview

This project is a keylogger that logs keystrokes in the background and encrypts them using AES encryption. The encrypted logs can be monitored via a Flask-based web dashboard.

## Requirements

- Python 3.x
- Required Python packages (`pip install -r requirements.txt`):
  - `pynput`
  - `cryptography`
  - `Flask`

## Setup Instructions

1. Clone this repository and navigate to the project directory.
2. Set up a virtual environment:
   ```bash
   python -m venv venv
   ```
