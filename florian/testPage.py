import definitionsLabyrinth as dl

def leftHandLabyrinthSolver(Sp):
        if Sp.relationalSurroundingsDict()[2] == '#':
            Sp.changeDirection(1)
        if Sp.relationalSurroundingsDict()[3] == '#' and Sp.relationalSurroundingsDict()[1] != '#':
            Sp.changeDirection(2)
        if Sp.relationalSurroundingsDict()[1] != '#' and Sp.relationalSurroundingsDict()[2] != '#' and Sp.relationalSurroundingsDict()[3] != '#' and Sp.relationalSurroundingsDict()[4] != '#':
            Sp.goOneStepForward()
        
        while(Sp.relationalSurroundingsDict()[1] != 'X'):
            
            if Sp.relationalSurroundingsDict()[2] != '#' and Sp.relationalSurroundingsDict()[1] == '#':
                Sp.goOneStepForward()
            
            if Sp.relationalSurroundingsDict()[2] == '#':
                if Sp.relationalSurroundingsDict()[1] != '#':
                    Sp.changeDirection(-1)
                    Sp.goOneStepForward()
                elif Sp.relationalSurroundingsDict()[3] != '#':
                    Sp.changeDirection(1)
                    Sp.goOneStepForward()
                else:
                    Sp.changeDirection(2)
                    Sp.goOneStepForward()
            
            if Sp.relationalSurroundingsDict()[2] != '#' and Sp.relationalSurroundingsDict()[1] != '#':
                Sp.changeDirection(-1)
                Sp.goOneStepForward()
        

#reading the labyrinth out of the file
lab = dl.createLabyrinthDic()

#printing the labyrinth
for x in range(len(lab)):
    print(lab[x])

#trying to get my Ss location
locationS = dl.getFirstSLocation(lab)
#generating player
Spieler = dl.S(locationS,3,lab) 
#solving labyrinth
leftHandLabyrinthSolver(Spieler)



#lab = Spieler.goOneStepForward(lab)

#print(locationS)
#print(Spieler.directionalDict(lab))

#for x in range(len(lab)):
#    print(lab[x])
    

