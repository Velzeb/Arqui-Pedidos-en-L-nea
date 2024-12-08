from .api_gateway import api_gateway_bp

def init_routes(app):
    app.register_blueprint(api_gateway_bp, url_prefix='/api')