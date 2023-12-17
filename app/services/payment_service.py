'''
La capa service es la logica de negocio de la aplicacion. Le pide los datos al repository sin tener contacto con la infraestructura y la devuelve al controller.

'''
from app.repositories.payment_repository import PaymentRepository, PaymentMethodRepository, PriceRepository
from app.repositories.cubicle_repository import CubicleRepository
from app.models.models import Payment
from app.exceptions.exceptions import PaymentMethodNotFound, PriceNotValid, CubicleNotFound

class PaymentService():
    ''''''
    def get_payments(self)-> list[Payment]:
        return PaymentRepository().get_all()

    def create(self, cubicle_id:int, payment_method_id:int, price:float, type_vehicle:int)-> Payment:
        cubicle = CubicleRepository().get_by_id(cubicle_id)
        if not cubicle:
            raise CubicleNotFound()
        payment = PaymentMethodRepository().get_by_id(payment_method_id)
        if not payment:
            raise PaymentMethodNotFound()
        actual_price = PriceRepository().get_by_type_vehicle(type_vehicle)
        if not actual_price or actual_price != price:
            raise PriceNotValid()
        new_payment = Payment(cubicle_id = cubicle_id, payment_method_id = payment_method_id, price = price)
        return PaymentRepository().create(payment = new_payment)
