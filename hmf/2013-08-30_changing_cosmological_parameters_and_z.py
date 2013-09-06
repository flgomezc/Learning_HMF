# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

from hmf import Perturbations
import numpy as np
M = np.arange(10,15,0.01)
pert_object = Perturbations(M,z=0.0)
"""
PLANCK PARAMETERS (mar-2013)
Angular size of sound horizon at recombination
    theta_*     = (1.0414)*10^-2
Baryons density:
    Omega_b h^2 = 0.0220
    Omega_b     = 0.0486
Dark cold matter density:
    Omega_c h^2 = 0.1199
    Omega_c     = 0.2647
Spectral index
    n_s         =  0.9693
Hubble constant:
    H_0         = 67.3  km s^-1 Mpc ^-1
    h           = 0.67.3
Matter density:
    Omega_m     = 0.315
Optical depth
    tau = 0.089
"""

# <codecell>

pert_object.update(omegab = 0.0485, reion__optical_depth = 0.089, H0 = 67.3)
# The following are not valid parameters for the Perturbation Class
# omegam
# sigma_8

# <codecell>

mass_func = pert_object.dndlnm


pert_early = Perturbations(M,z=6.0)
pert_early.update()
early_mass_func = pert_early.dndlnm

# <codecell>

%pylab inline
plot (M, log10(mass_func))
plot (M,log10(early_mass_func))

# <codecell>


