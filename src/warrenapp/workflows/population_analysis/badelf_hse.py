# -*- coding: utf-8 -*-

from warrenapp.workflows.population_analysis.base import (
    VaspBadElfBase,
    prebadelf_incar_settings,
)
from warrenapp.workflows.static_energy import StaticEnergy__Warren__SeededHse
from warrenapp.workflows.static_energy.hse import StaticEnergy__Warren__Hse


class StaticEnergy__Warren__PrebadelfHse(StaticEnergy__Warren__Hse):
    """
    Runs a static energy calculation with a high-density FFT grid under HSE
    settings from the Warren Lab. Results can be used for Bader analysis where
    the ELF is used as the reference instead of the CHGCAR.

    We do NOT recommend running this calculation on its own. Instead, you should
    use the full workflow, which runs this calculation AND the following bader
    analysis for you. This S3Task is only the first step of that workflow.
    """

    # The key thing for bader analysis is that we need a very fine FFT mesh. Other
    # than that, it's the same as a static energy calculation.
    incar = StaticEnergy__Warren__Hse.incar.copy()
    incar.update(prebadelf_incar_settings)


# We prefer to use a workflow that seeds the HSE calculation with a PBE calculation
class StaticEnergy__Warren__PrebadelfSeededHse(StaticEnergy__Warren__SeededHse):

    second_calculation = StaticEnergy__Warren__PrebadelfHse


class PopulationAnalysis__Warren__BadelfHse(VaspBadElfBase):
    """
    Runs a static energy calculation using an extra-fine FFT grid and then
    carries out Bader analysis on the resulting charge density using the ELFCAR
    as a reference when partitioning. Uses the HSE functional and settings from
    the Warren Lab.
    """

    static_energy_prebadelf = StaticEnergy__Warren__PrebadelfSeededHse
