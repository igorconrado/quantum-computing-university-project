"""Unit tests for quantum circuit implementations."""

import pytest
import numpy as np
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.quantum_info import Statevector


class TestBellStates:
    """Tests for Bell state creation."""

    def test_phi_plus_superposition(self):
        """Test |Φ+⟩ = (|00⟩ + |11⟩)/√2 state."""
        qc = QuantumCircuit(2)
        qc.h(0)
        qc.cx(0, 1)

        sv = Statevector.from_instruction(qc)
        probs = sv.probabilities_dict()

        # Should only have |00⟩ and |11⟩ with equal probability
        assert abs(probs.get("00", 0) - 0.5) < 0.001
        assert abs(probs.get("11", 0) - 0.5) < 0.001
        assert probs.get("01", 0) < 0.001
        assert probs.get("10", 0) < 0.001

    def test_phi_minus_superposition(self):
        """Test |Φ-⟩ = (|00⟩ - |11⟩)/√2 state."""
        qc = QuantumCircuit(2)
        qc.h(0)
        qc.cx(0, 1)
        qc.z(0)

        sv = Statevector.from_instruction(qc)
        probs = sv.probabilities_dict()

        # Probabilities same as Φ+, but phase differs
        assert abs(probs.get("00", 0) - 0.5) < 0.001
        assert abs(probs.get("11", 0) - 0.5) < 0.001

    def test_psi_plus_superposition(self):
        """Test |Ψ+⟩ = (|01⟩ + |10⟩)/√2 state."""
        qc = QuantumCircuit(2)
        qc.h(0)
        qc.cx(0, 1)
        qc.x(0)

        sv = Statevector.from_instruction(qc)
        probs = sv.probabilities_dict()

        # Should only have |01⟩ and |10⟩
        assert abs(probs.get("01", 0) - 0.5) < 0.001
        assert abs(probs.get("10", 0) - 0.5) < 0.001


class TestGHZState:
    """Tests for GHZ state creation."""

    @pytest.mark.parametrize("n_qubits", [2, 3, 4, 5])
    def test_ghz_superposition(self, n_qubits):
        """Test GHZ state has only |00...0⟩ and |11...1⟩."""
        qc = QuantumCircuit(n_qubits)
        qc.h(0)
        for i in range(n_qubits - 1):
            qc.cx(i, i + 1)

        sv = Statevector.from_instruction(qc)
        probs = sv.probabilities_dict()

        all_zeros = "0" * n_qubits
        all_ones = "1" * n_qubits

        assert abs(probs.get(all_zeros, 0) - 0.5) < 0.001
        assert abs(probs.get(all_ones, 0) - 0.5) < 0.001

        # All other states should have zero probability
        for state, prob in probs.items():
            if state not in [all_zeros, all_ones]:
                assert prob < 0.001


class TestHadamardSuperposition:
    """Tests for Hadamard gate superposition."""

    def test_single_qubit_superposition(self):
        """Single H gate creates equal superposition."""
        qc = QuantumCircuit(1)
        qc.h(0)

        sv = Statevector.from_instruction(qc)
        probs = sv.probabilities_dict()

        assert abs(probs.get("0", 0) - 0.5) < 0.001
        assert abs(probs.get("1", 0) - 0.5) < 0.001

    def test_two_qubit_superposition(self):
        """H⊗H creates uniform superposition over 4 states."""
        qc = QuantumCircuit(2)
        qc.h([0, 1])

        sv = Statevector.from_instruction(qc)
        probs = sv.probabilities_dict()

        for state in ["00", "01", "10", "11"]:
            assert abs(probs.get(state, 0) - 0.25) < 0.001

    @pytest.mark.parametrize("n_qubits", [1, 2, 3, 4])
    def test_n_qubit_superposition(self, n_qubits):
        """H⊗n creates uniform superposition over 2^n states."""
        qc = QuantumCircuit(n_qubits)
        qc.h(range(n_qubits))

        sv = Statevector.from_instruction(qc)
        probs = sv.probabilities_dict()

        expected_prob = 1.0 / (2 ** n_qubits)
        for prob in probs.values():
            assert abs(prob - expected_prob) < 0.001


class TestDeutschJozsaOracle:
    """Tests for Deutsch-Jozsa algorithm oracles."""

    def test_constant_zero_oracle(self):
        """Constant f(x)=0 oracle leaves state unchanged."""
        qc = QuantumCircuit(3)  # 2 input + 1 ancilla
        qc.h([0, 1])
        qc.x(2)
        qc.h(2)
        # f(x) = 0: no operation
        qc.h([0, 1])
        qc.measure_all()

        simulator = AerSimulator()
        result = simulator.run(qc, shots=1000).result()
        counts = result.get_counts()

        # Should measure |00⟩ on input qubits (constant function)
        total_00 = sum(c for state, c in counts.items() if state[1:3] == "00")
        assert total_00 > 900  # Allow for some noise

    def test_balanced_parity_oracle(self):
        """Balanced f(x)=parity oracle gives non-zero result."""
        qc = QuantumCircuit(3, 2)  # 2 input + 1 ancilla
        qc.h([0, 1])
        qc.x(2)
        qc.h(2)
        # f(x) = x0 XOR x1 (parity - balanced)
        qc.cx(0, 2)
        qc.cx(1, 2)
        qc.h([0, 1])
        qc.measure([0, 1], [0, 1])

        simulator = AerSimulator()
        result = simulator.run(qc, shots=1000).result()
        counts = result.get_counts()

        # Should NOT measure |00⟩ (balanced function)
        assert counts.get("00", 0) < 100


class TestGroverIteration:
    """Tests for Grover's algorithm components."""

    def test_oracle_marks_target(self):
        """Oracle should flip phase of target state."""
        target = "11"
        qc = QuantumCircuit(2)
        qc.h([0, 1])  # Create superposition

        # Oracle for |11⟩
        qc.cz(0, 1)

        sv = Statevector.from_instruction(qc)
        amplitudes = sv.data

        # |11⟩ should have negative amplitude
        # Index 3 = |11⟩ in little-endian
        assert amplitudes[3].real < 0

    def test_diffusion_amplifies(self):
        """Diffusion operator should amplify marked state."""
        qc = QuantumCircuit(2)
        qc.h([0, 1])

        # Oracle for |11⟩
        qc.cz(0, 1)

        # Diffusion
        qc.h([0, 1])
        qc.x([0, 1])
        qc.cz(0, 1)
        qc.x([0, 1])
        qc.h([0, 1])

        sv = Statevector.from_instruction(qc)
        probs = sv.probabilities_dict()

        # |11⟩ should have highest probability
        assert probs.get("11", 0) > 0.7
