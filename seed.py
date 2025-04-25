from models.db import db
from models.client import Client
from models.vehicle import Vehicle
from models.repair import Repair
from app import app

with app.app_context():
    db.drop_all()
    db.create_all()

    # Clientes
    cliente1 = Client(nombre="Juan", apellido="Pérez", email="juanperez@example.com", telefono="2611234567")
    cliente2 = Client(nombre="Laura", apellido="Gómez", email="lauragomez@example.com", telefono="2617654321")

    db.session.add_all([cliente1, cliente2])
    db.session.commit()

    # Vehículos
    vehiculo1 = Vehicle(marca="Ford", modelo="Fiesta", anio=2015, patente="ABC123", cliente_id=cliente1.id)
    vehiculo2 = Vehicle(marca="Toyota", modelo="Corolla", anio=2020, patente="XYZ789", cliente_id=cliente2.id)

    db.session.add_all([vehiculo1, vehiculo2])
    db.session.commit()

    # Reparaciones
    reparacion1 = Repair(descripcion="Cambio de aceite", fecha_ingreso="2024-04-01", fecha_salida="2024-04-02", costo=5000, vehicle_id=vehiculo1.id)
    reparacion2 = Repair(descripcion="Frenos nuevos", fecha_ingreso="2024-04-10", fecha_salida=None, costo=12000, vehicle_id=vehiculo2.id)

    db.session.add_all([reparacion1, reparacion2])
    db.session.commit()

    print("Datos de prueba insertados exitosamente ✅")
