def extract_symmetric( lst ):
    newList = []
    for x, y in lst:
        if (y, x) in lst and x<y:
            newList.append((x, y))

    setSymetric = set(newList)
    return setSymetric
    