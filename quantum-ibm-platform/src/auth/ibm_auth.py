"""
IBM Quantum Authentication Module

Handles connection to IBM Quantum Platform via Qiskit Runtime.
"""

import requests
from typing import Optional, List
from qiskit_ibm_runtime import QiskitRuntimeService
from qiskit_ibm_runtime.fake_provider import FakeBelemV2

import sys
sys.path.insert(0, str(__file__).rsplit("src", 1)[0])
from config.quantum_config import QuantumConfig


class IBMQuantumAuth:
    """Manages authentication and connection to IBM Quantum Platform."""

    def __init__(self):
        self.service: Optional[QiskitRuntimeService] = None
        self.bearer_token: Optional[str] = None
        self._backends_cache: List = []

    def connect(self, save_credentials: bool = False) -> QiskitRuntimeService:
        """
        Connect to IBM Quantum Platform using Qiskit Runtime.

        Args:
            save_credentials: If True, saves credentials locally for future use

        Returns:
            QiskitRuntimeService instance
        """
        if not QuantumConfig.validate():
            raise ValueError("IBM Quantum credentials not configured. Set IQP_API_TOKEN.")

        if save_credentials:
            QiskitRuntimeService.save_account(
                token=QuantumConfig.API_TOKEN,
                instance=QuantumConfig.INSTANCE_CRN or None,
                channel=QuantumConfig.get_channel(),
                overwrite=True,
            )

        self.service = QiskitRuntimeService(
            token=QuantumConfig.API_TOKEN,
            instance=QuantumConfig.INSTANCE_CRN or None,
            channel=QuantumConfig.get_channel(),
        )

        return self.service

    def connect_saved(self) -> QiskitRuntimeService:
        """Connect using previously saved credentials."""
        self.service = QiskitRuntimeService()
        return self.service

    def get_bearer_token(self) -> str:
        """
        Get Bearer token for REST API access.

        Returns:
            Bearer token string
        """
        if not QuantumConfig.API_TOKEN:
            raise ValueError("API token not configured")

        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        data = f"grant_type=urn:ibm:params:oauth:grant-type:apikey&apikey={QuantumConfig.API_TOKEN}"

        response = requests.post(QuantumConfig.IAM_TOKEN_URL, headers=headers, data=data)
        response.raise_for_status()

        self.bearer_token = response.json()["access_token"]
        return self.bearer_token

    def get_backends(self, min_qubits: int = 5, operational: bool = True) -> List:
        """
        Get list of available backends.

        Args:
            min_qubits: Minimum number of qubits required
            operational: Only return operational backends

        Returns:
            List of backend objects
        """
        if not self.service:
            self.connect()

        self._backends_cache = self.service.backends(
            simulator=False,
            operational=operational,
            min_num_qubits=min_qubits,
        )
        return self._backends_cache

    def get_least_busy(self, min_qubits: int = 5) -> object:
        """
        Get the least busy backend.

        Args:
            min_qubits: Minimum number of qubits required

        Returns:
            Backend object
        """
        if not self.service:
            self.connect()

        return self.service.least_busy(
            simulator=False,
            operational=True,
            min_num_qubits=min_qubits,
        )

    def get_local_backend(self):
        """
        Get a local fake backend for testing.

        Returns:
            FakeBelemV2 backend
        """
        return FakeBelemV2()

    def print_backends(self) -> None:
        """Print information about available backends."""
        backends = self.get_backends()

        print(f"{'Backend':<20} {'Qubits':<8} {'Status':<12} {'Queue':<8}")
        print("-" * 50)

        for backend in backends:
            status = backend.status()
            print(
                f"{backend.name:<20} "
                f"{backend.num_qubits:<8} "
                f"{'Online' if status.operational else 'Offline':<12} "
                f"{status.pending_jobs:<8}"
            )


# Convenience function
def get_service() -> QiskitRuntimeService:
    """Quick access to IBM Quantum service."""
    auth = IBMQuantumAuth()
    return auth.connect()
