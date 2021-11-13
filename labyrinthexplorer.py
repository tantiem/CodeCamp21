from pgx import *
from pygame import Vector2, surface
import pygame
import labyrinthgen
from pgx import Input
from pgx import pgxText
from pygame import locals

pygame.init()

SCR_X = 1024
SCR_Y = 768

P_DISPLAY = pygame.display.set_mode((SCR_X,SCR_Y))

inputManager = Input.InputManager()

tileSize = 100

mainGroup = pgxObject.PgxGroup()

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



#FloorTile = Static.Static(Vector2(0,0),floorTileSurface,mainGroup)
#WallTile = Static.Static(Vector2(0,0),wallTileSurface,mainGroup)
#EntranceTile = Static.Static(Vector2(0,0),startTileSurface,mainGroup)
#ExitTile = Static.Static(Vector2(0,0),endTileSurface,mainGroup)

camScreen = pygame.surface.Surface((SCR_X,SCR_Y))
mainCam = Camera.Camera(Vector2(0,0),(SCR_X,SCR_Y),(0,0),camScreen)

labyrinthObjects = labyrinthgen.MatrixGridObjectContainer(wallTileSurface,floorTileSurface,startTileSurface,endTileSurface)

bruh = []

class LabyrinthParser:
    """
    Should parse the map section of a matrixGrid.
    map.GetEndOfLineObj should act as a new line
    """
    def __init__(self, origin:tuple, tileSize:int, group:pgxObject.PgxGroup) -> None:
        self.origin = origin
        self.tileSize = tileSize
        self.group = group

    def Parse(self, labyrinthMap:list):
        """
        Given a list of surface objects, the labyrinthMap will have a collection of surfaces used to create static
        pgx objects.
        """
        x = 0
        y = 0
        for image in labyrinthMap:
            if image is None:
                y += 1
                x = 0
                continue
            elif image == 0:
                return
            pos = Vector2(x*self.tileSize + self.origin[0], y*tileSize + self.origin[1])
            obj = Static.Static(pos,image,self.group)
            x+= 1
            

def main():
    running = True

    labyrinthParse = LabyrinthParser((0,0),tileSize,mainGroup)
    labyrinth = labyrinthgen.MatrixGrid(11)
    labyrinth.BuildMap(1,120,labyrinthObjects)
    startPos = labyrinth.GraphIndexToWallsPos(1)

    labyrinthParse.Parse(labyrinth.map)

    player = Dynamic.Dynamic(Vector2(0,0),playerSurface,mainGroup)
    player.MoveAbsolute(Vector2(startPos[0] * tileSize,startPos[1] * tileSize))
    mainCam.SetCamPos(Vector2(startPos[0]*tileSize,startPos[1]*tileSize))
    mainCam.MoveCam(Vector2(-SCR_X/4,-SCR_Y/4))

    Vec2Left = Vector2(-1,0)
    Vec2Right = Vector2(1,0)
    Vec2Up = Vector2(0,-1)
    Vec2Down = Vector2(0,1)

    while running:
        inputManager.Refresh()
        if inputManager.EventActive(locals.QUIT):
            running = False
        if inputManager.GetKeyHeld(locals.K_d):
            mainCam.MoveCam(Vec2Right)
            player.MoveRelative(Vec2Right)
        if inputManager.GetKeyHeld(locals.K_a):
            mainCam.MoveCam(Vec2Left)
            player.MoveRelative(Vec2Left)
        if inputManager.GetKeyHeld(locals.K_w):
            mainCam.MoveCam(Vec2Up)
            player.MoveRelative(Vec2Up)
        if inputManager.GetKeyHeld(locals.K_s):
            mainCam.MoveCam(Vec2Down)
            player.MoveRelative(Vec2Down)

        mainCam.SetCamZoom(0.6,P_DISPLAY)
        mainGroup.update(mainCam)
        mainCam.Clear((52,86,145))
        mainGroup.draw(mainCam)


        pygame.display.flip()
    else:
        pygame.quit()


main()