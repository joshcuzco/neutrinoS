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

"""
Module with known constants for neutrinos.
"""

#h-barra*c [eV*m]
hc=0.19733e-6
#FermiConstant [eV*m^3]
G=(1.166e-23)*(hc**3)

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
