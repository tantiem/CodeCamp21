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
#Set text for HOW TO PLAY screen items
howToPlayFont = pygame.font.SysFont(None, 150)
howToPlayTitle = howToPlayFont.render('How To Play', True, (0,0,0))
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
        PYGAME_WINDOW.fill((51,214,36))
        
    
    elif howToPlay:
        PYGAME_WINDOW.fill((51,214,36))
        makeFunctions.makeTitle(PYGAME_WINDOW, surface1,howToPlayTitle)
        mainButton = makeFunctions.makeButton(PYGAME_WINDOW, (400, 500), "Main Menu",(179,186,179),(49,96,196),(52,79,125),(52,86,145),50)
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