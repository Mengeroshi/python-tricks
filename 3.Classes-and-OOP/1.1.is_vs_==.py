"""
    == test for equality;  'is' for asignation
"""

a = [1, 2, 3]
b = a

print(a)
print(b)
print(a == b)

print(a is b)

c = list(a)
print(c)
print(a == b)

print(a is c)
