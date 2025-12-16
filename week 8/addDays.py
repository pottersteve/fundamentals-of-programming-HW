import datetime

print("Enter a date:")
input_date = input()
print("Enter a number of days:")
add_day = int(input())

oldDate = datetime.datetime.strptime(input_date, "%d.%m.%Y")
timeDifference = datetime.timedelta(days=add_day)
new_date = (oldDate + timeDifference).strftime("%d.%m.%Y")

print(f"The new date is: {new_date}")