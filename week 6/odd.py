input_string = input("Enter a list, separated by commas:\n")
list_chars = input_string.split(",")
list_numbs = []
final_list = []
for char in list_chars:
    list_numbs.append(float(char))

for i in range(len(list_numbs)):
    if i % 2 == 0:
        final_list.append(list_numbs[i])

print("Numbers at odd positions:")
print(*final_list, sep=", ")