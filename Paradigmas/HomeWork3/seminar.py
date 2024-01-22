import math


class Shape:
    def get_perimetr(self):
        pass

    def get_area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def get_perimetr(self):
        return 2 * math.pi * self.radius

    def get_area(self):
        return math.pi * self.radius ** 2


class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_perimetr(self):
        return self.a + self.b + self.c

    def get_area(self):
        p = self.get_perimetr() / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))


tri = Triangle(5, 5, 5)
print(tri.get_area())
