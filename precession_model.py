import qutip as qt
import constants as const
__author__ = 'Michal Kononenko'


class Particle(object):
    def __init__(self, field, mass=const.MASS_OF_PROTON,
                 charge=const.ELECTRON_CHARGE,
                 initial_state=qt.basis(2,0)):
        self.mass = mass
        self.charge = charge
        self.parent_field = field
        self.gyromagnetic_ratio = 267.513e6
        self.parent_field.particles.append(self)
        self.state = initial_state

    @property
    def local_hamiltonian(self):
        field_vector = self.parent_field.field_vector.values()
        pauli_basis = [qt.sigmax(), qt.sigmay(), qt.sigmaz()]

        b_field = sum(
            [field_vector[i] * pauli_basis[i]
             for i in xrange(0, len(field_vector))
             ]
        )
        return self.gyromagnetic_ratio * b_field * const.HBAR / 2

    def solve_particle(self, time_list):
        pauli_basis = [qt.sigmax(), qt.sigmay(), qt.sigmaz()]
        output = qt.sesolve(self.local_hamiltonian, self.state, time_list,
                            pauli_basis)
        return output


class MagneticField(object):
    def __init__(self, magnetic_field={'x': 0, 'y': 0, 'z': 1}):
        self.field_vector = magnetic_field
        self.particles = []

    @property
    def hamiltonian(self):
        return reduce(qt.tensor, [p.local_hamiltonian.unit() for p in self.particles])

