
def isarmstrong(n):
    number = n
    sum = 0
    lenght = len(str(n))
    #print(lenght)
    while n > 0:
        sum += (n%10)**lenght
        print(sum)
        n = n//10
    if sum == number:
        return True
    else:
        return False
