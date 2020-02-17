"""__str__  gets called when you try to convert an object to a string"""
class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __str__(self):
        return f'a {self.color} car'

my_car = Car('red', 37281)
print(my_car)