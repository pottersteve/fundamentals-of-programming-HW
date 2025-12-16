number         = int(input("Enter a number: "))
smallest_digit = 9
largest_digit  = 0

while number > 0:
    digit = number % 10
    if digit < smallest_digit:
        smallest_digit = digit
    if digit > largest_digit:
        largest_digit = digit
    number //= 10

print(f"The smallest digit is {smallest_digit} and the largest digit is {largest_digit}.")