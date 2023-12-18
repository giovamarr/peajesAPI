"""
La capa repository es la encargada de hacer las consultas a la base de datos
"""
from app.models.models import Cubicle
from app.repositories.base_repository import BaseRepository
from app.database.connection import db

class CubicleRepository(BaseRepository):
    """Clase para obtener los datos de las cabinas de la base de datos
    """
    def __init__(self):
        self.model = Cubicle

    def create(self, cubicle: Cubicle) -> Cubicle:
        """Registra la cabina
        """
        db.session.add(cubicle)
        db.session.commit()
        return cubicle
    
    def change_status(self, cubicle: Cubicle, enabled: bool) -> Cubicle:
        """Cambia el estado de la cabina

        Args:
            cubicle (Cubicle): la cabina que se quiere actualizar
            enabled (bool): el estado deseado
        """
        cubicle.enabled = enabled
        db.session.commit()
        return cubicle