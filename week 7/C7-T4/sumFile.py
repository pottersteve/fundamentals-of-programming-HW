revenueReportFile = open('revenue_report.txt', 'w')
revenueReportFile.write('Product,Total Revenue\n')

fileName = input("Enter the name of the CSV file: \n")
file = open(fileName, 'r')
lines = file.readlines()

for line in lines[1:]:  
    inputs = line.strip().split(',')
    productName = inputs[0]
    quantitySold = int(inputs[1])
    unitPrice = float(inputs[2])
    totalRevenue = quantitySold * unitPrice
    revenueReportFile.write(f"{productName} generated {totalRevenue:.2f} euros in revenue.\n")

print("Revenue has been recorded in the file \"revenue_report.txt\".")
revenueReportFile.close()   
file.close()