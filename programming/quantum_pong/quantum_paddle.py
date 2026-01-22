"""
Quantum Paddle - Paddle controlled by quantum mechanics.

This module implements the quantum logic for the paddle position.
The paddle exists in superposition until measured.

TODO: Implement the methods below.
"""

from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit_aer import AerSimulator


class QuantumPaddle:
    """
    A paddle whose position is determined by quantum measurement.

    The paddle can be in superposition of multiple positions.
    Applying quantum gates changes the probability distribution.
    Measuring collapses the state to a definite position.

    Attributes:
        n_qubits: Number of qubits (2^n_qubits possible positions)
        circuit: The quantum circuit
        simulator: Qiskit simulator
    """

    def __init__(self, n_qubits: int = 3):
        """
        Initialize the quantum paddle.

        Args:
            n_qubits: Number of qubits. Default 3 = 8 positions.
        """
        self.n_qubits = n_qubits
        self.n_positions = 2 ** n_qubits
        self.simulator = AerSimulator()
        self.reset()

    def reset(self):
        """Reset the paddle to initial state |0...0⟩."""
        # TODO: Initialize quantum and classical registers
        # TODO: Create new circuit
        pass

    def apply_hadamard(self, qubit: int = None):
        """
        Apply Hadamard gate to create/remove superposition.

        Args:
            qubit: Which qubit to apply H. None = all qubits.
        """
        # TODO: Apply H gate
        # If qubit is None, apply to all qubits
        pass

    def apply_x(self, qubit: int):
        """
        Apply X (NOT) gate to flip a qubit.

        Args:
            qubit: Which qubit to flip.
        """
        # TODO: Apply X gate
        pass

    def apply_z(self, qubit: int):
        """
        Apply Z gate to change phase.

        Args:
            qubit: Which qubit to apply Z.
        """
        # TODO: Apply Z gate
        pass

    def apply_cnot(self, control: int, target: int):
        """
        Apply CNOT gate.

        Args:
            control: Control qubit index.
            target: Target qubit index.
        """
        # TODO: Apply CNOT gate
        pass

    def get_probabilities(self) -> list[float]:
        """
        Get probability distribution without collapsing state.

        Returns:
            List of probabilities for each position.
        """
        # TODO: Use Statevector to get probabilities
        # Return list of length n_positions
        pass

    def measure(self) -> int:
        """
        Measure the paddle position (collapses superposition).

        Returns:
            int: The measured position (0 to n_positions-1).
        """
        # TODO: Add measurements to circuit
        # TODO: Run on simulator with shots=1
        # TODO: Parse result and return position
        # TODO: Reset circuit for next measurement
        pass

    def get_position_normalized(self) -> float:
        """
        Measure and return position normalized to [0, 1].

        Returns:
            float: Position between 0.0 and 1.0.
        """
        position = self.measure()
        return position / (self.n_positions - 1)

    def draw_circuit(self):
        """Return circuit drawing for visualization."""
        return self.circuit.draw('mpl')


# Simple test
if __name__ == "__main__":
    paddle = QuantumPaddle(n_qubits=3)

    # Put in superposition
    paddle.apply_hadamard()

    # Show probabilities
    probs = paddle.get_probabilities()
    print(f"Probabilities: {probs}")

    # Measure
    position = paddle.measure()
    print(f"Measured position: {position}")
