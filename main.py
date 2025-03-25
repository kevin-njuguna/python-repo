class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled
        
    def describe(self):
        print(f"It is {self.color} and {'filled' if self.is_filled else not 'filled'}")
    
class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius
        
    # method overriding    
    def describe(self):
        super().describe()
        print(f"It is a circle with an area of {(3.142 *self.radius ** 2):.2f}cm²")
        return 0
        

class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width 
    
    def describe(self):
        super().describe()
        print(f"It is a square with an area of {(self.width ** 2):.2f}cm²")

class Triangle(Shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width 
        self.height = height
        
    def describe(self):
        super().describe()
        print(f"It is a triangle with an area of {(self.width * self.height * 0.5):.2f}cm²")
        
circle = Circle(color = "blue", is_filled= True, radius= 5) #object
square = Square(color = "yellow", is_filled= True, width = 5) #object
triangle = Triangle(color = "grey", is_filled= False, width = 5, height = 10) #object


print(circle.color)
print(triangle.is_filled)
print(circle.describe())
print()
print(square.describe())
print()
print(triangle.describe())
