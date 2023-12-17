'''Para poder heredar los metodos basicos y reutilizarlos'''
from app.database.connection import db


class BaseRepository():
    def __init__(self, model):
        self.model = model
    
    def get_by_id(self, _id:int):
        return db.session.get(self.model, _id)

    def get_all(self):
        return self.model.query.all()