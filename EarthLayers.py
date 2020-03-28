import numpy as np
import matplotlib.pyplot as plt
from Layers import Layers, Layer
from Baseline import Baseline

#setting up the layers from a file
layers=Layers('layers.txt')

#setting up the baseline b
with open ('baseline.txt','r') as l:
	bAngle=float(l.read())

b=Baseline(bAngle)
#b.crosspoints(layers)

#b.plot()

#plt.show()
