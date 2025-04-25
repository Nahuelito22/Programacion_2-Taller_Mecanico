# app.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

# Cargar variables de entorno
load_dotenv()

# Inicializar Flask
app = Flask(__name__)

# Cargar configuración 
app.config.from_object('config.config.Config')

# Iniciar databse
from models.db import db
db.init_app(app)

# Importar y registrar blueprints
from routes.client_routes import client_bp
from routes.vehicle_routes import vehicle_bp
from routes.repair_routes import repair_bp

app.register_blueprint(client_bp)
app.register_blueprint(vehicle_bp)
app.register_blueprint(repair_bp)

# por los blueprints.
with app.app_context():
    print("Intentando crear tablas...") # Probar si funciona
    db.create_all()
    print("Llamada a db.create_all() completada.") # Debugg para crear tablas

# Ruta por defecto
@app.route('/')
def home():
    return {"mensaje": "API Taller Mecánico en funcionamiento"}

if __name__ == '__main__':
    app.run(debug=True)