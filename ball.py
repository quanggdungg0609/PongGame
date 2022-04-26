import pygame

class Ball:
    MAX_VEL=5
    COLOR=(255,255,255)
    def __init__(self, x, y, r):
        self.x=x
        self.y=y
        self.r=r
        self.x_vel=self.MAX_VEL
        self.y_vel=0

    def draw(self,win):
        pygame.draw.circle(win,self.COLOR,(self.x,self.y),self.r)
    def move(self):
        self.x+=self.x_vel
        self.y+=self.y_vel