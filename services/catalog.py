from flask import Blueprint, jsonify, render_template, request, redirect, url_for, flash
from database import db
from services.models import Producto

catalog_bp = Blueprint('catalog', __name__)

@catalog_bp.route('/products', methods=['GET', 'POST'])
def get_products():
    if request.method == 'POST':
        nombre = request.form['nombre']
        precio = request.form['precio']
        cantidad = request.form['cantidad']
        new_product = Producto(nombre=nombre, precio=precio, cantidad=cantidad)
        db.session.add(new_product)
        db.session.commit()
        flash('Product added successfully!', 'success')
        return redirect(url_for('api_gateway.catalog.get_products'))
    
    search_query = request.args.get('search')
    if search_query:
        products = Producto.query.filter(Producto.nombre.like(f'%{search_query}%')).all()
    else:
        products = Producto.query.all()
    return render_template('catalog.html', products=products)

@catalog_bp.route('/products/edit/<int:id>', methods=['POST'])
def edit_product(id):
    product = Producto.query.get(id)
    if product:
        product.nombre = request.form['nombre']
        product.precio = request.form['precio']
        product.cantidad = request.form['cantidad']
        db.session.commit()
        flash('Product updated successfully!', 'success')
    else:
        flash('Product not found!', 'danger')
    return redirect(url_for('api_gateway.catalog.get_products'))

@catalog_bp.route('/products/delete/<int:id>', methods=['POST'])
def delete_product(id):
    product = Producto.query.get(id)
    if product:
        db.session.delete(product)
        db.session.commit()
        flash('Product deleted successfully!', 'success')
    else:
        flash('Product not found!', 'danger')
    return redirect(url_for('api_gateway.catalog.get_products'))