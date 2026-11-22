def getPayRate(jobCode):
    if jobCode == "L":
        payRate = 25
    else:
        if jobCode == "A":
            payRate = 30
        else:
            payRate = 50
    
    return payRate

# Main
totalGross = 0
print("Enter employee last name, or X to stop:")
lastName = input()
while lastName != "X":
    print("Enter job code:")
    jobCode = input()
    print("Enter hours worked:")
    hours = float(input())
    payRate = getPayRate(jobCode)
    if hours > 40:
        grossPay = 40 * payRate + hours - 40 * payRate * 1.5
    else:
        grossPay = hours * payRate
    totalGross = totalGross + grossPay
    print(lastName + " $" + str(grossPay))
    print("Enter employee last name, or X to stop:")
    lastName = input()
print("Total gross pay: $" + str(totalGross))
