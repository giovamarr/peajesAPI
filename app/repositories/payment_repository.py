"""
La capa repository es la encargada de hacer las consultas a la base de datos
"""
from app.database.connection import db
from app.repositories.base_repository import BaseRepository
from app.models.models import Payment, PaymentMethod, Price

class PaymentRepository(BaseRepository):
    """Clase para obtener los datos de los pagos de la base de datos
    """
    def __init__(self):
        self.model = Payment

    def create(self, payment: Payment) -> Payment:
        """Registra el pago
        """
        db.session.add(payment)
        db.session.commit()
        return payment

class PaymentMethodRepository(BaseRepository):
    """Clase para obtener los datos de los medios de pagos de la base de datos
    """
    def __init__(self):
        self.model = PaymentMethod

class PriceRepository(BaseRepository):
    """Clase para obtener los datos de los precios de los vehiculos de la base de datos
    """
    def __init__(self):
        self.model = Price

    def get_by_type_vehicle(self, type_vehicle:int) -> int:
        """Metodo que valida el monto con el tipo de vehiculo

        Args:
            type_vehicle (int): el tipo de vehiculo

        Returns:
            int: el monto de ese tipo de vehiculo
        """
        price = self.model.query.filter_by(type_vehicle = type_vehicle).one()
        if not price:
            return None
        return price.price