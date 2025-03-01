rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))
symbol = (input("Enter a symbol: "))

""" for x in range(3):
    for x in range(1,10):
        print(x, end="")
    print() """
    
for x in range(rows):
    for x in range(1, columns+1):
        print(symbol, end="")
    print()