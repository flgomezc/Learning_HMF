# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

from hmf import Perturbations
import numpy as np
M = np.arange(10,15,0.01)
pert_object = Perturbations(M,z=6.0)
object_mass_func = pert_object.dndlnm

#Output:
#WARNING: Unrecognized parameters:
#transfer__kmax
#transfer__k_per_logint

# <codecell>

#"""
#PLANCK PARAMETERS (mar-2013)
#Angular size of sound horizon at recombination
#    theta_*     = (1.0414)*10^-2
#Baryons density:
#    Omega_b h^2 = 0.0220
#    Omega_b     = 0.0486
#Dark cold matter density:
#    Omega_c h^2 = 0.1199
#    Omega_c     = 0.2647
#Spectral index
#    n_s         =  0.9693
#Hubble constant:
#    H_0         = 67.3  km s^-1 Mpc ^-1
#    h           = 0.67.3
#Matter density:
#    Omega_m     = 0.315
#Optical depth
#    tau = 0.089
#"""

# <codecell>

pert_planck = Perturbations(M,z=6.0,omegab = 0.0485, reion__optical_depth = 0.089, H0 = 67.3)

#pert_planck.update(omegab = 0.0485, reion__optical_depth = 0.089, H0 = 67.3)
# The following are not valid parameters for the Perturbation Class
# omegam
# sigma_8


planck_mass_func = pert_planck.dndlnm
#Output:
#WARNING: Unrecognized parameters:
#transfer__kmax
#transfer__k_per_logint

# <codecell>

%pylab inline
plot (M,log10(object_mass_func))
plot (M,log10(planck_mass_func))

# <codecell>

%pylab inline
plot (M,log10(object_mass_func - planck_mass_func))



# <codecell>

#data = open("data.dat","wb" )
#data.write
#data.close()

print "#Log10(M)  Object \t Planck \t Difference"

for i in range(0, M.size):
    print M[i],"\t",object_mass_func[i],"\t", planck_mass_func[i], object_mass_func[i] - planck_mass_func[i]


# <codecell>


