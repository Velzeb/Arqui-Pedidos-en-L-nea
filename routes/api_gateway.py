from flask import Blueprint
from services.auth import auth_bp
from services.catalog import catalog_bp
from services.cart import cart_bp
from services.payment import payment_bp
from services.notification import notification_bp

api_gateway_bp = Blueprint('api_gateway', __name__)

api_gateway_bp.register_blueprint(auth_bp, url_prefix='/auth')
api_gateway_bp.register_blueprint(catalog_bp, url_prefix='/catalog')
api_gateway_bp.register_blueprint(cart_bp, url_prefix='/cart')
api_gateway_bp.register_blueprint(payment_bp, url_prefix='/payment')
api_gateway_bp.register_blueprint(notification_bp, url_prefix='/notification')