# .TXT
""" employees = ["Eugene", "Squidward", "Spongebob", "Patrick"]
txt_data = "I like pizza"

file_path = "output.txt"

try:
    with open(file_path, "w") as file:
        for employee in employees:
            file.write(employee + "\n")
        print(f"txt file '{file_path}' was created")
except FileExistsError:
    print("file exists")
    
 """
 
 #JSON
""" import json
 
employees = {
    "name": "Spongebob",
    "age": 30,
    "job": "cook"
}

file_path = "output.json"

try:
    with open(file_path, "w") as file:
        json.dump(employees, file, indent=4)
        print(f"json file '{file_path}' was created")
except FileExistsError:
    print("file exists")
     """

#CSV
import json
import csv
 
employees = [["Name", "Age", "Job"],
             ["Sandy", 27, "Scientist"],
             ["Spongebob", 30, "Cook"],
             ["Patrick", 37, "Unemployed"]]

file_path = "output.csv"

try:
    with open(file_path, "w", newline="") as file:
        writer = csv.writer(file)
        for row in employees:
            writer.writerow(row)
        print(f"csv file 'file_path' was created")
except FileExistsError:
    print("file exists")
    