#concession stand program

menu = {"ugali": 30.00,
        "chapati": 20.00,
        "samosa": 10.00,
        "beans": 30.00,
        "omena": 50.00}

cart = []
total = 0

print("-----------MENU-----------")
for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")
    
print("--------------------------")


while True:
    food = input("Select an item (q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
        
#print(cart)
print("--------YOUR ORDER--------")
for food in cart:
    total += menu.get(food)
    print(food, end=" ")

print()
print(f"Total: ${total:.2f}")

print("---------THANK YOU!---------")