def rotate(lst, pos):
    if pos <= len(lst):
        lst = lst[-pos:] + lst[:-pos]
    else:
        pos = pos%len(lst) + 1
        lst = lst[-pos:] + lst[:-pos]
    #print("Rotated list:", lst)

#input_list = input()
#chars_list = input_list.split(",")
#step = int(input())
#rotate(chars_list, step)
