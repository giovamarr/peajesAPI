"""
Archivo para crear la base de datos y cargar datos a las tablas de metodos de pago y precios para poder probar la API
"""

import sqlite3
from contextlib import contextmanager
from config import Config

@contextmanager
def __get_cursor():
    '''Metodo encargado de abrir y cerrar la conexion a la base de datos'''
    connection = sqlite3.connect(Config.DB_PATH)
    cursor = connection.cursor()
    try:
        yield cursor
        connection.commit()
    finally:
        cursor.close()
        connection.close()


def create_tables():
    '''Crea las tablas en la base de datos'''
    with __get_cursor() as cursor:
        cursor.execute("CREATE TABLE IF NOT EXISTS cubicles(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, date DATETIME, enabled BOOLEAN )")
        cursor.execute("CREATE TABLE IF NOT EXISTS payment_methods(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)")
        cursor.execute("CREATE TABLE IF NOT EXISTS prices(id INTEGER PRIMARY KEY AUTOINCREMENT, type_vehicle INTEGER, price FLOAT)")
        cursor.execute("CREATE TABLE IF NOT EXISTS payments(id INTEGER PRIMARY KEY AUTOINCREMENT, cubicle_id INTEGER, price FLOAT, \
                        payment_method_id INTEGER, date DATETIME,\
                        FOREIGN KEY (cubicle_id) \
                        REFERENCES cubicles (id) \
                        ON DELETE CASCADE \
                        FOREIGN KEY (payment_method_id) \
                        REFERENCES payment_methods (id) \
                        ON DELETE CASCADE)")


def insert_payment_method(name:str):
    '''Inserta datos de medios de pago'''
    with __get_cursor() as cursor:
        cursor.execute(f"INSERT INTO payment_methods (name) VALUES ('{name}')")

def insert_price(type_vehicle:int, price:int):
    '''Inserta datos de precios de tipos de vehiculos'''
    with __get_cursor() as cursor:
        cursor.execute(f"INSERT INTO prices (type_vehicle, price) VALUES ({type_vehicle}, {price})")

if __name__ == "__main__":
    create_tables()
    insert_payment_method('efectivo')
    insert_payment_method('SUBE')
    insert_payment_method('TelePASE')
    insert_price(type_vehicle=1, price=500)
    insert_price(type_vehicle=2, price=800)
