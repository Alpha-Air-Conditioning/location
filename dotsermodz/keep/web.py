from flask import Flask
import threading
from dotsermodz import PORT

flask_app = Flask(__name__)

@flask_app.route('/')
def home():
    return "Bot is running!"

def run_web():
    flask_app.run(host='0.0.0.0', port=PORT)

def keep_alive():
    server = threading.Thread(target=run_web, daemon=True)
    server.start()
