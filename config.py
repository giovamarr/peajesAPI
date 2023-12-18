import os
from flask_swagger_ui import get_swaggerui_blueprint

class Config():
    DEBUG = True
    DB_PATH = os.path.join(os.path.dirname(__file__), 'database.db')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(DB_PATH)

class ConfigSwagger():
    SWAGGER_URL = '/docs'
    API_URL = '/static/swagger.json'
    SWAGGER_BLUEPRINT = get_swaggerui_blueprint(
        SWAGGER_URL, API_URL, config ={
            'app_name': "Peajes API"
        }
    )