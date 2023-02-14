"""The Heisenberg model"""

from fractions import Fraction

from qiskit_nature.second_q.operators import SpinOp
from qiskit_nature.second_q.hamiltonians.ising_model import IsingModel

class HeisenbergModel(IsingModel):
    """The Heisenberg model."""

    def second_q_op(self) -> SpinOp:
        """Return the Hamiltonian of the Heisenberg model in terms of `SpinOp`.

        Args:
            display_format: Not supported for Spin operators. If specified, it will be ignored.

        Returns:
            SpinOp: The Hamiltonian of the Heisenberg model.
        """
        ham = {}
        weighted_edge_list = self._lattice.weighted_edge_list
        # kinetic terms
        for node_a, node_b, weight in weighted_edge_list:
            if node_a == node_b:
                index = node_a
                ham[f"X_{index}"] = weight

            else:
                index_left = node_a
                index_right = node_b
                coupling_parameter = weight
                ham[f"X_{index_left} X_{index_right}"] = coupling_parameter
                ham[f"Y_{index_left} Y_{index_right}"] = coupling_parameter
                ham[f"Z_{index_left} Z_{index_right}"] = coupling_parameter
        return SpinOp(ham, spin=Fraction(1, 2), num_spins=self.register_length)
