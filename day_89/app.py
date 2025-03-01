from flask import Flask, render_template, jsonify, request
import sqlite3

app = Flask(__name__)

def connect_db():
    return sqlite3.connect("tasks.db")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/tasks", methods=["GET"])
def get_tasks():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    conn.close()

    tasks_list = [{"id": task[0], "description": task[1], "completed": bool(task[2])} for task in tasks]
    return jsonify(tasks_list)

@app.route("/add_task", methods=["POST"])
def add_task():
    data = request.json
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (description, completed) VALUES (?, ?)", (data["description"], False))
    conn.commit()
    conn.close()
    return jsonify({"message": "Tarefa adicionada com sucesso!"})

@app.route("/toggle_task/<int:task_id>", methods=["PUT"])
def toggle_task(task_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT completed FROM tasks WHERE id = ?", (task_id,))
    task = cursor.fetchone()

    if task:
        new_status = not task[0]
        cursor.execute("UPDATE tasks SET completed = ? WHERE id = ?", (new_status, task_id))
        conn.commit()
    
    conn.close()
    return jsonify({"message": "Tarefa atualizada!"})

@app.route("/delete_task/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()
    return jsonify({"message": "Tarefa removida com sucesso!"})

if __name__ == "__main__":
    app.run(debug=True)
