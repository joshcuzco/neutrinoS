import numpy as np
import matplotlib.pyplot as plt

class Layers:
	"""
	the layers of a planet from a file
	"""

	def __init__(self,filename):
		#the layer list will contain all layers as Layer objects
		self.layers=[]

		#file reading
		radii=[]
		with open(filename,'r') as l:
			lines=l.readlines()

		for line in lines:
			radii.append(float(line))

		#finding the radius of the outermost layer
		self.R=max(radii)
		Layer.R=self.R

		#each radius defines a Layer object
		for r in radii:
			self.layers.append(Layer(r))

	#a method to plot all layers together
	def plot(self):
		for layer in self.layers:
			layer.plot()


class Layer:
	"""
	an individual layer of radius r
	"""

	def __init__(self,r):
		self.r=r
		#if the baseline angle is greater than this the neutrino will not cross the layer
		self.MaxAngle=np.arcsin(self.r/self.R)

	#a method to plot the layer circle
	def plot(self):
		x=np.linspace(-self.r,self.r,100)
		y=np.linspace(self.R-self.r,self.R+self.r,100)
		X,Y=np.meshgrid(x,y)
		C=X**2+(Y-self.R)**2-self.r**2
		plt.contour(X,Y,C,[0])

	#a method to plot the MaxAngle line
	def plotMaxAngle(self):
		self.plot()
		x=np.linspace(-self.r,self.r,100)
		y=np.linspace(0,2*self.R,100)
		X,Y=np.meshgrid(x,y)
		Z=Y-np.tan(np.pi/2-self.MaxAngle)*X
		plt.contour(X,Y,Z,[0])
