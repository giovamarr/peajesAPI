""""
La capa service es la logica de negocio de la aplicacion. Le pide los datos al repository sin tener contacto con la infraestructura y la devuelve al controller.

"""
from app.repositories.cubicle_repository import CubicleRepository
from app.models.models import Cubicle
from app.exceptions.exceptions import CubicleNotFound, NameNotValid, EnabledNotValid

class CubicleService():
    """
    clase encargada de manejar la logica de las cabinas
    """
    def get_cubicles(self)-> list[Cubicle]:
        """Obtiene todas las cabinas

        Returns:
            list[Cubicle]: devuelve una lista de cabinas
        """
        return CubicleRepository().get_all()

    def create(self, name:str)-> Cubicle:
        """Valida que los atributos de la cabina sean correctos

        Args:
            name (str): nombre de la cabina

        Raises:
            NameNotValid: cuando el nombre no es valido

        Returns:
            Cubicle: devuelve la cabina
        """
        if len(name) > 100:
            raise NameNotValid()
        new_cubicle = Cubicle(name = name)
        return CubicleRepository().create(cubicle = new_cubicle)


    def change_status(self, _id:int, enabled:bool)-> Cubicle:
        """Valida los datos para cambiar de estado la cabina

        Args:
            _id (int): el id de la cabina que se quiere actualizar
            enabled (bool): el estado que se desea

        Raises:
            EnabledNotValid: cuando el estado no es valido
            CubicleNotFound: cuando

        Returns:
            Cubicle: devuelve la cabina actualizada
        """
        if type(enabled) is not bool:
            raise EnabledNotValid()

        cubicle = CubicleRepository().get_by_id(_id = _id)
        if not cubicle:
            raise CubicleNotFound()
        if cubicle.enabled == enabled:
            # Se podria lanzar una excepcion si ya se encuentra en el estado
            pass
        return CubicleRepository().change_status(cubicle = cubicle, enabled = enabled)