import json

fileName = input("Enter the file name: \n")
file = open(fileName, "r")
list = json.load(file)
print("All the title of books in the JSON file:")
for item in list:
    print(f"- {item["title"]}")