from app import app
from flask import jsonify, request
from app.models.auth import User
from app.views.validator import Validation
from flasgger import swag_from
from flask_jwt_extended import (jwt_required, create_access_token,
                                get_jwt_identity)


user = User()
validator = Validation()


@app.route('/', methods=['GET'])
def index():
    """opening route."""
    return jsonify({
        "status": 200, 'message': 'welcome to Epic Email.'
        }), 200


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
    check_user = user.user_signin(data['email'].strip(), data['password'])
    if not check_user:
        return jsonify({
            "status": 200, "message": "wrong password or email"
            }), 200
    access_token = create_access_token(identity=check_user)
    return jsonify({
        'message': "Login successful", 'access_token': access_token}), 200
