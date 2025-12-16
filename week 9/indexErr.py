try:
    list1 = input("Enter a list, separated by commas: \n").split(",")
    print(f"There are currently {len(list1)} items in the list.")
    index = int(input("Enter an index number: \n"))
    print(f"The item in index {index} is {list1[index]}.")
except IndexError:
    print(f"Error: Out of the list. There are only {len(list1)} items in the list.")