import tkinter as tk
from customtkinter import *
import matplotlib.pyplot
from matplotlib import *
import numpy as np
from numpy import *
from sympy import *
from scipy import *
import math
from matplotlib.colors import ListedColormap


class cGraphics():
    def plotZW(frame, expression = "z**k", max_K = 10, grid_density = 5, grid = False):                                    
        x = np.linspace(-1, 1, grid_density)
        y = np.linspace(-1, 1, grid_density)
        X,Y = np.meshgrid(x,y)
        Z = X + 1j * Y
        expressions = []
        for cArray in Z:
            for cNum in cArray:
                expressions.append(expression.replace("z",str(cNum)))


        i = 1/sys.maxsize
        while i < max_K:
            reals = []
            imags = []

            frame.cla()
            for expr in expressions:
                expr = expr.replace("k", str(i))
                cNum = N(expr)
                cNum = complex(cNum)
                reals.append(cNum.real)
                imags.append(cNum.imag)
            frame.scatter(reals,imags, marker = ".")
            if grid == True:
                frame.grid(True)
            matplotlib.pyplot.pause(0.0001) 

            i += 0.01

        matplotlib.pyplot.show()

    def find_resulting_root(guess, f, df, roots):
        i=0
        closest_root = roots[0]
        while i < 5:
            guess = guess - f(guess)/df(guess)
            closest_root = roots[cGraphics.find_nearest(roots,guess)]
            i+=1
        try:
            return complex(guess)
        except:
            return complex(0)

    def find_nearest(array, value):
        array = np.asarray(array)
        idx = (np.abs(array - value)).argmin()
        return idx
        
    def plotNV(frame, expression = "z", resolution = 100,dynamic_rendering = False):
        # basically we need an array of for each root that contains all points that go there. 
        # We then plot all those points at once with one color and move on to the next root.
        # plotting everything at once means matplotlib doesnt have to take the time to plot. 

        z = Symbol("z")
        exp = sympify(expression)
        f = lambdify(z, exp)
        df = lambdify(z, diff(exp))

        roots_instance_a = solve(exp, z)
        for i in range(len(roots_instance_a)):
            roots_instance_a[i] = complex(roots_instance_a[i])

        if dynamic_rendering == False:
            k = resolution - 1
        else:
            k = 1

        for n in range(k,resolution,10):
            frame.cla()
            x = np.linspace(-0.9999, 0.9997, n)
            y = np.linspace(-1, 0.9998, n)
            X,Y = np.meshgrid(x,y)
            Z = X + 1j * Y  
            Q = np.empty_like(Z, dtype=np.float64)

            Qshape = Q.shape
            for j in range(Qshape[0]):
                for k in range(Qshape[1]):
                    Zk = Z[j,k]
                    kroot = cGraphics.find_resulting_root(Zk,f,df,roots_instance_a)
                    Q[j,k] = round((cGraphics.find_nearest(roots_instance_a, kroot)*3/len(roots_instance_a)),3)
            im = frame.imshow(Q, cmap="plasma", interpolation="bilinear")
            matplotlib.pyplot.axis('off')
            matplotlib.pyplot.pause(0.001)
        matplotlib.pyplot.show()
        # 1. solve for the roots
        # 2. for each root that exists, create a 2d array of falses and trues. 
        #    if its true it means that cnum at that point leads to the root when we do newtons method on it
        # 3. plot 

    def plot3D():
        pass
 
 
             
