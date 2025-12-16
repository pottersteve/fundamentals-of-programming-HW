def input_num(): 
    try:
        num = float(input())
        return num
    except ValueError:
        print("Wrong input. The input should be a number only.")
        return None


totalNum = int(input("How many numbers that you want to input:\n"))
leftNum = totalNum
suma = 0.0

while leftNum > 0:
    print(f"{leftNum} number(s) left to input. Enter a number:")
    num = input_num()
    if num is not None:
        suma = suma + num
        leftNum -= 1

suma = round(suma, 2)
    
print(f"The sum of {totalNum} input numbers is {suma}")

