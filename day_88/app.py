from flask import Flask, jsonify, request, render_template
import sqlite3

app = Flask(__name__)

def connect_db():
    return sqlite3.connect("cafes.db")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/cafes", methods=["GET"])
def get_cafes():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM cafes")
    cafes = cursor.fetchall()
    conn.close()
    
    cafes_list = []
    for cafe in cafes:
        cafes_list.append({
            "id": cafe[0],
            "name": cafe[1],
            "location": cafe[2],
            "coffee_price": cafe[3]
        })
    return jsonify(cafes_list)

@app.route("/add_cafe", methods=["POST"])
def add_cafe():
    data = request.json
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO cafes (name, location, coffee_price) VALUES (?, ?, ?)",
                   (data["name"], data["location"], data["coffee_price"]))
    conn.commit()
    conn.close()
    return jsonify({"message": "Café adicionado com sucesso!"})

@app.route("/delete_cafe/<int:cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM cafes WHERE id = ?", (cafe_id,))
    conn.commit()
    conn.close()
    return jsonify({"message": "Café excluído com sucesso!"})

if __name__ == "__main__":
    app.run(debug=True)
