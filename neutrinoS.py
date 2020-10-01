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
	"""
	Getting the angular probability curve.
	"""
	probTrans=[]
	for angle in range(0,90):
		n.neutrinoAngle(angle)
		St=MLP.Propagate(n,model)
		probTrans.append(abs(St[1]))

	return probTrans

def angularD_indplot(n,model):
	"""
	Plotting the angular probability curve for a specific energy.
	"""

	probTrans=angularD(n,model)

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

def angularD_multiplot(energiesList,model,savename=''):
	"""
	Plotting angular probability curves for several energies.
	"""

	probs=[]

	for E in energiesList:
		n=neutrino(E)
		aD=angularD(n,model)
		probs.append(aD)

	plt.title(r'Probabilidad de oscilación $\nu_e\longrightarrow\nu_\mu$')
	plt.xlabel(r'$\alpha$')
	plt.ylabel(r'$P_{e\mu}$')
	plt.axis([0,90,0,1])

	for layer in model.layers:
		if model.layers.index(layer)!=model.n-1:
			plt.axvline(x=layer.MaxAngleGrad,color='black')

	for i in range(0,len(probs)):
		line,=plt.plot(range(0,90),probs[i], label='{:}'.format(SIformat(energiesList[i])),linewidth=0.8)

	lgd=plt.legend(loc=1,bbox_to_anchor=(1.26,1))

	if not savename:
		savename='multi-probTrans'
	plt.savefig('figures/'+savename+'.pdf',bbox_extra_artists=(lgd,),bbox_inches='tight',format='pdf')
	plt.close()

#Winter says 100MeV-1GeV
#would be interesting to see up to 50GeV

if __name__=='__main__':

	earth=EM.Model()
	#energiesList=[100e6,200e6,300e6,400e6,500e6,600e6,700e6,800e6,900e6,1e9,10e9,20e9,30e9,40e9,50e9]
	#energiesList=[200e6,210e6,220e6,230e6,240e6,250e6]
	energiesList=[100e6,500e6,1e9]

	#plotting a bunch of individual plots
#	for E in energiesList:
#		n=neutrino(E)
#		angularD_indplot(n,earth)

	#a multiplot
	angularD_multiplot(energiesList,earth,'test')


