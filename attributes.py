#!/usr/bin/env python3


class Noisy:
    '''
    Makes noise when you get or set attributes
    '''

    def __getattribute__(self, name):
        ''' 
        Always called on attribute reads.  Overidding this method properly is 
        difficult so you should usually define __getattr__ if you want to handle 
        missing attributes in some way.
        '''
        print("__getattribute__ called (don't do this)")

        # Invokes __getattr__
        # You could call it directly instead
        raise AttributeError('{} not found'.format(name))

    def __getattr__(self, name):
        '''
        Called when attribute is not found by __getattibute__
        '''
        print('__getattr__ called')
        return 'default'



    def __setattr__(self, name, value):
        '''
        Called when and attribute is set.
        '''
        print("__setattr__ called but __dict__ is masked by __getattr__")
        super().__setattr__(name, value)


noisy = Noisy()
print('x=' + noisy.x)
noisy.x = 100
print('x', noisy.x)


class CarefulPerson:
    '''
    Person object that uses __setattr__ to validate inputs and prevent clients 
    adding unexpected attributes.
    '''
    attrs = { 'name': str, 'age': int }

    def __init__(self, name, age):
        self.name = name 
        self.age = age 
    
    def __repr__(self):
        _type = self.__class__.__name__
        return '{}({},{})'.format(_type, self.name, self.age)

    def __setattr__(self, name, value):
        if name not in self.attrs:
            raise AttributeError('unknown attribute {}'.format(name))
        _type = self.attrs[name]
        if not isinstance(value, _type):
            raise TypeError('{} must be {}'.format(name, _type.__name__))
        super().__setattr__(name, value)
        
p = CarefulPerson('bob', 45)
print(p)
p.age = 46
try:
    p.ages = 50
except AttributeError:
    print("Caught an annoying typo")

try:
    p.age = '50'
except TypeError:
    print("Can't set age to a string")
    