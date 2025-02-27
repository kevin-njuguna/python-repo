num = 5
a=6
b=5

print("Positive" if num > 0 else "Negative")
max_num = a if a > b else b 
min_num = a if a < b else b

print(f"max_num:  {max_num}")
print(f"min_num:  {min_num}")