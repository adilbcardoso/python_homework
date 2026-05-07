import math as m
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__ (self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def __str__ (self):
        return f"Point({self.x}, {self.y})"

    def euclidian_distance(self, other):
        if not isinstance (other, Point):
            raise TypeError ("Expect a Point")
        return m.sqrt((other.x - self.x)**2 + (other.y - self.y)**2)

class Vector(Point):

    def __str__ (self):
        return f"Vector<{self.x}, {self.y}>"
    
    def __add__ (self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self.x + other.x, self.y + other.y)



p1 = Point(1, 2)
p2 = Point(1, 2)

print(p1)
print(p2)
print("p1 == p2:", p1 == p2)
print("Distance p1 to p2:", p1.euclidian_distance(p2))

v1 = Vector(3, 4)
v2 = Vector(1, 2)

print(v1)
print(v2)

v3 = v1 + v2
print("v1 + v2 =", v3)








