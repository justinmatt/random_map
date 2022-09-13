# -*- coding: utf-8 -*-
"""
Spyder Editor

random map generator
"""

import numpy as np
import random
from matplotlib import pyplot as plt


def random_plot():
    x0,y0,z0 = (0,0,0)
    X=[]
    Y=[]
    #Z=[]
    for _ in range(10000):
        randx = round(random.uniform(-1,1),5)
        randy = round(random.uniform(-1,1),5)
        #randz = round(random.uniform(-1,1),5)
        x0 = x0+randx
        y0 = y0+randy
        #z0 = z0+randz
        X.append(x0)
        Y.append(y0)
        #Z.append(z0)
        
    #fig = plt.figure()
    #ax = fig.gca(projection='3d')
    #ax.plot3D(X,Y,Z)
    plt.plot(X,Y)
    
for _ in range(30):
    random_plot()
plt.axis('off')
plt.savefig("map_out/map.png",dpi=500)
plt.show()

    
