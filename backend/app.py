from flask import Flask, jsonify
import os

app = Flask(__name__)


@app.route("/health")
def health():
    return jsonify({"status": "ok", "service": "flask-app-backend"})


@app.route("/api/example")
def example():
    return jsonify({"message": "Hello from flask-app backend"})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 7000))
    app.run(host="0.0.0.0", port=port)
