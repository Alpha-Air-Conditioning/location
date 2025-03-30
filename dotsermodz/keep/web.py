from flask import Flask,render_template
import threading
from dotsermodz import PORT

flask_app = Flask(__name__)

@flask_app.route('/')
def home():
    return render_template('index.html')

def run_web():
    flask_app.run(host='0.0.0.0', port=PORT)

def keep_alive():
    server = threading.Thread(target=run_web, daemon=True)
    server.start()
