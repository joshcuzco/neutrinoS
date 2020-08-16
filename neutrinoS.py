import numpy as np
import MultiLayerPropagation as MLP

"""
Simulation main program.
"""

class neutrino:
	"""
	A joyful neutrino travelling through Earth.
	"""
	def __init__(self,E,a):
		#defined by its energy [eV] and zenith angle[degrees]
		self.E=E
		#converted to radian
		self.angle=a*np.pi/180

#example
n=neutrino(1,15)
St=MLP.Propagate(n)
print(abs(St[0]),abs(St[1]))
