number = int(input("Enter a number: "))

#odd = bool(number%2)
#array = ["even", "odd"]
#print(array[odd])

print("even" * (number%2 == 0) + "odd" * (number%2 == 1))