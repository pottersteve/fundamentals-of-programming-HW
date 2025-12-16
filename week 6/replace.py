input_string = input("Enter a list, separated by commas:\n")
list_chars = input_string.split(",")

list_chars[3] = 358

print("Modified list:")
print(*list_chars, sep=", ")