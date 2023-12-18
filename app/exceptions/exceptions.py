"""Define las excepciones personalizadas
"""

class PaymentMethodNotFound(Exception):
    pass

class PriceNotValid(Exception):
    pass

class CubicleNotFound(Exception):
    pass

class NameNotValid(Exception):
    pass

class EnabledNotValid(Exception):
    pass