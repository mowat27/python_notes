# decorators/classes.py

from functools import wraps
from datetime import datetime

# From the args example
def formatlog(fmt_str):
    def logged(func):  # this is the user's function
        print('Adding logging to', func.__name__)
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(datetime.now().time(), ":", fmt_str.format(func=func))
            return func(*args, **kwargs)
        return wrapper
    return logged

logged = formatlog('{func.__name__} was called')

def logall(cls):
    for key, value in list(vars(cls).items()):  # vars returns __dict__
        if callable(value):
            setattr(cls, key, logged(value))
    return cls

@logall 
class Product:
    def __init__(self, sku, description, stock):
        self.sku = sku
        self.description = description
        self.stock = int(stock)

    def __str__(self):
        return f'{self.sku},{self.description}, {self.stock}'

    def instock(self):
        return self.stock > 0
        
# $ python -i decorators/classes.py
# Adding logging to __init__
# Adding logging to __str__
# Adding logging to instock
# >>> lamp = Product('S0645', "A nice lamp", 10)
# 21:48:56.206171 : __init__ was called
# >>> bottle = Product('S4372', "A green bottle", 0)
# 21:49:20.068886 : __init__ was called
# >>> lamp.instock()
# 21:49:28.157348 : instock was called
# True
# >>> bottle.instock()
# 21:49:32.882591 : instock was called
# False