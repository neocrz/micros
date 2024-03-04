from app import app, db, jwt
from app.models import User
from flask import request, jsonify
from flask_jwt_extended import create_access_token

@app.route('/login', methods=['POST'])
def login():
    username = request.json['username']
    password = request.json['password']

    attempted_user = User.query.filter_by(username=username).first()
    
    if not attempted_user:
        return jsonify({'error': 'Invalid username'}), 401
    if not attempted_user.check_password(attemped_password=password):
        return jsonify({'error': 'Invalid password'}), 401

    access_token = create_access_token(identity=username)
    return jsonify({'access_token': access_token}), 200
