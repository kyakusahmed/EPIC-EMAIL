from flask import Flask
from flasgger import Swagger
from app.models.migration import Migration
from app.views import auth
from app.views import messages
from app.views import groups


app = Flask("__name__")

swagger = Swagger(app)
tables = Migration()

tables.create_tables()
tables.drop_tables()
tables.create_tables()
