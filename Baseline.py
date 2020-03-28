import numpy as np
import matplotlib.pyplot as plt
from Layers import Layers, Layer

def cot(x):
	return 1/np.tan(x)

class Baseline:
	"""
	baseline for a neutrino crossing the Earth
	"""

	#the layers crossed by the neutrino depend on the angle of the baseline
	def __init__(self,filename):
		with open(filename,'r') as l:
			self.angle=float(l.read())
		#complementary angle
		self.compAngle=np.pi/2 - self.angle

	#need to find the points where the baseline crosses to another layer
	def crosspoints(self,LayerList):
		self.CP=[]
		self.distances=[]
		#a list of segment objects
		self.segments=[]

		self.R=LayerList.R

		layers=LayerList.layers

		for layer in layers:
			#doesn't cross the layer if the baseline angle is greater than the layer MaxAngle
			if (self.angle<layer.MaxAngle):
				S=np.sqrt(self.R**2 -(self.R**2 - layer.r**2)*(1+(cot(self.compAngle))**2))
				D=1+(cot(self.compAngle))**2

				#crosspoint's coordinates
				y1=(self.R+S)/D
				p1=(cot(self.compAngle)*y1,y1)
				y2=(self.R-S)/D
				p2=(cot(self.compAngle)*y2,y2)

				#distance from the crosspoint to the origin
				d1=np.sqrt(p1[0]**2+p1[1]**2)
				d2=np.sqrt(p2[0]**2+p2[1]**2)

				self.distances.append(d1)
				self.distances.append(d2)
				self.CP.append(p1)
				self.CP.append(p2)

		#segment the baseline: find the distance between crosspoints
		self.distances.sort(reverse=True)

		for i in range(len(self.distances)-1):
			self.segments.append(Segment(self.distances[i]-self.distances[i+1],i))

	#plot the baseline
	def plot(self):
		x=np.linspace(0,self.R,100)
		y=np.linspace(0,2*self.R,100)
		X,Y=np.meshgrid(x,y)
		F=Y-np.tan(self.compAngle)*X
		plt.contour(X,Y,F,[0])

		for crosspoint in self.CP:
			plt.scatter(crosspoint[0],crosspoint[1])

class Segment:
	"""
	characteristics of each segment
	"""

	def __init__(self,l,i):
		#to identify each segment
		self.tag=i
		#size of segment
		self.l=l
		#electron density of segment
		self.ne=0
		
