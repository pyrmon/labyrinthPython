import os

#beginning of the S class
class S:
    def __init__(self, location, direction, labyrinth):
        self.SX = location["xValue"]
        self.SY = location ["yValue"]
        self.direction = direction
        self.labyrinth = labyrinth 
    
    #here I want to scout the area and base decisions based on the Ss location and direction. 
    # 0 = own location, 1 = left square, 2 = front square, 3 = right square, 4 = back square
    def relationalSurroundingsDict(self):
        sur = {}
        yValue = self.SY
        xValue = self.SX
        sur[0] = self.labyrinth[yValue][xValue]
        sur[1] = self.labyrinth[self.calculatePosition(xValue,yValue,self.direction - 1)[0]][self.calculatePosition(xValue,yValue,self.direction - 1)[1]]
        sur[2] = self.labyrinth[self.calculatePosition(xValue,yValue,self.direction + 0)[0]][self.calculatePosition(xValue,yValue,self.direction + 0)[1]]
        sur[3] = self.labyrinth[self.calculatePosition(xValue,yValue,self.direction + 1)[0]][self.calculatePosition(xValue,yValue,self.direction + 1)[1]]
        sur[4] = self.labyrinth[self.calculatePosition(xValue,yValue,self.direction + 2)[0]][self.calculatePosition(xValue,yValue,self.direction + 2)[1]]
        return sur

    def changeDirection(self, changedDirection):
        self.direction += changedDirection
        self.direction = self.direction % 4
        
    def calculatePosition(self, xcoord, ycoord, direction):
        xcoordn = xcoord
        ycoordn = ycoord
        tempdirection = direction % 4
        if tempdirection == 0:
            ycoordn -= 1
        elif tempdirection == 1:
            xcoordn += 1
        elif tempdirection == 2:
            ycoordn += 1
        else:
            xcoordn -= 1
        return [ycoordn,xcoordn]

    def goOneStepForward(self):
        if self.direction == 0:
            currentX = self.SX
            currentY = self.SY
            newStringYMinusOne = ''
            counter = 0
            for each in self.labyrinth[currentY-1]:
                if counter == currentX:
                    newStringYMinusOne += '^'
                else:
                    newStringYMinusOne += each
                counter += 1
            self.labyrinth[currentY-1] = newStringYMinusOne
            self.SY = currentY - 1
            
        
        if self.direction == 1:
            currentX = self.SX
            currentY = self.SY
            newStringY = ''
            counter = 0
            for each in self.labyrinth[currentY]:
                if counter == currentX + 1:
                    newStringY += '>'
                else:
                    newStringY += each
                counter += 1
            self.labyrinth[currentY] = newStringY
            self.SX = currentX + 1
            
        
        
        if self.direction == 2:
            currentX = self.SX
            currentY = self.SY
            newStringYPlusOne = ''
            counter = 0
            for each in self.labyrinth[currentY+1]:
                if counter == currentX:
                    newStringYPlusOne += 'v'
                else:
                    newStringYPlusOne += each
                counter += 1
            self.labyrinth[currentY+1] = newStringYPlusOne
            self.SY = currentY + 1
            
        
        if self.direction == 3:
            currentX = self.SX
            currentY = self.SY
            newStringY = ''
            counter = 0
            for each in self.labyrinth[currentY]:
                if counter == currentX - 1:
                    newStringY += '<'
                else:
                    newStringY += each
                counter += 1
            self.labyrinth[currentY] = newStringY
            self.SX = currentX - 1
        
        #printing the labyrinth
        #print("\n\n")
        #for x in range(len(self.labyrinth)):
        #    print(self.labyrinth[x])
            


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
#Max: hab diese Methode mal abgekürzt
def getFirstSLocation(labyrinth):
        location = {}
        for y in range(len(labyrinth)):
            if labyrinth[y].__contains__("S"):
                location["yValue"] = y
                location["xValue"] = labyrinth[y].find("S")
        return location
