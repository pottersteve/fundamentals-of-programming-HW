rows = int(input("Enter number of rows: \n"))
columns = int(input("Enter number of columns: \n"))

matrix = []
sum_rows = []
sum_columns = [0] * columns
total_sum = 0

for i in range(rows):
    print(f"Enter the numbers for row {i}:")
    row = []
    suma = 0
    values = input().split(" ")
    for j in range(columns):
        num = int(values[j])
        row.append(num)
        suma += num
        sum_columns[j] += num
        total_sum += num
    matrix.append(row)
    sum_rows.append(suma)

print(f"Row sums: {sum_rows}")
print(f"Column sums: {sum_columns}")
print(f"Total sum: {total_sum}")