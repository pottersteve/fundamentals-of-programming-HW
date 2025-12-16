def analyze_nums(lst):
    print(f"The input list is: {lst}")

    lst_tuple_float = []
    for num in lst:
        lst_tuple_float.append(float(num))
    lst_tuple_float = tuple(lst_tuple_float)

    minNum = lst_tuple_float[0]
    maxNum= lst_tuple_float[0] 
    suma = 0
    for number in lst_tuple_float:
        suma += number
        if number < minNum:
            minNum = number
        if number > maxNum:
            maxNum = number 

    print(f"min: {minNum}")
    print(f"max: {maxNum}")
    print(f"count: {len(lst)}")
    unique = tuple(sorted(set(lst_tuple_float)))
    print(f"unique: {unique}")
    reversedlst = tuple(reversed(lst_tuple_float))
    print(f"reversed: {reversedlst}")
    mean = round(suma/len(lst), 2)
    print(f"mean: {mean}")

    dict = {}
    dict["min"] = minNum
    dict["max"] = maxNum
    dict["count"] = len(lst)
    dict["unique"] = unique
    dict["reversed"] = reversedlst
    dict["mean"] = mean

    return dict
    


#lst = input("enter a list of numbers: ")
#analyze_nums(lst)