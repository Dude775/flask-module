from flask import jsonify, request, Blueprint
from werkzeug.exceptions import NotFound, BadRequest
from bson import ObjectId
from db import get_collection

todos_bp = Blueprint("todos", __name__)

# כל הtodos
@todos_bp.route('/todos', methods=['GET'])
def get_todos():
    col = get_collection("todos")
    todos = list(map(lambda t: {**t, "_id": str(t["_id"])}, col.find()))
    return jsonify(todos)


@todos_bp.route('/todos/<id>', methods=['GET'])
def get_todo(id):
    col = get_collection("todos")
    try:
        todo = col.find_one({"_id": ObjectId(id)})
    except:
        raise NotFound(f"invalid id format")
    if not todo:
        raise NotFound(f"Todo with ID {id} not found")
    todo["_id"] = str(todo["_id"])
    return jsonify(todo)

@todos_bp.route('/todos', methods=['POST'])
def create_todo():
    col = get_collection("todos")
    if not request.is_json:
        raise BadRequest("Request body must be JSON")
    data = request.get_json()
    if 'title' not in data:
        raise BadRequest("Missing required field: 'title'")
    if not data["title"].strip():
        raise BadRequest("title cant be empty")
    new_todo = {
        "title": data["title"].strip(),
        "completed": False
    }
    col.insert_one(new_todo)
    new_todo["_id"] = str(new_todo["_id"])
    return jsonify(new_todo), 201

# update - מקבל title או completed או שניהם
@todos_bp.route('/todos/<id>', methods=['PUT'])
def update_todo(id):
    col = get_collection("todos")
    try:
        todo = col.find_one({"_id": ObjectId(id)})
    except:
        raise NotFound("invalid id")
    if not todo:
        raise NotFound("todo not found")
    data = request.get_json()
    if not data or ("title" not in data and "completed" not in data):
        raise BadRequest("need title or completed field")
    update_fields = {}
    if "title" in data:
        update_fields["title"] = data["title"]
    if "completed" in data:
        update_fields["completed"] = data["completed"]
    col.update_one({"_id": ObjectId(id)}, {"$set": update_fields})
    updated = col.find_one({"_id": ObjectId(id)})
    updated["_id"] = str(updated["_id"])
    return jsonify(updated)

@todos_bp.route('/todos/<id>', methods=['DELETE'])
def delete_todo(id):
    col = get_collection("todos")
    try:
        todo = col.find_one({"_id": ObjectId(id)})
    except:
        raise NotFound("invalid id")
    if not todo:
        raise NotFound("not found")
    col.delete_one({"_id": ObjectId(id)})
    return jsonify({"message": "deleted successfuly"}), 200
