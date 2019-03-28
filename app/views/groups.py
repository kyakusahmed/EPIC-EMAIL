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


@app.route('/api/v1/groups/<int:id>/users', methods=['POST'])
@jwt_required
@swag_from('../docs/send_emails_to_individuals.yml')
def add_user_to_group(id):
    """send email to an individual."""
    current_user = get_jwt_identity()
    if current_user[6] != "user":
        return jsonify({"message": "unauthorized access"})
    validate_credentials = validator.input_data_validation([
        'user_id', 'user_role'])
    if validate_credentials:
        return jsonify({
            "message": 'Validation error',
            "errors": validate_credentials
        }), 400
    data = request.get_json()
    if type(data['user_id']) is not int:
        return jsonify({
            "data_type_error": "please enter an integer",
            "status": 400
            }), 400
    if current_user[0] == data['user_id']:
        return jsonify({
            "status": 400, "message": "you are an administrator of this group"
            }), 400
    check_user = user.search_user_by_id(data['user_id'])
    if not check_user:
        return jsonify({"status": 404, "message": "unable to find user"}), 404
    group_search = group.search_group(id)
    if not group_search:
        return jsonify({
            "status": 404, "message": "unable to find this group"
            }), 404
    send_message = group.add_user_to_group(
        data['user_id'],
        id,
        data["user_role"]
        )
    return jsonify({"data": [{"message": send_message}], "status": 201}), 201
