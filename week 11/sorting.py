def sort_lst_tup(tup):
    newTuple = ()
    newLists = []
    for list in tup:
        listSorted = sorted(list)
        newLists.append(listSorted)
    newTuple = tuple(newLists)
    return newTuple