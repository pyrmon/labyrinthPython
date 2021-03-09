import definitionsLabyrinth as dl

#reading the labyrinth out of the file
lab = dl.createLabyrinthDic()

#printing the labyrinth
for x in range(len(lab)):
    print(lab[x])

#trying to get my Ss location
print(dl.getS(lab))

