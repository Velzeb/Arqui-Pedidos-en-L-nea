from flask import Blueprint, jsonify, request
from database import db

payment_bp = Blueprint('payment', __name__)

class Compra(db.Model):
    __tablename__ = 'compra'
    id_compra = db.Column(db.Integer, primary_key=True)
    total = db.Column(db.Integer, nullable=False)
    carrito_id_carrito = db.Column(db.Integer, nullable=False)
    forma_pago_id_forma_pago = db.Column(db.Integer, nullable=False)

@payment_bp.route('/payment', methods=['POST'])
def process_payment():
    data = request.get_json()
    new_payment = Compra(total=data['total'], carrito_id_carrito=data['carrito_id_carrito'], forma_pago_id_forma_pago=data['forma_pago_id_forma_pago'])
    db.session.add(new_payment)
    db.session.commit()
    return jsonify(new_payment.to_dict()), 201