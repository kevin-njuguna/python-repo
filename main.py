#decorator - a function that extends the behaviour of another funtion w/o modifying the base function
#pass the base function as an argument to the decorator

#decor ator
def add_sprinkles(func):
    def wrapper(*args, **kwargs):
        print("***You add sprinkles🎊")
        func(*args, **kwargs)
    return wrapper

def add_fudge(func):
    def wrapper(*args, **kwargs):
        print("You add fudge")
        func(*args, **kwargs)
    return wrapper
        
@add_sprinkles
@add_fudge 
def get_ice_cream(flavor):
    print(f"Here is your {flavor} ice cream🍨")
    

get_ice_cream("vanilla")

