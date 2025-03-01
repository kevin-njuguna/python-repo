#compound interest calculator
principle = 0
rate = 0
time = 0

while principle <=0:
    principle = float(input("Enter principle amount: "))
    if principle <=0:
        print("principle can't be less than or equal to 0")
        
while rate <=0:
    rate = float(input("Enter interest rate: "))
    if rate <=0:
        print("rate can't be less than or equal to 0")
        
while True:
    time = int(input("Enter time in years: "))
    if time < 0:
        print("time can't be less than 0")
    else:
        break
    
total = principle * pow((1 + rate/100), time)
interest = total - principle

print(f"principle: {principle}")
print(f"rate: {rate}")
print(f"time: {time}")

print(f"total amount: ${round(total, 2)}")
print(f"interest: ${round(interest, 2)}")
