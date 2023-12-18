from flask import Flask
from config import Config, ConfigSwagger
from app.controllers.cubicle_controller import cubicle_controller
from app.controllers.payment_controller import payment_controller
from app.controllers.error_controller import error_controller
from app.database.connection import db

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

# Blueprints (rutas)
app.register_blueprint(error_controller, url_prefix="/api")
app.register_blueprint(cubicle_controller, url_prefix="/api/cabinas")
app.register_blueprint(payment_controller, url_prefix="/api/pagos")
# Pagina de documentacion
app.register_blueprint(ConfigSwagger.SWAGGER_BLUEPRINT, url_prefix=ConfigSwagger.SWAGGER_URL)