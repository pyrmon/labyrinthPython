import os

#beginning of the S class
class S:
    def __init__(self, location, direction):
        self.location = location
        self.direction = direction
    
    #here I want to scout the area and base decisions based on the Ss location. 0 = up, 1 = right, 2 = down, 3 = up
    def directionalDict(self,labyrinth):
        directions = {}
        yValue = self.location["yValue"]
        xValue = self.location["xValue"]
        directions[0] = labyrinth[yValue - 1 ][xValue]
        directions[1] = labyrinth[yValue][xValue + 1]
        directions[2] = labyrinth[yValue + 1 ][xValue]
        directions[3] = labyrinth[yValue][xValue - 1]
        return directions
    
    def goOneStepForward(self,labyrinth):
        if self.direction == 0:
            currentX = self.location["xValue"]
            currentY = self.location["yValue"]
            newStringY = ''
            newStringYMinusOne = ''
            counter = 0
            for each in labyrinth[currentY]:
                if counter == currentX:
                    newStringY += ' '
                else:
                    newStringY += each
                counter += 1
            counter = 0
            for each in labyrinth[currentY-1]:
                if counter == currentX:
                    newStringYMinusOne += 'S'
                else:
                    newStringYMinusOne += each
                counter += 1
            labyrinth[currentY] = newStringY
            labyrinth[currentY-1] = newStringYMinusOne
            self.location["yValue"] = currentY - 1
            return labyrinth
        
        if self.direction == 1:
            currentX = self.location["xValue"]
            currentY = self.location["yValue"]
            newStringY = ''
            counter = 0
            for each in labyrinth[currentY]:
                if counter == currentX:
                    newStringY += ' '
                elif counter == currentX + 1:
                    newStringY += 'S'
                else:
                    newStringY += each
                counter += 1
            labyrinth[currentY] = newStringY
            self.location["xValue"] = currentY + 1
            return labyrinth
        
        if self.direction == 2:
            currentX = self.location["xValue"]
            currentY = self.location["yValue"]
            newStringY = ''
            newStringYPlusOne = ''
            counter = 0
            for each in labyrinth[currentY]:
                if counter == currentX:
                    newStringY += ' '
                else:
                    newStringY += each
                counter += 1
            counter = 0
            for each in labyrinth[currentY+1]:
                if counter == currentX:
                    newStringYPlusOne += 'S'
                else:
                    newStringYPlusOne += each
                counter += 1
            labyrinth[currentY] = newStringY
            labyrinth[currentY-1] = newStringYPlusOne
            self.location["yValue"] = currentY + 1
            return labyrinth
        
        if self.direction == 3:
            currentX = self.location["xValue"]
            currentY = self.location["yValue"]
            newStringY = ''
            counter = 0
            for each in labyrinth[currentY]:
                if counter == currentX:
                    newStringY += ' '
                elif counter == currentX - 1:
                    newStringY += 'S'
                else:
                    newStringY += each
                counter += 1
            labyrinth[currentY] = newStringY
            self.location["xValue"] = currentY + 1
            return labyrinth



# here I am reading out the labyrinthfile
def createLabyrinthDic():
    #fileDir = os.path.dirname(os.path.realpath('__file__'))
    #filename = os.path.join(fileDir, 'labyrinthPython/labyrinth.map')
    filename = "labyrinth.map" 
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
        
#getting S location
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
