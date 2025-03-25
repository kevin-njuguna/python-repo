# MULTIPLE INHERITANCE fish
""" class Prey:
    def flee(self):
        print("This animal is fleeing")

class Predator:
    def hunt(self):
        print("This animal is hunting")
class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass

rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

rabbit.flee()
hawk.hunt()
fish.hunt()
 """
#MULTILEVEL INHERITANCE

class Animal:
    def __init__(self, name):
        self.name = name
    
    def eat(self):
        print(f"{self.name}  eats")
        
    def sleep(self):
        print(f"{self.name} sleeps")
class Prey(Animal):
    def flee(self):
        print(f"{self.name} is fleeing")

class Predator(Animal):
    def hunt(self):
        print(f"{self.name} is hunting")
class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass

rabbit = Rabbit("Bugs")
hawk = Hawk("Tony")
fish = Fish("Nemo")

rabbit.flee()
hawk.hunt()
fish.hunt()

fish.eat()
rabbit.sleep()