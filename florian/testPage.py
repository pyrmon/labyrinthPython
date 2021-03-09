import definitionsLabyrinth as dl

#reading the labyrinth out of the file
lab = dl.createLabyrinthDic()

#printing the labyrinth
for x in range(len(lab)):
    print(lab[x])

#trying to get my Ss location
location = dl.getS(lab)
Spieler = dl.S(location,3) 

lab = Spieler.goOneStepForward(lab)

print("\n\n\n\n\n")

for x in range(len(lab)):
    print(lab[x])
    

