weight = float(input("Enter your weight: "))
unit = input("Kilograms or Pounds? (K or L): ")

if unit == "K":
    weight = weight * 2.205
    print(f"{round(weight, 1)} Pounds")
elif unit == "L":
    weight = weight / 2.205
    print(f"{weight} Kilograms")
else:
    print(f"{unit} was not valid")
    

    

