from flask import Flask, jsonify, request
from app.email import Emails
from app.validator import Validation


app = Flask(__name__)
emails = Emails()
validator = Validation()   


@app.route('/api/v1/users/login', methods=['POST'])
def user_login():
    """Login User."""
    validate_credentials = validator.input_data_validation(['email', 'password'])
    if validate_credentials:
        return jsonify({
            "message": 'Validation error',
            "errors": validate_credentials
        }), 400
    get_input = request.get_json()
    user_login = emails.search_user_by_email(get_input['email'].strip())
    if user_login:
        return jsonify(status=200, message="Login successful"), 200
    return jsonify(error="Wrong Email or password"), 401      


