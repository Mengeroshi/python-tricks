class Car:
    rev = lambda self: print('Wroom')
    crash = lambda self:print('Crash')

my_car = Car()
my_car.crash()


#harmfull
list(filter(lambda x: x % 2 == 0, range(16)))
#better
[x for x in range(16) if x % 2 == 0]