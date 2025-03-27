#.TXT
""" file_path ="output.txt"

try:
    with open(file_path, "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("That file not found")
except PermissionError:
    print("You do not have permission to read that file") """
    

#JSON
""" import json

file_path = "output.json"

try:
    with open(file_path, "r") as file:
        content = json.load(file)
        print(content)
        print(content["name"])
except FileNotFoundError:
    print("That file not found")
except PermissionError:
    print("You do not have permission to read that file") """
    

#CSV
import csv

file_path = "output.csv"

try:
    with open(file_path, "r") as file:
        content = csv.reader(file)
        for line in content:
            print(line)
            print(line[2])
        
except FileNotFoundError:
    print("That file not found")
except PermissionError:
    print("You do not have permission to read that file")