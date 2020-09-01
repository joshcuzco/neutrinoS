import numpy as np
import matplotlib.pyplot as plt
import EarthModel as EM

"""
This module calculates the baseline for a neutrino crossing the Earth.
"""

#--------------------------------------------------------------------

def cot(x):
	return 1/np.tan(x)

#--------------------------------------------------------------------

def BaselinePlot(neutrino):
	"""
	Plot the baseline, just for fun.
	"""
	#the layers crossed by the neutrino depend on the angle of the baseline
	angle=neutrino.angle
	#complementary angle
	compAngle=np.pi/2-angle	

	#need the CrossPoints to plot
	CrossPoints=GetBaseline(neutrino,True)

	x=np.linspace(0,EM.R,100)
	y=np.linspace(0,2*EM.R,100)
	X,Y=np.meshgrid(x,y)
	F=Y-np.tan(compAngle)*X
	plt.contour(X,Y,F,[0])
	for crosspoint in CrossPoints:
		plt.scatter(crosspoint[0],crosspoint[1])

class Segment:
	"""
	All relevant info of a segment.
	"""

	def __init__(self,l):
		#size of segment
		self.l=l
		#electron density of segment
		self.ne=0

#--------------------------------------------------------------------

def GetBaseline(neutrino,GetCrossPoints=False):

	#the layers crossed by the neutrino depend on the angle of the baseline
	angle=neutrino.angle
	#complementary angle
	compAngle=np.pi/2-angle

	#need to find the points where the baseline crosses to another layer
	CrossPoints=[]
	distances=[]

	for layer in EM.layers:
		#doesn't cross the layer if the baseline angle is greater than the layer's MaxAngle 
		if (angle<layer.MaxAngle):
			S=np.sqrt(EM.R**2-(EM.R**2-layer.r**2)*(1+(cot(compAngle))**2))
			D=1+(cot(compAngle))**2

			#crosspoint's coordinates
			y1=(EM.R+S)/D
			p1=(cot(compAngle)*y1,y1)
			y2=(EM.R-S)/D
			p2=(cot(compAngle)*y2,y2)

			#distance from the crosspoint to the origin
			d1=np.sqrt(p1[0]**2+p1[1]**2)
			d2=np.sqrt(p2[0]**2+p2[1]**2)

			distances.append(d1)
			distances.append(d2)
			CrossPoints.append(p1)
			CrossPoints.append(p2)

	#intermediate result for plotting
	if GetCrossPoints==True:
		return CrossPoints

	#segment the baseline: find the distance between crosspoints
	distances.sort(reverse=True)

	baseline=[]
	for i in range(len(distances)-1):
		baseline.append(Segment(distances[i]-distances[i+1]))

	#number of layers of the baseline
	k=len(baseline)

	#let's assign densities for the corresponding segments of the baseline
	for i in range(0,1+k//2):
		ne=EM.layers[-1-i].ne
		baseline[i].ne=ne
		baseline[-1-i].ne=ne

	return baseline
