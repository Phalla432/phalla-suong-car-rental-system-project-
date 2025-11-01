# routes/cars.py
from flask import Blueprint, request, jsonify
from models import db, Car

cars_bp = Blueprint('cars', __name__, url_prefix='/api/cars')

@cars_bp.route('', methods=['GET'])
def get_cars():
    cars = Car.query.all()
    return jsonify([c.to_dict() for c in cars])

@cars_bp.route('', methods=['POST'])
def create_car():
    data = request.get_json()
    car = Car(name=data['name'], price_per_day=data['price_per_day'])
    db.session.add(car)
    db.session.commit()
    return jsonify(car.to_dict()), 201

@cars_bp.route('/<int:id>', methods=['GET'])
def get_car(id):
    car = Car.query.get_or_404(id)
    return jsonify(car.to_dict())

@cars_bp.route('/<int:id>', methods=['PUT'])
def update_car(id):
    car = Car.query.get_or_404(id)
    data = request.get_json()
    car.name = data.get('name', car.name)
    car.price_per_day = data.get('price_per_day', car.price_per_day)
    db.session.commit()
    return jsonify(car.to_dict())

@cars_bp.route('/<int:id>', methods=['DELETE'])
def delete_car(id):
    car = Car.query.get_or_404(id)
    db.session.delete(car)
    db.session.commit()
    return '', 204