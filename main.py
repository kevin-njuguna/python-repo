operator = input("Enter an operator: (+ - * /): ")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if operator == "+" :
    print(f"sum: {num1 +num2}")
elif operator =="-":
    print(f"subtraction: {num1 - num2}")
elif operator == "*" :
    print(f"product: {num1*num2}")
elif operator == "/":
    print(f"division: {num1/num2}")
else:
    print("Please enter a valid operator (+ - * /)")
    

    

