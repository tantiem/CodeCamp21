import pygame
def makeButton(screen,position,text,textColor,leftBorder,rightBorder,buttonColor,fontHeight):
    font = pygame.font.SysFont("Arial", fontHeight)
    text_render = font.render(text, 1, textColor)
    x, y, w , h = text_render.get_rect()
    x, y = position
    pygame.draw.line(screen, leftBorder, (x, y), (x + w , y), 5)
    pygame.draw.line(screen, leftBorder, (x, y - 2), (x, y + h), 5)
    pygame.draw.line(screen, rightBorder, (x, y + h), (x + w , y + h), 5)
    pygame.draw.line(screen, rightBorder, (x + w , y+h), [x + w , y], 5)
    pygame.draw.rect(screen, buttonColor, (x, y, w , h))
    return screen.blit(text_render, (x,y))

def makeTitle(screen, overLay,renderedTitle):
    screen.blit(overLay, (0,0))
    screen.blit(renderedTitle, (512-renderedTitle.get_width()/2, 35))
    pygame.draw.line(screen, (0,0,0), (0,175), (1024,175), 5)