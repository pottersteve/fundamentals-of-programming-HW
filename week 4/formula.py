#n = int(input("Enter a integer: "))
s = 0.00
for k in range(1, n + 1):
    s += (-1)**(k+1)/k**3
print(s)