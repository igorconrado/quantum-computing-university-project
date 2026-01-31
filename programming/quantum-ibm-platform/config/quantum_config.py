"""
IBM Quantum Platform Configuration

Loads credentials from environment variables for secure access.
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# Load .env file from project root
env_path = Path(__file__).parent.parent / ".env"
load_dotenv(env_path)


class QuantumConfig:
    """Configuration for IBM Quantum Platform access."""

    # API credentials
    API_TOKEN: str = os.getenv("IQP_API_TOKEN", "")
    INSTANCE_CRN: str = os.getenv("IBM_QUANTUM_CRN", "")
    REGION: str = os.getenv("IBM_QUANTUM_REGION", "us-east")

    # API URLs
    IAM_TOKEN_URL: str = "https://iam.cloud.ibm.com/identity/token"
    QUANTUM_API_URL: str = "https://quantum.cloud.ibm.com/api/v1"

    # Default settings
    DEFAULT_SHOTS: int = 4000
    DEFAULT_OPTIMIZATION_LEVEL: int = 1
    DEFAULT_RESILIENCE_LEVEL: int = 1

    @classmethod
    def validate(cls) -> bool:
        """Check if required credentials are configured."""
        if not cls.API_TOKEN:
            print("Warning: IQP_API_TOKEN not set in environment")
            return False
        return True

    @classmethod
    def get_channel(cls) -> str:
        """Get the appropriate channel based on credentials."""
        if cls.INSTANCE_CRN:
            return "ibm_cloud"
        return "ibm_quantum"
