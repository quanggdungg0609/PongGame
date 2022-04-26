import pygame
from paddle import Paddle
from ball import Ball
WIDTH,HEIGHT=700,500
FPS=60
clock= pygame.time.Clock()
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
BLACK=(0,0,0)
WHITE=(255,255,255)
PADDLE_W, PADDLE_H=20,100
BALL_R=10
class Pong:
    window = pygame.display.set_mode((WIDTH,HEIGHT))
    pygame.init()
    pygame.display.set_caption("Pong game")
    def __init__(self):
        run=True
        #initate 2 paddle
        left_paddle=Paddle(10, HEIGHT//2-PADDLE_H//2,PADDLE_W,PADDLE_H )
        right_paddle=Paddle(WIDTH-10-PADDLE_W, HEIGHT//2-PADDLE_H//2,PADDLE_W,PADDLE_H )
        #initate the ball
        ball=Ball(WIDTH//2,HEIGHT//2,BALL_R)
        while run:
            clock.tick(FPS)
            self.draw(self.window,[left_paddle,right_paddle],ball)
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    run=False
                    break
            #get the keys when we pressed    
            keys=pygame.key.get_pressed()
            self.handle_paddle_movement(keys,left_paddle,right_paddle)

            ball.move()

        pygame.quit()
    
    def draw(self,win, paddles,ball):
        win.fill(BLACK)
        #draw the paddle
        for paddle in paddles:
            paddle.draw(self.window)
        #draw the line center of the screen
        for i in range(10,HEIGHT,HEIGHT//20):
            if i%2 ==1:
                continue
            pygame.draw.rect(self.window,WHITE,(WIDTH//2-5,i,10,HEIGHT//20))
        #draw the ball
        ball.draw(self.window)
        
        pygame.display.update()


    def handle_paddle_movement(self,keys,left_paddle, right_paddle):
        #movement of the left paddle
        if keys[pygame.K_w] and (left_paddle.y - left_paddle.VEL>=0):
            left_paddle.move(up=True)
        if keys[pygame.K_s] and (left_paddle.y + left_paddle.VEL+ left_paddle.h<=HEIGHT):
            left_paddle.move(up=False)
        #movement of the right paddle
        if keys[pygame.K_UP] and (right_paddle.y - right_paddle.VEL>=0):
            right_paddle.move(up=True)
        if keys[pygame.K_DOWN] and (right_paddle.y + right_paddle.VEL + right_paddle.h<=HEIGHT):
            right_paddle.move(up=False)

if __name__=="__main__":
    g=Pong()