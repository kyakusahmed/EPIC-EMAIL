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
    return jsonify({
        "data": [{
            "Receiver_id": data[
                "receiver_id"], "message": send_message}], "status": 201}), 201
