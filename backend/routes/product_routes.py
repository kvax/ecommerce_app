from flask import Blueprint, request, jsonify
from models import db, Product
from flask_jwt_extended import jwt_required, get_jwt_identity
from services.elasticsearch import index_product, search_product

product_blueprint = Blueprint('product', __name__)

@product_blueprint.route('/', methods=['GET'])
def get_catalog():
    query = request.args.get('query')
    if query:
        results = search_product(query)
        return jsonify(results)
    products = Product.query.all()
    return jsonify([product.to_dict() for product in products])

@product_blueprint.route('/', methods=['POST'])
@jwt_required()
def add_product():
    user = get_jwt_identity()
    if user['role'] != 'admin':
        return jsonify({"message": "Admins only"}), 403

    data = request.json
    new_product = Product(name=data['name'], price=data['price'], description=data['description'])
    db.session.add(new_product)
    db.session.commit()
    index_product(new_product.to_dict())
    return jsonify(new_product.to_dict()), 201
