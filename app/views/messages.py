from flask import Flask, jsonify, request
from app import app
from app.views.auth import User
from app.models.messages import Messages
from app.views.validator import Validation
from flasgger import swag_from


messages = Messages()
user = User()
validator = Validation()


@app.route('/api/v1/messages', methods=['POST'])
@swag_from('../docs/send_emails_to_individuals.yml')
def send_message_to_user():
    """send email to an individual."""
    validate_credentials = validator.input_data_validation([
        'subject', 'message', 'sender_id', 'status', 'receiver_id'])
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
    if type(data['sender_id']) is not int:
        return jsonify({
            "data_type_error": "please enter an integer",
            "status": 400
            }), 400
    if data['sender_id'] == data['receiver_id']:
        return jsonify({
            "status": 400, "message": "you can not send an email to yourself"
            }), 400
    user_search = user.search_user_by_id(data['receiver_id'])
    if not user_search:
        return jsonify({
            "status": 404, "message": "user does not exist"
            }), 404
    send_message = messages.send_message(
        data['subject'],
        data["message"],
        data["status"],
        data['sender_id'],
        data['receiver_id'],
        False
        )
    return jsonify({"data": [send_message], "status": 201}), 201


@app.route('/api/v1/messages/received', methods=['GET'])
@swag_from('../docs/get_user_received_emails.yml')
def get_user_received_messages():
    """fetch all user received messages"""
    return jsonify({
        "sent-emails": messages.get_user_message('status', 'read'),
        "status": 200
        }), 200


@app.route('/api/v1/messages/unread', methods=['GET'])
@swag_from('../docs/get_user_unread_emails.yml')
def get_all_user_unread_emails():
    """fetch all user unread emails"""
    return jsonify({
        "unread-emails": messages.get_user_unread_message('status', 'read'),
        "status": 200
        }), 200


@app.route('/api/v1/messages/sent', methods=['GET'])
@swag_from('../docs/get_user_sent_emails.yml')
def get_user_sent_messages():
    """fetch sent messages."""
    return jsonify({
        "sent-emails": messages.get_user_sent_message('status'), "status": 200
                }), 200


@app.route('/api/v1/messages/delete/<int:message_id>', methods=['DELETE'])
@swag_from('../docs/delete_user_inbox_email.yml')
def delete_user_message(message_id):
    """delete user's message"""
    return jsonify({
        "deleted_message": messages.delete_message(message_id), "status": 200
        }), 200


@app.route('/api/v1/messages/<int:message_id>', methods=['GET'])
@swag_from('../docs/get_specific_user_email.yml')
def get_specific_user_message(message_id):
    """get specific user's email"""
    return jsonify({
        "status": 200,
        "specific user email": messages.get_specific_message(message_id)
        }), 200
