import numpy as np
import matplotlib.pyplot as plt
import neutrinoConstants as nC
import EarthModel as EM
import BaselineCalculator as BC

"""
Calculate the transition probabilities of neutrinos (2 flavors) using the evolution matrix S in a medium with k layers of constant density.
"""

#definitions---------------------------------------------------------

class Smatrix:
	"""
	Propagation matrix and its parameters.
	"""
	def __init__(self,x,n,D):
		self.parameters=[x,n,D]
		#properties of the medium
		#matter potential
		self.V=np.sqrt(2)*nC.G*n
		#resonance factor
		self.R=nC.s2T**2+(nC.c2T-self.V/D)**2
		#matter oscilation frequency
		self.Dm=D*np.sqrt(self.R)
		#mixing angle in matter
		self.s2t=(1/np.sqrt(self.R))*nC.s2T
		self.c2t=(1/np.sqrt(self.R))*(nC.c2T-self.V/D)
		#half oscilation frequency
		self.f=0.5*self.Dm*x/nC.hc
		
		#the shape of the evolution matrix is
		#	S=(a   b )
		#	  (-b* a*)
		#this allows to get all the information with just 2 components
		#	S=[a,b]
		self.S=[complex(np.cos(self.f),np.sin(self.f)*self.c2t),complex(0,-np.sin(self.f)*self.s2t)]

def Smult(B,A):
	"""
	Multiplication of evolution matrices.
	"""
	#* conjugation
	#. multiplication
	#given the shape of evolution matrices
	#	A=(a1   a2 )	,	B=(b1   b2 )
	#	  (-a2* a1*)		  (-b2* b1*)
	#all their information can be represented
	#	A=[a1,a2]	,	B=[b1,b2]
	#in the same representation, the multiplication is
	#	C=BA=[a1.b1-a2*.b2, b1.a2+b2.a1*]
	return [A[0]*B[0]-A[1].conjugate()*B[1], B[0]*A[1]+B[1]*A[0].conjugate()]

#identity matrix in the S representation
I=[1,0]

#--------------------------------------------------------------------

def Propagate(neutrino):
	#vacuum oscilation frequency, in natural units
	D=nC.dm/(2*neutrino.E)

	#need a baseline to propagate along
	baseline=BC.GetBaseline(neutrino.angle)

	#generating S matrices for every segment of the baseline
	Smatrices=[]
	for segment in baseline:
		Smatrices.append(Smatrix(segment.l,segment.ne,D))

	#number of layers of propagation
	k=len(baseline)

	#Propagation
	St=I
	for i in range(0,k):
		S=Smatrices[i].S
		St=Smult(S,St)

	#St[0] is the survival probability
	#St[1] the transition probability
	return St
