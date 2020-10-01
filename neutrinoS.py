import numpy as np
import matplotlib.pyplot as plt
import MultiLayerPropagation as MLP
import EarthModel as EM
from matplotlib.ticker import EngFormatter as EF

"""
Simulation main program.
"""

SIformat=EF(unit='eV',places=0)
SIfileformat=EF(unit='eV',places=0,sep='')

class neutrino:
	"""
	A joyful neutrino travelling through Earth.
	"""
	def __init__(self,E):
		#defined by its energy [eV]
		self.E=E

	def neutrinoAngle(self,a):
		#assign a zenith angle [degrees] to the neutrino
		self.a=a
		#convert to radians
		self.angle=a*np.pi/180

def angularD(n,model):
	probTrans=[]
	for angle in range(0,90):
		n.neutrinoAngle(angle)
		St=MLP.Propagate(n,model)
		probTrans.append(abs(St[1]))

	plt.title(r'Probabilidad de transición $\nu_e\longrightarrow\nu_\mu$, E={:}'.format(SIformat(n.E)))
	plt.xlabel(r'$\alpha$')
	plt.ylabel(r'$P_{e\mu}$')
	plt.axis([0,90,0,1])

	for layer in model.layers:
		if model.layers.index(layer)!=model.n-1:
			plt.axvline(x=layer.MaxAngleGrad,color='red')
	plt.plot(range(0,90),probTrans)

	plt.savefig('figures/probTrans{:}.pdf'.format(SIfileformat(n.E)),format='pdf')
	plt.close()

#Winter says 100MeV-1GeV
#would be interesting to see up to 50GeV

if __name__=='__main__':

	earth=EM.Model()

	energiesList=[100e6,200e6,300e6,400e6,500e6,600e6,700e6,800e6,900e6,1e9,10e9,20e9,30e9,40e9,50e9]
	#energiesList=[200e6,210e6,220e6,230e6,240e6,250e6]

	for E in energiesList:
		n=neutrino(E)
		angularD(n,earth)
