from collections import namedtuple

Car = namedtuple('Car', 'color milieage')

class MyCarWithMethods(Car):
    def hexcolor(self):
        if self.color == 'red':
            return '#ff0000'
        else:
            return '#000000'


c = MyCarWithMethods('red', 1234)

print(c.hexcolor())

""" herarchies on named tuples """

ElectricCar = namedtuple('ElectricCar', Car._fields +
                        ('charge', ))

tesla = ElectricCar('red', 1234, 45.0)

print(tesla)