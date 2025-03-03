capitals = {"USA": "Washington DC",
            "India": "New Delhi",
            "Russia": "Moscow",
            "Kenya": "Nairobi"
            }

#print(dir(capitals))
#print(help(capitals))

print(capitals.get("USA"))

if capitals.get("Japan"):
    print("That capital exists")
else:
    print("That capital does not exist")
    

#capitals.update({"Uganda": "Kampala"})
#capitals.update({"USA": "Detroit"})

#capitals.pop("India")
#capitals.popitem() #removes the latest key value pair that was inserted.

#capitals.clear()
keys = capitals.keys()
values = capitals.values()
items = capitals.items()
print(values)

for key in keys:
    print(key)
    
    
for value in values:
    print(value, end= " ")
    
for key, value in items:
    print(f"{key}: {value}")