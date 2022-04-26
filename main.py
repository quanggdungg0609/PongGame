import pygame
from paddle import Paddle
from ball import Ball

WIDTH,HEIGHT = 700,500
FPS = 60
clock = pygame.time.Clock()
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
BLACK = (0,0,0)
WHITE = (255,255,255)
PADDLE_W, PADDLE_H=20,100
WIN_SCORE = 10
BALL_R=7


class Pong:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WIDTH,HEIGHT))
        self.SCORE_FONT = pygame.font.SysFont("comicsans", 50)
        pygame.display.set_caption("Pong game")
        run=True
        #initate 2 paddle
        left_paddle=Paddle(10, HEIGHT//2-PADDLE_H//2,PADDLE_W,PADDLE_H )
        right_paddle=Paddle(WIDTH-10-PADDLE_W, HEIGHT//2-PADDLE_H//2,PADDLE_W,PADDLE_H )
        #initate the ball
        ball=Ball(WIDTH//2,HEIGHT//2,BALL_R)
        #initiate the scores
        self.left_score = 0
        self.right_score = 0
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
            self.handle_collision(ball,left_paddle,right_paddle)
            #implement Score
            if ball.x<0:
                self.right_score+=1
                ball.reset()
            elif ball.x>=WIDTH:
                self.left_score+=1
                ball.reset()
            #win condition
            won=False
            if self.left_score>=WIN_SCORE:
                won=True
                win_text="Left player won"
            elif self.right_score>=WIN_SCORE:
                won=True
                win_text="Right player won"
            if won:
                text=self.SCORE_FONT.render(win_text,1,WHITE)
                self.window.blit(text,(WIDTH//2-text.get_width()//2, HEIGHT//2 - text.get_height()//2))
                pygame.display.update()
                pygame.time.delay(50000)
                #reset everything
                ball.reset()
                left_paddle.reset()
                right_paddle.reset()
                self.left_score=0
                self.right_score=0
        pygame.quit()
    
    def draw(self,win, paddles,ball):

        win.fill(BLACK)
        #draw the scores
        left_score_text = self.SCORE_FONT.render(f"{self.left_score}", 1, WHITE)
        right_score_text = self.SCORE_FONT.render(f"{self.right_score}", 1, WHITE)
        win.blit(left_score_text,(WIDTH//4-left_score_text.get_width()//2,20))
        win.blit(right_score_text,(WIDTH* (3/4)-right_score_text.get_width()//2,20))
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

    def handle_collision(self,ball, left_paddle, right_paddle):
        #handling the collision of the ball with the bottom and the ceilling
        if ball.y + ball.r>=HEIGHT:
            ball.y_vel*=-1
        elif ball.y +ball.r<=10:
            ball.y_vel*=-1
        #handling the collision with the 2 paddles
        if ball.x_vel < 0:
            #left paddle
            if ball.y >= left_paddle.y and ball.y <= left_paddle.y + left_paddle.h:
                if ball.x - ball.r <= left_paddle.x + left_paddle.w:
                    ball.x_vel *= -1
                    midle_y= left_paddle.y+left_paddle.h/2
                    diff_in_y=  midle_y - ball.y
                    reduction_factor=(left_paddle.h/2)/ball.MAX_VEL
                    y_vel= diff_in_y/reduction_factor
                    ball.y_vel=-1 * y_vel

        else:
            #right paddle
            if ball.y >= right_paddle.y and ball.y <= right_paddle.y + right_paddle.h:
                if ball.x + ball.r >= right_paddle.x:
                    ball.x_vel*=-1
                    midle_y = right_paddle.y + right_paddle.h/2
                    diff_in_y = midle_y - ball.y
                    reduction_factor = (right_paddle.h / 2) / ball.MAX_VEL
                    y_vel = diff_in_y / reduction_factor
                    ball.y_vel = -1 * y_vel
if __name__=="__main__":
    g=Pong()