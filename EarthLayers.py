#!/usr/bin/python3

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

#visualizing
layers.plot()
baseline.plot()
#plt.show()
plt.savefig('output.png')

#writing output
with open('output.txt','w') as o:
	print('#número de capas',layers.n,file=o)
	print('#segmentos recorridos',file=o)
	print('#segmento\tlongitud',file=o)
	for segment in baseline.segments:
		print(segment.tag,'\t',segment.l,file=o)
