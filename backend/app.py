# backend/app.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from routes.auth_routes import auth_blueprint
from routes.product_routes import product_blueprint
from routes.order_routes import order_blueprint
import config

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)
jwt = JWTManager(app)

# Register Blueprints
app.register_blueprint(auth_blueprint, url_prefix='/auth')
app.register_blueprint(product_blueprint, url_prefix='/product')
app.register_blueprint(order_blueprint, url_prefix='/order')

if __name__ == "__main__":
    app.run(debug=True)
