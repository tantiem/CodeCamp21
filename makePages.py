import pygame
import makeFunctions
def makeMainMenu(screen,surface,mainTitle):
    screen.fill((51,214,36))
    makeFunctions.makeTitle(screen, surface,mainTitle)
    startButton = makeFunctions.makeButton(screen, (400, 250), "Enter Oasis",(179,186,179),(49,96,196),(52,79,125),(52,86,145),50)
    howToPlayButton = makeFunctions.makeButton(screen, (397, 350), "How To Play",(179,186,179),(49,96,196),(52,79,125),(52,86,145),50)
    optionsButton = makeFunctions.makeButton(screen, (440, 450), "Options",(179,186,179),(49,96,196),(52,79,125),(52,86,145),50)
    quitButton = makeFunctions.makeButton(screen, (470, 550), "Quit",(179,186,179),(49,96,196),(52,79,125),(52,86,145),50)
    return startButton,howToPlayButton,optionsButton,quitButton

def makeStartGame():
    pass

def makeHowToPlay(screen,surface,howToPlayTitle,loreText,loreText2,howToWinTitle,howToWinText,howToLoseTitle,howToLoseText,howToLoseText2,howOptionsWorkTitle,howOptionsWorkText,howOptionsWorkText1,howOptionsWorkText2):
    screen.fill((51,214,36))
    makeFunctions.makeTitle(screen, surface,howToPlayTitle)
    mainButton = makeFunctions.makeButton(screen, (775, 650), "Main Menu",(179,186,179),(49,96,196),(52,79,125),(52,86,145),50)
    screen.blit(loreText, (512-loreText.get_width()/2 + 2, 240))
    screen.blit(loreText2, (512-loreText2.get_width()/2 + 2, 260))
    screen.blit(howToWinTitle, (512-howToWinTitle.get_width()/2 + 2, 300))
    screen.blit(howToWinText, (512-howToWinText.get_width()/2 + 2, 350))
    screen.blit(howToLoseTitle, (512-howToLoseTitle.get_width()/2 + 2, 390))
    screen.blit(howToLoseText, (512-howToLoseText.get_width()/2 + 2, 440))
    screen.blit(howToLoseText2, (512-howToLoseText2.get_width()/2 + 2, 460))
    screen.blit(howOptionsWorkTitle, (512-howOptionsWorkTitle.get_width()/2 + 2, 500))
    screen.blit(howOptionsWorkText, (512-howOptionsWorkText.get_width()/2 + 2, 550))
    screen.blit(howOptionsWorkText1, (512-howOptionsWorkText1.get_width()/2 + 2, 570))
    screen.blit(howOptionsWorkText2, (512-howOptionsWorkText2.get_width()/2 + 2, 590))
    return mainButton

def makeOptions(screen,surface1,optionsTitle,numberLabyrinthsTitle,underLayNumberLabyrinths,numberLabyrinthsCounterShown,numberDaysTitle,numberDaysCounterShown,allowedTimeTitle,underLayallowedTime,allowedTimeCounterShown):
    screen.fill((51,214,36))
    makeFunctions.makeTitle(screen, surface1,optionsTitle)
    screen.blit(numberLabyrinthsTitle, (512-numberLabyrinthsTitle.get_width()/2 + 2, 250))
    lower1 = makeFunctions.makeButton(screen, (440, 300), " - ",(179,186,179),(49,96,196),(52,79,125),(52,86,145),30)
    screen.blit(underLayNumberLabyrinths, (480,300))
    screen.blit(numberLabyrinthsCounterShown, (500, 303))
    upper1 = makeFunctions.makeButton(screen, (557, 300), " + ",(179,186,179),(49,96,196),(52,79,125),(52,86,145),30)
    
    screen.blit(numberDaysTitle, (512-numberDaysTitle.get_width()/2 + 2, 350))
    lower2 = makeFunctions.makeButton(screen, (440, 400), " - ",(179,186,179),(49,96,196),(52,79,125),(52,86,145),30)
    screen.blit(underLayNumberLabyrinths, (480,400))
    screen.blit(numberDaysCounterShown, (500, 403))
    upper2 = makeFunctions.makeButton(screen, (557, 400), " + ",(179,186,179),(49,96,196),(52,79,125),(52,86,145),30)

    screen.blit(allowedTimeTitle, (512-allowedTimeTitle.get_width()/2 + 2, 450))
    lower3 = makeFunctions.makeButton(screen, (350, 500), " - ",(179,186,179),(49,96,196),(52,79,125),(52,86,145),30)
    screen.blit(underLayallowedTime, (512-allowedTimeCounterShown.get_width()/2 - 15,500))
    screen.blit(allowedTimeCounterShown, (512-allowedTimeCounterShown.get_width()/2 + 2, 503))
    upper3 = makeFunctions.makeButton(screen, (660, 500), " + ",(179,186,179),(49,96,196),(52,79,125),(52,86,145),30)

    mainButton = makeFunctions.makeButton(screen, (775, 650), "Main Menu",(179,186,179),(49,96,196),(52,79,125),(52,86,145),50)
    return lower1,upper1,lower2,upper2,lower3,upper3,mainButton

#GAMEOVER screen
#PYGAME_WINDOW.fill((0,0,0))
#        PYGAME_WINDOW.blit(gameOverTitle, (512-gameOverTitle.get_width()/2 + 2,340))
#        quitButton = makeFunctions.makeButton(PYGAME_WINDOW, (480, 440), "Quit",(179,186,179),(49,96,196),(52,79,125),(52,86,145),50)
#        for event in pygame.event.get():
#            if event.type == pygame.MOUSEBUTTONDOWN:
#                if quitButton.collidepoint(pygame.mouse.get_pos()):
#                    test = False
#                    quit = True
#WIN screen
#PYGAME_WINDOW.fill((51,214,36))
#        PYGAME_WINDOW.blit(winTitle, (512-winTitle.get_width()/2 + 2,340))
#        quitButton = makeFunctions.makeButton(PYGAME_WINDOW, (480, 440), "Quit",(179,186,179),(49,96,196),(52,79,125),(52,86,145),50)
#        for event in pygame.event.get():
#            if event.type == pygame.MOUSEBUTTONDOWN:
#                if quitButton.collidepoint(pygame.mouse.get_pos()):
#                    test = False
#                    quit = True