# IBM Quantum Platform SDK

A structured Python project for running quantum experiments on IBM Quantum hardware.

## Project Structure

```
quantum-ibm-platform/
├── config/
│   └── quantum_config.py    # Configuration and credentials
├── src/
│   ├── auth/
│   │   └── ibm_auth.py      # IBM Quantum authentication
│   ├── circuits/
│   │   └── basic_circuits.py # Common circuit patterns
│   ├── utils/
│   │   ├── local_simulator.py # Local testing utilities
│   │   ├── job_manager.py    # Job tracking and retrieval
│   │   └── visualization.py  # Plotting functions
│   └── examples/
│       └── hello_world.py    # Bell state experiment
├── notebooks/                 # Jupyter notebooks
├── tests/                     # Unit tests
├── requirements.txt
├── .env.example              # Environment template
└── README.md
```

## Quick Start

### 1. Setup Environment

```bash
# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
# or: .venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt
```

### 2. Configure Credentials

```bash
# Copy environment template
cp .env.example .env

# Edit .env with your IBM Quantum credentials
# Get API token from: https://quantum.cloud.ibm.com
```

### 3. Run Examples

```bash
# Local simulation (no IBM account needed)
python src/examples/hello_world.py --mode local

# Run on IBM Quantum hardware
python src/examples/hello_world.py --mode ibm
```

## Usage Examples

### Connect to IBM Quantum

```python
from src.auth import IBMQuantumAuth

auth = IBMQuantumAuth()
service = auth.connect()

# List available backends
auth.print_backends()

# Get least busy backend
backend = auth.get_least_busy(min_qubits=5)
```

### Create and Run Circuits

```python
from src.circuits import create_bell_state, get_pauli_observables
from src.utils import run_local_experiment

# Create Bell state circuit
circuit = create_bell_state()

# Define observables
observables = get_pauli_observables(["ZZ", "XX"])

# Run locally
result = run_local_experiment(circuit, observables)
print(f"Expectation values: {result['values']}")
```

### Manage Jobs

```python
from src.utils import JobManager

manager = JobManager()

# List recent jobs
manager.print_jobs(limit=5)

# Get job results
result = manager.wait_for_result("job_id_here")
```

## Key Features

- **Secure credential management** via environment variables
- **Local simulation** for testing before using real hardware
- **Automatic transpilation** for target backends
- **Job tracking** and result retrieval
- **Visualization utilities** for expectation values and counts

## Dependencies

- `qiskit >= 1.0.0` - Quantum circuit SDK
- `qiskit-ibm-runtime >= 0.20.0` - IBM Quantum access
- `matplotlib >= 3.7.0` - Visualization
- `python-dotenv >= 1.0.0` - Environment management

## References

- [Qiskit Documentation](https://docs.quantum.ibm.com/)
- [IBM Quantum Platform](https://quantum.cloud.ibm.com/)
- [Qiskit Tutorials](https://learning.quantum.ibm.com/)
