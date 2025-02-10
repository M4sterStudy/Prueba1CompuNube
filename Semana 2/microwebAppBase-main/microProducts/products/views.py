# microProducts/products/views.py
from flask import Flask, jsonify
from flask_cors import CORS
from flask_consulate import Consul
from products.controllers.product_controller import product_controller
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
    return jsonify(status="OK", service="products-service"), 200

# Registrar Blueprint
app.register_blueprint(product_controller)

if __name__ == '__main__':
    # Registrar el servicio en Consul con un Health Check
    consul.register_service(
        name="products-service",
        service_id="products-service-1",
        address="192.168.80.3",
        port=5003,
        tags=["flask", "products"],
        check={
            "http": "http://192.168.80.3:5003/health",  # URL para verificar salud
            "interval": "10s",  # Consul revisará la salud cada 10 segundos
            "timeout": "5s"  # Esperará 5 segundos antes de marcar error
        }
    )
    
    # Arrancar la aplicación Flask
    app.run(host='0.0.0.0', port=5003)
