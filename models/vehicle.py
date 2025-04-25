from models.db import db

class Vehicle(db.Model):
    __tablename__ = 'vehicles'

    id = db.Column(db.Integer, primary_key=True)
    marca = db.Column(db.String(100), nullable=False)
    modelo = db.Column(db.String(100), nullable=False)
    anio = db.Column(db.Integer)
    patente = db.Column(db.String(20), unique=True, nullable=False)

    # Clave foránea al cliente
    cliente_id = db.Column(db.Integer, db.ForeignKey('clients.id'), nullable=False)

    # Relación con reparaciones
    reparaciones = db.relationship('Repair', backref='vehiculo', lazy=True)

    def __repr__(self):
        return f"<Vehicle {self.patente} - {self.marca} {self.modelo}>"

    def to_dict(self):
        return {
            "id": self.id,
            "marca": self.marca,
            "modelo": self.modelo,
            "anio": self.anio,
            "patente": self.patente,
            "cliente_id": self.cliente_id,
        }
