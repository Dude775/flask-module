from flask import Flask, jsonify, request

app = Flask(__name__)

# data
tasks = [
    {"id": 1, "title": "Learn Flask", "completed": False},
    {"id": 2, "title": "Build API", "completed": False},
    {"id": 3, "title": "Test with Postman", "completed": True}
]

# get all tasks
@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks)

# get singel task by id
@app.route("/tasks/<int:task_id>", methods=["GET"])
def get_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            return jsonify(task)
    return jsonify({"error": "task not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)
