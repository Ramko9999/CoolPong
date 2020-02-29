import math
import random
from constants import *

class Ball:

    RADIUS = 12

    def __init__(self):
        self.speed = 10
        self.component = [random.uniform(-1,1),random.uniform(-1,1)]
        self.x = math.floor(GAME_WIDTH/2)
        self.y = math.floor(GAME_HEIGHT/2)

    def get_position(self):
        return (self.x, self.y)

    def move(self):
        self.x = math.floor(self.x + self.component[0] * self.speed)
        if self.x > GAME_WIDTH - Ball.RADIUS:
            self.x = GAME_WIDTH - Ball.RADIUS
            self.reverse_x()
        if self.x < Ball.RADIUS:
            self.x = Ball.RADIUS
            self.reverse_x()
        self.y = math.floor(self.y + self.component[1] * self.speed)
        if self.y > GAME_HEIGHT - Ball.RADIUS:
            self.y = GAME_HEIGHT- Ball.RADIUS
            self.reverse_y()
        if self.y < Ball.RADIUS:
            self.y = Ball.RADIUS
            self.reverse_y()

    def on_collision(self, paddle):
        midpoint = paddle.y + paddle.h/2
        relative_y = self.y - midpoint
        self.speed = min(20, self.speed * 1.2)
        self.reverse()


    def collision_check(self, paddle):
        ball_x = [max(self.x - Ball.RADIUS, 0), min(self.x + Ball.RADIUS,GAME_WIDTH)]
        ball_y = [max(self.y - Ball.RADIUS, 0), min(self.y + Ball.RADIUS, GAME_HEIGHT)]
        x_range = [paddle.x, paddle.x + paddle.w]
        y_range = [paddle.y, paddle.y + paddle.h]
        is_x_range = self.is_in(ball_x, x_range)
        is_y_range = self.is_in(ball_y, y_range)
        if is_x_range:
            # collision will have occured
            if is_y_range:
                self.on_collision(paddle)
                return True
        return False

    def is_in(self, p1, p2):
        lesser = p1
        greater = p2
        if p2[0] < p1[1]:
            lesser = p2
            greater = p1
        return lesser[0] <= greater[0] and lesser[1] >= greater[0]

    def reverse(self):
        self.component[0] *= -1
        self.component[1] *= -1

    def reverse_x(self):
        self.component[0] *= -1

    def reverse_y(self):
        self.component[1] *= -1


