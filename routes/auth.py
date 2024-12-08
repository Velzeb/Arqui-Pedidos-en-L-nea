from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from database import db

auth_bp = Blueprint('auth', __name__)

class Cliente(db.Model):
    __tablename__ = 'cliente'
    id_cliente = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    correo = db.Column(db.String(50), nullable=False, unique=True)
    contrasena = db.Column(db.String(50), nullable=False)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        # Verificar el email y la contraseña con la base de datos
        user = Cliente.query.filter_by(correo=email).first()
        if user and (user.contrasena, password):
            session['user_id'] = user.id_cliente
            return redirect(url_for('home'))
        else:
            flash('Invalid email or password', 'danger')
    return render_template('login.html')

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        nombre = request.form['nombre']
        email = request.form['email']
        password = request.form['password']
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
        
        new_user = Cliente(nombre=nombre, correo=email, contrasena=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        
        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('auth.login'))
    return render_template('register.html')

@auth_bp.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('You have been logged out.', 'success')
    return redirect(url_for('home'))