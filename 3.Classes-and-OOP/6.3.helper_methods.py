from collections import namedtuple
import json

Car = namedtuple('Car', 'color milieage')

my_car = Car('red', 1234)

print(my_car._asdict())

print(json.dumps(my_car._asdict()))

