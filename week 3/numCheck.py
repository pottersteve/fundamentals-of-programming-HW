print("Enter a number:")
number = int(input())
if number>0:
    positive = 1
else:
    positive = 0

if number%2==0:
    even = 1
else:
    even =0 

if positive:
    if even:
        print("This is a positive even number.")
    else:
        print("This is a positive odd number.")
else:
    if even:
        print("This is a negative even number.")
    else:
        print("This is a negative odd number.")

if number == 0:
    print("This is zero, which is an even number")