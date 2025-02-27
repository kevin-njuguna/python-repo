#or, and and not
#OR
temp = 40
is_raining = True

if temp >455 or temp<0 or is_raining:
    print("The outdoor event is cancelled!")

#AND
if temp > 40 and is_raining:
    print("The outdoor event is cancelled!")
else: 
    print("The outdoor event is ongoing!")
    
#NOT
if not is_raining:
    print("It is sunny")
else:
    print("It is raining")