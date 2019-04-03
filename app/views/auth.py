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

    registered = user.get_user_by_email(data['email'])
    if registered:
        return jsonify({
            "status": 400, "error": "user registered already"
            }), 400
    user_info = user.create_user_account(
        data['firstname'],
        data['lastname'],
        data['email'],
        data['password']
    )
    
    return jsonify({"message": user_info, "status": 201}), 201
  
  
@app.route('/api/v1/auth/login', methods=['POST'])
@swag_from('../docs/signin.yml')
def signin_user():
    """Login User."""
    validate_credentials = validator.input_data_validation([
        'email', 'password'
        ])
    if validate_credentials:
        return jsonify({
            "status": 400,
            "error": validate_credentials
        }), 400
    data = request.get_json()
    check_user = user.user_signin(data['email'].strip(), data['password'])
    if not check_user:
        return jsonify({
            "status": 200, "error": "wrong password or email"
            }), 200
    access_token = [{'access_token':create_access_token(identity=check_user)}]
    return jsonify({'status': 200, "message": "login successfull", 'data': access_token}), 200


@app.route('/api/v1/auth', methods=['GET'])
@jwt_required
def get_all_users():
    """fetch all users."""
    current_user = get_jwt_identity()
    if current_user[6] != "user":
        return jsonify({"message": "unauthorized access"})
    get_users = user.get_all_users()
    users = []
    for key in range(len(get_users)):
        users.append({
            'id': get_users[key][0],
            'firstname': get_users[key][1],
            'lastname': get_users[key][2],
            'email': get_users[key][3],
            'password': get_users[key][4],
            'phone_number': get_users[key][5],
            'role': get_users[key][6],
            'createdon': get_users[key][7]
        })
    return jsonify({"status": 200, "messages_sent": users}), 200
