from flask import Blueprint, request, jsonify
from app.services.payment_service import PaymentService
from app.logs.logger import Logger
import traceback
from app.exceptions.exceptions import PaymentMethodNotFound, PriceNotValid, CubicleNotFound

payment_controller = Blueprint("payment_controller", __name__)

@payment_controller.route("/", methods=["GET"])
def get_payments():
    ''''''
    try:
        cubicles = PaymentService().get_payments()
        to_return = [cubicle.serialize() for cubicle in cubicles]
        return jsonify({"payments": to_return}), 200
    except Exception as ex:
        Logger.add_to_log("error", str(ex))
        Logger.add_to_log("error", traceback.format_exc())
        return jsonify({"error": "Internal Error"}), 500

@payment_controller.route("/", methods=["POST"])
def create_payment():
    ''''''
    # try:
    data = request.get_json()
    cubicle_id = data.get('cubicle_id')
    payment_method_id = data.get('payment_method_id')
    price = data.get('price')
    type_vehicle = data.get('type_vehicle')
    payment = PaymentService().create(cubicle_id = cubicle_id, payment_method_id = payment_method_id, price = price, type_vehicle = type_vehicle)
    return jsonify({"payment": payment.serialize()}), 201
    # except PriceNotValid:
    #     raise PriceNotValid("Price and type vehicle not match")
    # except CubicleNotFound:
    #     raise CubicleNotFound("Cubicle not valid")
    # except PaymentMethodNotFound:
    #      raise PaymentMethodNotFound("Payment method not valid")
    # except Exception as ex:
    #     Logger.add_to_log("error", str(ex))
    #     Logger.add_to_log("error", traceback.format_exc())
    #     return jsonify({"error": "Internal Error"}), 500
