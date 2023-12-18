"""Unit Tests realizados con pytest
"""
from app import app


# Crea los datos de prueba con los diferentes escenarios capturados. Es una lista de tuplas del objeto a crear y el codigo que deberia retornar la API.
CUBICLES_TESTS = [({
      "name": "Cabina 10"
        }, 201),
({
      "name": ""
        }, 400),
]

PAYMENTS_TESTS = [
     ({
        "cubicle_id": 1,
        "payment_method_id": 1,
        "price": 500,
        "type_vehicle": 1}, 201),
        ({
        "cubicle_id": 1000,
        "payment_method_id": 1,
        "price": 500,
        "type_vehicle": 1}, 404),
        ({
        "cubicle_id": 1,
        "payment_method_id": 1000,
        "price": 500,
        "type_vehicle": 1}, 404),
        ({
        "cubicle_id": 1,
        "payment_method_id": 1,
        "price": 2500,
        "type_vehicle": 1}, 409)
]

def test_get_cubicles():
    '''Test unitario del metodo obtener cabinas'''
    with app.test_client() as c:
            response = c.get('/api/cabinas/')
            assert response.status_code == 200
            assert b"cubicles" in response.data


def test_get_payments():
    '''Test unitario del metodo obtener pagos'''
    with app.test_client() as c:
            response = c.get('/api/pagos/')
            assert response.status_code == 200
            assert b"payments" in response.data


def test_register_cubicle():
    '''Test unitario del metodo para registrar cabinas'''
    for CUBICLE in CUBICLES_TESTS:
        with app.test_client() as c:
                response = c.post('/api/cabinas/', json = CUBICLE[0])
                assert response.status_code == CUBICLE[1]

def test_register_payment():
    '''Test unitario del metodo para registrar pagos'''
    for PAYMENT in PAYMENTS_TESTS:
        with app.test_client() as c:
                response = c.post('/api/pagos/', json = PAYMENT[0])
                assert response.status_code == PAYMENT[1]
