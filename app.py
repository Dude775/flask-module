from flask import Flask, jsonify, request
from datetime import datetime, timezone
from werkzeug.exceptions import NotFound, BadRequest, UnprocessableEntity

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "API is running"
    })

@app.route("/status")
def status():
    return jsonify({
        "status": "ok",
        "version": "1.0.0"
    })

@app.route("/time")
def current_time():
    now = datetime.now(timezone.utc)
    return jsonify({
        "time": now.isoformat()
    })

@app.route("/info")
def info():
    return jsonify({
        "app": "Flask Practice",
        "author": "Student",
        "day": 2
    })

@app.route("/echo", methods=["POST"])
def echo():
    data = request.json
    
    if data is None:
        return jsonify({
            "success": False,
            "error": "JSON body required"
        }), 400
    
    return jsonify({
        "success": True,
        "received": data
    }), 200

if __name__ == "__main__":
    app.run(debug=True)
