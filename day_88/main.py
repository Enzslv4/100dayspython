from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

def connect_db():
    return sqlite3.connect("cafes.db")

@app.route("/cafes", methods=["GET"])
def get_cafes():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM cafes")
    cafes = cursor.fetchall()
    conn.close()
    return jsonify(cafes)

@app.route("/add_cafe", methods=["POST"])
def add_cafe():
    data = request.json
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO cafes (name, location, coffee_price) VALUES (?, ?, ?)",
                   (data["name"], data["location"], data["coffee_price"]))
    conn.commit()
    conn.close()
    return jsonify({"message": "Cafe added successfully!"})

@app.route("/delete_cafe/<int:cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM cafes WHERE id = ?", (cafe_id,))
    conn.commit()
    conn.close()
    return jsonify({"message": "Cafe deleted successfully!"})

if __name__ == "__main__":
    app.run(debug=True)