import time
duration = int(input("How long would you like to set the timer for (seconds): "))

for x in (range(duration, 0, -1)):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600) % 60
   
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("TIME'S UP")