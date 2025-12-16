def contains_duplicates(lst):
    lst_set = set(lst)
    if len(lst_set) != len(lst):
        return True
    return False