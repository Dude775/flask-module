from flask import jsonify, request, Blueprint
from werkzeug.exceptions import NotFound, BadRequest
from models import get_all_tasks, get_task_by_id, create_task, update_task, delete_task

tasks_bp = Blueprint("tasks", __name__)

# מחזיר את כל המשימות
@tasks_bp.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(get_all_tasks())

@tasks_bp.route('/tasks/<task_id>', methods=['GET'])
def get_task(task_id):
    task = get_task_by_id(task_id)
    if not task:
        raise NotFound(f"Task with ID {task_id} not found")
    return jsonify(task)

@tasks_bp.route('/tasks', methods=['POST'])
def create_task_route():
    if not request.is_json:
        raise BadRequest("Request body must be JSON")
    data = request.get_json()
    # חייב להיות title
    if 'title' not in data:
        raise BadRequest("Missing required field: 'title'")
    if not data["title"].strip():
        raise BadRequest("title cant be empty")
    new_task = create_task(data)
    return jsonify(new_task), 201

# PUT - פחות validations מ-POST
@tasks_bp.route('/tasks/<task_id>', methods=['PUT'])
def update_task_route(task_id):
    t = get_task_by_id(task_id)
    if not t:
        raise NotFound("task not found")
    data = request.get_json()
    if not data or ("title" not in data and "completed" not in data):
        raise BadRequest("need title or completed field")
    updated = update_task(task_id, data)
    return jsonify(updated)

@tasks_bp.route('/tasks/<task_id>', methods=['DELETE'])
def delete_task_route(task_id):
    # בודק שקיים לפני שמוחק
    t = get_task_by_id(task_id)
    if not t:
        raise NotFound("not found")
    delete_task(task_id)
    return jsonify({"message": "deleted successfuly"}), 200