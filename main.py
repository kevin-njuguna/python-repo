#format specifiers - {:flags} that allows us to format a value based on what flags are inserted

price1 = 3000.14519
price2 = -9087.651
price3 = 1200.34

print(f"price 1: ${price1:.2f}")
print(f"price 2: ${price2:.2f}")
print(f"price 3: ${price3:.2f}")
print(f"price 1: ${price1:>14}")
print(f"price 2: ${price2:,}")