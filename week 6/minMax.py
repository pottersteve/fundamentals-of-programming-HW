provided_list = [73, 12, 95, 41, -8, 27, 66, 30, -89, 54]

smallest_num = provided_list[0]
largest_num = provided_list[0]

for num in provided_list:
    if num < smallest_num:
        smallest_num = num
    if num > largest_num:
        largest_num = num

print("Smallest number: ", smallest_num)
print("Largest number: ", largest_num)