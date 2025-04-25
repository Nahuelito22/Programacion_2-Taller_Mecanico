from models.db import db
from datetime import datetime

class Repair(db.Model):
    __tablename__ = 'repairs'

    id = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.Text, nullable=False)
    fecha_ingreso = db.Column(db.DateTime, default=datetime.utcnow)
    fecha_egreso = db.Column(db.DateTime, nullable=True)
    costo = db.Column(db.Float, nullable=False)

    # Clave foránea al vehículo
    vehiculo_id = db.Column(db.Integer, db.ForeignKey('vehicles.id'), nullable=False)

    def __repr__(self):
        return f"<Repair {self.id} - Vehículo ID: {self.vehiculo_id}>"

    def to_dict(self):
        return {
            "id": self.id,
            "descripcion": self.descripcion,
            "fecha_ingreso": self.fecha_ingreso.strftime('%Y-%m-%d %H:%M:%S'),
            "fecha_egreso": self.fecha_egreso.strftime('%Y-%m-%d %H:%M:%S') if self.fecha_egreso else None,
            "costo": self.costo,
            "vehiculo_id": self.vehiculo_id,
        }
