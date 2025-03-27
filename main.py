import datetime

date = datetime.date(2025, 1, 2)
today = datetime.date.today()

time = datetime.time(12, 30, 0)
now = datetime.datetime.now()

now = now.strftime("%H:%M:%S %d-%m-%Y")

target_date_time = datetime.datetime(2040, 1, 2,  12, 30, 1)
current_date_time = datetime.datetime.now()

#print(date)
#print(today)
#print(now)

if target_date_time < current_date_time:
    print("Target Date has passed")
else:
    print("Target date has not passed")


