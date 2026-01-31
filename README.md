# Quantum Computing University Project

[![CI](https://github.com/igorconrado/quantum-computing-university-project/actions/workflows/ci.yml/badge.svg)](https://github.com/igorconrado/quantum-computing-university-project/actions/workflows/ci.yml)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Qiskit](https://img.shields.io/badge/Qiskit-1.0+-blueviolet.svg)](https://qiskit.org/)

A Project-Based Learning approach to Quantum Software Engineering, combining theoretical foundations with industrial applications.

## Overview

This project implements a comprehensive study of quantum computing through:

- 📚 **Academic Article**: Formal documentation following SBC (Brazilian Computing Society) standards
- 🎮 **Quantum Pong**: Interactive game for learning quantum measurement concepts
- 🔬 **Algorithm Comparison**: Classical vs. Quantum-Inspired approaches for TSP
- 📓 **Jupyter Notebooks**: Hands-on exercises from "Quantum Computing for the Quantum Curious"

## Project Structure

```
quantum-computing-university-project/
│
├── article/                    # Academic article (PT/EN)
│   ├── portuguese.md
│   └── english.md
│
├── case_study/                 # KPMG/TDC Net case analysis (PT/EN)
│   ├── portuguese.md
│   └── english.md
│
├── programming/                # Practical implementations
│   ├── quantum_pong/           # Quantum Pong game
│   ├── tsp_comparison/         # TSP algorithm comparison
│   │   ├── classical/          # Brute force, Nearest Neighbor, SA
│   │   ├── quantum_inspired/   # QUBO solver
│   │   └── utils/              # Visualization, graph generation
│   └── exercises/              # Textbook exercises
│       ├── chapter_09/         # Quantum algorithms
│       └── chapter_10/         # Practical worksheets
│
├── quantum-ibm-platform/       # IBM Quantum SDK wrapper
│
└── tests/                      # Unit tests
```

## Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/igorconrado/quantum-computing-university-project.git
cd quantum-computing-university-project

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install package with dependencies
pip install -e ".[all]"
```

### Running the Tests

```bash
pytest -v
```

### Running Quantum Pong

```bash
cd programming/quantum_pong
python main.py
```

### Exploring Notebooks

```bash
jupyter notebook programming/exercises/
```

## Key Components

### 1. Quantum Pong 🎮

An interactive game where players control a paddle using quantum gates. The paddle exists in superposition until measured, teaching the quantum measurement postulate through gameplay.

**Controls:**
- `H`: Apply Hadamard gate (create superposition)
- `X`: Apply Pauli-X gate (NOT operation)
- `Z`: Apply Pauli-Z gate (phase flip)
- `M`: Measure (collapse superposition)

### 2. TSP Comparison 📊

Implementation and benchmarking of multiple algorithms for the Traveling Salesman Problem:

| Algorithm | Complexity | Optimality |
|-----------|------------|------------|
| Brute Force | O(n!) | Guaranteed |
| Nearest Neighbor | O(n²) | Heuristic |
| Simulated Annealing | O(k·n²) | Heuristic |
| QUBO Solver | O(k·n²) | Quantum-inspired |

### 3. Exercise Notebooks 📓

Complete solutions for Chapters 9 and 10 of "Quantum Computing for the Quantum Curious":

- Deutsch-Jozsa Algorithm
- Grover's Search
- Quantum Oracles
- Bell States
- Quantum Teleportation

## Documentation

- **Academic Article**: [article/portuguese.md](article/portuguese.md) | [article/english.md](article/english.md)
- **Case Study**: [case_study/portuguese.md](case_study/portuguese.md) | [case_study/english.md](case_study/english.md)
- **Programming Guide**: [programming/README.md](programming/README.md)

## Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

1. Fork the repository
2. Create a feature branch (`git checkout -b feat/amazing-feature`)
3. Commit your changes (`git commit -m 'feat: add amazing feature'`)
4. Push to the branch (`git push origin feat/amazing-feature`)
5. Open a Pull Request

## References

### Books & Papers

- Hughes, C. et al. (2021). *Quantum Computing for the Quantum Curious*. Springer.
- Nielsen, M. A. & Chuang, I. L. (2010). *Quantum Computation and Quantum Information*. Cambridge.
- Lucas, A. (2014). Ising formulations of many NP problems. *Frontiers in Physics*.

### Online Resources

- [Qiskit Documentation](https://qiskit.org/documentation/)
- [IBM Quantum Platform](https://quantum.ibm.com/)
- [16 Danish Quantum Use Cases](https://www.oqi.dk/files/pdf/Digitalt-brochure-enkelt.pdf)

### Interactive Tools

- [TSP Game](https://algorithms.discrete.ma.tum.de/graph-games/tsp-game/index_en.html)
- [Simulated Annealing Visualization](https://www.fourmilab.ch/documents/travelling/anneal/)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Qiskit Community](https://qiskit.org/community)
- [IBM Quantum](https://quantum.ibm.com/)
- SBC (Sociedade Brasileira de Computação)
