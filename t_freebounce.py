#coding=utf-8
import numpy as np
import plotext as plt

# initial condition
ini_y = 20
ini_x = 0
ini_vx = 0
ini_vy = 0

# set the position, velocity variables, acceleration variables
x = [ini_x]
y = [ini_y]
vx = ini_vx
vy = ini_vy
ax = 0
ay = -9.8*0.01

#resistant damp coefficient
#damping = -0.001
damping = 0

# set the plot
plt.ylim(0,20)
plt.xlim(-10,10)

# set time condition
tt = 1000
dt = 1

# plot the animation
for t in range(tt):
    plt.cld()
    plt.clt()
    ay = ay + vy*damping
    vx = vx + dt*ax 
    vy = vy + dt*ay
    x[0] = x[0] + vx*dt
    y[0] = y[0] + vy*dt

    # condition of the ball collide with ground
    if y[0]<0:                   
        vy = -vy
        # those two line below can get rid of the unexpected damping problem
        x[0] = x[0] + vx*dt     
        y[0] = y[0] + vy*dt    
    plt.scatter(x, y, marker = "big")
    plt.plotsize(50,50)
    plt.colorless()
    plt.show()
