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


@app.route('/api/v1/messages', methods=['POST'])
@jwt_required
@swag_from('../docs/send_emails_to_individuals.yml')
def send_message_to_individual():
    """send email to an individual."""
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
    data = request.get_json()
    if type(data['receiver_id']) is not int:
        return jsonify({
            "data_type_error": "please enter an integer",
            "status": 400
            }), 400
    if current_user[0] == data['receiver_id']:
        return jsonify({
            "status": 400, "message": "you can not send an email to yourself"
            }), 400
    user_search = user.search_user_by_id(data['receiver_id'])
    if not user_search:
        return jsonify({
            "status": 404, "message": "Recipient does not exist"
            }), 404
    send_message = messages.add_message(
        data['subject'],
        data["message"],
        data['parentMessageID'],
        data["status"],
        current_user[0],
        data['receiver_id'],
        False
        )
    user_details = messages.get_data(data['receiver_id'])
    return jsonify({"message": user_details, "status": 201}), 201


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


@app.route('/api/v1/messages/delete/<int:message_id>', methods=['DELETE'])
@jwt_required
@swag_from('../docs/delete_user_inbox_email.yml')
def delete_user_message(message_id):
    """delete user's message"""
    current_user = get_jwt_identity()
    if current_user[6] != "user":
        return jsonify({"status": 401, "message": "unauthorized access"}), 401
    search_message = messages.search_message(message_id)
    if not search_message:
        return jsonify({"status": 404, "messaege": "message not found"}), 404
    message_to_delete = [{"message": messages.delete_message(message_id)}]
    return jsonify({
        "data": message_to_delete , "status": 200
        }), 200


