#list comprehension - a concise way to create lists in Python
# Compact and easier to read than traditional loops
#[expression for value in iterable if condition]

#EXAMPLE 1 NUMBERS
""" import math
doubles = [x*2 for x in range(1,11)]
print(doubles)

triples = [y*3 for y in range(1,11)]
print(triples)

squares = [math.pow(z,2) for z in range(1,11)]
print(squares) """


#EXAMPLE 2 STRINGS
""" fruits = ["apple", "orange", "banana", "coconut"]
fruits =[fruit.upper() for fruit in fruits]

print(fruits) """

#EXAMPLE 3
numbers = [1, -2, 3, -4, 5, -6]
positive_nums = [num for num in numbers if num>=0]
negative_nums = [num for num in numbers if num<0]
even_nums = [num for num in numbers if num%2==0]
odd_nums = [num for num in numbers if num%2==1]

print(positive_nums)
print(negative_nums)
print(even_nums)
print(odd_nums)

grades = [65, 30, 40, 90, 87, 26, 44]
passing_grades = [num for num in grades if num>=60]
print(passing_grades)