#!/usr/bin/env python3

class Readonly:
    ''' 
    Wraps and object to make it read only
    '''
    def __init__(self, obj):
        self._obj = obj 

    def __setattr__(self, name, value):
        if name == '_obj':
            super().__setattr__(name, value)
        else:
            raise AttributeError('{} is read only'.format(name))

    def __getattr__(self, name):
        return getattr(self._obj, name)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

pt = Readonly(Point(1,2))

print(pt.x, pt.y)
try:
    pt.x = 5
    print('Should not get here')
except AttributeError as ex:
    print('Caught:', ex) 