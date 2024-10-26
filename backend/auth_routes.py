from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from models import User
from app import db  # Import db from backend/__init__.py

auth_blueprint = Blueprint('auth', __name__)

@auth_blueprint.route('/register', methods=['POST'])
def register():
    data = request.json
    user = User(username=data['username'], role=data['role'])
    user.set_password(data['password'])
    db.session.add(user)
    db.session.commit()
    return jsonify(message="User registered successfully"), 201

@auth_blueprint.route('/login', methods=['POST'])
def login():
    data = request.json
    user = User.query.filter_by(username=data['username']).first()
    if user and user.check_password(data['password']):
        token = create_access_token(identity={'username': user.username, 'role': user.role})
        return jsonify(access_token=token), 200
    return jsonify(message="Invalid credentials"), 401
