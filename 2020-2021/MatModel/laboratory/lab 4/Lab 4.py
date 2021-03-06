import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import math

w2 = 2.4
tmax = 60
step = 0.05
y0 = [2, -1]

def W(y, t):
    y1, y2 = y
    return [y2, -w2*y1]

t = np.arange (0, tmax, step)
w1 = odeint (W, y0, t)
y11 = w1[:,0]
y21 = w1[:,1]

fig1 = plt.figure (facecolor = 'white')
plt.plot (t, y11, linewidth = 2)
plt.ylabel ("x")
plt.xlabel ("t")
plt.grid (True)
plt.show ()
fig1.savefig('01.png', dpi = 600)

fig2 = plt.figure (facecolor = 'white')
plt.plot (t, y21, linewidth = 2)
plt.ylabel ("x")
plt.xlabel ("t")
plt.grid (True)
plt.show ()
fig2.savefig('02.png', dpi = 600)


w2 = 9
g = 7

def W(y, t):
    y1, y2 = y
    return [y2, -w2*y1 - g*y2]

t = np.arange (0, tmax, step)
w1 = odeint (W, y0, t)
y11 = w1[:,0]
y21 = w1[:,1]

fig3 = plt.figure (facecolor = 'white')
plt.plot (t, y11, linewidth = 2)
plt.ylabel ("x")
plt.xlabel ("t")
plt.grid (True)
plt.show ()
fig3.savefig('03.png', dpi = 600)

fig4 = plt.figure (facecolor = 'white')
plt.plot (t, y21, linewidth = 2)
plt.ylabel ("x")
plt.xlabel ("t")
plt.grid (True)
plt.show ()
fig4.savefig('04.png', dpi = 600)

w2 = 3
g = 12

def f(t):
    f = math.sin(5*t)*0.2
    return f

def W(y, t):
    y1, y2 = y
    return [y2, -w2*y1 - g*y2 +f(t)]

t = np.arange (0, tmax, step)
w1 = odeint (W, y0, t)
y11 = w1[:,0]
y21 = w1[:,1]

fig5 = plt.figure (facecolor = 'white')
plt.plot (t, y11, linewidth = 2)
plt.ylabel ("x")
plt.xlabel ("t")
plt.grid (True)
plt.show ()
fig5.savefig('05.png', dpi = 600)

fig6 = plt.figure (facecolor = 'white')
plt.plot (t, y21, linewidth = 2)
plt.ylabel ("x")
plt.xlabel ("t")
plt.grid (True)
plt.show ()
fig6.savefig('06.png', dpi = 600)



