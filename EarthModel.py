#    Copyright (C) 2020
#    J. Cuzco
#    jcr131998@gmail.com
#
#    This program is free software: you can redistribute it and/or
#    modify it under the terms of the GNU General Public License as
#    published by the Free Software Foundation, either version 3 of
#    the License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#    General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see
#    <http://www.gnu.org/licenses/>.

import numpy as np
import matplotlib.pyplot as plt

"""
This module contains the Earth Model for neutrino propagation.

The model is read from a file, that can be specified when declaring
the model:
	model=Model('model.txt')
Otherwise, will read from a default file EarthModel.txt 

The data in the model file must read:
	radious [m]	density [kg m**-3]
"""

#---------------------------------------------------------------------

#density constants
#electron fraction
f=0.5
#nucleon mass [kg] (using average of proton and neutron masses)
m=1.6738e-27

#---------------------------------------------------------------------

class Layer:
	"""
	All relevant info of a layer.
	"""

	def __init__(self,r,rho,R):
		#takes a layer from EarthModel [radius,e density] as input
		self.r=r
		self.rho=rho
		self.ne=f*self.rho/m
		#if the baseline angle is greater than this the neutrino will not cross the layer
		self.MaxAngle=np.arcsin(self.r/R)
		self.MaxAngleGrad=self.MaxAngle*(180/np.pi)

		self.R=R

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

#---------------------------------------------------------------------

class Model:
	"""
	An earth model that contains layers.
	"""

	def __init__(self,modelFile=''):
		#loading the model from a text file
		if not modelFile:
			modelFile='EarthModel.txt'

		EarthModel=[]

		with open(modelFile,'r') as model:
			for layer in model:
				if layer[0]!='#':
					l=float(layer.split()[0])
					rho=float(layer.split()[1])
					EarthModel.append([l,rho])

		#making sure its sorted from small to large
		EarthModel.sort(key=lambda x:x[0])

		#radius of the earth=outermost layer
		self.R=EarthModel[-1][0]

		#layers is a list of layer objects
		self.layers=[]
		for layer in EarthModel:
			self.layers.append(Layer(layer[0],layer[1],self.R))

		#number of layers
		self.n=len(self.layers)

	#plotting for fun
	def LayersPlot(self):
		"""
		Plot all layers, just for fun.
		"""
		for layer in self.layers:
			layer.plot()
