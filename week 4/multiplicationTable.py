print("Enter an integer:")
num = int(input())
print(f"The multiplication table of {num} is:")

for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")