from flask import Blueprint, jsonify
from werkzeug.exceptions import NotFound, BadRequest, UnprocessableEntity

errors_bp = Blueprint("errors", __name__)

# 404
@errors_bp.app_errorhandler(NotFound)
def handle_not_found(e):
    return jsonify({
        "error": str(e)
    }), 404

# 400 - בעיה במבנה הבקשה
@errors_bp.app_errorhandler(BadRequest)
def handle_bad_request(e):
    return jsonify({
        "error": str(e)
    }), 400

# 422
@errors_bp.app_errorhandler(UnprocessableEntity)
def handle_unprocessable(e):
    return jsonify({
        "error": str(e)
    }), 422