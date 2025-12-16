try:
    int1 = int(input("Enter the first number: \n"))
    int2 = int(input("Enter the second number: \n"))
    result = round(int1 / int2, 2)
    print(f"The result is {result}")
except ValueError:
    print("Error: both inputs should be numbers.")
except ZeroDivisionError:
    print(f"Error: {int1} cannot be divided by 0.")