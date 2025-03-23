#print(dir())
#print(__name__)
from script2 import *
def favourite_food(food):
    print(f"Your favourite food is {food}")
    
def main():
    print("This is script 1")
    favourite_food("Mukimo and beef stew")
    print("Goodbye")
    
if __name__ == '__main__':
    main()
    
