print("Enter a non-negative integer: ")
n = int(input())
a = 0
b = 1

if  n <= 0:
    print("You entered an invalid number.")

while n>0:
    print(a)
    b = a + b
    a = b - a
    n -= 1
