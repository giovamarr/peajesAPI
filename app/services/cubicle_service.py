'''
La capa service es la logica de negocio de la aplicacion. Le pide los datos al repository sin tener contacto con la infraestructura y la devuelve al controller.

'''
from app.repositories.cubicle_repository import CubicleRepository
from app.models.models import Cubicle
from app.exceptions.exceptions import CubicleNotFound, NameNotValid

class CubicleService():
    ''''''
    def get_cubicles(self)-> list[Cubicle]:
        return CubicleRepository().get_all()

    def create(self, name:str)-> Cubicle:
        if len(name) > 100:
            raise NameNotValid()
        new_cubicle = Cubicle(name = name)
        return CubicleRepository().create(cubicle = new_cubicle)


    def change_status(self, _id:int, enabled:bool)-> Cubicle:
        cubicle = CubicleRepository().get_by_id(_id = _id)
        if not cubicle:
            raise CubicleNotFound(f"Cubicle not found")
        if cubicle.enabled == enabled:
            # Se podria lanzar una excepcion si ya se encuentra en el estado
            pass
        return CubicleRepository().change_status(cubicle = cubicle, enabled = enabled)