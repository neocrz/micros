import os

from flask import Flask, request, jsonify
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from flask_marshmallow import Marshmallow

app = Flask(__name__)

APPDIR = os.path.abspath(os.path.dirname(__file__))

app.config["SECRET_KEY"] = "secret-key"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(APPDIR, "data.sqlite")

bcrypt = Bcrypt(app)
db = SQLAlchemy(app)
jwt = JWTManager(app)
ma = Marshmallow(app)

from app.models import *
from app.routes import *
