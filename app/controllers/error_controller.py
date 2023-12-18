"""
Maneja las respuestas de las diferentes excepciones personalizadas
"""
from flask import jsonify, Blueprint, Response
from app.exceptions.exceptions import PaymentMethodNotFound, PriceNotValid, CubicleNotFound, NameNotValid, EnabledNotValid

error_controller = Blueprint("error_controller", __name__)


def _generate_error_response(error: Exception) -> Response:
    """Metodo generico para que todas las excepciones devuelvan un mensaje de erorr y el tipo de error
    """
    message = {
        "ErrorType": type(error).__name__,
        "Message": str(error)
    }
    return jsonify(message)


@error_controller.app_errorhandler(PaymentMethodNotFound)
def handle_payment_method_not_found(error: PaymentMethodNotFound) -> Response:
    """Maneja la excepcion cuando tipo de pago no es valido
    """
    response = _generate_error_response(error)
    response.status_code = 404
    return response


@error_controller.app_errorhandler(CubicleNotFound)
def handle_cubicle_not_found(error: PaymentMethodNotFound) -> Response:
    """Maneja la excepcion cuando la cabina no es valida
    """
    response = _generate_error_response(error)
    response.status_code = 404
    return response

@error_controller.app_errorhandler(PriceNotValid)
def handle_price_not_valid(error: Exception) -> Response:
    """maneja la excepcion cuando el monto y monto del tipo de vehiculo no coincide
    """
    response = _generate_error_response(error)
    response.status_code = 409
    return response

@error_controller.app_errorhandler(NameNotValid)
def handle_name_not_valid(error: Exception) -> Response:
    """maneja la excepcion cuando el nombre no cumple las validaciones
    """
    response = _generate_error_response(error)
    response.status_code = 400
    return response

@error_controller.app_errorhandler(EnabledNotValid)
def handle_enabled_not_valid(error: Exception) -> Response:
    """maneja la excepcion cuando el habilitado no es booleano
    """
    response = _generate_error_response(error)
    response.status_code = 400
    return response