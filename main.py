""" name = input("Enter your name: ")
result = len(name)

print(result)
position = name.find(" ")
print(position)

last_position = name.rfind("a")
print(last_position)

print(name.capitalize()) #capitalize the first letter of the first word
print(name.upper())
print(name.lower())
print(name.isdigit())
print(name.isalpha())

"""
 
""" phone_number = input("Enter your phone number: ")
space_length = phone_number.count(" ")
new_phone_number = phone_number.replace(" ", "-")
print(space_length)
print(new_phone_number) """

name = input("Enter your name: ")

if len(name) >12:
    print("Username is too long!")
#elif not name.find(" ") == -1:
    #print("Username must not contain spaces!")
elif " " in name:
    print("Username must not contain spaces!")
elif name.isdigit():
    print("Username must not contain digits")
else:
    print("success!")