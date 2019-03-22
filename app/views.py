from flask import Flask, jsonify, request
from app.email import Emails
from app.validator import Validation
from flasgger import Swagger
from flasgger import swag_from


app = Flask(__name__)
emails = Emails()
validator = Validation()
swagger = Swagger(app)


@app.route('/', methods=['GET'])
def index():
    """opening route."""
    return jsonify({
        "status": 200, 'message': 'welcome to Epic Email.'
        }), 200


@app.route('/api/v1/users/signup', methods=['POST'])
@swag_from('docs/signup.yml')
def create_user_account():
    """add new user to self.users"""
    data = request.get_json()
    val_input_data = validator.input_data_validation([
        'email', 'firstname', 'lastname', 'password'
        ])
    if val_input_data:
        return jsonify({"status": 400, "error": val_input_data}), 400
    registered = emails.search_user_by_email(data['email'], data['password'])
    if registered:
        return jsonify({
            "status": 200, "message": "user registered already"
            }), 200
    user = emails.add_new_user(
        data['email'],
        data['firstname'],
        data['lastname'],
        data['password']
    )
    new_user = [{
        "user_id": user['id'],
        "user": user
        }]
    return jsonify({"data": new_user, "status": 201}), 201


@app.route('/api/v1/users/login', methods=['POST'])
@swag_from('docs/signin.yml')
def user_login():
    """Login User."""
    validate_credentials = validator.input_data_validation([
        'email', 'password'
        ])
    if validate_credentials:
        return jsonify({
            "message": 'Validation error',
            "errors": validate_credentials
        }), 400
    data = request.get_json()
    check_user = emails.search_user_by_email(
        data['email'].strip(), data['password'])
    if not check_user:
        return jsonify({
            "status": 200, "message": "wrong password or email"
            }), 200
    return jsonify({'user': check_user, 'status': 200}), 200


@app.route('/api/v1/emails/user', methods=['POST'])
@swag_from('docs/send_emails_to_individuals.yml')
def send_email_to_user():
    """send email to a user."""
    validate_credentials = validator.input_data_validation([
        'subject', 'message', 'sender_id', 'status'])
    if validate_credentials:
        return jsonify({
            "message": 'Validation error',
            "errors": validate_credentials
        }), 400
    data = request.get_json()
    if type(data['sender_id']) is not int:
        return jsonify({
            "data_type_error": "please enter an integer",
            "status": 400
            }), 400
    if data['sender_id'] == data['receiver_id']:
        return jsonify({
            "status": 200, "message": "you can not send an email to yourself"
            }), 200
    user_search = emails.search_user_by_id(data['receiver_id'])
    if not user_search:
        return jsonify({
            "status": 404, "message": "user does not exist"
            }), 200
    email_send = emails.send_email(
        data['subject'],
        data["message"],
        data["status"],
        data['sender_id'],
        data['receiver_id']
        )
    return jsonify({"data": [email_send], "status": 201}), 201


@app.route('/api/v1/emails/user/received/<int:id>', methods=['GET'])
@swag_from('docs/get_user_received_emails.yml')
def get_all_user_received_emails(id):
    """fetch all user emails"""
    return jsonify({
        "sent-emails": emails.get_user_email(id), "status": 200
        }), 200


@app.route('/api/v1/emails/specific-user/<int:id>', methods=['GET'])
@swag_from('docs/get_specific_user_email.yml')
def get_specific_user_email(id):
    """get specific user's email"""
    return jsonify({
        "status": 200,
        "specific user email": emails.get_specific_user_email(id, 'email_id')
        }), 200


@app.route('/api/v1/emails/user/unread/<int:id>', methods=['GET'])
@swag_from('docs/get_user_unread_emails.yml')
def get_all_user_unread_emails(id):
    """fetch all user unread emails"""
    return jsonify({
        "unread-emails": emails.get_user_unread_email(id, 'read'),
        "status": 200
        }), 200


@app.route('/api/v1/emails/user/sent/<int:id>', methods=['GET'])
@swag_from('docs/get_user_sent_emails.yml')
def get_all_user_sent_emails(id):
    """fetch all user emails"""
    return jsonify({
        "sent-emails": emails.get_user_sent_email(id), "status": 200
        }), 200


@app.route('/api/v1/emails/user/delete/<int:id>', methods=['DELETE'])
@swag_from('docs/delete_user_inbox_email.yml')
def delete_user_emails(id):
    """delete user's email"""
    return jsonify({
        "deleted email": emails.delete_user_email(id), "status": 200
        }), 200
