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


@app.route('/api/v1/groups/<int:group_id>/messages', methods=['POST'])
@jwt_required
@swag_from('../docs/send_emails_to_individuals.yml')
def send_message_to_group():
    """send messages to a group."""
    current_user = get_jwt_identity()
    if current_user[6] != "user":
        return jsonify({"message": "unauthorized access"})
    validate_credentials = validator.input_data_validation([
        'subject', 'message', 'status', 'receiver_id'])
    if validate_credentials:
        return jsonify({
            "message": 'Validation error',
            "errors": validate_credentials
        }), 400
   