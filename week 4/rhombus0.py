print("Enter an odd integer: ")
n = int(input())
if n % 2 == 0:
    print("You entered an invalid number.")
    n = int(input("Enter an odd integer: "))

middle = n//2
#print(middle)

for i in range(0, n):
    if i < middle:
        spaces = (middle - i)/2 + 1
        stars = i + 1
    
    if i > middle:
        spaces = (i - middle)/2 + 1        
        stars = n - i

    if i == middle:
        for star in range(0, middle+1):
            print("*", sep=" ", end=" ")
    else:
        for space in range(0, int(spaces)):
            print(" ", sep=" ", end ="")
        for star in range(0, stars):
            print("*", sep=" ", end=" ")
    
    print(" ")