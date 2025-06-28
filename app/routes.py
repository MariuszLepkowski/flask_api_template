from flask import Blueprint, jsonify, request
from app.services import make_prediction, greet_user

api = Blueprint('api', __name__)

@api.route('/', methods=['GET'])
def home_page():
    welcome_message = greet_user()
    return jsonify(welcome_message), 200

@api.route('/ping', methods=['GET'])
def ping():
    return jsonify({'message': 'pong'}), 200

@api.route('/predict', methods=['GET', 'POST'])
def predict():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Brak danych'}), 400

    result = make_prediction(data)
    return jsonify(result), 200
