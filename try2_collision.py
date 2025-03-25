import pygame, sys, random
from pygame.locals import QUIT
from bouncy_class import Bouncy

'''
    the plan:
    the player will move with the mouse
    enemies will change color when they collide with the player
        ex: player.check_collision(enemies)
    enemies will disappear when clicked
        ex: loop thorough all enemies
            if clicked, remove from list
'''

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Hello World!')

# define the 'player' object


# define a list of bouncy objects (the 'enemies')



running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    # -------- end event loop
    screen.fill((255,255,255))        
    
    # check if mouse click




    # check for collision



    # draw and move


    pygame.display.update()
    pygame.time.delay(20)


    # check for game over


print("Game over!")