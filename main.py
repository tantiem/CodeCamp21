import pygame
from pygame import locals
import makeFunctions
import makePages
import labyrinthexplorer
#Initialize Pygame
pygame.init()
PYGAME_WINDOW = pygame.display.set_mode((1024,768))
#Counters for OPTIONS menu
labyrinths = 2
days = 4
allowedTime = 120
#Global fonts
fontSize50 = pygame.font.SysFont(None, 50)
fontSize30 = pygame.font.SysFont(None, 30)
#used for title underlay in each page
surface1 = pygame.surface.Surface((1024,175))
surface1.fill((179,186,179))
#Set text for MAIN MENU screen items
menuFont = pygame.font.SysFont(None, 150)
mainTitle = menuFont.render('Oasis Escape', True, (0,0,0))
#StartGame variables
gameGrass = pygame.surface.Surface((824,568))
gameGrass.fill((51,214,36))
gameWater = pygame.surface.Surface((824,200))
gameWater.fill((49,135,196))
triggerGrass = pygame.surface.Surface((200,100))
triggerGrass.fill((51,214,36))
daysLeftSign = pygame.surface.Surface((200,75))
daysLeftSign.fill((161,89,21))
daysLeftTitle = fontSize50.render(str(days) +' days left', True, (0,0,0))
playerOasisX = 500
playerOasisy = 500
#HOW TO PLAY variables
howToPlayFont = pygame.font.SysFont(None, 150)
howToPlayTitle = howToPlayFont.render('How To Play', True, (0,0,0))
loreText = fontSize30.render("Oh no! You’re stuck in the Oasis! The Oasis might sound great, but it’s not at all what it seems.", True, (0,0,0))
loreText2 = fontSize30.render("If you don’t escape the Oasis in time, you’ll be doomed forever.", True, (0,0,0))
howToWinTitle = fontSize50.render('How To Win', True, (255,255,255))
howToWinText = fontSize30.render('The only way to escape the Oasis is to find the exit in the labyrinths in time', True, (0,0,0))
howToLoseTitle = fontSize50.render('How To Lose', True, (255,255,255))
howToLoseText = fontSize30.render('You won’t escape if you run out of days. You will also die if you don’t get back to the Oasis in', True, (0,0,0))
howToLoseText2 = fontSize30.render('time.', True, (0,0,0))
howOptionsWorkTitle = fontSize50.render('How Options Work', True, (255,255,255))
howOptionsWorkText = fontSize30.render('You can increase the number of labyrinths generated. If you have more days than the number of', True, (0,0,0))
howOptionsWorkText1 = fontSize30.render('labyrinths, the labyrinths will cycle through from the beginning. You may also set the amount of', True, (0,0,0))
howOptionsWorkText2 = fontSize30.render('time you would like per labyrinth.', True, (0,0,0))
#OPTIONS variables
optionsFont = pygame.font.SysFont(None, 150)
optionsTitle = optionsFont.render('Options', True, (0,0,0))
numberLabyrinthsTitle = fontSize50.render('Number of Labyrinths', True, (255,255,255))
underLayNumberLabyrinths = pygame.surface.Surface((60,40))
underLayNumberLabyrinths.fill((52,86,145))
numberLabyrinthsCounterShown = fontSize50.render(str(labyrinths), True, (179,186,179))
numberDaysTitle = fontSize50.render('Number of Days', True, (255,255,255))
numberDaysCounterShown = fontSize50.render(str(days), True, (179,186,179))
allowedTimeTitle = fontSize50.render('Allowed Time Per Labyrinth', True, (255,255,255))
underLayallowedTime = pygame.surface.Surface((250,40))
underLayallowedTime.fill((52,86,145))
allowedTimeCounterShown = fontSize50.render(str(allowedTime)+' seconds', True, (179,186,179))
#TEST variables
fontSize100 = pygame.font.SysFont(None, 100)
gameOverTitle = fontSize100.render('GAME OVER', True, (255,255,255))
winTitle = fontSize100.render('YOU WIN!', True, (255,255,255))
##################################################################################################

#Game runnning
main = True
startGame = False
howToPlay = False
options = False
test = False
quit = False
exploring = False
win = False
lose = False
running = True
while running:
    for event in pygame.event.get():
            if event.type == locals.QUIT:
                running = False
    if main:
        #MAIN MENU items drawn
        startButton,howToPlayButton,optionsButton,quitButton = makePages.makeMainMenu(PYGAME_WINDOW, surface1,mainTitle)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if startButton.collidepoint(pygame.mouse.get_pos()):
                    main = False
                    startGame = True
                    #######GENERATE MAZES############
                    for i in range(labyrinths):
                        labyrinthexplorer.AddLabyrinth()
                if howToPlayButton.collidepoint(pygame.mouse.get_pos()):
                    main = False
                    howToPlay = True
                if optionsButton.collidepoint(pygame.mouse.get_pos()):
                    main = False
                    options = True
                if quitButton.collidepoint(pygame.mouse.get_pos()):
                    main = False
                    quit = True
    elif startGame:
        PYGAME_WINDOW.fill((179,186,179))
        PYGAME_WINDOW.blit(gameGrass, (100,100))
        PYGAME_WINDOW.blit(gameWater, (100,500))
        pygame.draw.line(PYGAME_WINDOW, (221,224,29), (100,500), (923,500), 10)
        triggerGrassRect = PYGAME_WINDOW.blit(triggerGrass, (425,0))
        PYGAME_WINDOW.blit(daysLeftSign, (724,15))
        daysLeftTitle = fontSize50.render(str(days) +' days left', True, (0,0,0))
        PYGAME_WINDOW.blit(daysLeftTitle, (729, 32))
        #player stuff
        player = pygame.surface.Surface((50,50))
        player.fill((250,3,11))

        heldDownKeys = pygame.key.get_pressed()
        if heldDownKeys[locals.K_d]:
            if triggerGrassRect.collidepoint((playerOasisX,playerOasisy)):
                if playerOasisX < 575:
                    playerOasisX+=1
            elif (playerOasisX + 1) < 875:
                playerOasisX+=1
        elif heldDownKeys[locals.K_a]:
            if triggerGrassRect.collidepoint((playerOasisX,playerOasisy)):
                if playerOasisX > 425:
                    playerOasisX-=1
            elif (playerOasisX - 1) > 99:
                playerOasisX-=1
        if heldDownKeys[locals.K_w]:
            if triggerGrassRect.collidepoint((playerOasisX,playerOasisy-1)):
                playerOasisy-=1
                if (playerOasisy - 1) < 0:
                    #This triggers going into the maze, and thus also mainexplore()
                    startGame = False
                    exploring = True
            elif (playerOasisy - 1) > 99:
                playerOasisy-=1
        elif heldDownKeys[locals.K_s]:
            if (playerOasisy + 1) < 651:
                playerOasisy+=1
        PYGAME_WINDOW.blit(player, (playerOasisX,playerOasisy))

    elif howToPlay:
        mainButton = makePages.makeHowToPlay(PYGAME_WINDOW,surface1,howToPlayTitle,loreText,loreText2,howToWinTitle,howToWinText,howToLoseTitle,howToLoseText,howToLoseText2,howOptionsWorkTitle,howOptionsWorkText,howOptionsWorkText1,howOptionsWorkText2)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mainButton.collidepoint(pygame.mouse.get_pos()):
                    howToPlay = False
                    main = True

    elif options:
        lower1,upper1,lower2,upper2,lower3,upper3,mainButton = makePages.makeOptions(PYGAME_WINDOW,surface1,optionsTitle,numberLabyrinthsTitle,underLayNumberLabyrinths,numberLabyrinthsCounterShown,numberDaysTitle,numberDaysCounterShown,allowedTimeTitle,underLayallowedTime,allowedTimeCounterShown)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if lower1.collidepoint(pygame.mouse.get_pos()):
                    if labyrinths != 1:
                        labyrinths -= 1
                        numberLabyrinthsCounterShown = fontSize50.render(str(labyrinths), True, (179,186,179))
                elif upper1.collidepoint(pygame.mouse.get_pos()):
                    if labyrinths != 8:
                        labyrinths += 1
                        numberLabyrinthsCounterShown = fontSize50.render(str(labyrinths), True, (179,186,179))
                elif lower2.collidepoint(pygame.mouse.get_pos()):
                    if days > labyrinths:
                        days -= 1
                        numberDaysCounterShown = fontSize50.render(str(days), True, (179,186,179))
                elif upper2.collidepoint(pygame.mouse.get_pos()):
                    if days != 16:
                        days += 1
                        numberDaysCounterShown = fontSize50.render(str(days), True, (179,186,179))
                elif lower3.collidepoint(pygame.mouse.get_pos()):
                    if allowedTime != 5:
                        allowedTime -= 5
                        allowedTimeCounterShown = fontSize50.render(str(allowedTime)+' seconds', True, (179,186,179))
                elif upper3.collidepoint(pygame.mouse.get_pos()):
                    if allowedTime != 995:
                        allowedTime += 5
                        allowedTimeCounterShown = fontSize50.render(str(allowedTime)+' seconds', True, (179,186,179))
                
                if mainButton.collidepoint(pygame.mouse.get_pos()):
                    options = False
                    main = True
    elif win:
        PYGAME_WINDOW.fill((51,214,36))
        PYGAME_WINDOW.blit(winTitle, (512-winTitle.get_width()/2 + 2,340))
        quitButton = makeFunctions.makeButton(PYGAME_WINDOW, (480, 440), "Quit",(179,186,179),(49,96,196),(52,79,125),(52,86,145),50)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if quitButton.collidepoint(pygame.mouse.get_pos()):
                    win = False
                    quit = True
    elif lose:
        PYGAME_WINDOW.fill((0,0,0))
        PYGAME_WINDOW.blit(gameOverTitle, (512-gameOverTitle.get_width()/2 + 2,340))
        quitButton = makeFunctions.makeButton(PYGAME_WINDOW, (480, 440), "Quit",(179,186,179),(49,96,196),(52,79,125),(52,86,145),50)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if quitButton.collidepoint(pygame.mouse.get_pos()):
                    test = False
                    quit = True
    elif exploring:
        status = labyrinthexplorer.mainexplore(allowedTime, days)
        if status == 0:
            exploring = False
            win = True
        elif status == 1:
            days -= 1
            if days < 1:
                startGame = False
                exploring = False
                lose = True
                continue
            exploring = False
            startGame = True
        elif status == 2:
            startGame = False
            exploring = False
            lose = True
    elif quit:
        pygame.quit()
    pygame.display.flip()
else:
    pygame.quit()