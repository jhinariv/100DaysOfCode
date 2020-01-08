from datetime import datetime
from datetime import date
from datetime import timedelta

#datetime.datetime(2018, 2, 19, 14, 38, 52, 133483)

# get current date
today = datetime.today()
# print (today)

# get current year
# print(today.year)

# get current day of the year
# print(today.day)

# get current month of the year
# print(today.month)

# format datetime
today_format = today.strftime("%m/%d/%y")
# print(today_format)
today_format = today.strftime("%d-%m-%y")
# print(today_format)
today_format = today.strftime("%H:%M:%S %p")
# print(today_format)

# sum 3 days to current date
endDate = today.replace(today.year + 3).strftime("%m/%d/%y")
# print(endDate)

# res 5 years to current date
endDate = today.replace(today.year - 5).strftime("%m/%d/%y")
# print(endDate)

# get if today is christmas day
christmas = date(2020, 12, 25)
today_2 = date(2020, 1, 6)
if christmas is not today_2:
    diff = christmas - today_2
    print("Sorry there are still " + str(diff) + " days until Christmas!")
else:
    print("Yay it's Christmas!")

# get 30 days before today
print(today)
before = today - timedelta(days=30)
print(before)

# get 60 days after today
after = today + timedelta(days=60)
print(after)

# get 6 weeks after today
afterw = today + timedelta(weeks=6)
print(afterw)

# get 6 years before today
beforey = today - timedelta(days=2190)
print(beforey)
