from abc import ABC, abstractmethod

class Shape:
    
    @abstractmethod
    def area(self):
        pass
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
      
    def area(self):
        return 3.142 * self.radius ** 2

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return  self.side ** 2
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
        
    def area(self):
        return self.height * self.base ** 0.5

shapes = [Circle(4), Square(4), Triangle(3, 4)]

for shape in shapes:
    print(f"{shape.area():.2f} cm²" )