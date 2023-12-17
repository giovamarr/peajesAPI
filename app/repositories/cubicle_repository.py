from app.models.models import Cubicle
from app.repositories.base_repository import BaseRepository
from app.database.connection import db

class CubicleRepository(BaseRepository):
    def __init__(self):
        self.model = Cubicle

    def create(self, cubicle: Cubicle) -> Cubicle:
        db.session.add(cubicle)
        db.session.commit()
        return cubicle
    
    def change_status(self, cubicle: Cubicle, enabled: bool) -> Cubicle:
        cubicle.enabled = enabled
        db.session.commit()
        return cubicle