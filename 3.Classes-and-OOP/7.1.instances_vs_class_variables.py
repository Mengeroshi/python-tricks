class Dog:
    num_legs = 4 #<-- class variable

    def __init__(self, name):
        self.name = name #<--- instance variable


jack = Dog('Jack')
jill = Dog('Jill')

print(jack.name)
print(jill.name)

print(jack.num_legs)
print(jill.num_legs)
print(Dog.num_legs)