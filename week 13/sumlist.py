def sum_of_list_recursive(numbers):
    if len(numbers) == 0:
        return 0
    else:
        return numbers[0] + sum_of_list_recursive(numbers[1:])