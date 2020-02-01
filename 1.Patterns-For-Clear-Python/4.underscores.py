"""_var means that class/variable is private """
class Test:
    def __init__(self):
        self.foo = 11
        self._bar = 23

t = Test()

print(t.foo)
print(t._bar)

""" var_ used to avoid conflicts with reserved words """
#def my_function (class_, def_, int_ )


""" __var change the name of variable to avoid collision with other class """

class Testing:
    def __init__(self):
        self.foo = 11
        self._bar = 23
        self.__baz = 42

t = Testing()
print(dir(t))

class ExtendedTest(Testing):
    def __init__(self):
        super().__init__()
        self.foo = 'overridden'
        self._bar = 'overridden'
        self.__baz = 'overridden'#dunde baz

t2 = ExtendedTest()
print(t2.foo)
print(t2._bar)
#print(t2.__baz)
"""Dunders = double underscore """
class MangledMethod:
    def __method(self): 
        return 42

    def call_it(self):
        return self.__method()

print(MangledMethod().call_it())    
#print(MangledMethod().__method())


"""  Magic Methods: __var__"""