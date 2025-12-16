from datetime import datetime

date = input("Enter a date in format DD/MM/YYYY:\n")
format = "%d/%m/%Y"

try:
    datetime.strptime(date, format)
    print("The date is valid.")
except ValueError:
    print("Error: The date is invalid.")