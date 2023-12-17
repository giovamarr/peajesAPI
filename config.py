import os

class Config():
    DEBUG = True
    DB_PATH = os.path.join(os.path.dirname(__file__), 'database.db')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(DB_PATH)