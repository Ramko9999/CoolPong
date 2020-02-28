class Paddle:
    def __init__(self, x, y, w, h, k):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.key = k

    def set_position(self, p):
        self.y = p[1]

    def set_height(self, h):
        self.h = h

    def geometry(self):
        return (self.x, self.y, self.w, self.h)