def display_menu():
    print("\n--- Menu ---\n1) Input numbers\n2) Ordered numbers\n3) Minimum of the numbers\n4) Maximum of the numbers\n5) Average of the numbers\n0) End\n ------------")
    choice = int(input("Enter your choice (0-5):\n"))
    match choice:
        case 1:
            #Input numbers
            listChars = input("Enter numbers separated by blanks:\n").split()
            for i in listChars:
                numbers.append(int(i))
            print(f"Successfully stored {len(numbers)} numbers.")
            display_menu()
        case 2:
            #Ordered numbers
            numbers.sort()
            print("Numbers in ascending order:")
            print(*numbers, sep=' ')
            display_menu()
        case 3:
            #Minimum of the numbers
            minim = numbers[0]
            for i in numbers:
                if i < minim:
                    minim = i
            print(f"The minimum number is: {minim}")
            display_menu()
        case 4:
            #Maximum of the numbers
            maxim = numbers[0]
            for i in numbers:
                if i > maxim:
                    maxim = i
            print(f"The maximum number is: {maxim}")
            display_menu()
        case 5:
            #Average of the numbers
            total = 0
            lenght = 0
            for i in numbers:
                total += i
                lenght += 1
            print(f"The average of the numbers is: {round(total/lenght, 2)}")
            display_menu()
        case 0:
            #End 
            print("Exiting the program. Goodbye!")
            return 0

numbers = []      
display_menu()

