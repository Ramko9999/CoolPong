import pygame
from paddle import Paddle




class Color:
    white = (255,255,255)

class Pong:

    HEIGHT = 480
    WIDTH = 640
    PAD_HEIGHT = 80
    PAD_WIDTH = 30

    def __init__(self):
        pygame.init()
        self.screen  = pygame.display.set_mode((Pong.WIDTH,Pong.HEIGHT))
        self.game_state = True
        self.paddles = [Paddle(5,Pong.HEIGHT/2, Pong.PAD_WIDTH,Pong.PAD_HEIGHT, "CAM"),
                        Paddle(Pong.WIDTH - 80,Pong.HEIGHT/2, Pong.PAD_WIDTH,Pong.PAD_HEIGHT, "AI")]

    def update(self):
        for paddle in self.paddles:
            pygame.draw.rect(self.screen, Color.white, paddle.geometry())
        pygame.display.update()

