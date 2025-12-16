fileName = input("Enter the name of the file: ")
file = open(fileName, 'r')
lines = file.readlines()
count = 0
for line in lines:
    count += 1
print(f"The file contains {count} lines.")
