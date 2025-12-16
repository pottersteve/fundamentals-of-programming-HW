
def yearsize(n):
        if n % 4 == 0:
            if n % 100 == 0:
                if n % 400 == 0:
                    return 366
                else:
                    return 365
            else:
                return 366
        else:
            return 365
