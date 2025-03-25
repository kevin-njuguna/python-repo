class Animal:
    alive = True
    
class Dog(Animal):
    def speak(self):
        print("Woof!")
        
class Cat(Animal):
    def speak(self):
        print("Meow!")
        
class Car(Animal):
    alive = False
    def speak(self):
        print("HONK!")
        
animals = [Dog(), Cat(), Car()]

for animal in animals:
    animal.speak()
    print(animal.alive)