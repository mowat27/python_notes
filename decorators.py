#!/usr/bin/env python3

import functools

# Simple decorators takes a function as an argument but there's a twist that 
# means using functools.wraps is advisable to preserve the name and docstrings
# from the wrapped function.

def simple(func):
    def wrapper(*args, **kwargs):
        '''
        simple wrapper
        '''
        print('{} was wrapped by simple'.format(func.__name__))
        return func(*args, **kwargs)
    return wrapper


@simple
def hello():
    '''
    function that prints hello
    '''
    return 'Hello!'


msg = hello()
print(f'{msg} was returned')


print(hello.__name__)  # prints 'wrapper' instead of 'hello'
print(hello.__doc__.strip())  # prints doc string from decorator

# functools.wraps fixes this by hiding the wrapper function
def simple2(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        '''
        simple2 wrapper
        '''
        print('{} was wrapped by simple2'.format(func.__name__))
        return func(*args, **kwargs)
    return wrapper


@simple2
def goodbye():
    '''
    function that prints goodbye
    '''
    return 'Goodbye!'


print(goodbye.__name__)
print(goodbye.__doc__.strip())
