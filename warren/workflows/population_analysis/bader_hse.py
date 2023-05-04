# -*- coding: utf-8 -*-

from warren.workflows.population_analysis.badelf_hse import (
    StaticEnergy__Warren__PrebadelfHse,
)
from warren.workflows.population_analysis.base import (
    VaspBaderBase,
    prebader_incar_settings,
)
from warren.workflows.static_energy.hse import StaticEnergy__Warren__Hse


class StaticEnergy__Warren__PrebaderHse(StaticEnergy__Warren__Hse):
    """
    Runs a static energy calculation with a high-density FFT grid setting.
    Results can be used for Bader analysis.

    We do NOT recommend running this calculation on its own. Instead, you should
    use the full workflow, which runs this calculation AND the following bader
    analysis for you. This S3Task is only the first step of that workflow.
    """

    # The key thing for bader analysis is that we need a very fine FFT mesh. Other
    # than that, it's the same as a static energy calculation.
    incar = StaticEnergy__Warren__Hse.incar.copy()
    incar.update(prebader_incar_settings)


class PopulationAnalysis__Warren__BaderHse(VaspBaderBase):
    """
    Runs a static energy calculation using an extra-fine FFT grid using vasp
    and then carries out Bader analysis on the resulting charge density.
    Uses the Warren lab HSE settings.
    """

    static_energy_prebader = StaticEnergy__Warren__PrebaderHse
