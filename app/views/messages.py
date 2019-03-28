from flask import jsonify, request
from app import app
from app.views.auth import User
from app.models.messages import Messages
from app.views.validator import Validation
from flasgger import swag_from
from flask_jwt_extended import (jwt_required, get_jwt_identity)


messages = Messages()
user = User()
validator = Validation()


@app.route('/api/v1/messages/delete/<int:message_id>', methods=['DELETE'])
@jwt_required
def delete_user_message(message_id):
    """delete user's message"""
    current_user = get_jwt_identity()
    if current_user[6] != "user":
        return jsonify({"status": 401, "message": "unauthorized access"})
    search_message = messages.search_message(message_id)
    if not search_message:
        return jsonify({"status": 404, "messaege": "message not found"}), 404
    return jsonify({
        "message": messages.delete_message(message_id), "status": 200
        }), 200
