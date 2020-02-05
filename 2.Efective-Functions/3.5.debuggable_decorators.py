"""
    When a function have a decorator, the closure wrapper erease
    its name and docstring
"""
def greet():
    """ Return a friendly greeting. """
    return 'Hello'

def uppercase(func):
    def wrapper():
        original_result = func()
        modified_result = original_result.upper()

        return modified_result
    return wrapper

decorated_greet = uppercase(greet)

print(greet.__name__)
print(greet.__doc__)

print(decorated_greet.__name__)
print(decorated_greet.__doc__)

""" FIXED with 'functools'""" #####################################
import functools

def uppercase_FX(func):
    @functools.wraps(func)
    def wrapper():
        original_result = func()
        modified_result = original_result.upper()

        return modified_result
    return wrapper


@uppercase_FX
def greet_FX():
    """ Return a friendly greeting. """
    return 'Hello'

print(greet_FX.__name__)
print(greet_FX.__doc__)
