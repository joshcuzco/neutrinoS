import numpy as np
import matplotlib.pyplot as plt
from Layers import Layer

def cot(x):
	return 1/np.tan(x)

class Baseline:
	"""baseline for a neutrino crossing the Earth"""

	#the layers crossed by the neutrino depend on the angle of the baseline
	def __init__(self,angle):
		self.angle=angle
		self.compAngle=np.pi/2 - self.angle

	#need to find the points where the baseline crosses to another layer
	def crosspoints(self,layers):
		self.CP=[]
		self.allCP=[]
		self.R=Layer.R

		for layer in layers:
			#doesn't cross the layer if the baseline angle is greater than the layer MaxAngle
			if (self.angle<layer.MaxAngle):
				S=np.sqrt(self.R**2 -(self.R**2 - layer.r**2)*(1+(cot(self.compAngle))**2))
				D=1+(cot(self.compAngle))**2

				y1=(self.R+S)/D
				p1=(cot(self.compAngle)*y1,y1)
				y2=(self.R-S)/D
				p2=(cot(self.compAngle)*y2,y2)

				self.allCP.append(p1)
				self.allCP.append(p2)
				self.CP.append([layer.name,[p1,p2]])

	def plot(self):
		x=np.linspace(0,self.R,100)
		y=np.linspace(0,2*self.R,100)
		X,Y=np.meshgrid(x,y)
		F=Y-np.tan(self.compAngle)*X
		plt.contour(X,Y,F,[0])

		for cps in self.CP:
			for crosspoint in cps[1]:
				plt.scatter(crosspoint[0],crosspoint[1])

