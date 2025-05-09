from models.db import db

# Clase de clientes
class Client(db.Model):
    __tablename__ = 'clients'

    # Atributos de los clientes
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    apellido = db.Column(db.String(100), nullable=False)
    telefono = db.Column(db.String(20))
    email = db.Column(db.String(120), unique=True)

    # La relacion de los vehiculos es 1:N
    vehiculos = db.relationship('Vehicle', backref='cliente', lazy=True)

    def __repr__(self):
        return f"<Client {self.nombre} {self.apellido}>"

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "apellido": self.apellido,
            "telefono": self.telefono,
            "email": self.email,
        }
