from flask import Flask, render_template, flash
from routes import init_routes

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Necesario para usar flash messages

# Inicializa las rutas
init_routes(app)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)