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


@app.route('/api/v1/messages/sent', methods=['GET'])
@jwt_required
@swag_from('../docs/get_user_sent_emails.yml')
def get_user_sent_messages():
    """fetch sent messages."""
    current_user = get_jwt_identity()
    if current_user[6] != "user":
        return jsonify({"message": "unauthorized access"})
    sent_messages = messages.get_sent_messages('status')
    sent_emails = []
    for key in range(len(sent_messages)):
        sent_emails.append({
            'message_id': sent_messages[key][0],
            'user_id': sent_messages[key][1],
            'subject': sent_messages[key][2],
            'message': sent_messages[key][3],
            'parentMessageID': sent_messages[key][4],
            'status': sent_messages[key][5],
            'receiver_id': sent_messages[key][6],
            'read': sent_messages[key][7],
            'createdon': sent_messages[key][8]
        })
    return jsonify({"status": 200, "messages_sent": sent_emails}), 200
