from flask import Blueprint, jsonify

microservice_bp = Blueprint('microservice', __name__)

@microservice_bp.route('/api/data', methods=['GET'])
def get_data():
    data = {
        'message': 'This is data from the microservice',
        'status': 'success'
    }
    return jsonify(data)