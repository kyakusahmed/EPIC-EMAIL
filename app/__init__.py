from flask import Flask
from flasgger import Swagger

app = Flask("__name__")

swagger = Swagger(app)


from app.views import auth
from app.views import messages
