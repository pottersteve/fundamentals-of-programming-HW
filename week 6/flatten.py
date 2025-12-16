def flatten (lst):
    helper = []
    for matrix in lst:
        for item in matrix:
            helper.append(item)
    return helper