"""
    Allow to function accept optional arguments
    *args collect them as a tuple
    **kwargs collect them as a dictionary
"""

def foo(required, *args, **kwargs):
    print(required)
    
    if args:
        print(args)
    if kwargs:
        print(kwargs)
    
foo("hello")

foo('hello', 1,2,3)

foo('hello', 1,2,3, key1= 'value', key2=999)