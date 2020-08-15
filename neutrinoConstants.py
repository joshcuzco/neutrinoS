import numpy as np

"""
Module with known constants for neutrinos.
"""

#FermiConstant [GeV**(-2)]
G=1.166*10**(-5)
#mix angle in the vacuum, its sin and cos
T=0.1
s2T=np.sin(2*T)
c2T=np.cos(2*T)
#squared masses diference [eV/c**2]
dm=0.1
