import pygame
from pygame import locals
import makeFunctions
#Initialize Pygame
pygame.init()
PYGAME_WINDOW = pygame.display.set_mode((1024,768))
#Counters for OPTIONS menu
labyrinths = 2
days = 4
allowedTime = 120
#Set variable for title and color it
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
daysLeftFont = pygame.font.SysFont(None, 50)
daysLeftTitle = daysLeftFont.render(str(days) +' days left', True, (0,0,0))
playerOasisX = 500
playerOasisy = 500
#Set text for HOW TO PLAY screen items
howToPlayFont = pygame.font.SysFont(None, 150)
howToPlayTitle = howToPlayFont.render('How To Play', True, (0,0,0))
loreFont = pygame.font.SysFont(None, 30)
loreText = loreFont.render("Oh no! You’re stuck in the Oasis! The Oasis might sound great, but it’s not at all what it seems.", True, (0,0,0))
loreText2 = loreFont.render("If you don’t escape the Oasis in time, you’ll be doomed forever.", True, (0,0,0))
howToWinFont = pygame.font.SysFont(None, 50)
howToWinTitle = howToWinFont.render('How To Win', True, (255,255,255))
howToWinTextFont = pygame.font.SysFont(None, 30)
howToWinText = howToWinTextFont.render('The only way to escape the Oasis is to find the exit in the labyrinths in time', True, (0,0,0))
howToLoseFont = pygame.font.SysFont(None, 50)
howToLoseTitle = howToWinFont.render('How To Lose', True, (255,255,255))
howToLoseTextFont = pygame.font.SysFont(None, 30)
howToLoseText = howToWinTextFont.render('You won’t escape if you run out of days. You will also die if you don’t get back to the Oasis in', True, (0,0,0))
howToLoseText2 = howToWinTextFont.render('time.', True, (0,0,0))
howOptionsWorkFont = pygame.font.SysFont(None, 50)
howOptionsWorkTitle = howOptionsWorkFont.render('How Options Work', True, (255,255,255))
howOptionsWorkFont = pygame.font.SysFont(None, 30)
howOptionsWorkText = howOptionsWorkFont.render('You can increase the number of labyrinths generated. If you have more days than the number of', True, (0,0,0))
howOptionsWorkText1 = howOptionsWorkFont.render('labyrinths, the labyrinths will cycle through from the beginning. You may also set the amount of', True, (0,0,0))
howOptionsWorkText2 = howOptionsWorkFont.render('time you would like per labyrinth.', True, (0,0,0))


#Set text for OPTIONS screen items
optionsFont = pygame.font.SysFont(None, 150)
optionsTitle = optionsFont.render('Options', True, (0,0,0))

numberLabyrinthsFont = pygame.font.SysFont(None, 50)
numberLabyrinthsTitle = numberLabyrinthsFont.render('Number of Labyrinths', True, (255,255,255))
underLayNumberLabyrinths = pygame.surface.Surface((60,40))
underLayNumberLabyrinths.fill((52,86,145))
numberLabyrinthsCounterFont = pygame.font.SysFont(None, 50)
numberLabyrinthsCounterShown = numberLabyrinthsCounterFont.render(str(labyrinths), True, (179,186,179))

numberDaysFont = pygame.font.SysFont(None, 50)
numberDaysTitle = numberLabyrinthsFont.render('Number of Days', True, (255,255,255))
numberDaysCounterFont = pygame.font.SysFont(None, 50)
numberDaysCounterShown = numberDaysCounterFont.render(str(days), True, (179,186,179))

allowedTimeFont = pygame.font.SysFont(None, 50)
allowedTimeTitle = allowedTimeFont.render('Allowed Time Per Labyrinth', True, (255,255,255))
underLayallowedTime = pygame.surface.Surface((250,40))
underLayallowedTime.fill((52,86,145))
allowedTimeCounterFont = pygame.font.SysFont(None, 50)
allowedTimeCounterShown = allowedTimeCounterFont.render(str(allowedTime)+' seconds', True, (179,186,179))
##################################################################################################
#Game runnning
main = True
startGame = False
howToPlay = False
options = False
quit = False
running = True
while running:
    for event in pygame.event.get():
            if event.type == locals.QUIT:
                running = False
    if main:
        PYGAME_WINDOW.fill((51,214,36))
        makeFunctions.makeTitle(PYGAME_WINDOW, surface1,mainTitle)
        startButton = makeFunctions.makeButton(PYGAME_WINDOW, (400, 250), "Enter Oasis",(179,186,179),(49,96,196),(52,79,125),(52,86,145),50)
        howToPlayButton = makeFunctions.makeButton(PYGAME_WINDOW, (397, 350), "How To Play",(179,186,179),(49,96,196),(52,79,125),(52,86,145),50)
        optionsButton = makeFunctions.makeButton(PYGAME_WINDOW, (440, 450), "Options",(179,186,179),(49,96,196),(52,79,125),(52,86,145),50)
        quitButton = makeFunctions.makeButton(PYGAME_WINDOW, (470, 550), "Quit",(179,186,179),(49,96,196),(52,79,125),(52,86,145),50)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if startButton.collidepoint(pygame.mouse.get_pos()):
                    main = False
                    startGame = True
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
        daysLeftTitle = daysLeftFont.render(str(days) +' days left', True, (0,0,0))
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
                    pygame.quit()
            elif (playerOasisy - 1) > 99:
                playerOasisy-=1
        elif heldDownKeys[locals.K_s]:
            if (playerOasisy + 1) < 651:
                playerOasisy+=1
        PYGAME_WINDOW.blit(player, (playerOasisX,playerOasisy))

    elif howToPlay:
        PYGAME_WINDOW.fill((51,214,36))
        makeFunctions.makeTitle(PYGAME_WINDOW, surface1,howToPlayTitle)
        mainButton = makeFunctions.makeButton(PYGAME_WINDOW, (775, 650), "Main Menu",(179,186,179),(49,96,196),(52,79,125),(52,86,145),50)
        PYGAME_WINDOW.blit(loreText, (512-loreText.get_width()/2 + 2, 240))
        PYGAME_WINDOW.blit(loreText2, (512-loreText2.get_width()/2 + 2, 260))
        PYGAME_WINDOW.blit(howToWinTitle, (512-howToWinTitle.get_width()/2 + 2, 300))
        PYGAME_WINDOW.blit(howToWinText, (512-howToWinText.get_width()/2 + 2, 350))
        PYGAME_WINDOW.blit(howToLoseTitle, (512-howToLoseTitle.get_width()/2 + 2, 390))
        PYGAME_WINDOW.blit(howToLoseText, (512-howToLoseText.get_width()/2 + 2, 440))
        PYGAME_WINDOW.blit(howToLoseText2, (512-howToLoseText2.get_width()/2 + 2, 460))
        PYGAME_WINDOW.blit(howOptionsWorkTitle, (512-howOptionsWorkTitle.get_width()/2 + 2, 500))
        PYGAME_WINDOW.blit(howOptionsWorkText, (512-howOptionsWorkText.get_width()/2 + 2, 550))
        PYGAME_WINDOW.blit(howOptionsWorkText1, (512-howOptionsWorkText1.get_width()/2 + 2, 570))
        PYGAME_WINDOW.blit(howOptionsWorkText2, (512-howOptionsWorkText2.get_width()/2 + 2, 590))
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mainButton.collidepoint(pygame.mouse.get_pos()):
                    howToPlay = False
                    main = True

    elif options:
        PYGAME_WINDOW.fill((51,214,36))
        makeFunctions.makeTitle(PYGAME_WINDOW, surface1,optionsTitle)
        PYGAME_WINDOW.blit(numberLabyrinthsTitle, (512-numberLabyrinthsTitle.get_width()/2 + 2, 250))
        lower1 = makeFunctions.makeButton(PYGAME_WINDOW, (440, 300), " - ",(179,186,179),(49,96,196),(52,79,125),(52,86,145),30)
        PYGAME_WINDOW.blit(underLayNumberLabyrinths, (480,300))
        PYGAME_WINDOW.blit(numberLabyrinthsCounterShown, (500, 303))
        upper1 = makeFunctions.makeButton(PYGAME_WINDOW, (557, 300), " + ",(179,186,179),(49,96,196),(52,79,125),(52,86,145),30)

        PYGAME_WINDOW.blit(numberDaysTitle, (512-numberDaysTitle.get_width()/2 + 2, 350))
        lower2 = makeFunctions.makeButton(PYGAME_WINDOW, (440, 400), " - ",(179,186,179),(49,96,196),(52,79,125),(52,86,145),30)
        PYGAME_WINDOW.blit(underLayNumberLabyrinths, (480,400))
        PYGAME_WINDOW.blit(numberDaysCounterShown, (500, 403))
        upper2 = makeFunctions.makeButton(PYGAME_WINDOW, (557, 400), " + ",(179,186,179),(49,96,196),(52,79,125),(52,86,145),30)

        PYGAME_WINDOW.blit(allowedTimeTitle, (512-allowedTimeTitle.get_width()/2 + 2, 450))
        lower3 = makeFunctions.makeButton(PYGAME_WINDOW, (350, 500), " - ",(179,186,179),(49,96,196),(52,79,125),(52,86,145),30)
        PYGAME_WINDOW.blit(underLayallowedTime, (512-allowedTimeCounterShown.get_width()/2 - 15,500))
        PYGAME_WINDOW.blit(allowedTimeCounterShown, (512-allowedTimeCounterShown.get_width()/2 + 2, 503))
        upper3 = makeFunctions.makeButton(PYGAME_WINDOW, (660, 500), " + ",(179,186,179),(49,96,196),(52,79,125),(52,86,145),30)

        mainButton = makeFunctions.makeButton(PYGAME_WINDOW, (775, 650), "Main Menu",(179,186,179),(49,96,196),(52,79,125),(52,86,145),50)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if lower1.collidepoint(pygame.mouse.get_pos()):
                    if labyrinths != 1:
                        labyrinths -= 1
                        numberLabyrinthsCounterShown = numberLabyrinthsCounterFont.render(str(labyrinths), True, (179,186,179))
                elif upper1.collidepoint(pygame.mouse.get_pos()):
                    if labyrinths != 8:
                        labyrinths += 1
                        numberLabyrinthsCounterShown = numberLabyrinthsCounterFont.render(str(labyrinths), True, (179,186,179))
                elif lower2.collidepoint(pygame.mouse.get_pos()):
                    if days > labyrinths:
                        days -= 1
                        numberDaysCounterShown = numberDaysCounterFont.render(str(days), True, (179,186,179))
                elif upper2.collidepoint(pygame.mouse.get_pos()):
                    if days != 16:
                        days += 1
                        numberDaysCounterShown = numberDaysCounterFont.render(str(days), True, (179,186,179))
                elif lower3.collidepoint(pygame.mouse.get_pos()):
                    if allowedTime != 5:
                        allowedTime -= 5
                        allowedTimeCounterShown = allowedTimeCounterFont.render(str(allowedTime)+' seconds', True, (179,186,179))
                elif upper3.collidepoint(pygame.mouse.get_pos()):
                    if allowedTime != 995:
                        allowedTime += 5
                        allowedTimeCounterShown = allowedTimeCounterFont.render(str(allowedTime)+' seconds', True, (179,186,179))
                
                if mainButton.collidepoint(pygame.mouse.get_pos()):
                    options = False
                    main = True

    elif quit:
        pygame.quit()
    pygame.display.flip()
else:
    pygame.quit()