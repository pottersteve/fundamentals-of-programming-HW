

fileToOpen = input("Enter the name of the file: ")
file = open(fileToOpen, 'r')
lines = file.readlines()

for line in lines:
    print(f"The content of the file is: \"{line.strip()}\"")

file.close()