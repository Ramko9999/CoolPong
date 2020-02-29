import pygame
from paddle import Paddle
from constants import *
from ball import Ball


class Color:

    WHITE = (255,255,255)
    BLACK = (0,0,0)

class Pong:

    def __init__(self):
        pygame.init()
        self.screen  = pygame.display.set_mode((GAME_WIDTH,GAME_HEIGHT))
        self.game_state = True
        self.paddles = [Paddle(5,GAME_HEIGHT/2, PAD_WIDTH,PAD_HEIGHT, "CAM"),
                        Paddle(GAME_WIDTH - 80,GAME_HEIGHT/2, PAD_WIDTH,PAD_HEIGHT, "AI")]
        self.ball = Ball()

    def update(self):
        self.screen.fill(Color.BLACK)
        for paddle in self.paddles:
            if paddle.key == "CAM":
                pass
            pygame.draw.rect(self.screen, Color.WHITE, paddle.geometry())
            self.ball.collision_check(paddle)
        self.ball.move()
        pygame.draw.circle(self.screen, Color.WHITE, self.ball.get_position(), Ball.RADIUS)
        pygame.display.flip()


