import numpy as np
import matplotlib.pyplot as plt
from Layers import Layers, Layer
from Baseline import Baseline

#this module is used to test the interaction between the Layers and Baseline modules

#setting up the layers from a file
layers=Layers('layers.txt')

#setting up the baseline b
baseline=Baseline('baseline.txt')

#segmenting the baseline
baseline.crosspoints(layers)

print(baseline.segments)

#visualizing
layers.plot()
baseline.plot()
plt.show()
