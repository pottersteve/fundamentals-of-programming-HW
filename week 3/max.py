first = int(input("Enter a number: "))
second = int(input("Enter a number: "))
third = int(input("Enter a number: "))

if first > second:
    if second > third:
        print("Number 1 is the greatest")
    else:
        if first > third:
            print("Number 1 is the greatest")
        else:
            print("Number 3 is the greatest")
elif second > first:
    if first > third:
        print("Number 2 is the greatest")
    else:
        if second > third:
            print("Number 2 is the greatest")
        else:
            print("Number 3 is the greatest")
elif first == second and first == third:
    print("All three numbers are equal")
    