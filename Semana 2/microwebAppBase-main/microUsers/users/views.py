# microUsers/users/views.py
from flask import Flask, jsonify
from flask_cors import CORS
from flask_consulate import Consul
from users.controllers.user_controller import user_controller
from db.db import db

app = Flask(__name__)
CORS(app)
app.config.from_object('config.Config')
db.init_app(app)

# Inicializar Consul
consul = Consul(app=app)

# Endpoint de Health Check
@app.route('/health', methods=['GET'])
def health():
    return jsonify(status="OK", service="users-service"), 200

# Registrar Blueprint
app.register_blueprint(user_controller)

if __name__ == '__main__':
    # Registrar el servicio en Consul con un Health Check
    consul.register_service(
        name="users-service",
        service_id="users-service-1",
        address="192.168.80.3",
        port=5002,
        tags=["flask", "users"],
        check={
            "http": "http://192.168.80.3:5002/health",  # Ruta de monitoreo
            "interval": "10s",  # Consul revisará la salud del servicio cada 10 segundos
            "timeout": "5s"  # Esperará 5 segundos por respuesta antes de marcar error
        }
    )
    
    # Arrancar la aplicación Flask
    app.run(host='0.0.0.0', port=5002)
