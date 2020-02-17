""" this modules alerts you what methods are you missing """

from abc import ABCMeta, abstractmethod

class Base(metaclass=ABCMeta):
    @abstractmethod
    def foo(self):
        pass

    @abstractmethod
    def bar(self):
        pass

class Concrete(Base):
    def foo(self):
        pass

assert issubclass(Concrete, Base)

"""Example """ 
c = Concrete()