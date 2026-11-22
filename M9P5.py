def calcTuition(creditHours, districtCode):
    if districtCode == "I":
        tuition = creditHours * 250
    else:
        tuition = creditHours * 550
    
    return tuition

# Main
totalTuition = 0
print("Enter student last name, or X to stop:")
lastName = input()
while lastName != "X":
    print("Enter credit hours:")
    creditHours = int(input())
    print("Enter district code (I or O):")
    districtCode = input()
    tuition = calcTuition(creditHours, districtCode)
    print(lastName + " $" + str(tuition))
    totalTuition = totalTuition + tuition
    print("Enter student last name, or X to stop:")
    lastName = input()
print("Total tuition owed: $" + str(totalTuition))
