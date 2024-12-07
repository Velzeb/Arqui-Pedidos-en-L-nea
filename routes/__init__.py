from .microservicios import microservice_bp
from .auth import auth_bp

def init_routes(app):
    app.register_blueprint(microservice_bp)
    app.register_blueprint(auth_bp)