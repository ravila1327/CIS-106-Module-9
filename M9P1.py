def calcExtended(quantity, price):
    extendedPrice = quantity * price
    if extendedPrice > 10000:
        extendedPrice = extendedPrice * 0.9
    
    return extendedPrice

# Main
totalExtended = 0
print("Enter Quanttity")
quantity = int(input())
while quantity != 0:
    print("Enter price:")
    price = float(input())
    extendedPrice = calcExtended(quantity, price)
    print(str(quantity) + " " + str(price) + " " + str(extendedPrice))
    totalExtended = totalExtended + extendedPrice
    print("Enter quantity, or 0 to stop:")
    quantity = int(input())
print("Total extended price: $" + str(totalExtended))
