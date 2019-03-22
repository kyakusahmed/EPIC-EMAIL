from flask import Flask, jsonify, request
from app.email import Emails
from app.validator import Validation
from flask_jwt_extended import (JWTManager, jwt_required, create_access_token, get_jwt_identity)


app = Flask(__name__)
emails = Emails()
validator = Validation()
JWT = JWTManager(app)

app.config['JWT_SECRET_KEY'] = 'super-secret'



@app.route('/api/v1/emails/user/received/<int:id>', methods=['GET'])
def get_all_user_received_emails(id):
    """fetch all user emails"""
    return jsonify({"sent-emails": emails.get_user_email(id), "status": 200}), 200
