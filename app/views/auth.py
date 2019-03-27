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