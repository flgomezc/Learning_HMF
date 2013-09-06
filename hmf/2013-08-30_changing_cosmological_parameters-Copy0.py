# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

from hmf import Perturbations
import numpy as np
M = np.arange(10,15,0.01)
"""
PLANCK PARAMETERS
Angular size of sound horizon at recombination
    theta_*     = (1.0414)*10^-2
Baryons density:
    Omega_b h^2 = 0.0220
Dark cold matter density:
    Omega_c h^2 = 0.1199
Spectral index
    n_s         =  0.9693
Hubble constant:
    H_0         = 67.3  km s^-1 Mpc ^-1
Matter density:
    Omega_m     = 0.315
Optical depth
    tau = 0.089
"""

# <codecell>

pert_object = Perturbations(M,z=1.0)

pert_object.update(omegab = 0.05)

print "Transfer Cosmo"
print pert_object._transfer_cosmo
print "Extra Cosmo"
print pert_object._extra_cosmo
print "Cosmo Params"
print pert_object.cosmo_params

# <codecell>

#kwargs = {'sigma_8':0.9}
#kwargs = {'z':6.0, 'sigma_8'}
#pert_object.update(**kwargs)
#print pert_object._extra_cosmo
#pert_object._extra_cosmo.update({'sigma_8':0.9})
#del pert_object._power_cdm_0
print "cosmo_params" 
#"If it is defined already, just return it. Whenever a parameter is modfied, the dictionary is deleted
#and so will be remade here".
print pert_object.cosmo_params
print "\n_extra_cosmo" 
print pert_object._extra_cosmo
print "\n_transfer_cosmo" 
print pert_object._transfer_cosmo
print "\n_camb_params"
print pert_object.camb_params


"""
print pert_object.cosmo_params
print "\n_extra_cosmo" 
print pert_object._extra_cosmo
print "\n_transfer_cosmo" 
print pert_object._transfer_cosmo
print "\n_camb_params"
print pert_object.camb_params"""

# <codecell>

mass_func = pert_object.dndlnm
%pylab inline
plot (M, log10(mass_func))

# <codecell>


