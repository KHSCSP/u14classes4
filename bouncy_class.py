import pygame, random, math

class Bouncy:
    def __init__(self, xp=100, yp=100, sizep=10, colp=None):
        self.x = xp
        self.y = yp
        self.size = sizep
        self.xV = random.randint(-2,2)
        self.yV = random.randint(-2,2)
        if colp == None:
            self.color = Bouncy.rand_col()
        else:
            self.color = colp

    
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.size)
    

    def move(self, screen):
        w, h = screen.get_size()
        if self.x-self.size<0 or self.x+self.size>w:
            self.xV *= -1
        if self.y-self.size<0 or self.y+self.size>h:
            self.yV *= -1
        self.x += self.xV
        self.y += self.yV
    
    def check_click(self, mx, my):
        pass


    def check_collision(self, other):
        pass


    # a helper function
    # not a method because no instance will call this
    def rand_col():
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        return (r,g,b)