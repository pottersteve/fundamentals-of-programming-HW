firstString = input("Enter the first string: ")
secondString = input("Enter the second string: ")

firstString = firstString[:len(firstString)//2] + secondString + firstString[len(firstString)//2:]

print(firstString)