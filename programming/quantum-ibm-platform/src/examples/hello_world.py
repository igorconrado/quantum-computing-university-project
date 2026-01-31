"""
Hello World - Bell State Experiment

Run a simple Bell state experiment on IBM Quantum hardware.
"""

import sys
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from qiskit import QuantumCircuit
from qiskit.quantum_info import SparsePauliOp
from qiskit.transpiler import generate_preset_pass_manager
from qiskit_ibm_runtime import QiskitRuntimeService
from qiskit_ibm_runtime import EstimatorV2 as Estimator
import matplotlib.pyplot as plt

from src.auth import IBMQuantumAuth
from src.circuits import create_bell_state, get_pauli_observables
from src.utils import plot_expectation_values


def run_bell_experiment_local():
    """Run Bell state experiment on local simulator."""
    print("Running Bell State Experiment (Local Simulator)")
    print("=" * 50)

    # Import local utilities
    from src.utils.local_simulator import run_local_experiment

    # Create Bell state
    circuit = create_bell_state()
    print("\nCircuit:")
    print(circuit.draw())

    # Define observables
    obs_labels = ["II", "IZ", "ZI", "ZZ", "XX", "YY"]
    observables = get_pauli_observables(obs_labels)

    # Run experiment
    result = run_local_experiment(circuit, observables, shots=4000)

    print("\nResults:")
    for label, value in zip(obs_labels, result["values"]):
        print(f"  <{label}> = {value:.4f}")

    # Plot
    fig, ax = plot_expectation_values(
        obs_labels,
        result["values"],
        result.get("errors"),
        title="Bell State |Φ+⟩ Expectation Values"
    )
    plt.show()

    return result


def run_bell_experiment_ibm():
    """Run Bell state experiment on IBM Quantum hardware."""
    print("Running Bell State Experiment (IBM Quantum)")
    print("=" * 50)

    # Connect to IBM Quantum
    auth = IBMQuantumAuth()
    service = auth.connect()

    # Get least busy backend
    backend = auth.get_least_busy(min_qubits=2)
    print(f"\nUsing backend: {backend.name}")

    # Create and transpile circuit
    circuit = create_bell_state()
    pm = generate_preset_pass_manager(backend=backend, optimization_level=1)
    isa_circuit = pm.run(circuit)

    print("\nTranspiled circuit:")
    print(isa_circuit.draw())

    # Define observables
    obs_labels = ["IZ", "ZI", "ZZ", "XX"]
    observables = get_pauli_observables(obs_labels)

    # Map to circuit layout
    mapped_obs = [obs.apply_layout(isa_circuit.layout) for obs in observables]

    # Run with Estimator
    estimator = Estimator(mode=backend)
    estimator.options.resilience_level = 1
    estimator.options.default_shots = 5000

    job = estimator.run([(isa_circuit, mapped_obs)])
    print(f"\nJob ID: {job.job_id()}")
    print("Waiting for results...")

    result = job.result()[0]
    values = result.data.evs

    print("\nResults:")
    for label, value in zip(obs_labels, values):
        print(f"  <{label}> = {value:.4f}")

    # Plot
    fig, ax = plot_expectation_values(
        obs_labels,
        list(values),
        title=f"Bell State on {backend.name}"
    )
    plt.savefig("bell_state_ibm.png", dpi=150)
    plt.show()

    return {"job_id": job.job_id(), "values": list(values)}


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Run Bell State Experiment")
    parser.add_argument(
        "--mode",
        choices=["local", "ibm"],
        default="local",
        help="Run locally or on IBM Quantum"
    )

    args = parser.parse_args()

    if args.mode == "local":
        run_bell_experiment_local()
    else:
        run_bell_experiment_ibm()
