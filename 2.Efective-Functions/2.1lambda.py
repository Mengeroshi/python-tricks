""" Lambda are single statement anonymous function """

add = lambda x, y: x + y
print(add(5, 3))


print((lambda x, y: x + y)(10, 20))


"""Sorting iterables with alt key """

tuples = [(1, 'd'), (2, 'b'), (4, 'a'), (3, 'c')]

tuples.sort(key=lambda x: x[1])
print(tuples)

""" this are the same"""
lel = list(range(-5, 6))
lel.sort(key=lambda x: x * x)
print(lel)

print(sorted(range(-5, 6), key=lambda x: x*x))