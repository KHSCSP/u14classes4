class Bouncy:
    def __init__(self, xp=100, yp=100, sizep=10):
        self.x = xp
        self.y = yp
        self.size = sizep
        self.xV = random.randint(-2,2)
        self.yV = random.randint(-2,2)
        # TODO variables for costumes
        # note: could use a list of image filenames
 

    def draw(self, screen, ticks):
        # TODO change costume
        pygame.draw.circle(screen, self.costumes[self.costume], (self.x, self.y), self.size)


import pygame, sys, random
from pygame.locals import QUIT

pygame.init()
w=800
h=600
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption('Hello World!')
clock = pygame.time.Clock()
FPS = 30

# TODO create object (note draw function)


# TODO ticks

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((255,255,255))

    # TODO draw, update screen, clock

    

    # TODO ticks