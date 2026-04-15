from flask import Flask, jsonify, request
import uuid


app = Flask(__name__)

tasks = [
    {"id": "1", "title": "Learn Flask", "completed": False},
    {"id": "2", "title": "Build API", "completed": False},
    {"id": "3", "title": "Test with Postman", "completed": True}
]

@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks)

@app.route("/tasks/<int:task_id>", methods=["GET"])
def get_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            return jsonify(task)
    return jsonify({"error": "task not found"}), 404

@app.route("/tasks", methods=["POST"])
def create_task():
    global task_id_counter
    data = request.get_json()

    new_task = {
        "id": task_id_counter,
        "title": data["title"],
        "completed": False
    }
    tasks.append(new_task)
    task_id_counter += 1
    return jsonify(new_task), 201

@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    data = request.get_json()
    for task in tasks:
        if task["id"] == task_id:
            if "title" in data:
                task["title"] = data["title"]
            if "completed" in data:
                task["completed"] = data["completed"]
            return jsonify(task)
    return jsonify({"error": "task not found"}), 404

@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            return jsonify({"message": "task deleted"})
    return jsonify({"error": "task not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
