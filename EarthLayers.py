import numpy as np
import matplotlib.pyplot as plt
from Layers import Layers, Layer
from Baseline import Baseline

#setting up the layers from a file
layers=Layers('layers.txt')

#setting up the baseline b
baseline=Baseline('baseline.txt')
baseline.crosspoints(layers)

layers.plot()
baseline.plot()

plt.show()
