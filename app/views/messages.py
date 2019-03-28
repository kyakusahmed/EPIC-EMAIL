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


@app.route('/api/v1/messages/unread', methods=['GET'])
@jwt_required
@swag_from('../docs/get_user_unread_emails.yml')
def get_all_user_unread_emails():
    """fetch all user unread emails"""
    current_user = get_jwt_identity()
    if current_user[6] != "user":
        return jsonify({"message": "unauthorized access"})
    unread_messages = messages.get_user_received_messages('status', 'read')
    unread_emails = []
    for key in range(len(unread_messages)):
        unread_emails.append({
            'message_id': unread_messages[key][0],
            'user_id': unread_messages[key][1],
            'subject': unread_messages[key][2],
            'message': unread_messages[key][3],
            'parentMessageID': unread_messages[key][4],
            'status': unread_messages[key][5],
            'receiver_id': unread_messages[key][6],
            'read': unread_messages[key][7],
            'createdon': unread_messages[key][8]
        })
    return jsonify({"status": 200, "messages_unread": unread_emails}), 200
