from flask import jsonify, request
from app import app
from app.views.auth import User
from app.models.messages import Messages
from app.models.groups import Group
from app.views.validator import Validation
from flasgger import swag_from
from flask_jwt_extended import (jwt_required, get_jwt_identity)

group = Group()
messages = Messages()
user = User()
validator = Validation()


@app.route(
    '/api/v1/groups/<int:group_id>/users/<int:user_id>', methods=['DELETE'])
@jwt_required
@swag_from('../docs/delete_user_inbox_email.yml')
def delete_user_from_group(group_id, user_id):
    """delete user from group"""
    current_user = get_jwt_identity()
    if current_user[6] != "user":
        return jsonify({"status": 401, "message": "unauthorized access"})
    search_group = group.search_group(group_id)
    if not search_group:
        return jsonify({"status": 404, "group": "unable to find group"}), 404
    check_user = user.search_user_by_id(user_id)
    if not check_user:
        return jsonify({"status": 404, "message": "unable to find user"}), 404
    delete_message = [{
        "message": group.delete_user_from_group(group_id, user_id)}]
    return jsonify({
        "data": delete_message, "status": 200
        }), 200
