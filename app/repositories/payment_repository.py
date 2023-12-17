from app.database.connection import db
from app.repositories.base_repository import BaseRepository
from app.models.models import Payment, PaymentMethod, Price

class PaymentRepository(BaseRepository):
    def __init__(self):
        self.model = Payment

    def create(self, payment: Payment) -> Payment:
        db.session.add(payment)
        db.session.commit()
        return payment

class PaymentMethodRepository(BaseRepository):
    def __init__(self):
        self.model = PaymentMethod

class PriceRepository(BaseRepository):
    def __init__(self):
        self.model = Price

    def get_by_type_vehicle(self, type_vehicle:int) ->int:
        price = self.model.query.filter_by(type_vehicle = type_vehicle).one()
        if not price:
            return None
        return price.price