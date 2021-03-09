import os

#beginning of the S class
class S:
    def __init__(self, location):
        self.location = location
    
    #here I want to scout the area and base decisions based on the Ss location
    def getWhiteSpace(s,labyrinth):
        directions = {}

# here I am reading out the labyrinthfile
def createLabyrinthDic():
    #fileDir = os.path.dirname(os.path.realpath('__file__'))
    #filename = os.path.join(fileDir, 'labyrinthPython/labyrinth.map')
    filename = "labyrinth.map" #Max: added this line to simply read map file in working dir
    f = open(filename,"r")
    labyrinth = {}
    counter = 0
    for x in f:
        size = len(x)
        if counter == 23:
            labyrinth[counter] = x
        else:
            labyrinth[counter] = x[:size-1]
        counter += 1
    return labyrinth
        
#Max: fixed output of location of S by moving some indents around
def getS(labyrinth):
    location = {}
    yValue = 0
    xValue = 0
    for x in range(len(labyrinth)):
        xValue = 0
        for each in labyrinth[x]:
            if each == "S":
                location["yValue"] = yValue
                location["xValue"] = xValue
                pass
            else:
                xValue += 1
        yValue += 1
    return location
