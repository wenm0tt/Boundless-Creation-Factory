import matplotlib.pyplot
from matplotlib import *
import numpy as np
from numpy import *
from sympy import *
from scipy.interpolate import * 
import math

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
        while i < 3:
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
        
    def custom_taylor(expression_string, iterates=15, initx=0):
        z = Symbol("z")
        f = sympify(expression_string)
        # an array that holds all derivatives of the function.
        # at index 0 it holds the function, at index 1 it holds first deriv, etc.
        diffs = []
        df = f
        for i in range(iterates):
            diffs.append(df)
            df = diff(df)

        f = 0
        for i in range(iterates):
            f += ((diffs[i].subs(z,initx))*(z-initx)**i)/math.factorial(i) 
        print(simplify(f))
        return simplify(f)

    def plotNV(roots_instance_a, x1, x2, y1, y2, f,df, expression = "z", resolution = 100):
        
        x = np.linspace(x1 - 0.00001, x2 + 0.00002, resolution)
        y = np.linspace(y1 - 0.00002, y2 + 0.00001, resolution)
        X,Y = np.meshgrid(x,y)
        Z = X + 1j * Y  
        Q = np.empty_like(Z, dtype=np.float64)

        Qshape = Q.shape
        for j in range(Qshape[0]):
            for k in range(Qshape[1]):
                Zk = Z[j,k]
                kroot = cGraphics.find_resulting_root(Zk,f,df,roots_instance_a)
                Q[j,k] = round((cGraphics.find_nearest(roots_instance_a, kroot)/len(roots_instance_a)),3)
        
        return Q

    def plot3D():
        pass
 
 
             
