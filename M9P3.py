def calcMPG(miles, gallons):
    mpg = miles / gallons
    
    return mpg

# Main
tripCount = 0
print("Enter a destination below:")
destination = input()
while destination != "X":
    print("Enter miles traveled:")
    miles = float(input())
    print("Enter gallons used:")
    gallons = float(input())
    mpg = calcMPG(miles, gallons)
    print(destination + " " + str(miles) + " " + str(mpg))
    tripCount = tripCount + 1
    print("Enter destination, or X to stop:")
    destination = input()
print("Number of trips: " + str(tripCount))
