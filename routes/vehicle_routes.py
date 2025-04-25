from flask import Blueprint, request, jsonify
from models.vehicle import Vehicle
from models.db import db

vehicle_bp = Blueprint('vehicles', __name__, url_prefix='/vehicles')

# Obtener todos los vehículos
@vehicle_bp.route('/', methods=['GET'])
def get_vehicles():
    vehicles = Vehicle.query.all()
    return jsonify([vehicle.to_dict() for vehicle in vehicles])

# Obtener un vehículo por ID
@vehicle_bp.route('/<int:vehicle_id>', methods=['GET'])
def get_vehicle(vehicle_id):
    vehicle = Vehicle.query.get_or_404(vehicle_id)
    return jsonify(vehicle.to_dict())

# Crear un nuevo vehículo
@vehicle_bp.route('/', methods=['POST'])
def create_vehicle():
    data = request.json
    new_vehicle = Vehicle(
        marca=data['marca'],
        modelo=data['modelo'],
        anio=data.get('anio'),
        patente=data['patente'],
        cliente_id=data['cliente_id']
    )
    db.session.add(new_vehicle)
    db.session.commit()
    return jsonify(new_vehicle.to_dict()), 201

# Actualizar un vehículo
@vehicle_bp.route('/<int:vehicle_id>', methods=['PUT'])
def update_vehicle(vehicle_id):
    vehicle = Vehicle.query.get_or_404(vehicle_id)
    data = request.json

    vehicle.marca = data.get('marca', vehicle.marca)
    vehicle.modelo = data.get('modelo', vehicle.modelo)
    vehicle.anio = data.get('anio', vehicle.anio)
    vehicle.patente = data.get('patente', vehicle.patente)
    vehicle.cliente_id = data.get('cliente_id', vehicle.cliente_id)

    db.session.commit()
    return jsonify(vehicle.to_dict())

# Eliminar un vehículo
@vehicle_bp.route('/<int:vehicle_id>', methods=['DELETE'])
def delete_vehicle(vehicle_id):
    vehicle = Vehicle.query.get_or_404(vehicle_id)
    db.session.delete(vehicle)
    db.session.commit()
    return jsonify({"mensaje": "Vehículo eliminado"})
