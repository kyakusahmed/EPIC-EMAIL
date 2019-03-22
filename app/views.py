from flask import Flask, jsonify, request
from app.email import Emails
from app.validator import Validation


app = Flask(__name__)
emails = Emails()
validator = Validation()


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



