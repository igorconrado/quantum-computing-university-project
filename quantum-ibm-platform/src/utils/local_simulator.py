"""
Local Simulator Utilities

Run quantum circuits locally for testing before using real hardware.
"""

from typing import Tuple
from qiskit import QuantumCircuit
from qiskit.transpiler import generate_preset_pass_manager
from qiskit_ibm_runtime import EstimatorV2 as Estimator
from qiskit_ibm_runtime import SamplerV2 as Sampler
from qiskit_ibm_runtime.fake_provider import FakeBelemV2, FakeManilaV2, FakeSherbrooke


def get_fake_backend(name: str = "belem"):
    """
    Get a fake backend for local testing.

    Args:
        name: Backend name ("belem", "manila", "sherbrooke")

    Returns:
        Fake backend object
    """
    backends = {
        "belem": FakeBelemV2,
        "manila": FakeManilaV2,
        "sherbrooke": FakeSherbrooke,
    }

    if name not in backends:
        raise ValueError(f"Unknown backend: {name}. Choose from {list(backends.keys())}")

    return backends[name]()


def get_local_estimator(backend_name: str = "belem") -> Tuple[Estimator, object]:
    """
    Get an Estimator configured with a local fake backend.

    Args:
        backend_name: Name of fake backend to use

    Returns:
        Tuple of (Estimator, backend)
    """
    backend = get_fake_backend(backend_name)
    estimator = Estimator(backend)
    return estimator, backend


def get_local_sampler(backend_name: str = "belem") -> Tuple[Sampler, object]:
    """
    Get a Sampler configured with a local fake backend.

    Args:
        backend_name: Name of fake backend to use

    Returns:
        Tuple of (Sampler, backend)
    """
    backend = get_fake_backend(backend_name)
    sampler = Sampler(backend)
    return sampler, backend


def transpile_for_backend(
    circuit: QuantumCircuit,
    backend,
    optimization_level: int = 1
) -> QuantumCircuit:
    """
    Transpile circuit for a specific backend.

    Args:
        circuit: Input circuit
        backend: Target backend
        optimization_level: 0-3, higher = more optimization

    Returns:
        Transpiled (ISA) circuit
    """
    pm = generate_preset_pass_manager(
        backend=backend,
        optimization_level=optimization_level
    )
    return pm.run(circuit)


def run_local_experiment(
    circuit: QuantumCircuit,
    observables: list = None,
    backend_name: str = "belem",
    shots: int = 4000
) -> dict:
    """
    Run a complete local experiment.

    Args:
        circuit: Circuit to run
        observables: List of observables (if None, uses Sampler)
        backend_name: Fake backend name
        shots: Number of shots

    Returns:
        Results dictionary
    """
    backend = get_fake_backend(backend_name)
    isa_circuit = transpile_for_backend(circuit, backend)

    if observables:
        # Use Estimator for expectation values
        estimator = Estimator(backend)
        estimator.options.default_shots = shots

        # Map observables to circuit layout
        mapped_obs = [obs.apply_layout(isa_circuit.layout) for obs in observables]

        job = estimator.run([(isa_circuit, mapped_obs)])
        result = job.result()[0]

        return {
            "type": "estimator",
            "values": result.data.evs,
            "errors": result.data.stds,
        }
    else:
        # Use Sampler for counts
        sampler = Sampler(backend)
        sampler.options.default_shots = shots

        isa_circuit.measure_all()
        job = sampler.run([isa_circuit])
        result = job.result()[0]

        return {
            "type": "sampler",
            "counts": result.data.meas.get_counts(),
        }
