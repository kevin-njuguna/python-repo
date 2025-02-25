import math

friends = 10
# (power) friends **= 2
friends %= 2

print(friends)

x = 9.1
y = 4
z= 5 

#result = round(x)
#result = abs(y)
#result = pow(y,3)
result = max(x,y,z)



#print(math.pi)
#print(math.e)
#result = math.sqrt(x)
result = math.ceil(x)

print(result)

#Exercise 1: circumfrence of a circle
radius = 2

circumfrence = 2 * math.pi * radius
print(round(circumfrence, 2))

#Exercise 2: area of a circle
radius = 2

area = math.pi * (radius**2)
print(round(area, 2))

#exercise 3: hypotenuse
a =3
b=4

c = math.sqrt(pow(a,2) + pow(b,2))
print(c)


