from app import app
from flask import Flask, jsonify, request
from app.models.auth import User
from app.views.validator import Validation
from flasgger import swag_from


user = User()
validator = Validation()


@app.route('/', methods=['GET'])
def index():
    """opening route."""
    return jsonify({
        "status": 200, 'message': 'welcome to Epic Email.'
        }), 200


@app.route('/api/v1/auth/signup', methods=['POST'])
@swag_from('../docs/signup.yml')
def create_user_account():
    """add new user to self.users"""
    data = request.get_json()
    val_input_data = validator.input_data_validation([
        'email', 'firstname', 'lastname', 'password'
        ])
    if val_input_data:
        return jsonify({"status": 400, "error": val_input_data}), 400
    registered = user.search_user_by_email(data['email'], data['password'])
    if registered:
        return jsonify({
            "status": 200, "message": "user registered already"
            }), 200
    user_info = user.add_new_user(
        data['email'],
        data['firstname'],
        data['lastname'],
        data['password']
    )
    new_user = [{
        "user_id": user_info['id'],
        "user": user_info
        }]
    return jsonify({"data": new_user, "status": 201}), 201


@app.route('/api/v1/auth/login', methods=['POST'])
@swag_from('../docs/signin.yml')
def signin_user():
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
    check_user = user.search_user_by_email(
        data['email'].strip(), data['password'])
    if not check_user:
        return jsonify({
            "status": 200, "message": "wrong password or email"
            }), 200
    return jsonify({'user': check_user, 'status': 200}), 200
