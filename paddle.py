import pygame


class Paddle:
    VEL = 4 #Velocity
    COLOR = (255,255,255)
    def __init__(self,x,y,w,h):
        self.x=x
        self.y=y
        self.w=w
        self.h=h
    #draw the paddle on the screen
    def draw(self,win):
        pygame.draw.rect(win, self.COLOR,(self.x, self.y, self.w, self.h))
    #Move the paddle up and down
    def move(self, up=True):
        if up:
            self.y-=self.VEL
        else:
            self.y+=self.VEL
            
