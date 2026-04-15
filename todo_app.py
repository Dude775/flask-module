from flask import Flask, jsonify, request
import uuid


app = Flask(__name__)

# רשימת המשימות - זמני עד שנעבור ל-DB
tasks = [
    {"id": "1", "title": "Learn Flask", "completed": False},
    {"id": "2", "title": "Build API", "completed": False},
    {"id": "3", "title": "Test with Postman", "completed": True}
]


# === GET ===
@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks)

@app.route("/tasks/<task_id>", methods=["GET"])
def get_task(task_id):
    for t in tasks:
        if t["id"] == task_id:
            return jsonify(t)
    return jsonify({"error": "task not found"}), 404

# === POST - יצירת משימה חדשה ===
@app.route("/tasks", methods=["POST"])
def create_task():
    data = request.get_json()

    new_task = {
        "id": str(uuid.uuid4()),
        "title": data["title"],
        "completed": False
    }
    tasks.append(new_task)
    return jsonify(new_task), 201

if __name__ == "__main__":
    app.run(debug=True)
