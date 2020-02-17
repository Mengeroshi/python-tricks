""" Named Tupples: each object stored can be accesed through a unique
identifier """
tup = ('hello', object(), 42)
print(tup)

print(tup[2])

#tup[2] = 53

from collections import namedtuple

Car = namedtuple('Car', 'color milieage') #first argument is for class name

Car_same = namedtuple('Car', [
        'color',
        'miliage'
])

my_car = Car('red', 3812.4)

print(my_car.color)
print(my_car.milieage)

print(my_car[0])

print(*my_car) #unpacking the tupple

print(my_car)


