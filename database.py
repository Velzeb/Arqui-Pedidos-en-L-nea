from flask_sqlalchemy import SQLAlchemy
from flask import Flask

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.secret_key = 'your_secret_key'  # Necesario para usar flash messages

    # Configuración de la base de datos
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/to'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    return app