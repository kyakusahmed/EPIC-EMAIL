from flask_jwt_extended import (JWTManager)
from flask import jsonify
from app.models.migration import Migration
from app import app

app.config['JWT_SECRET_KEY'] = 'super-secret'
JWT = JWTManager(app)
DB = Migration()
DB.create_tables()