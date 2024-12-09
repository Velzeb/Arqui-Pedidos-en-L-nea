from database import db

class Producto(db.Model):
    __tablename__ = 'producto'
    id_producto = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(30), nullable=False)
    precio = db.Column(db.Integer, nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {
            'id_producto': self.id_producto,
            'nombre': self.nombre,
            'precio': self.precio,
            'cantidad': self.cantidad
        }

class Carrito(db.Model):
    __tablename__ = 'carrito'
    id_carrito = db.Column(db.Integer, primary_key=True)
    cliente_id_cliente = db.Column(db.Integer, nullable=False)
    producto_id_producto = db.Column(db.Integer, db.ForeignKey('producto.id_producto'), nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)

    producto = db.relationship('Producto', backref=db.backref('carritos', lazy=True))

class Cliente(db.Model):
    __tablename__ = 'cliente'
    id_cliente = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    correo = db.Column(db.String(50), nullable=False, unique=True)
    contrasena = db.Column(db.String(50), nullable=False)

class Compra(db.Model):
    __tablename__ = 'compra'
    id_compra = db.Column(db.Integer, primary_key=True)
    total = db.Column(db.Integer, nullable=False)
    carrito_id_carrito = db.Column(db.Integer, db.ForeignKey('carrito.id_carrito', ondelete='CASCADE'), nullable=False)
    forma_pago_id_forma_pago = db.Column(db.Integer, db.ForeignKey('forma_pago.id_forma_pago'), nullable=False)

class FormaPago(db.Model):
    __tablename__ = 'forma_pago'
    id_forma_pago = db.Column(db.Integer, primary_key=True)
    forma_pago = db.Column(db.String(50), nullable=False)