from flask import request, jsonify

TOKEN = "SecretToken"

def authenticate_token():
    token = request.headers.get("Authorization")
    if not token or token != f"bearer {TOKEN}": 
        return jsonify({"error": "unauthorized"}), 401
