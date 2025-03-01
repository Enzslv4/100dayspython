from flask import Flask, jsonify
import requests

app = Flask(__name__)

HP_API_URL = "https://hp-api.onrender.com/api/characters"

@app.route("/characters", methods=["GET"])
def get_characters():
    response = requests.get(HP_API_URL)
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({"error": "Failed to fetch data"}), 500

if __name__ == "__main__":
    app.run(debug=True)
