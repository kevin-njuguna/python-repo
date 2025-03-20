#FUNCTION INTRODUCTION
""" def happy_birthday(name, age):
    print(f"Happy Birthday {name}! You are now {age}!")
    print(f"Happy Birthday {name}! You are now {age}!")
    print(f"Happy Birthday {name}! You are now {age}!")
    print(f"Happy Birthday {name}! You are now {age}!")
    
happy_birthday("Kevin", 21)
happy_birthday("Fridah", 20) """

""" def display_invoice(username, amount, due_date):
    print(f"Hello {username}")
    print(f"Your bill of ksh {amount:.2f} is due : {due_date}")
    
display_invoice("Maureen", 1500, 2027/2028) """

#EXAMPLE 2
""" def add(x, y):
    return x + y
    

def subtract(x, y):
    z = x - y
    return z

def multiply(x, y):
    z = x / y
    return z

def divide(x, y):
    z = x * y
    return z

print(add(4,3)) """

#EXAMPLE 3

def create_name(first, last):
    first = first.upper()
    last = last.capitalize()
    return first + " " + last

full_name = create_name("kevin", "njuguna")
print(full_name)