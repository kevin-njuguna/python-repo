#Inheritance - allows a class to inherit attributes and methods from another class
# Helps with code reusability and extensibility
#class Child(Parent)

class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True
        
    def eat(self):
        print(f"{self.name} is eating")
        
    def sleep(self):
        print(f"{self.name} is sleeping")
        

class Dog(Animal):
    def speak():
        print("Woof")

class Cat(Animal):
    def speak(self):
        print("Meoow")



dog = Dog("scooby")
cat = Cat("Tom")

print(dog.name)
cat.speak()
cat.eat()