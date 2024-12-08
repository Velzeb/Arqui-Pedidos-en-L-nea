from flask import Blueprint, jsonify
from database import db

catalog_bp = Blueprint('catalog', __name__)

class Producto(db.Model):
    __tablename__ = 'producto'
    id_producto = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(30), nullable=False)
    precio = db.Column(db.Integer, nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)

@catalog_bp.route('/products', methods=['GET'])
def get_products():
    products = Producto.query.all()
    return jsonify([product.to_dict() for product in products])

@catalog_bp.route('/product/<int:id>', methods=['GET'])
def get_product(id):
    product = Producto.query.get(id)
    if product:
        return jsonify(product.to_dict())
    return jsonify({'error': 'Product not found'}), 404