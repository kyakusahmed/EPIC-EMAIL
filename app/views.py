from flask import Flask, jsonify, request
from app.email import Emails
from app.validator import Validation
from flask_jwt_extended import (JWTManager, jwt_required, create_access_token, get_jwt_identity)


app = Flask(__name__)
emails = Emails()
validator = Validation()
JWT = JWTManager(app)

app.config['JWT_SECRET_KEY'] = 'super-secret'



@app.route('/api/v1/users/login', methods=['POST'])
def user_login():
    """Login User."""
    validate_credentials = validator.input_data_validation(['email', 'password'])
    if validate_credentials:
        return jsonify({
            "message": 'Validation error',
            "errors": validate_credentials
        }), 400
    pick_input = request.get_json()
    user_login = emails.search_user_by_email(pick_input['email'].strip(), pick_input['password'])
    print(user_login)
    if user_login:
        return jsonify(
            user_token=create_access_token([user_login]),
            message="Login successful"), 200
    return jsonify(error="Wrong Email or password"), 401


@app.route('/api/v1/users', methods=['POST'])
def add_new_user():
    """add new user to self.users"""

    data = request.get_json()
    val_input_data = validator.input_data_validation(['firstname', 'lastname', 'email', 'password'])
    if val_input_data:
        return jsonify({"status": 400, "error": val_input_data}), 400

    registered = emails.search_user_by_email(data['email'], data['password'])
    if registered:
        return jsonify({
            "status": 200, "message": "user registered already"
            }), 200

    user = emails.add_new_user(
        data['firstname'],
        data['lastname'],
        data['email'],
        data['password']
    )
    new_user = [{
        "user_id": user['id'],
        "message": "user registration successful"
        }]
    return jsonify({"data": new_user, "status": 201}), 201


