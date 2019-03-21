from flask import Flask, jsonify, request
from app.email import Emails
from app.validator import Validation
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token, get_jwt_identity)


app = Flask(__name__)
emails = Emails()
validator = Validation()
JWT = JWTManager(app)
app.config['JWT_SECRET_KEY'] = 'super-secret'


@app.route('/', methods=['GET'])
def index():
    """opening route."""
    return jsonify({
        "status": 200, 'message': 'welcome to Epic Email.'
        }), 200


@app.route('/api/v1/users', methods=['POST'])
def add_new_user():
    """add new user to self.users"""
    data = request.get_json()
    val_input_data = validator.input_data_validation([
        'firstname', 'lastname', 'email', 'password'
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
        "message": "user registration successful"
        }]
    return jsonify({"data": new_user, "status": 201}), 201


@app.route('/api/v1/users/login', methods=['POST'])
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
        return jsonify({"status": 200, "message": "register_first"}), 200
    access_token = create_access_token(identity=check_user)
    return jsonify({
        'message': "Login successful", 'access_token': access_token}), 200


@app.route('/api/v1/emails/user/received', methods=['GET'])
@jwt_required
def get_all_received_emails():
    """fetch all recieved emails for a user"""
    current_user = get_jwt_identity()
    print(current_user[0]['email'])
    inbox_view = emails.get_all_received_emails(current_user[0]['email'])
    print(inbox_view)
    return jsonify({"recieved-emails": inbox_view, "status": 200}), 200