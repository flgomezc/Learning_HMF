# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

from hmf import Perturbations
import numpy as np
M = np.arange(10,15,0.01)
pert_object = Perturbations(M,z=6.0)
mass_func = pert_object.dndlnm

# <codecell>

%pylab inline
plot (M, log10(mass_func))

# <codecell>


