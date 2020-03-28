import numpy as np
import matplotlib.pyplot as plt

class Layer:
	"""managing the layers of a planet of radius R"""

	#the maximum radius is a global variable
	R=0

	#every individual layer is a Layer object
	def __init__(self,r,name):
		self.r=r
		self.name=name
		#if the baseline angle is greater than this the neutrino will not cross the layer
		self.MaxAngle=np.arcsin(self.r/self.R)

	#a handy method to plot the layer circle
	def plot(self):
		x=np.linspace(-self.r,self.r,100)
		y=np.linspace(self.R-self.r,self.R+self.r,100)
		X,Y=np.meshgrid(x,y)
		C=X**2+(Y-self.R)**2-self.r**2
		plt.contour(X,Y,C,[0])

