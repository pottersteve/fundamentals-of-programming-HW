principalAmount = input("Enter the principal amount: ")
annualInterestRate = input("Enter the annual interest rate: ")
timeInYears = input("Enter the time in years: ")

interest = (float(principalAmount) * float(annualInterestRate) * float(timeInYears)) / 100

print("The interest is:", interest)