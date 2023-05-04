# -*- coding: utf-8 -*-

from warren.workflows.relaxation.pbesol import Relaxation__Warren__Pbesol
from warren.workflows.static_energy.pbe import static_settings


class StaticEnergy__Warren__Pbesol(Relaxation__Warren__Pbesol):
    """
    Performs a static energy calculation based on the settings for Warren Lab
    PBEsol functional relaxation.
    """

    incar = Relaxation__Warren__Pbesol.incar.copy()
    incar.update(static_settings)
