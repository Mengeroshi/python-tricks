import copy
"""Shallow copy of an object """
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return f'Point({self.x!r}, {self.y!r})'



a = Point(23, 42)
b = copy.copy(a)

print(a)
print(b)

print(a is b)

class Rectangle:
    def __init__(self, topleft, bottomright):
        self.topleft = topleft
        self.bottomright = bottomright

    def __repr__(self):
        return(f'Rectangle({self.topleft!r}, {self.bottomright!r})')

rect = Rectangle(Point(0,1), Point(5, 6))
srect = copy.copy(rect)

print(rect)
print(srect)
print(rect is srect)

rect.topleft.x = 999
print(rect)
print(srect)

""" Deep copy of an object """

deep_rect = copy.deepcopy(rect)
deep_rect.topleft.x = 222

print(rect)
print(deep_rect)