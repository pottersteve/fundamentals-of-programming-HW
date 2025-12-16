import numpy

rows = int(input("Enter number of rows: \n"))
columns = int(input("Enter number of columns: \n"))

matrix = []

for i in range(rows):
    print(f"Enter row {i+1}:")
    row = []
    values = input().split(" ")
    for j in range(columns):
        num = int(values[j])
        row.append(num)
    matrix.append(row)

matrixnp = numpy.array(matrix)

found = False
for i in range(rows):
    for j in range(columns):
        if matrixnp[i][j] == 0:
            row0 = i
            col0 = j
            found = True
            break
    if found:
        break

if found:
    matrixnp[row0, :] = 0
    matrixnp[:, col0] = 0

print("Modified matrix:")
print(matrixnp)