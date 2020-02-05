def foo(x, *args, **kwargs):
    kwargs['name'] = 'Alice'
    new_args =  args +('extra',)
    bar(*new_args, **kwargs)


class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage


class AlwaysBlueCar(Car):
    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs)
        self.color = 'blue'

print(AlwaysBlueCar('green', 48392).color)

import functools

def trace(f):
    @functools.wraps(f)
    def decorated_function(*args, **kwargs):
        
        print(f.__name__, args, kwargs)
        result = f(*args, **kwargs)
        print(result)
    return decorated_function


@trace
def greet(greeting, name):
    return f'{greeting}, {name}'

print(greet('hello', 'Bob'))