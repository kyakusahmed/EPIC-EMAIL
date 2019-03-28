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


@app.route('/api/v1/messages/received', methods=['GET'])
@jwt_required
@swag_from('../docs/get_user_received_emails.yml')
def get_user_received_messages():
    """fetch all user received messages"""
    current_user = get_jwt_identity()
    if current_user[6] != "user":
        return jsonify({"message": "unauthorized access"})
    received_messages = messages.get_user_received_messages('status', 'read')
    received = []
    for key in range(len(received_messages)):
        received.append({
            'message_id': received_messages[key][0],
            'user_id': received_messages[key][1],
            'subject': received_messages[key][2],
            'message': received_messages[key][3],
            'parentMessageID': received_messages[key][4],
            'status': received_messages[key][5],
            'receiver_id': received_messages[key][6],
            'read': received_messages[key][7],
            'createdon': received_messages[key][8]
        })
    return jsonify({"status": 200, "messages_received": received}), 200
