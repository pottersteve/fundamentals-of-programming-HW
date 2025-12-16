import numpy

def create_matrix():
    rows = int(input("Enter number of rows: \n"))
    columns = int(input("Enter number of columns: \n"))

    matrix = []

    for i in range(rows):
        print(f"Enter the numbers for row {i+1}:")
        row = []
        values = input().split(" ")
        for j in range(columns):
            num = int(values[j])
            row.append(num)
        matrix.append(row)

    matrixnp = numpy.array(matrix)

    return matrixnp

def is_square(matrix):
    rows, columns = numpy.shape(matrix)
    if rows == columns:
        return True
    return False

print("Matrix A:")
matrixA = create_matrix()
print("Matrix B:")
matrixB = create_matrix()

if is_square(matrixA) == False and is_square(matrixB) == False:
    print("Both matrices A and B are not square and cannot be inverted.")
    exit
elif is_square(matrixA) == False:
    print("Matrix A is not square and cannot be inverted.")
    exit
elif is_square(matrixB) == False:
    print("Matrix B is not square and cannot be inverted.")
    exit
else:
    A_inv = numpy.linalg.inv(matrixA)
    B_inv = numpy.linalg.inv(matrixB)

    final_result = numpy.dot(A_inv, B_inv)

    print("Inverse of matrix A:")
    print(A_inv)
    print("Inverse of matrix B:")
    print(B_inv)
    print("Product of A_inv and B_inv:")
    print(final_result)