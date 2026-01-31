"""
Quantum Paddle - Paddle controlled by quantum mechanics.

This module implements the quantum logic for the paddle position.
The paddle exists in superposition until measured.

Based on the 'Programming on Quantum Computers' YouTube series.
"""

from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit_aer import AerSimulator
from qiskit.quantum_info import Statevector


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
        self.qr = QuantumRegister(self.n_qubits, 'q')
        self.cr = ClassicalRegister(self.n_qubits, 'c')
        self.circuit = QuantumCircuit(self.qr, self.cr)

    def apply_hadamard(self, qubit: int = None):
        """
        Apply Hadamard gate to create/remove superposition.

        Args:
            qubit: Which qubit to apply H. None = all qubits.
        """
        if qubit is None:
            for i in range(self.n_qubits):
                self.circuit.h(self.qr[i])
        else:
            if 0 <= qubit < self.n_qubits:
                self.circuit.h(self.qr[qubit])

    def apply_x(self, qubit: int):
        """
        Apply X (NOT) gate to flip a qubit.

        Args:
            qubit: Which qubit to flip.
        """
        if 0 <= qubit < self.n_qubits:
            self.circuit.x(self.qr[qubit])

    def apply_z(self, qubit: int):
        """
        Apply Z gate to change phase.

        Args:
            qubit: Which qubit to apply Z.
        """
        if 0 <= qubit < self.n_qubits:
            self.circuit.z(self.qr[qubit])

    def apply_cnot(self, control: int, target: int):
        """
        Apply CNOT gate.

        Args:
            control: Control qubit index.
            target: Target qubit index.
        """
        if 0 <= control < self.n_qubits and 0 <= target < self.n_qubits:
            self.circuit.cx(self.qr[control], self.qr[target])

    def get_probabilities(self) -> list[float]:
        """
        Get probability distribution without collapsing state.

        Returns:
            List of probabilities for each position.
        """
        statevector = Statevector(self.circuit)
        probs_dict = statevector.probabilities_dict()

        probabilities = [0.0] * self.n_positions
        for bitstring, prob in probs_dict.items():
            # Convert binary string to integer (reverse for little-endian)
            position = int(bitstring, 2)
            probabilities[position] = prob

        return probabilities

    def measure(self) -> int:
        """
        Measure the paddle position (collapses superposition).

        Returns:
            int: The measured position (0 to n_positions-1).
        """
        # Create a copy of circuit for measurement
        measure_circuit = self.circuit.copy()
        measure_circuit.measure(self.qr, self.cr)

        # Run simulation with single shot
        job = self.simulator.run(measure_circuit, shots=1)
        result = job.result()
        counts = result.get_counts()

        # Get the measured bitstring
        measured_bitstring = list(counts.keys())[0]
        position = int(measured_bitstring, 2)

        # Reset circuit to the collapsed state
        self.reset()
        # Set the circuit to the measured state using X gates
        for i in range(self.n_qubits):
            if (position >> i) & 1:
                self.circuit.x(self.qr[i])

        return position

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
