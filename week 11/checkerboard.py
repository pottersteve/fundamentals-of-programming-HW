import numpy

def checkerboard( n ):
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append((i+j)%2)
        matrix.append(row)

    ndarray = numpy.array(matrix)

    return ndarray