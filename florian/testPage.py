import definitionsLabyrinth as dl

def directionDecision(Sp, directionalDict):
        if directionalDict[0] == ' ' and directionalDict[1] == ' ' and directionalDict[2] == ' ' and directionalDict[3] == ' ':
            direction = 3
            Sp.changeDirection(direction)
        elif directionalDict[3] == '#':
            direction = 0
            Sp.changeDirection(direction)
        elif directionalDict[2] == '#':
            direction = 3
            Sp.changeDirection(direction)
        elif directionalDict[1] == '#':
            direction = 2
            Sp.changeDirection(direction)
        elif directionalDict[0] == '#':
            direction = 1
            Sp.changeDirection(direction)

#reading the labyrinth out of the file
lab = dl.createLabyrinthDic()

#printing the labyrinth
for x in range(len(lab)):
    print(lab[x])

#trying to get my Ss location
locationS = dl.getS(lab)
Spieler = dl.S(locationS,3) 
dirDict = Spieler.directionalDict(lab)
directionDecision(Spieler,dirDict)

print(dirDict)
print(Spieler.direction)



#lab = Spieler.goOneStepForward(lab)

#print(locationS)
#print(Spieler.directionalDict(lab))

#for x in range(len(lab)):
#    print(lab[x])
    

