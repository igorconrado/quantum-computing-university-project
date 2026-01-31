"""
Basic Quantum Circuits

Common circuit patterns for quantum computing experiments.
"""

from typing import List
from qiskit import QuantumCircuit
from qiskit.quantum_info import SparsePauliOp, random_statevector
import numpy as np


def create_bell_state(variant: str = "phi_plus") -> QuantumCircuit:
    """
    Create a Bell state circuit.

    Args:
        variant: One of "phi_plus", "phi_minus", "psi_plus", "psi_minus"

    Returns:
        QuantumCircuit preparing the Bell state
    """
    qc = QuantumCircuit(2, name=f"Bell_{variant}")

    qc.h(0)
    qc.cx(0, 1)

    if variant == "phi_minus":
        qc.z(0)
    elif variant == "psi_plus":
        qc.x(0)
    elif variant == "psi_minus":
        qc.x(0)
        qc.z(0)

    return qc


def create_ghz_state(n_qubits: int) -> QuantumCircuit:
    """
    Create a GHZ (Greenberger-Horne-Zeilinger) state.

    |GHZ⟩ = (|00...0⟩ + |11...1⟩) / √2

    Args:
        n_qubits: Number of qubits (minimum 2)

    Returns:
        QuantumCircuit preparing the GHZ state
    """
    if n_qubits < 2:
        raise ValueError("GHZ state requires at least 2 qubits")

    qc = QuantumCircuit(n_qubits, name=f"GHZ_{n_qubits}")

    qc.h(0)
    for i in range(n_qubits - 1):
        qc.cx(i, i + 1)

    return qc


def create_random_state(n_qubits: int, seed: int = None) -> QuantumCircuit:
    """
    Create a circuit that prepares a random quantum state.

    Args:
        n_qubits: Number of qubits
        seed: Random seed for reproducibility

    Returns:
        QuantumCircuit preparing a random state
    """
    qc = QuantumCircuit(n_qubits, name="Random")

    # Generate random state vector
    if seed is not None:
        np.random.seed(seed)

    statevector = random_statevector(2**n_qubits)
    qc.initialize(statevector, range(n_qubits))

    return qc


def create_w_state(n_qubits: int) -> QuantumCircuit:
    """
    Create a W state.

    |W⟩ = (|100...0⟩ + |010...0⟩ + ... + |000...1⟩) / √n

    Args:
        n_qubits: Number of qubits (minimum 2)

    Returns:
        QuantumCircuit preparing the W state
    """
    if n_qubits < 2:
        raise ValueError("W state requires at least 2 qubits")

    qc = QuantumCircuit(n_qubits, name=f"W_{n_qubits}")

    # First rotation
    theta = 2 * np.arccos(1 / np.sqrt(n_qubits))
    qc.ry(theta, 0)

    # Controlled rotations for remaining qubits
    for i in range(1, n_qubits):
        theta = 2 * np.arccos(1 / np.sqrt(n_qubits - i))
        qc.cry(theta, i - 1, i)
        qc.cx(i, i - 1)

    return qc


def get_pauli_observables(labels: List[str]) -> List[SparsePauliOp]:
    """
    Create Pauli observables from string labels.

    Args:
        labels: List of Pauli strings (e.g., ["ZZ", "XX", "IZ"])

    Returns:
        List of SparsePauliOp objects
    """
    return [SparsePauliOp(label) for label in labels]


def get_standard_observables(n_qubits: int) -> tuple:
    """
    Get standard observables for benchmarking.

    Args:
        n_qubits: Number of qubits

    Returns:
        Tuple of (labels, observables)
    """
    # Generate all single-qubit Z observables
    labels = []
    for i in range(n_qubits):
        label = "I" * (n_qubits - i - 1) + "Z" + "I" * i
        labels.append(label)

    # Add all-Z correlator
    labels.append("Z" * n_qubits)

    return labels, get_pauli_observables(labels)
