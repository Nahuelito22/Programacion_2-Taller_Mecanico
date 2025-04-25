from flask import Blueprint, request, jsonify
from models.client import Client
from models.db import db

client_bp = Blueprint('clients', __name__, url_prefix='/clients')

# Obtener todos los clientes
@client_bp.route('/', methods=['GET'])
def get_clients():
    clients = Client.query.all()
    return jsonify([client.to_dict() for client in clients])

# Obtener un cliente por ID
@client_bp.route('/<int:client_id>', methods=['GET'])
def get_client(client_id):
    client = Client.query.get_or_404(client_id)
    return jsonify(client.to_dict())

# Crear un nuevo cliente
@client_bp.route('/', methods=['POST'])
def create_client():
    data = request.json
    new_client = Client(
        nombre=data['nombre'],
        apellido=data['apellido'],
        telefono=data.get('telefono'),
        email=data.get('email')
    )
    db.session.add(new_client)
    db.session.commit()
    return jsonify(new_client.to_dict()), 201

# Actualizar un cliente existente
@client_bp.route('/<int:client_id>', methods=['PUT'])
def update_client(client_id):
    client = Client.query.get_or_404(client_id)
    data = request.json

    client.nombre = data.get('nombre', client.nombre)
    client.apellido = data.get('apellido', client.apellido)
    client.telefono = data.get('telefono', client.telefono)
    client.email = data.get('email', client.email)

    db.session.commit()
    return jsonify(client.to_dict())

# Eliminar un cliente
@client_bp.route('/<int:client_id>', methods=['DELETE'])
def delete_client(client_id):
    client = Client.query.get_or_404(client_id)
    db.session.delete(client)
    db.session.commit()
    return jsonify({"mensaje": "Cliente eliminado"})
