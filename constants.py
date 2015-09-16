import qutip as qt

__author__ = 'Michal Kononenko'

qt.settings.auto_tidyup = False

HBAR = 1.055e-34
ELECTRON_CHARGE = 1.609e-19
MASS_OF_PROTON = 1.673e-27

GYROMAGNETIC_RATIO = ELECTRON_CHARGE * HBAR / (2 * MASS_OF_PROTON)
