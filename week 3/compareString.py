print("Enter the first string:")
firstString = input()
print("Enter the second string:")
secondString = input()

if len(firstString)>len(secondString):
    print(firstString, "is bigger than ", secondString)
else:
    print(secondString, "is bigger than", firstString)