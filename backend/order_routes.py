from flask import Blueprint, request, jsonify
from models import Order, User
from app import db  # Import db from backend/__init__.py
from flask_jwt_extended import jwt_required, get_jwt_identity
# from ..services.kinesis import put_user_activity

order_blueprint = Blueprint('order', __name__)

@order_blueprint.route('/', methods=['POST'])
@jwt_required()
def place_order():
    user = get_jwt_identity()
    data = request.json
    user = User.query.filter_by(username=user['username']).first()
    new_order = Order(user_id=user.id, product_id=data['product_id'])
    db.session.add(new_order)
    db.session.commit()
    
    # Log order activity to Kinesis
    # put_user_activity({"user": user['username'], "action": "placed order", "order_id": new_order.id})
    
    return jsonify(new_order.to_dict()), 201
