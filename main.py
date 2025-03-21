#EXAMPLE 1
""" def hello(greeting- title, first, last):
    print(f"{greeting} {title} {first} {last}")
    
hello("Hello", first="Kevin", last="Njuguna", title="Mr.") """

#EXAMPLE 2
#end is a keyword argurment
""" for x in range(1,10):
    print(x, end=" ") 
     """

#EXAMPLE 3
#sep is a keyword argurment   
print("1","1","1","1","1","1", sep=" ")

def get_phone(country, area, first, last):
    return(f"{country}-{area}-{first}-{last}")
    
phone_number = get_phone(country=254, area=123, first=456, last=789)
print(phone_number)