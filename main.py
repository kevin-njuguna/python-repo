#EXAMPLE 1
age = int(input("Enter your age: "))

if age>100:
    print("You are too old to sign up!")
elif age>=18:
    print("Sign up succesful")
elif age<0:
    print("You haven't been born yet")

else:
    print("Sign up failed! You must be 18+ to sign up4")


#EXAMPLE 2
response = input("Would you like some food? (y/n)?: ")

if response=="y":
    print("Here is some food for you!")
else:
    print("Got it! No food for you!")
    
#EXAMPLE 3:
for_sale = True

if for_sale:
    print("Purchase succesful!")
else:
    print("Not for sale!")