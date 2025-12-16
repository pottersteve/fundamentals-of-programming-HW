def dec(i):
    try:
        num = int(i)
        num -= 1
        return num
    except ValueError:
        return None