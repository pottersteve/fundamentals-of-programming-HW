def sum_nums( lst ):
    length = len(lst)
    total = 0
    while length > 0:
        try:
            total += float(lst[length-1])
            length -= 1
        except ValueError:
            total += 0
            length -= 1
    return total