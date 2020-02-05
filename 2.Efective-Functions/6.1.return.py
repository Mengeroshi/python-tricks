def foo(value):
    if value:
        return value
    else:
        return

def foo_2(value):
    if value:
        return value


print(type(foo(0)))
print(type(foo_2(0)))
