x1 = int(input("Input x1: "))
x2 = int(input("Input x2: "))
y1 = int(input("Input y1: "))
y2 = int(input("Input y2: "))

if x1 == x2:
    print("vertical line")
else:
    m = (y2 - y1) / (x2 - x1)
    if m>0:
        print("positive slope")
    elif m<0:
        print("negative slope")
    else:
        print("herizontal line")