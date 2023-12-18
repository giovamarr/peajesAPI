from datetime import datetime
from app.database.connection import db


class Cubicle(db.Model):
    """Cabina de peaje"""
    __tablename__ = 'cubicles'
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.String(100))
    date = db.Column(db.DateTime, default=datetime.now, nullable=False)
    enabled = db.Column(db.Boolean, default = True)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "date": self.date,
            "enabled": self.enabled
        }

    def serialize_simple(self):
        return {
            "id": self.id,
            "name": self.name
        }

class PaymentMethod(db.Model):
    """Metodos de pago"""
    __tablename__ = 'payment_methods'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
        }

class Price(db.Model):
    """Precios por tipo de vehiculos"""
    __tablename__ = 'prices'
    id = db.Column(db.Integer, primary_key = True)
    type_vehicle = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float(precision=2), nullable=False)

class Payment(db.Model):
    """Pagos realizados"""
    __tablename__ = 'payments'
    id = db.Column(db.Integer, primary_key = True)
    cubicle_id = db.Column(db.Integer, db.ForeignKey('cubicles.id'), nullable=False)
    payment_method_id = db.Column(db.Integer, db.ForeignKey('payment_methods.id'), nullable=False)
    price = db.Column(db.Float(precision=2), nullable=False)
    date = db.Column(db.DateTime, default=datetime.now, nullable=False)

    # Relationships
    payment_method = db.relationship("PaymentMethod")
    cubicle = db.relationship("Cubicle")


    def serialize(self):
        return {
            "id": self.id,
            "price": self.price,
            "date": self.date,
            "cubicle": self.cubicle.serialize_simple(),
            "payment_method": self.payment_method.serialize()
        }
