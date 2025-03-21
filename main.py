#ARGS EXAMPLE 1
""" def add(*args):
    for arg in args:
        total=0
        total += (arg)
    print(total)

add(4,5,6) """

#EXAMPLE 2
""" def name(*args):
    for arg in args:
        print(arg)
        
name("Kevin", "Fridah", "Maureen")
 """
 
 #EXAMPLE 3
""" def print_address(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}: {value}")

print_address(street="123", city="Mathioya", state="Murang'a", zip=123) """


#EXAMPLE 4
def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end= "")
    print()
    for key, value in kwargs.items():
        print(f"{key}: {value}")
    print(kwargs.get("apt"))

shipping_label("Dr.", "Spongebob", street="123FakeStreet" , county="Murang'a", country="Kenya", apt = "100")