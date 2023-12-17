'''Unit Tests realizados con pytest
pytest tests.py
'''
import json 
from app import app

NEW_CUBICLE = {
      "name": "Cabina 10"
}

NEW_PAYMENT = {
        "cubicle_id": 1,
        "payment_method_id": 5,
        "price": 500,
        "type_vehicle": 1
}

# def test_get_cubicles():
#     with app.test_client() as c:
#             response = c.get('/api/cabinas/')
#             assert response.status_code == 200
#             assert b"cubicles" in response.data


# def test_get_payments():
#     with app.test_client() as c:
#             response = c.get('/api/pagos/')
#             assert response.status_code == 200
#             assert b"payments" in response.data


# def test_register_cubicle():
#     with app.test_client() as c:
#             response = c.post('/api/cabinas/', json = NEW_CUBICLE)
#             assert response.status_code == 201

# def test_register_payment():
#     with app.test_client() as c:
#             response = c.post('/api/pagos/', json = NEW_PAYMENT)
#             assert response.status_code == 201

def test_change_state_cubicle():
    with app.test_client() as c:
            # Agrego un nuevo pago para despues cambiarlo a deshabiitado
            response = c.post('/api/cabinas/', json = NEW_CUBICLE)
            assert response.status_code == 201
            _id = json.loads(response.data.decode(encoding='UTF-8'))
            response = c.put('/api/cabinas/', json={
                "id": _id["cubicle"]["id"],
                "enable": "Falso"
            })
            assert response.status_code == 200