"""
La capa repository es la encargada de hacer las consultas a la base de datos
"""
from app.database.connection import db


class BaseRepository():
    """Clase abstracta para definir metodos comunes
    """
    def __init__(self, model):
        self.model = model
    
    def get_by_id(self, _id:int):
        return db.session.get(self.model, _id)

    def get_all(self):
        return self.model.query.all()