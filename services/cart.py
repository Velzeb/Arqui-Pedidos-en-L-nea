from flask import Blueprint, jsonify, request
from database import db

cart_bp = Blueprint('cart', __name__)

class Carrito(db.Model):
    __tablename__ = 'carrito'
    id_carrito = db.Column(db.Integer, primary_key=True)
    cliente_id_cliente = db.Column(db.Integer, nullable=False)
    producto_id_producto = db.Column(db.Integer, nullable=False)

@cart_bp.route('/cart', methods=['GET'])
def get_cart():
    cart_items = Carrito.query.all()
    return jsonify([item.to_dict() for item in cart_items])

@cart_bp.route('/cart', methods=['POST'])
def add_to_cart():
    data = request.get_json()
    new_item = Carrito(cliente_id_cliente=data['cliente_id_cliente'], producto_id_producto=data['producto_id_producto'])
    db.session.add(new_item)
    db.session.commit()
    return jsonify(new_item.to_dict()), 201