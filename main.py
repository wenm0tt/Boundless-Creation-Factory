from cGraphics import *
import tkinter as tk
import customtkinter as ctk
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure

matplotlib.pyplot.style.use('dark_background')

# THINGS TO ADD
#   NUM ITERATIONS
#   COLOR SCHEME SETTINGS

INITIAL_ZOOM = 1
DESIRED_ZOOM = 500
DESIRED_RESOLUTION = 2000
DESIRED_EXP = "sin(z**2)*z-1"
ZOOM = False
z = Symbol("z")
exp = sympify(DESIRED_EXP)
f = lambdify((z), exp)
df = lambdify(z, diff(exp))

z = Symbol("z")
exp = cGraphics.custom_taylor(DESIRED_EXP)
roots_instance_a = solve(exp, z,check=false)
for i in range(len(roots_instance_a)):
    roots_instance_a[i] = complex((roots_instance_a[i]))

im = matplotlib.pyplot.imshow(cGraphics.plotNV(roots_instance_a, -3,3,-3,3,f,df,expression=DESIRED_EXP,resolution=DESIRED_RESOLUTION), cmap = "Greys", interpolation="gaussian")
matplotlib.pyplot.axis('off')

if ZOOM == True:
    for i in range(INITIAL_ZOOM,DESIRED_ZOOM):
        im.set_data(cGraphics.plotNV(roots_instance_a,100/-i,100/i,100/-i,100/i,f,df,expression=DESIRED_EXP,resolution=DESIRED_RESOLUTION))
        matplotlib.pyplot.pause(0.001)
        matplotlib.pyplot.axis('off')

matplotlib.pyplot.show()
# app.mainloop()



