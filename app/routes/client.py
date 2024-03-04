from app import app, db
from app.models import Client, ClientSchema
from flask import request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

user_schema = ClientSchema()
users_schema = ClientSchema(many=True)

@app.route("/clients", methods=["POST"])
def add_client():
    data = request.get_json(force=True)
