fib = [0, 1]
stopping = int(input("Enter a positive integer: "))

while len(fib) <= stopping:  
    next = fib[-1] + fib[-2]
    fib.append(next)
    
print(fib[stopping])