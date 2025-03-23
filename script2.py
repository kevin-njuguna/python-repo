from script1 import *

def favourite_drink(drink):
    print(f"Your favourite drink is {drink}")
    
def main():
    print("script2")
    favourite_drink("Cognac")
    favourite_food("Eggs")
    print("Goodbye")

if __name__ == '__main__':
    main()