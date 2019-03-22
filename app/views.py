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
        return jsonify({"status": 200, "message": "wrong password or email"}), 200
    return jsonify({'user': check_user, 'status': 200}), 200


