import random
import queue

CWALL = 0
CFLOOR = 1
CENTRANCE = 2
CEXIT = 3


class MatrixGridObjectContainer:
    def __init__(self, *args):
        self.objContainer = []
        for i in range(4):
            self.objContainer.append(args[i])

    def GetObjAtIndex(self,index):
        #Hardcoded based on consts
        if index >= 0 and index < 4:
            return self.objContainer[index]

    def GetEndOfLineObj(self):
        return None


class MatrixGrid:
    """
    A matrix grid that builds a maze and puts it into a graph data structure

    self.walls key:

    CWALL = 0
    CFLOOR = 1
    CENTRANCE = 2
    CEXIT = 3
    """
    def __init__(self, size) -> None:
        
        self.size = size
        if size % 2 == 0:
            self.size += 1
        self.map = []
        self.adjacencyList = []

        self.walls = []
        for y in range(self.size + 1 + self.size):
            row = []
            for x in range(self.size + 1 + self.size):
                row.append(CWALL)
            self.walls.append(row)
        
        for i in range(self.size*self.size):
            self.adjacencyList.append([])
        
        for j in range(self.size*self.size):
            if (j + 1) % self.size != 0:
                #im not on the right edge, so i can add to the right
                self.adjacencyList[j].append(j+1)
            if j % self.size != 0:
                #im not on the left edge, so i can add to the left
                self.adjacencyList[j].append(j-1)
            if j + self.size < self.size*self.size:
                #im not on the bottom row, so i can add below
                self.adjacencyList[j].append(j+self.size)
            if j - self.size >= 0:
                #im not on the top, so i can add to the top
                self.adjacencyList[j].append(j-self.size)

        


    def __str__(self):
        return self.map

    def Generate(self,start,end):
        stack = queue.LifoQueue()
        #init empty stack
        visitedDict = {}
        #init empty visited dict
        for j in range(self.size*self.size):
            #set all corresponding grid squares to empty on the map
            #convert from linear j pos to grid xy coord
            wallsLoc = self.GraphIndexToWallsPos(j)
            #convert from xy coord to a self.walls location
            self.walls[wallsLoc[1]][wallsLoc[0]] = CFLOOR
            #set that self.walls location to be walkable = true
            visitedDict[j] = False
        visitedDict[start] = True
        #make the start node visited
        stack.put(start)
        #put start node on the stack
        while not stack.empty():
            #while the stack isn't empty, aka not all spaces visited
            curCell = stack.get()
            #current cell is top from stack
            unvisitedNeighbors = []
            #initialzie a new list of unvisited neighbors
            for neighbor in self.adjacencyList[curCell]:
                #for each neighbor of curCell's
                if visitedDict[neighbor] == False:
                    #if it has not been visited yet, add it to the unvisited neighbors
                    unvisitedNeighbors.append(neighbor)
            #if there are any unvisited neighbors
            if len(unvisitedNeighbors) > 0:
                #put the current cell on the stack to be revisited later
                stack.put(curCell)
                #choose a random unvisited neighbor
                choice = unvisitedNeighbors[random.randint(0,len(unvisitedNeighbors)-1)]
                #remove the wall between the choice cell and the current cell
                cellDif = choice - curCell

                #convert from linear j pos to grid xy coord
                wallsLocCurCell = self.GraphIndexToWallsPos(curCell)

                if cellDif < 0:
                    #if diff is neg, it is either to the left or top
                    if 0 - cellDif < self.size:
                        #then it must be to the left of cur cell
                        self.walls[wallsLocCurCell[1]][wallsLocCurCell[0]-1] = CFLOOR
                    else:
                        #it is to the top of cur cell
                        self.walls[wallsLocCurCell[1]-1][wallsLocCurCell[0]] = CFLOOR
                else:
                    #if diff is pos, it is either to the right or bottom
                    if cellDif < self.size:
                        #it must be to the right of cur cell
                        self.walls[wallsLocCurCell[1]][wallsLocCurCell[0]+1] = CFLOOR
                    else:
                        #it must be to the bottom
                        self.walls[wallsLocCurCell[1]+1][wallsLocCurCell[0]] = CFLOOR
                #Mark choice number as visited
                visitedDict[choice] = True
                #put it on the stack
                stack.put(choice)
    
    def GraphIndexToWallsPos(self,index):
        gridLocCurCell = (index%self.size,index//self.size)
        #convert from linear j pos to grid xy coord
        return ((gridLocCurCell[0]*2) + 1,(gridLocCurCell[1]*2) + 1)

    def BuildMap(self,start,end,matrixObjContainer:MatrixGridObjectContainer):
        self.Generate(start,end)
        self.map = []
        startWallsPos = self.GraphIndexToWallsPos(start)
        endWallsPos = self.GraphIndexToWallsPos(end)
        self.walls[startWallsPos[1]][startWallsPos[0]] = CENTRANCE
        self.walls[endWallsPos[1]][endWallsPos[0]] = CEXIT
        for row in self.walls:
            for col in row:
                if col == CFLOOR:
                    self.map.append(matrixObjContainer.GetObjAtIndex(CFLOOR))
                elif col == CWALL:
                    self.map.append(matrixObjContainer.GetObjAtIndex(CWALL))
                elif col == CENTRANCE:
                    self.map.append(matrixObjContainer.GetObjAtIndex(CENTRANCE))
                elif col == CEXIT:
                    self.map.append(matrixObjContainer.GetObjAtIndex(CEXIT))
            self.map.append(matrixObjContainer.GetEndOfLineObj())
        self.map.append(0)
        

        
        

#labyrinth = MatrixGrid(11)
#labyrinth.BuildMap(0,120)


