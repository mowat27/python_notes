# decorators/args.py

from functools import wraps


def formatlog(fmt_str):
    def logged(func):  # this is the user's function
        print('Adding logging to', func.__name__)
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(fmt_str.format(func=func))
            return func(*args, **kwargs)
        return wrapper
    return logged


@formatlog('Calling {func.__name__}')
def add(x, y):
    z = 2+3
    print('{} + {} = {}'.format(x, y, z))
    return z

# $ python -i decorators/args.py
# Adding logging to add
# >>> add(2,3)
# Calling add
# 2 + 3 = 5
# 5

# The nested functions in the decorator looks cumbersome, but it let's
# you DRY things up really nicely

logged = formatlog('Calling {func.__name__}')

@logged 
def sub(x,y):
    return x - y

@logged 
def mul(x,y):
    return x * y

# $ python -i decorators/args.py
# Adding logging to add
# Adding logging to sub
# Adding logging to mul
# >>> sub(2,3)
# Calling sub
# -1
# >>> mul(2,3)
# Calling mul
# 6


