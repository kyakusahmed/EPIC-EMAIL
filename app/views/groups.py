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



@app.route('/api/v1/groups', methods=['POST'])
@jwt_required
@swag_from('../docs/send_emails_to_individuals.yml')
def create_group():

    """send email to an individual."""
    current_user = get_jwt_identity()
    if current_user[6] != "user":
        return jsonify({"message": "unauthorized access"})
    validate_info = validator.input_data_validation([
        'group_name', 'user_role'
        ])
    if validate_info:
        return jsonify({
            "message": 'Validation error',
            "errors": validate_credentials
        }), 400
    data = request.get_json()
    send_group = group.add_group(
        current_user[0],
        data['group_name'],
        data['user_role'],
        )
    return jsonify({
        "data": [{"message": send_group}], "status": 201}), 201
