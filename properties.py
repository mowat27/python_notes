#!/usr/bin/env python3
# pylint: disable=E1101

# Properties
class Example:
    '''
    Demonstrates out-of-the-box behaviour for setting properties
    '''
    def __init__(self, x):
        self._x = x 

    @property
    def x(self):
        '''
        Accessor for x
        '''
        return self._x 
    
    @x.setter 
    def x(self, value):
        '''
        Setter for x.  You could put validation in here. 
        '''
        self._x = value             

    @property
    def xx(self):
        '''
        Method that looks like an attribute.
        '''
        return self.x + self.x 

example = Example(1)
assert example.x == 1
assert example.xx == 2
print('x={}, xx={}'.format(example.x, example.xx))

example.x = 'bob'
assert example.x == 'bob'
assert example.xx == 'bobbob'
print('x={}, xx={}'.format(example.x, example.xx))

# How attribute and property access works
class Popo:
    '''
    A Plain Old Python Object (POPO?).  No funny business.
    '''

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self._z = z

    @property
    def z(self):
        return self._z

    def whats_x(self):
        return 'x is {}'.format(self.x)


popo = Popo(1, 'hello', [1, 2, 3])

# Attributes are stored in a dict inside an object
print('popo object:', popo.__dict__)
popo.__dict__['x'] = 'bob'
assert popo.x == 'bob'

# Python lets you add items to the dict
popo.__dict__['a'] = False
assert popo.a == False


# Methods are stored as properties on the class's dict
assert popo.__class__.__dict__['whats_x'](popo) == 'x is bob'

# Property objects have __get__ and __set__ methods that manage the __dict__ of
# the object passed.
# Python translates the dot to __get__ or __set__ as appopriate
zprop = popo.__class__.__dict__['z']
assert zprop.__get__(popo) == popo.z
print('z =', zprop.__get__(popo))
try:
    zprop.__set__(popo, 'new value')
except AttributeError:
    print('z is read only')

# Same for methods
mprop = popo.__class__.__dict__['whats_x']
print(mprop.__get__(popo)())

