from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from database import db
from services.models import Producto

cart_bp = Blueprint('cart', __name__)

@cart_bp.route('/cart', methods=['GET', 'POST'])
def view_cart():
    if request.method == 'POST':
        producto_id = request.form['producto_id']
        cantidad = int(request.form['cantidad'])
        cliente_id = session.get('user_id')

        if not cliente_id:
            flash('You need to log in first.', 'danger')
            return redirect(url_for('api_gateway.auth.login'))

        if 'cart' not in session:
            session['cart'] = []

        cart = session['cart']
        existing_item = next((item for item in cart if item['producto_id'] == producto_id), None)
        if existing_item:
            existing_item['cantidad'] += cantidad
        else:
            cart.append({'producto_id': producto_id, 'cantidad': cantidad})

        session['cart'] = cart
        flash('Product added to cart!', 'success')
        return redirect(url_for('api_gateway.cart.view_cart'))

    cliente_id = session.get('user_id')
    if not cliente_id:
        flash('You need to log in first.', 'danger')
        return redirect(url_for('api_gateway.auth.login'))

    cart = session.get('cart', [])
    cart_items = [{'producto': Producto.query.get(item['producto_id']), 'cantidad': item['cantidad']} for item in cart]
    products = Producto.query.all()
    return render_template('cart.html', cart_items=cart_items, products=products)

@cart_bp.route('/cart/delete/<int:producto_id>', methods=['POST'])
def delete_from_cart(producto_id):
    cart = session.get('cart', [])
    cart = [item for item in cart if item['producto_id'] != producto_id]
    session['cart'] = cart
    flash('Item removed from cart.', 'success')
    return redirect(url_for('api_gateway.cart.view_cart'))