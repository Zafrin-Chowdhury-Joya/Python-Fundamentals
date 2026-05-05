class Shape :
    def area(self) :
        pass
class Square(Shape) :
    def __init__(self, size) :
        self.size = size
    def area(self) :
        return self.size * self.size

class Circle(Shape) :
    def __init__(self, radius):
        self.radius = radius
    def area(self) :
        return self.radius * self.radius * 3.1416


square = Square(10)
square.area()
print(square.area())
circle = Circle(2)
circle.area()
print(circle.area())
