"""
Decorators: allow you to extend the behaviour of a callable(fun, class, method)
"""

def null_decorator(func):
    return func


def greet():
    return 'hello'

greet = null_decorator(greet)

print(greet())

@null_decorator
def greeting():
    return 'hello!'

print(greeting())
