from flask import Flask
from config import Config
from app.controllers.cubicle_controller import cubicle_controller
from app.controllers.payment_controller import payment_controller
from app.controllers.error_controller import error_controller
from app.models.models import db #REVISAR CUAL DE LOS 2 DB VA
from app.database.connection import db
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

# SWAGGER CONFIG
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGER_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL, API_URL, config ={
        'app_name': "Peajes API"
    }
)


# Blueprints
app.register_blueprint(error_controller, url_prefix="/api")
app.register_blueprint(cubicle_controller, url_prefix="/api/cabinas")
app.register_blueprint(payment_controller, url_prefix="/api/pagos")
app.register_blueprint(SWAGGER_BLUEPRINT, url_prefix=SWAGGER_URL)