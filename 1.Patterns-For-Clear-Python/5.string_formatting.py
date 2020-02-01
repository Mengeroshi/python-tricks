errno = 1231232334
name = 'Bob'

""" old style"""
print('Hello, %s' %name)

print('%x ' %errno)

print('Hey %s, there is a 0x%x error!' %(name, errno))

""" new format back ported"""

print("Hello, {}".format(name))
print("hey {name}, there is a 0x{errno: x} error".format(
    name=name,
    errno=errno)
    )

""" Interpolation Python 3.6 + """

a = 5
b = 10

print(f"five plus ten is {a+b} not {2* (a+b)}")

print("hello, "+ name)
