#1. LISTs 

""" fruits = ["apple", "orange", "banana"] 
print(fruits[0])

    
print(dir(fruits))
print(help(fruits))
print(len(fruits))
print("apple" in fruits)
fruits[0] = "watermelon"
fruits.append("dragon fruit")
fruits.remove("watermelon")
fruits.insert(0, "watermelon")
fruits.sort()
fruits.reverse()
fruits.clear()
print(fruits.count("dragon fruit"))
print(fruits.index("watermelon"))
for fruit in fruits:
    print(fruit) """

#2. SET UNORDERED AND IMUTABLE. WE CAN HOWEVER ADD/REMOVE ELEMENTS.
""" fruits = {"apple", "orange", "banana", "coconut"}

print(dir(fruits))
print(help(fruits))

fruits.add("pineapple")
fruits.remove("coconut")
fruits.pop()
fruits.clear()


print(fruits) """

#3. TUPLES. ORDERED AND UNCHANGEABLE. FASTER THAN LISTS

fruits = ("apple", "pineapple", "orange", "banana")

#print(dir(fruits))
#print(help(fruits))
#print(len(fruits))
#print("pineapple" in fruits)

print(fruits.index("apple"))
print(fruits.count("orange"))
print(fruits)
for fruit in fruits:
    print(fruit)
