import matplotlib.pyplot as plt
import numpy as np

m = 5                           # mass of cow [kg]
ag = np.array([[0, -9.8]])      # acceleration due to gravity [m/s^2]

t0 = np.array([0])              # start at time 0 [s]
dt = 0.1                        # fixed time interval [s]
hg = 0                          # ground height at 0 [m]

r0x = 0                         # initial x-position                         
r0y = 0                         # initial y-position
v0 = 15                         # initial speed of 15 mph
theta = np.pi/3                 # angle between v & the horizontal axis
v0x = v0 * np.cos(theta)        # initial x-velocity      
v0y = v0 * np.sin(theta)        # initial y-velocity

r0 = np.array([[r0x, r0y]])     # initial position vector
v0 = np.array([[v0x, v0y]])     # initial velocity vector

c=0.75                          # input parameters for acceleration
ax = "-(c/m)*np.sqrt(v[0]**2+v[1]**2)*v[0]"            # initial x-acceleration
ay = "-(c/m)*np.sqrt(v[0]**2+v[1]**2)*v[1]-9.81"       # initial y-acceleration    

# FUNCTIONS DESCRIBED IN THE ASSIGNMENT INSTRUCTIONS

# 3a: Force as a function of position & velocity– assume only gravity & wind resistance
# 9/9/26  changed force below - Gabe
def force(r, v, c):
    F= m * np.array([[eval(ax),eval(ay)]])
    return F

# 3b: New position and velocity from the current position and velocity
def newState(r, v, F, t, dt, c):
    """
    Function that takes the cow's current position
    ,velocity, and force and returns a new position 
    at a small time step later'
    r (2D array): current position list
    v (2D array): current velocity list
    F (2D array): current force list
    t (1D array): current time axis
    dt: time interval
    """

    t0 = t[-1]
    t0 += dt
    t = np.append(t, t0)

    F_tot = np.append(F, force(r[-1], v[-1], c), axis = 0)
    F_new = F_tot[-1]

    a = F_new / m
    v_new = np.add(v, np.multiply(a, dt))
    r_new = np.add(r, np.multiply(v_new, dt))
    
    r_tot = np.append(r, [r_new[-1]], axis=0)
    v_tot = np.append(v, [v_new[-1]], axis=0)
    #print(r[-1])

    if r_tot[-1,1] < 0:
        return r_tot, v_tot, F_tot, t, dt
    else:
        return newState(r_tot, v_tot, F_tot, t, dt, c)

# Function to give total potential and total kinetic energy at a given instance
def energy(t0):
    """
    Function that calculates the potential, kinetic,
    and total energy
    """
    i = np.argmin(np.abs(t - t0))

    x = r[i, 0]
    y = r[i, 1]
    vx = v[i, 0]
    vy = v[i, 1]

    Px = m * vx
    Py = m * vy
    T = 0.5 * m * (vx**2 + vy**2)
    V = -m * ag[0,1] * y
    E = T + V

    return Px, Py, T, V, E


# Running Code
F0 = force(r0[0], v0[0], c)                                # Force vector
r, v, F, t, dt = newState(r0, v0, F0, t0, dt, c)           # New State

x = r[:,0]                                              # x Positions
y = r[:,1]                                              # y Positions

plt.figure()
fig, (ax1, ax2) = plt.subplots(2, 1)

ax1.plot(x,y, label = 'y(x)')                           
ax2.plot(t,x, label = 'x(t)')
ax2.plot(t,y, label = 'y(t)')

ax1.legend()
ax2.legend()
plt.tight_layout()
plt.show()

