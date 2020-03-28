import numpy as np
import matplotlib.pyplot as plt
from Layers import Layer
from Baseline import Baseline

layers=[]
radii=[]

with open('layers.txt','r') as l:
	lines=l.readlines()
	
for line in lines:
	layers.append(line.split(' '))
	radii.append(float(line.split(' ')[0]))

Layer.R=max(radii)

L=[]

for layer in layers:
	L.append(Layer(float(layer[0]),layer[1]))

b=Baseline(np.pi/16)
b.crosspoints(L)

for l in L:
	l.plot()

b.plot()

plt.show()

for layer in L:
	print(layer.r,layer.name,layer.MaxAngle)

print(Layer.R)
print(b.R)

