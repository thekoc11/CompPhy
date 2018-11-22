import random as rn
from math import floor, ceil, fabs, sqrt
from particle import *

class Vec:
    x = 0.0
    y = 0.0
    z = 0.0

    def __init__(self):
        self.r = sqrt(self.x**2 + self.y**2 + self.z**2)
        # print(self.x, self.y, self.z)

    def getVal(self):
        return sqrt(self.x **2 + self.y**2 + self.z**2)

    def reScale(self, n):
        self.x = self.x/n
        self.y = self.y/n
        self.z = self.z/n




boxl = 15.0
N = 51
P = []
c = 0
sumv = Vec()
sumv2 = 0
T = 200.0
fs = 0
nu = 14

Time = 1.0
t = 0
dt = 0.001

while len(P) < N:
    temPos = Vec()
    temPos.x = (rn.random() - 0.5)* boxl
    temPos.y = (rn.random() - 0.5)* boxl
    temPos.z = (rn.random() - 0.5)* boxl

    tempVel = Vec()
    tempVel.x = rn.random() - 0.5
    tempVel.y = rn.random() - 0.5
    tempVel.z = rn.random() - 0.5

    temP = Particle(len(P))
    temP.x = temPos.x
    temP.y = temPos.y
    temP.z = temPos.z
    temP.vx = tempVel.x
    temP.vy = tempVel.y
    temP.vz = tempVel.z


    if temPos.x > boxl/2:
        temPos.x = temPos.x - boxl
    if temPos.x < -boxl/2:
        temPos.x = temPos.x + boxl
    if temPos.y > boxl/2:
        temPos.y = temPos.y - boxl
    if temPos.y < -boxl/2:
        temPos.y = temPos.y + boxl
    if temPos.z > boxl/2:
        temPos.z = temPos.z - boxl
    if temPos.z < -boxl/2:
        temPos.z = temPos.z + boxl

    for i in range(len(P)):
        if fabs(temP.distanceTo(P[i], boxl)) < 2.0:
            c = c + 1
        sumv.x = sumv.x + P[i].vx
        sumv.y = sumv.y + P[i].vy
        sumv.z = sumv.z + P[i].vz

        sumv2 = sumv2 + (sumv.getVal())**2
    if len(P) > 0:
        sumv.reScale(len(P))
        sumv2 = sumv2 / len(P)
    if sumv2 > 0:
        fs = (3 * T / sumv2)
    else:
        fs = 1
    for i in range(len(P)):
        P[i].vx = (P[i].vx - sumv.x)*fs
        P[i].vy = (P[i].vy - sumv.y)*fs
        P[i].vz = (P[i].vz - sumv.z)*fs

        P[i].position[0] = P[i].x - P[i].vx*dt
        P[i].position[1] = P[i].y - P[i].vy*dt
        P[i].position[2] = P[i].z - P[i].vz*dt
    if c is 0:
        P.append(temP)
    c = 0

g = P.pop(len(P)-1)

print len(P)

"""Force Calculation"""
def force(P):
    U = 0
    ljcut = 2*(2.0**(1.0/6.0))
    for i in range(len(P)):
        for j in range(i+1, len(P)):
            r = P[i].distanceTo(P[j], boxl)
            # print(r, ljcut**2)
            if (r**2) < ljcut**2 and r > 2.0:
                f = (48 / r ** 2) * ((1 / r ** 12) - 0.5 * (1 / r ** 6))
                U = U + 4 * ((1/r**12) - (1/r**6))
            else:
                f = 0
            P[i].fx = P[i].fx + f*((P[i].x - P[j].x) - boxl*nint((P[i].x - P[j].x)/boxl))
            P[j].fx = P[j].fx - f*((P[i].x - P[j].x) - boxl*nint((P[i].x - P[j].x)/boxl))
            P[i].fy = P[i].fy + f * ((P[i].y - P[j].y) - boxl * nint((P[i].y - P[j].y) / boxl))
            P[j].fy = P[j].fy - f*((P[i].y - P[j].y) - boxl*nint((P[i].y - P[j].y)/boxl))
            P[i].fz = P[i].fz + f * ((P[i].z - P[j].z) - boxl * nint((P[i].z - P[j].z) / boxl))
            P[j].fz = P[j].fz - f*((P[i].z - P[j].z) - boxl*nint((P[i].z - P[j].z)/boxl))
    return U

"""Update equations of motion"""
def update(P, dt,  T, switch):
    _T = 0
    if(switch) is 0:
        for i in range(len(P)):
            P[i].x = P[i].x + P[i].vx*dt + P[i].fx * dt * dt/2.0
            P[i].y = P[i].y + P[i].vy*dt + P[i].fy * dt * dt/2.0
            P[i].z = P[i].z + P[i].vz*dt + P[i].fz * dt * dt/2.0

            P[i].vx = P[i].vx + P[i].fx * dt / 2.0
            P[i].vy = P[i].vy + P[i].fy * dt / 2.0
            P[i].vz = P[i].vz + P[i].fz * dt / 2.0
    else:
        for i in range(len(P)):
            P[i].vx = P[i].vx + P[i].fx * dt / 2.0
            P[i].vy = P[i].vy + P[i].fy * dt / 2.0
            P[i].vz = P[i].vz + P[i].fz * dt / 2.0
            _T = _T + (P[i].vx**2 + P[i].vy**2 + P[i].vz**2)
        _T = _T / (3.0*len(P))
        sigma = sqrt(T)
        for i in range(len(P)):
            if(rn.random() < nu*dt):
                P[i].vx = sigma * (rn.random()*2 - 1)
                P[i].vy = sigma * (rn.random()*2 - 1)
                P[i].vz = sigma * (rn.random()*2 - 1)


U = force(P)

print (U)

while t < Time:
    update(P, dt, T, 0)
    U = force(P)
    update(P, dt, T, 1)
    t = t + dt
print (U)