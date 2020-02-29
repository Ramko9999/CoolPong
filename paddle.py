import math
from constants import *

class Paddle:

    Y_THRESHOLD = 20

    def __init__(self, x, y, w, h, k):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.key = k

    def set_position(self, p):
        y = math.floor(p[1])
        if y < GAME_HEIGHT / 2:
            y = max(y, 0)
            if abs(y - self.y) > Paddle.Y_THRESHOLD:
                self.y = y
        else:
            y = min(y, GAME_HEIGHT - self.h)
            if abs(y - self.y) > Paddle.Y_THRESHOLD:
                self.y = y

    def set_height(self, h):
        self.h = h

    def geometry(self):
        return (self.x, self.y, self.w, self.h)