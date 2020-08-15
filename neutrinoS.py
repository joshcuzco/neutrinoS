import numpy as np

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
		self.angle=angle*np.pi/180

