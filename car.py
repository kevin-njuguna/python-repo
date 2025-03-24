class Car():
    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale
        
    def drive(self):
        print(f"You drive the {self.year} {self.color} {self.model}")
    
    def stop(self):
        print(f"You stop the {self.year} {self.color} {self.model}")
        
    def accelerate(self):
        print(f"You accelerate {self.year} {self.color} {self.model}")
        
car1 = Car("Mustang", 2024, "red", False)
car2 = Car("Corvette", 2025, "blue", True)

car1.drive()
print(car1.model)
print(car2.year)