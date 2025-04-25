from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

# Cargar variables de entorno
load_dotenv()

# Inicializar Flask
app = Flask(__name__)

# Cargar configuración desde config/config.py
app.config.from_object('config.config.Config')

# Inicializar la base de datos
from models.db import db
db.init_app(app)

# Migraciones (opcional, pero útil)
migrate = Migrate(app, db)

# Importar y registrar blueprints
from routes.client_routes import client_bp
from routes.vehicle_routes import vehicle_bp
from routes.repair_routes import repair_bp

app.register_blueprint(client_bp)
app.register_blueprint(vehicle_bp)
app.register_blueprint(repair_bp)

# Ruta por defecto
@app.route('/')
def home():
    return {"mensaje": "API Taller Mecánico en funcionamiento"}

# Ejecutar app
if __name__ == '__main__':
    app.run(debug=True)
