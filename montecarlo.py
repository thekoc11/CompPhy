from numpy import array
import random as rn
import matplotlib.pyplot as plt
import numpy as np
from math import fabs
from math import sqrt
from particle import Particle
from particle import nint
from math import exp

def LJPotential(r):
    sigma = 2.0
    eps = 0.01
    uLJ = 4*eps*((sigma/r)**12 - (sigma/r)**6)
    return uLJ

def run(P, Time, deltaT):
    Ulj = 0
    t = 0
    UljS = 0.0
    beta = 1.0
    while t < Time:
        for x in range(len(P)):
            for y in range(x + 1, len(P)):
                r = P[x].distanceTo(P[y], boxl)
                Ulj = Ulj + LJPotential(r)

        for x in range(len(P)):
            P[x].position = shift(P[x], boxl)
        for x in range(len(P)):
            for y in range(x + 1, len(P)):
                r = sqrt((P[x].position[0] - P[y].position[0])**2 + (P[x].position[1] - P[y].position[1])**2 + (P[x].position[2] - P[y].position[2])**2)
                UljS = UljS + LJPotential(r)

        print(UljS, Ulj)
        if UljS < Ulj:
            for i in range(len(P)):
                P[i].x = P[i].position[0]
                P[i].y = P[i].position[1]
                P[i].z = P[i].position[2]
            print ("program flow reached here!!!", UljS, Ulj)

        else:
            acc = exp(-beta*(UljS - Ulj))
            print ("this is acc", acc)
            if acc > rn.random():
                for i in range(len(P)):
                    P[i].x = P[i].position[0]
                    P[i].y = P[i].position[1]
                    P[i].z = P[i].position[2]

        t = t + deltaT
        Ulj = 0
        UljS = 0

def shift(P, boxl):
    pos = [P.x, P.y, P.z]

    x = P.x + (0.01 * (rn.random() - 0.5))*boxl
    y = P.y + (0.01 * (rn.random() - 0.5))*boxl
    z = P.z + (0.01 * (rn.random() - 0.5))*boxl

    x = x - nint(x/boxl)*boxl
    y = y - nint(y/boxl)*boxl
    z = z - nint(z/boxl)*boxl

    pos = [x, y, z]

    return pos


boxl = 15.0
nOP = 100
index = np.arange(nOP)

"""initialization"""
c = 0
i = 0
P = []
temP = array([0, 0, 0])
while len(P) < nOP:
    temp = Particle(len(P))
    temp.x = (rn.random() - 0.5) * boxl
    temp.y = (rn.random() - 0.5) * boxl
    temp.z = (rn.random() - 0.5) * boxl

    for j in range(len(P)):
        if fabs(temp.distanceTo(P[j], boxl)) < 2:
            c = c+1
            # print (temp.distanceTo(P[j], boxl))
    if c is 0:
        P.append(temp)
    c = 0
"""run simulation for 10 secs, dt = 0.01"""
run(P, 10, 0.05)

