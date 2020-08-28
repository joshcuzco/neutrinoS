import numpy as np

"""
Module with known constants for neutrinos.
"""

#h-barra*c [eV*m]
hc=0.19733e-6
#FermiConstant [eV*m^3]
G=(1.166e4)*(hc**3)

#neutrino parameters from:
#Tanabashi et al. (Particle Data Group), Phys Rev. D 98, (2018) and 2019 update

#mix angle in the vacuum T
#(sin T)**2
sT=0.310
#cos(2T)
c2T=1-2*sT
#sin(2T)
s2T=2*np.sqrt(sT)*np.sqrt(1-sT)

#squared masses diference [eV**2] 8.1\pm1.0
dm=7.39e-5
