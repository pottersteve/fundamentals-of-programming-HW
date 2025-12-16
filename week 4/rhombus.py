space = " "
star = "* "

print("Enter an odd integer: ")
n = int(input())

if n % 2 == 0:
    print("You entered an invalid number.")
    n = int(input("Enter an odd integer: "))
else:
    middle = n//2

    for i in range(0, middle+1):
        print(space * (middle - i) + star * (i + 1))
    for i in range(middle-1, -1, -1):
        print(space * (middle - i) + star * (i + 1))

        