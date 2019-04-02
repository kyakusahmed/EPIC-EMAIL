from flask import Flask
from flasgger import Swagger
from app.models.migration import Migration
from flask_cors import CORS

app = Flask("__name__")

swagger = Swagger(app)
tables = Migration()
cors = CORS(app)

tables.create_tables()
tables.drop_tables()
tables.create_tables()

from app.views import auth
from app.views import messages
from app.views import groups
