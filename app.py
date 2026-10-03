from flask import Flask, send_from_directory
from pathlib import Path
app = Flask(__name__, static_folder=".", static_url_path="")
@app.route("/")
def index():
    return send_from_directory(Path(__file__).parent, "index.html")
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
