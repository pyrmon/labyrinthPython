import definitionsLabyrinth as dl

#reading the labyrinth out of the file
lab = dl.createLabyrinthDic()

#printing the labyrinth
for x in range(len(lab)):
    print(lab[x])

#trying to get my Ss location
locationS = dl.getS(lab)
Spieler = dl.S(locationS,0) 

lab = Spieler.goOneStepForward(lab)

print("\n\n\n\n\n")
#print(locationS)
#print(Spieler.directionalDict(lab))

for x in range(len(lab)):
    print(lab[x])
    

