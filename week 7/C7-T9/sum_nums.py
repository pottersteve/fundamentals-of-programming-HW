def sum_num_file(path):
    file = open(path, 'r')
    lines = file.readlines()
    suma = 0
    for line in lines:
        suma += float(line.strip()) 
    return round(suma, 3)