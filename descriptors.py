#!/usr/bin/env python3

# Basic Descriptor Class


class Integer:
    '''
    Descriptors implement the dot. This one wraps an integer and allows you 
    to prevent deletion
    '''

    def __init__(self, name, can_delete=True):
        self._name = name
        self._can_delete = can_delete

    def __set__(self, instance, value):
        if type(value) != int:
            raise ValueError('expected int')
        instance.__dict__[self._name] = value

    def __get__(self, instance, owner=None):
        return instance.__dict__[self._name]

    def __delete__(self, instance):
        if self._can_delete:
            del(instance.__dict__[self._name])
        else:
            raise RuntimeError("{} cannot be deleted".format(self._name))


class Point:
    '''
    Creates a 2 dimensional point using the Integer to validate and store the 
    x and y coordinates.  Clumsy because you need to name them twice.
    '''
    x = Integer('x', can_delete=False)
    y = Integer('y', can_delete=False)

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Point({},{})'.format(self.x, self.y)

pt = Point(1,2)
my_x = pt.__class__.__dict__['x'].__get__(pt)
assert my_x == pt.x

pt.__class__.__dict__['y'].__set__(pt, 25)
assert pt.y == 25