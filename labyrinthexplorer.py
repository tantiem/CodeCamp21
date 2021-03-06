from pgx import *
from pygame import Vector2, surface
import pygame
import labyrinthgen
from pgx import Input
from pgx import pgxText
from pygame import locals
import math

pygame.init()

SCR_X = 1024
SCR_Y = 768

RENDER_DISTANCE = 500

P_DISPLAY = pygame.display.set_mode((SCR_X,SCR_Y))

inputManager = Input.InputManager()

tileSize = 100

mainGroup = pgxObject.PgxGroup()
wallGroup = pgxObject.PgxGroup()
floorGroup = pgxObject.PgxGroup()
winGroup = pgxObject.PgxGroup()
homeGroup = pgxObject.PgxGroup()
constGroup = pgxObject.PgxGroup()

floorTileSurface = pygame.surface.Surface((tileSize,tileSize))
floorTileSurface.fill((100,50,30))

wallTileSurface = pygame.surface.Surface((tileSize,tileSize))
wallTileSurface.fill((100,100,100))

startTileSurface = pygame.surface.Surface((tileSize,tileSize))
startTileSurface.fill((200,200,50))

endTileSurface = pygame.surface.Surface((tileSize,tileSize))
endTileSurface.fill((100,200,50))

playerSurface = pygame.surface.Surface((50,50))
playerSurface.fill((250,30,11))

timerBackground = pygame.surface.Surface((200,90))
timerBackground.fill((255,255,255))

timerTextBg = Static.Static(Vector2(0,0),timerBackground,constGroup)
timerText = pgxText.Text(Vector2(20,20),'verdana',"",50,constGroup)





#FloorTile = Static.Static(Vector2(0,0),floorTileSurface,mainGroup)
#WallTile = Static.Static(Vector2(0,0),wallTileSurface,mainGroup)
#EntranceTile = Static.Static(Vector2(0,0),startTileSurface,mainGroup)
#ExitTile = Static.Static(Vector2(0,0),endTileSurface,mainGroup)

camScreen = pygame.surface.Surface((SCR_X,SCR_Y))
uiScreen = pygame.surface.Surface((SCR_X,SCR_Y))
mainCam = Camera.Camera(Vector2(0,0),(SCR_X,SCR_Y),(0,0),camScreen)
uiCam = Camera.Camera(Vector2(0,0),(SCR_X,SCR_Y),(0,0),uiScreen)

labyrinthObjects = labyrinthgen.MatrixGridObjectContainer((wallTileSurface, wallGroup),(floorTileSurface, floorGroup),(startTileSurface,homeGroup),(endTileSurface,winGroup))


class Timer:
    def __init__(self) -> None:
        self.start = 0
        self.end = 0

    def StartTimer(self):
        self.start=pygame.time.get_ticks()

    def GetCurTime(self):
        return (pygame.time.get_ticks() - self.start) / 1000

    def StopTimer(self):
        self.end = pygame.time.get_ticks()
        return (self.end - self.start) / 1000

class LabyrinthParser:
    """
    Should parse the map section of a matrixGrid.
    map.GetEndOfLineObj should act as a new line
    """
    def __init__(self, origin:tuple, tileSize:int) -> None:
        self.origin = origin
        self.tileSize = tileSize

    def Parse(self, labyrinthMap:list):
        """
        Given a list of surface objects, the labyrinthMap will have a collection of surfaces used to create static
        pgx objects.

        gridObjList: pass in, func will return a 2d array.
        """

        x = 0
        y = 0
        for i in range(len(labyrinthMap)):
            if labyrinthMap[i] is None:
                y += 1
                x = 0
                continue
            elif labyrinthMap[i] == 0:
                return
            pos = Vector2(x*self.tileSize + self.origin[0], y*tileSize + self.origin[1])
            obj = Static.Static(pos,labyrinthMap[i][0],labyrinthMap[i][1])
            x+= 1
        

def sqrMagnitude(x1,y1,x2,y2):
    return (y2-y1)*(y2-y1) + (x2-x1)*(x2-x1)


labyrinths = []


def AddLabyrinth():
    ###GENERATE A MAZE
    labyrinth = labyrinthgen.MatrixGrid(11)
    labyrinth.BuildMap(1,120,labyrinthObjects)
    labyrinths.append(labyrinth)
    ###GENERATE A MAZE


    

def mainexplore(time, curDays):
    running = True

    mazeTimer = Timer()
    mazeTimer.StartTimer()

    #Cycle the mazes

    labyrinth = labyrinths[curDays%(len(labyrinths)) - 1]
    
    ###READS MAZE INTO MEMORY
    labyrinthParse = LabyrinthParser((0,0),tileSize)
    startPos = labyrinth.GraphIndexToWallsPos(1)
    labyrinthParse.Parse(labyrinth.map)
    ###READS MAZE INTO EMMO
    

    player = Dynamic.Dynamic(Vector2(0,0),playerSurface,mainGroup)
    player.MoveAbsolute(Vector2(startPos[0] * tileSize,startPos[1] * tileSize))
    mainCam.SetCamPos(Vector2(startPos[0]*tileSize,startPos[1]*tileSize))
    mainCam.MoveCam(Vector2(-SCR_X/4,-SCR_Y/4))

    Vec2Left = Vector2(-2,0)
    Vec2Right = Vector2(2,0)
    Vec2Up = Vector2(0,-2)
    Vec2Down = Vector2(0,2)

    while running:
        inputManager.Refresh()
        if inputManager.EventActive(locals.QUIT):
            running = False
        if inputManager.GetKeyHeld(locals.K_d):
            valid = True
            testRect = pygame.rect.Rect(player.rect.left + 2,player.rect.top,player.rect.width,player.rect.height)
            for spr in wallGroup:
                distanceSquared = sqrMagnitude(player.gPosition.x, player.gPosition.y, spr.rect.x,spr.rect.y)
                if distanceSquared < RENDER_DISTANCE * RENDER_DISTANCE:
                    if spr.rect.colliderect(testRect):
                        valid = False
                        break

            if(valid):
                mainCam.MoveCam(Vec2Right)
                player.MoveRelative(Vec2Right)

        if inputManager.GetKeyHeld(locals.K_a):
            valid = True
            testRect = pygame.rect.Rect(player.rect.left - 2,player.rect.top,player.rect.width,player.rect.height)
            for spr in wallGroup:
                distanceSquared = sqrMagnitude(player.gPosition.x, player.gPosition.y, spr.rect.x,spr.rect.y)
                if distanceSquared < RENDER_DISTANCE * RENDER_DISTANCE:
                    if spr.rect.colliderect(testRect):
                        valid = False
                        break

            if(valid):
                mainCam.MoveCam(Vec2Left)
                player.MoveRelative(Vec2Left)

        if inputManager.GetKeyHeld(locals.K_w):
            valid = True
            testRect = pygame.rect.Rect(player.rect.left,player.rect.top - 2,player.rect.width,player.rect.height)
            for spr in wallGroup:
                distanceSquared = sqrMagnitude(player.gPosition.x, player.gPosition.y, spr.rect.x,spr.rect.y)
                if distanceSquared < RENDER_DISTANCE * RENDER_DISTANCE:
                    if spr.rect.colliderect(testRect):
                        valid = False
                        break

            if(valid):
                mainCam.MoveCam(Vec2Up)
                player.MoveRelative(Vec2Up)
        if inputManager.GetKeyHeld(locals.K_s):
            valid = True
            testRect = pygame.rect.Rect(player.rect.left,player.rect.top + 2,player.rect.width,player.rect.height)
            for spr in wallGroup:
                distanceSquared = sqrMagnitude(player.gPosition.x, player.gPosition.y, spr.rect.x,spr.rect.y)
                if distanceSquared < RENDER_DISTANCE * RENDER_DISTANCE:
                    if spr.rect.colliderect(testRect):
                        valid = False
                        break

            if(valid):
                mainCam.MoveCam(Vec2Down)
                player.MoveRelative(Vec2Down)

        
                

        mainCam.SetCamZoom(0.6,P_DISPLAY)
        uiCam.SetCamZoom(1,P_DISPLAY)

        mainGroup.update(mainCam)
        constGroup.update(uiCam)

        mainCam.Clear((52,86,145))
        uiCam.Clear((0,0,0),(0,0,0))
        #mainGroup.draw(mainCam)
        
        curTimeInMaze = mazeTimer.GetCurTime()
        timerText.ChangeText("%.3f" % (time - curTimeInMaze))

        if curTimeInMaze > time:
            #2 means too much time passed in a maze. We lose instantly. bam.
            return 2

        for spr in floorGroup:
            distanceSquared = sqrMagnitude(player.gPosition.x, player.gPosition.y, spr.rect.x,spr.rect.y)
            if distanceSquared < RENDER_DISTANCE * RENDER_DISTANCE:
                spr.Draw(mainCam)


        for spr in wallGroup:
            distanceSquared = sqrMagnitude(player.gPosition.x, player.gPosition.y, spr.rect.x,spr.rect.y)
            if distanceSquared < RENDER_DISTANCE * RENDER_DISTANCE:
                spr.Draw(mainCam)


        for spr in winGroup:
            distanceSquared = sqrMagnitude(player.gPosition.x, player.gPosition.y, spr.rect.x,spr.rect.y)
            if distanceSquared < RENDER_DISTANCE * RENDER_DISTANCE:
                spr.Draw(mainCam)
                if spr.rect.colliderect(player.rect):
                    #Return 0 means we are returning a WIN status back to main
                    floorGroup.empty()
                    wallGroup.empty()
                    winGroup.empty()
                    homeGroup.empty()
                    mainGroup.empty()
                    return 0

        for spr in homeGroup:
            distanceSquared = sqrMagnitude(player.gPosition.x, player.gPosition.y, spr.rect.x,spr.rect.y)
            if distanceSquared < RENDER_DISTANCE * RENDER_DISTANCE:
                spr.Draw(mainCam)
                if spr.rect.colliderect(player.rect) and curTimeInMaze > 5:
                    #Return 1 means we are returning a GO BACK HOME status back to main
                    floorGroup.empty()
                    wallGroup.empty()
                    winGroup.empty()
                    homeGroup.empty()
                    mainGroup.empty()
                    return 1
                    

        for spr in mainGroup:
            distanceSquared = sqrMagnitude(player.gPosition.x, player.gPosition.y, spr.rect.x,spr.rect.y)
            if distanceSquared < RENDER_DISTANCE * RENDER_DISTANCE:
                spr.Draw(mainCam)

        
        constGroup.draw(uiCam)


        pygame.display.flip()
    else:
        pygame.quit()

