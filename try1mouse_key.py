import pygame, sys, random
from pygame.locals import QUIT
from bouncy_class import Bouncy

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Hello World!')

# define a few bouncy objects
# s1 will move where the mouse moves
# s2 will move where the mouse is clicked
# s3 and s4 will move with arrow key press



while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        # a bit slower keypress (not continuous)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pass
    # -------- end event loop
    screen.fill((255,255,255))
    # move with mouse click
    if pygame.mouse.get_pressed()[0]:
        pass
    
    # move with mouse motion
    if pygame.MOUSEMOTION:
        pass

    # move with keyboard
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        pass
        
    
    # draw


    pygame.display.update()
    pygame.time.delay(2)