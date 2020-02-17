class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __repr__(self):
        return (f'{self.__class__.__name__}('
            f'{self.color!r}, {self.mileage!r})')

my_car = Car('red', 37281)
print(my_car)

print(str(my_car))
print(repr(my_car))
