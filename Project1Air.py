import math

import numpy as np
import matplotlib.pyplot as plt

Fx = input("Input force function Fx(x, y, vx, vy):")

fx = lambda x, y, vx, vy: eval(Fx)

Fy = input("Input force function Fy(x, y, vx, vy):")

fy = lambda x, y, vx, vy: eval(Fy)

   

v0=float(input("initial magnitude of velocity:"))

theta=float(input("initial angle with x-axis:"))

x=float(input("initial x:"))

y=float(input("initial y:"))
 
m=float(input("initial mass:"))

vy= math.sin(math.radians(theta))*v0

vx= math.cos(math.radians(theta))*v0

g= -9.8 

dt = 0.01

def force(x, y, vx, vy, m, g):

    forcex = fx(x, y, vx, vy)
    forcey = fy(x, y, vx, vy) + m*g

    return forcex, forcey


def update(x, y, vx, vy):

    y = y + vy * dt
    vy = vy + g * dt + (fy(x, y, vx, vy)/m) * dt
    x = x + vx * dt
    vx = vx + (fx(x, y, vx, vy) / m) * dt

    return x, y, vx, vy

x0 = x
y0 = y
vx0 = vx
vy0 = vy

def ME(t0):
    t = 0
    xn = x0
    yn = y0
    vxn = vx0
    vyn = vy0

    while t < t0:
        yn = yn + vyn * dt
        vyn = vyn + g * dt + (fy(xn, yn, vxn, vyn) / m) * dt
        xn = xn + vxn * dt
        vxn = vxn + (fx(xn, yn, vxn, vyn) / m) * dt

        t = t + dt

    Px = m * vxn
    Py = m * vyn
    T = 0.5 * m * (vxn**2 + vyn**2)
    V = -m * g * yn
    E = T + V

    return Px, Py, T, V, E

xlist = [x]
ylist = [y]
xlist.append(x)
ylist.append(y)

while y>0:
    y = y + vy * dt
    vy = vy + g * dt + (fy(x, y, vx, vy)/m) * dt
    x = x + vx * dt
    vx = vx + (fx(x, y, vx, vy) / m) * dt
    xlist.append(x)
    ylist.append(y)
print(x) 

plt.plot(xlist, ylist)
plt.xlabel("x")
plt.ylabel("y")
plt.show()
   
