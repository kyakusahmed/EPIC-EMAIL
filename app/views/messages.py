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

  
@app.route('/api/v1/messages/sent', methods=['GET'])
@jwt_required
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

  
@app.route('/api/v1/messages/<int:message_id>', methods=['GET'])
@jwt_required
@swag_from('../docs/get_specific_user_email.yml')
def get_specific_user_message(message_id):
    """get specific user's email"""
    current_user = get_jwt_identity()
    if current_user[6] != "user":
        return jsonify({"message": "unauthorized access"})
    search_message = messages.search_message(message_id)
    if not search_message:
        return jsonify({"status": 404, "messaege": "message not found"}), 404
    return jsonify({"status": 200, "message": {
        'message_id': search_message[0],
        'user_id': search_message[1],
        'subject': search_message[2],
        'message': search_message[3],
        'parentMessageID': search_message[4],
        'status': search_message[5],
        'receiver_id': search_message[6],
        'read': search_message[7],
        'createdon': search_message[8]
    }})


