from flask import Blueprint, jsonify, request
from database import db

notification_bp = Blueprint('notification', __name__)

class Notificacion(db.Model):
    __tablename__ = 'notificacion'
    id_notificacion = db.Column(db.Integer, primary_key=True)
    notificacion = db.Column(db.String(100), nullable=False)
    compra_id_compra = db.Column(db.Integer, nullable=False)
    cliente_id_cliente = db.Column(db.Integer, nullable=False)

@notification_bp.route('/notification', methods=['POST'])
def send_notification():
    data = request.get_json()
    new_notification = Notificacion(notificacion=data['notificacion'], compra_id_compra=data['compra_id_compra'], cliente_id_cliente=data['cliente_id_cliente'])
    db.session.add(new_notification)
    db.session.commit()
    return jsonify(new_notification.to_dict()), 201