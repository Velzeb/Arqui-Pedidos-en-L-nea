from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from database import db
from services.models import Carrito, Producto, Compra, FormaPago

payment_bp = Blueprint('payment', __name__)

@payment_bp.route('/payment', methods=['GET', 'POST'])
def process_payment():
    cliente_id = session.get('user_id')
    if not cliente_id:
        flash('You need to log in first.', 'danger')
        return redirect(url_for('api_gateway.auth.login'))

    if request.method == 'POST':
        forma_pago_id = request.form['forma_pago']
        cart = session.get('cart', [])
        total = sum(Producto.query.get(item['producto_id']).precio * item['cantidad'] for item in cart)

        # Insertar los items del carrito en la base de datos
        for item in cart:
            new_item = Carrito(cliente_id_cliente=cliente_id, producto_id_producto=item['producto_id'], cantidad=item['cantidad'])
            db.session.add(new_item)
        db.session.commit()

        # Obtener el id del carrito recién creado
        carrito_id = Carrito.query.filter_by(cliente_id_cliente=cliente_id).first().id_carrito

        # Crear una nueva compra
        new_compra = Compra(total=total, carrito_id_carrito=carrito_id, forma_pago_id_forma_pago=forma_pago_id)
        db.session.add(new_compra)
        db.session.commit()

        # Limpiar el carrito después de la compra
        session.pop('cart', None)

        flash('Purchase successful!', 'success')
        return redirect(url_for('home'))

    formas_pago = FormaPago.query.all()
    return render_template('payment.html', formas_pago=formas_pago)