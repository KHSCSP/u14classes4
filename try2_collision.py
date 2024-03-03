import pygame, sys, random
from pygame.locals import QUIT
from bouncy_class import Bouncy

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Hello World!')

# define a list of bouncy objects



while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    # -------- end event loop
    screen.fill((255,255,255))        
    
    # check if mouse click
    if pygame.mouse.get_pressed()[0]:
        mx, my = pygame.mouse.get_pos()



    # check for collision



    # draw and move



    pygame.display.update()
    pygame.time.delay(20)