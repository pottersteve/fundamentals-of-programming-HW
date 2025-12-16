# all the damn lists
input_string = input("Enter a list, separated by commas:\n")
list_chars = input_string.split(",")
list_ints = []
list_final = []

# it was read as string, converted to char in split, and this finally makes it an int damn you python
for char in list_chars:
    list_ints.append(int(char))

# the actual code
for num in list_ints:
    if list_final.count(num) == 0: 
            list_final.append(num)
        
print("Modified list:")
print(*list_final, sep=", ")