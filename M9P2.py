def calcAverage(hits, atBats):
    battingAverage = float(hits) / atBats
    
    return battingAverage

# Main
playerCount = 0
print("Enter player last name, or X to stop:")
lastName = input()
while lastName != "X":
    print("Enter number of hits:")
    hits = int(input())
    print("Enter number of at bats:")
    atBats = int(input())
    battingAverage = calcAverage(hits, atBats)
    print(lastName + " " + str(battingAverage))
    playerCount = playerCount + 1
    print("Enter player last name, or X to stop:")
    lastName = input()
print("Number of players: " + str(playerCount))
