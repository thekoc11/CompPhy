from numpy import array
import numpy as np
import random as rn
from math import sqrt, ceil, floor, exp

def Energy(s):
    H = 0
    J = 1
    sumAdj = 0
    L = len(s)
    h = L - 1
    v = L-1
    for i in range(L):
        for j in range(L):
            sumAdj = sumAdj + (s[h][j] * s[i][j])
            sumAdj = sumAdj + (s[i][v] * s[i][j])
            v = (v + 1) % L
        h = (h + 1) % L

    H = J * sumAdj
    return H

def MonteCarlo(s):
    H = Energy(s)
    s_ = flip(s)
    H_ = Energy(s_)

    print (H_, H)
    if(H_ <= H):
        s = s_
        H = H_
        print("flip support")
    else:
        acc = exp(-(H_ - H))
        if acc > rn.random():
            s = s_
            H = H_
            print ("accepted")
    return s


def flip(s):
    sprime = []
    h = floor(len(s)*rn.random())
    v = floor(len(s) * rn.random())
    for i in range(len(s)):
        sP = []
        for j in range(len(s)):
            if(i == h) and (j == v):
                sP.append(-s[i][j])
            else:
                sP.append(s[i][j])
        sP = array(sP)
        sprime.append(sP)
    return array(sprime)


L = 10
s = []
for i in range(L):
    sh = []
    for j in range(L):
        num = rn.random() * 2 - 1
        if num > 0:
            sh.append(ceil(num))
        else:
            sh.append(floor(num))
    sh = array(sh)
    s.append(sh)
s = array(s)
print (s)

U = Energy(s)

print (U)

dt = 0.1
T = 10
t = 0
while t<T:
    s = MonteCarlo(s)
    print (Energy(s))
    t = t + dt
