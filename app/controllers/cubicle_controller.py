""""
La capa controller se encarga de recibir las peticiones y enviarla a los services. El service le envia la respuesta que debe responder.

"""

from flask import Blueprint, request, jsonify
from app.services.cubicle_service import CubicleService
from app.logs.logger import Logger
import traceback
from app.exceptions.exceptions import NameNotValid, CubicleNotFound, EnabledNotValid

cubicle_controller = Blueprint("cubicle_controller", __name__)

@cubicle_controller.route("/", methods=["GET"])
def get_cubicles():
    """Lista todas las cabinas existentes
    """
    try:
        cubicles = CubicleService().get_cubicles()
        cubicles_serialized = [cubicle.serialize() for cubicle in cubicles]
        return jsonify({"cubicles": cubicles_serialized}), 200
    except Exception as ex:
        Logger.add_to_log("error", str(ex))
        Logger.add_to_log("error", traceback.format_exc())
        return jsonify({"error": "as"}), 500

@cubicle_controller.route("/", methods=["POST"])
def create_cubicle():
    """Registrar nueva cabina
    """
    try:
        data = request.get_json()
        name = data.get('name')
        if not name:
            raise NameNotValid()        
        cubicle = CubicleService().create(name = name)
        return jsonify({"cubicle": cubicle.serialize()}), 201
    except NameNotValid:
        raise NameNotValid("Name is not valid")
    except Exception as ex:
        Logger.add_to_log("error", str(ex))
        Logger.add_to_log("error", traceback.format_exc())
        return jsonify({"error": "as"}), 500

@cubicle_controller.route("/", methods=["PUT"])
def toggle_cubicle():
    """Actualiza una cabina entre habilitada y deshabilitada
    """
    try:
        data = request.get_json()
        _id = data.get('id')
        enabled = data.get('enabled')
        cubicle = CubicleService().change_status(_id = _id, enabled = enabled)
        return jsonify({"cubicle": cubicle.serialize()}), 201
    except CubicleNotFound:
        raise CubicleNotFound("Cubicle is not valid")
    except EnabledNotValid:
        raise EnabledNotValid("Enabled is not valid")
    except Exception as ex:
        Logger.add_to_log("error", str(ex))
        Logger.add_to_log("error", traceback.format_exc())
        return jsonify({"error": "as"}), 500