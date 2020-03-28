import numpy as np
import matplotlib.pyplot as plt
from Layers import Layer
from Baseline import Baseline

#setting up layers
with open('layers.txt','r') as l:
	lines=l.readlines()

radii=[]
for line in lines:
	radii.append(float(line))

#radius of the outermost layer
Layer.R=max(radii)

layers=[]

for r in radii:
	layers.append(Layer(r))

#setting up the baseline b
with open ('baseline.txt','r') as l:
	bAngle=float(l.read())

b=Baseline(bAngle)
b.crosspoints(layers)

for layer in layers:
	layer.plot()

b.plot()

plt.show()
