from flask import Flask, render_template, flash, redirect, url_for, session
from database import create_app, db
from routes import init_routes

app = create_app()

# Inicializa las rutas
init_routes(app)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Crea las tablas en la base de datos si no existen
    app.run(debug=True)