from flask import Blueprint, request, jsonify
from models.repair import Repair
from models.db import db

repair_bp = Blueprint('repairs', __name__, url_prefix='/repairs')

# Obtener todas las reparaciones
@repair_bp.route('/', methods=['GET'])
def get_repairs():
    repairs = Repair.query.all()
    return jsonify([repair.to_dict() for repair in repairs])

# Obtener una reparación por ID
@repair_bp.route('/<int:repair_id>', methods=['GET'])
def get_repair(repair_id):
    repair = Repair.query.get_or_404(repair_id)
    return jsonify(repair.to_dict())

# Crear una nueva reparación
@repair_bp.route('/', methods=['POST'])
def create_repair():
    data = request.json
    new_repair = Repair(
        descripcion=data['descripcion'],
        fecha_ingreso=data['fecha_ingreso'],
        fecha_salida=data.get('fecha_salida'),
        costo=data['costo'],
        vehicle_id=data['vehicle_id']
    )
    db.session.add(new_repair)
    db.session.commit()
    return jsonify(new_repair.to_dict()), 201

# Actualizar una reparación
@repair_bp.route('/<int:repair_id>', methods=['PUT'])
def update_repair(repair_id):
    repair = Repair.query.get_or_404(repair_id)
    data = request.json

    repair.descripcion = data.get('descripcion', repair.descripcion)
    repair.fecha_ingreso = data.get('fecha_ingreso', repair.fecha_ingreso)
    repair.fecha_salida = data.get('fecha_salida', repair.fecha_salida)
    repair.costo = data.get('costo', repair.costo)
    repair.vehicle_id = data.get('vehicle_id', repair.vehicle_id)

    db.session.commit()
    return jsonify(repair.to_dict())

# Eliminar una reparación
@repair_bp.route('/<int:repair_id>', methods=['DELETE'])
def delete_repair(repair_id):
    repair = Repair.query.get_or_404(repair_id)
    db.session.delete(repair)
    db.session.commit()
    return jsonify({"mensaje": "Reparación eliminada"})
