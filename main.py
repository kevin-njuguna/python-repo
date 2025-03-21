#membership operators = used to test whether a variable is found in a sequence(string, list, tuple, set or dictionary)
                #1.in
                #2. not in
                
#EXAMPLE 1
""" word = "apple"

letter = input("Guess a letter in the secret word: ").lower()

if letter not in word:
    print("Failed!")
else:
   print("CORRECT!")  """
   

#EXAMPLE 2
grades = {
    "Peter": "A",
    "Fridah": "B",
    "Maureen": "C",
    "Moraa": "D"
}

student = input("Enter name of student: ").capitalize()

if student in grades:
    print(f"{student}'s grade is {grades[student]}")
else:
    print(f"{student} was not found!")