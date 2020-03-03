import math

class Hand:

    def __init__(self):
        self.previous_frame = None
        self.hull = []
        self.center_pos = [0,0]

    def set_frame(self, f):
        self.previous_frame = f

    def set_hull(self, hull):
        self.hull = hull

    def set_center(self, center):
        self.center_pos = center

    def get_movement(self, new_pos):
        return abs(new_pos[1] - self.center_pos[1])

def compute_center(L):
    pos = [0,0]
    for point in L:
        p = point[0]
        pos[0] += p[0]
        pos[1] += p[1]
    pos[0] = math.floor(pos[0]/len(L))
    pos[1] = math.floor(pos[1]/len(L))
    return pos