from flask import Flask, jsonify, request
from app.email import Emails
from app.validator import Validation
from flask_jwt_extended import (JWTManager, jwt_required, create_access_token, get_jwt_identity)


app = Flask(__name__)
emails = Emails()
validator = Validation()
JWT = JWTManager(app)

app.config['JWT_SECRET_KEY'] = 'super-secret'



@app.route('/api/v1/email/inbox/<int:id>', methods=['GET'])
def get_all_user_inbox_emails(id):
    """fetch all inbox emails"""
    # current_user = get_jwt_identity()
    # if current_user[0] != "id":
    #     return jsonify({"error": "emails do not belong to you"}), 401

    inbox_view = emails.get_all_recieved_emails_by_user(id)
    return jsonify({
        "inbox": inbox_view, "status": 200
        }), 200
