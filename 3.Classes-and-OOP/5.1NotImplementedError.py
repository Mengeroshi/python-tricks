""" To enforce that derived class implements a number of methods
    from base class we use 'NoImplementedError'  """

class Base:
    def foo(self):
        raise NotImplementedError
    
    def bar(self):
        raise NotImplementedError

class Concrete(Base):
    def foo(self):
        return 'foo() called'
    
b = Base()

#b.foo()

c = Concrete()

print(c.foo())
c.bar()
