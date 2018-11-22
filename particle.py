from math import sqrt
from math import floor
from math import ceil
import random as rn

def nint(p):
    if(ceil(p) - p) < 0.5:
        return ceil(p)
    else:
        return floor(p)

class Particle:
    x = 0
    y = 0
    z = 0
    vx = 0
    vy = 0
    vz = 0
    fx = 0
    fy = 0
    fz = 0
    index = 0
    position = [x, y, z]

    def __init__(self, ind):
        self.index = ind

    def getDistance(self):
        self.position = [self.x, self.y, self.z]
        return sqrt(self.x*self.x + self.y*self.y + self.z*self.z)

    def distanceTo(self, p2, boxl):
        self.position = [self.x, self.y, self.z]
        _x = self.x - p2.x
        _y = self.y - p2.y
        _z = self.z - p2.z

        _x = _x - nint(_x/boxl)*boxl
        _y = _y - nint(_y/boxl)*boxl
        _z = _z - nint(_z/boxl)*boxl

        return sqrt(_x*_x + _y*_y + _z*_z)
