# decorators/typing.py


class Typed:
    data_type = object

    def __init__(self, name=None):
        self.name = name

    def __set__(self, instance, value):
        if not isinstance(value, self.data_type):
            etype = self.data_type.__name__
            gtype = value.__class__.__name__
            raise ValueError(f'{self.name}: expected {etype}, got {gtype} ({value})')
        instance.__dict__[self.name] = value

    def __get__(self, instance, cls):
        return instance.__dict__[self.name]



class Integer(Typed):
    data_type = int


class String(Typed):
    data_type = str

def typed(cls):
    '''
    This decorator adds the name of the class level variable to 
    Typed objects at run time
    '''
    for key, value in vars(cls).items():
        if isinstance(value, Typed):
            value.name = key
    return cls

@typed
class Person:
    name = String()
    age = Integer()

    def __init__(self, name, age):
        self.name = name
        self.age = age


# Using a class decorator to describe the class externally

def typed2(**kwargs):
    '''
    This decorator adds Typed descriptor objects to the classes it wraps
    based on the name/type pairs provided
    '''
    def decorator(cls):
        for name, data_type in kwargs.items():
            print(f'Adding {name} ({data_type.__name__}) to {cls.__name__}')
            setattr(cls, name, data_type(name))                
        return cls 
    return decorator

@typed2(name=String, age=Integer)
class Person2:
    def __init__(self, name, age):
        self.name = name 
        self.age = age


# $ python -i decorators/typing.py
# Adding name (String) to Person2
# Adding age (Integer) to Person2

# >>> bob = Person('Bob',45)
# >>> tam = Person('Bob','78')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "decorators/typing.py", line 46, in __init__
#     self.age = age
#   File "decorators/typing.py", line 14, in __set__
#     raise ValueError(f'{self.name}: expected {etype}, got {gtype} ({value})')
# ValueError: age: expected int, got str (78)

# >>> kim = Person2('Kim', 21)
# >>> betty = Person2('Betty','56')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "decorators/typing.py", line 67, in __init__
#     self.age = age
#   File "decorators/typing.py", line 14, in __set__
#     raise ValueError(f'{self.name}: expected {etype}, got {gtype} ({value})')
# ValueError: age: expected int, got str (56)