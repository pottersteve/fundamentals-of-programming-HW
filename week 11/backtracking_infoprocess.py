list = [177, 337, 354, 365, 493, 573, 651, 691]

suma = 0
total = 2200
gasit = False
for i in range(0, len(list)):
    for j in range(i, len(list)):
        for k in range(j, len(list)):
            for l in range(k, len(list)):
                for m in range(l, len(list)):
                    suma = list[i] + list[j] + list[k] + list[l] + list[m]
                    if suma == total:
                        gasit = True
                        print(f"unu: {list[i]} doi: {list[j]} trei: {list[k]} patru: {list[l]} cinci: {list[m]}")
                    