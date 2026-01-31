# Programming - Quantum Computing Exercises

Implementation of quantum computing concepts using Qiskit framework.

## Structure

```
programming/
├── exercises/              # Book exercises (Hughes et al.)
│   ├── chapter_09/         # Quantum algorithms (Deutsch-Jozsa, Grover)
│   └── chapter_10/         # Practical worksheets (gates, Bell states, teleportation)
│
├── quantum_pong/           # Interactive quantum game
│   ├── game.py             # Pygame rendering and game logic
│   ├── quantum_paddle.py   # Qiskit-based paddle mechanics
│   └── main.py             # Entry point
│
├── tsp_comparison/         # TSP algorithm comparison
│   ├── classical/          # Brute force, Simulated Annealing, Nearest Neighbor
│   ├── quantum_inspired/   # QUBO solver
│   ├── benchmarks/         # Performance comparison notebook
│   ├── utils/              # Graph generation and visualization
│   └── data/               # Test datasets (cities.json)
│
└── testing/                # Basic Qiskit tests
```

## Quick Start

```bash
# Activate environment
conda activate qiskit_env

# Run Quantum Pong
python quantum_pong/main.py

# Run TSP comparison
python tsp_comparison/classical/brute_force.py
python tsp_comparison/classical/simulated_annealing.py
python tsp_comparison/quantum_inspired/qubo_solver.py

# Open exercise notebooks
jupyter notebook exercises/
```

## Dependencies

See [requirements.txt](requirements.txt) for full list.

Core dependencies:
- **qiskit** >= 1.0.0 - Quantum circuit construction and simulation
- **qiskit-aer** >= 0.13.0 - High-performance simulators
- **pygame** >= 2.5.0 - Game rendering (Quantum Pong)
- **jupyter** >= 4.0.0 - Interactive notebooks
- **matplotlib** >= 3.7.0 - Visualization

## Exercises Overview

### Chapter 9 - Quantum Algorithms
| Notebook | Algorithm | Speedup |
|----------|-----------|---------|
| 01_deutsch_jozsa.ipynb | Deutsch-Jozsa | Exponential |
| 02_grover_search.ipynb | Grover Search | Quadratic (√N) |
| 03_quantum_oracle.ipynb | Oracle Construction | - |

### Chapter 10 - Practical Worksheets
| Notebook | Topic |
|----------|-------|
| 01_single_qubit_gates.ipynb | X, Y, Z, H, S, T gates + Bloch sphere |
| 02_multi_qubit_circuits.ipynb | CNOT, CZ, SWAP, Toffoli |
| 03_bell_states.ipynb | Entanglement and Bell states |
| 04_quantum_teleportation.ipynb | Quantum teleportation protocol |

## TSP Comparison

Demonstrates the "classical bottleneck" for NP-hard problems:

| Algorithm | Complexity | 10 cities | Optimal? |
|-----------|------------|-----------|----------|
| Brute Force | O(n!) | 3.6M perms | Yes |
| Nearest Neighbor | O(n²) | Fast | No |
| Simulated Annealing | O(k·n²) | Fast | No |
| QUBO Solver | O(k·n²) | Fast | No |

## References

- Hughes, C. et al. (2021). *Quantum Computing for the Quantum Curious*. Springer.
- [Qiskit Documentation](https://qiskit.org/documentation/)
- [IBM Quantum Learning](https://learning.quantum.ibm.com/)
