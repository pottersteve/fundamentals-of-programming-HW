from csv import DictReader

fileName = input("Enter the file name: \n")
file = open(fileName, "r")
reader = DictReader(file)
sum_result = 0
for row in reader:
    try:
        number = float(row[reader.fieldnames[1]])
        sum_result += number
    except ValueError:
        continue
sum_result = round(sum_result, 2)
print(f"The sum of all numbers in the second column is: {sum_result}")
file.close()