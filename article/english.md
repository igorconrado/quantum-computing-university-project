# From Playful to Industrial: A Project-Based Approach to Teaching Quantum Software Engineering

## Abstract

This paper presents a Project-Based Learning (PBL) experience report for teaching Quantum Software Engineering. The methodology combines theoretical foundations in computational quantum mechanics with solving industrially-relevant NP-hard problems, operating on two axes: (i) consolidating fundamentals through Hughes et al. (2021) curriculum and implementing interactive artifacts; and (ii) prototyping solutions for the Vehicle Routing Problem (VRP) via QUBO formulations. Results demonstrate that empirical comparison between exact classical algorithms and quantum-inspired heuristic exploration constitutes an effective pedagogical instrument for understanding complexity classes.

**Keywords:** Quantum Software Engineering; Project-Based Learning; Combinatorial Optimization; QUBO Formulation; Qiskit.

## Resumo

Este trabalho apresenta um relato de experiência em Project-Based Learning (PBL) para o ensino de Engenharia de Software Quântica. A metodologia articula fundamentação teórica em mecânica quântica computacional com resolução de problemas NP-difíceis de relevância industrial, operando em dois eixos: (i) consolidação dos fundamentos através do currículo de Hughes et al. (2021) e implementação de artefatos interativos; e (ii) prototipagem de soluções para o Vehicle Routing Problem (VRP) via formulações QUBO. Os resultados evidenciam que a contraposição empírica entre algoritmos clássicos exatos e exploração heurística quantum-inspired constitui instrumento pedagógico eficaz para compreensão de classes de complexidade.

**Palavras-chave:** Engenharia de Software Quântica; Aprendizagem Baseada em Projetos; Otimização Combinatória; Formulação QUBO; Qiskit.

---

## 1. Introduction

Quantum Computing is undergoing a paradigmatic inflection point. What for decades remained confined to theoretical physics departments — coherent manipulation of two-level quantum systems, exploitation of superposition and entanglement for information processing — now emerges as applied engineering technology. Google's demonstration of quantum supremacy in 2019 (Arute et al., 2019), advances in quantum error correction (Google Quantum AI, 2023), and hardware availability via cloud (IBM Quantum, Amazon Braket) signal the maturation of the NISQ (*Noisy Intermediate-Scale Quantum*) era.

This scenario poses a non-trivial pedagogical challenge: how to train software engineers capable of fluently transitioning between the deterministic paradigm of Boolean logic and the probabilistic-interferometric paradigm of quantum computing? Literature indicates that purely theoretical approaches, centered on Dirac formalism and linear algebra of Hilbert spaces, frequently alienate computer science students without physics backgrounds (Seskir et al., 2022; Aiello et al., 2021).

### 1.1. Contributions

This work offers the following contributions:

1. **Pedagogical framework**: Structuring of a learning path in two epics (foundations + industrial application) with concrete and measurable deliverables.

2. **Interactive artifact**: Implementation of Quantum Pong as a tool for internalizing the measurement postulate, available as an open educational resource.

3. **Comparative analysis**: Implementation and benchmarking of classical algorithms (brute force, simulated annealing) and quantum-inspired (QUBO solver) for the TSP.

4. **Open source**: Full availability of source code in a public repository: [github.com/igorconrado/quantum-computing-university-project](https://github.com/igorconrado/quantum-computing-university-project).

### 1.2. Paper Organization

The remainder of this paper is organized as follows: Section 2 presents the theoretical background; Section 3 describes the methodology; Section 4 details development and results; Section 5 discusses implications and limitations; and Section 6 concludes the work.

## 2. Theoretical Background

### 2.1. Postulates of Computational Quantum Mechanics

Quantum computing is grounded in four postulates governing the evolution and measurement of quantum systems (Nielsen & Chuang, 2010):

**Postulate 1 (State Space):** The state of a quantum system is described by a unit vector |ψ⟩ in a Hilbert space ℋ of dimension 2ⁿ for n qubits:

$$|\psi\rangle = \sum_{i=0}^{2^n-1} \alpha_i |i\rangle, \quad \sum_i |\alpha_i|^2 = 1 \tag{1}$$

**Postulate 2 (Unitary Evolution):** The temporal evolution of closed systems is governed by unitary operators U, where U†U = I.

**Postulate 3 (Projective Measurement):** Measurement of an observable M with spectral decomposition M = Σₘ m Pₘ collapses the state |ψ⟩ to the corresponding eigenspace with probability:

$$p(m) = \langle\psi|P_m|\psi\rangle \tag{2}$$

**Postulate 4 (Tensor Composition):** The state space of a composite system is the tensor product of component spaces: ℋ_AB = ℋ_A ⊗ ℋ_B.

The phenomenon of entanglement — the impossibility of factoring certain composite states — emerges naturally from the fourth postulate and constitutes the distinctive computational resource of quantum computing.

### 2.2. Complexity Classes and Quantum Advantage

The Traveling Salesman Problem (TSP) belongs to the NP-hard class, implying that, under the P ≠ NP conjecture, no polynomial algorithm exists for its exact solution. The complexity of the brute force algorithm is O(n!), making instances with n > 12 computationally intractable on conventional hardware.

Quantum algorithms offer speedups for specific problem classes:

- **Exponential speedup**: Shor's algorithm for factoring — BQP vs presumably non-P (Shor, 1994)
- **Quadratic speedup**: Grover's algorithm for unstructured search — O(√N) vs O(N) (Grover, 1996)
- **Tunneling speedup**: Quantum annealing for combinatorial optimization — heuristic (Kadowaki & Nishimori, 1998)

The QUBO (Quadratic Unconstrained Binary Optimization) formulation enables mapping combinatorial optimization problems to Ising Hamiltonians, compatible with quantum annealing architectures (Lucas, 2014).

### 2.3. Hybrid Variational Algorithms

The NISQ era motivated the development of hybrid classical-quantum variational algorithms, where parameterized circuits are classically optimized. QAOA (Quantum Approximate Optimization Algorithm) is particularly relevant for combinatorial problems (Farhi et al., 2014):

$$|\gamma, \beta\rangle = \prod_{p=1}^{P} e^{-i\beta_p H_M} e^{-i\gamma_p H_C} |s\rangle \tag{3}$$

Where H_C encodes the cost function, H_M is the mixer Hamiltonian, and parameters (γ, β) are classically optimized.

## 3. Methodology

### 3.1. Pedagogical Design: Project-Based Learning

The adopted pedagogical approach is grounded in Project-Based Learning principles (Krajcik & Shin, 2014), structured in two development epics with concrete deliverables:

**Epic 1 — Foundations (8 weeks)**
- Complete study of Hughes et al. (2021), Chapters 1-10
- Implementation of Jupyter notebooks for each canonical algorithm
- Development of Quantum Pong artifact as integrating project
- Resolution of theoretical and practical textbook exercises

**Epic 2 — Industrial Application (4 weeks)**
- Critical analysis of Case 10 (KPMG/TDC Net, 2020)
- Comparative implementation: brute force, nearest neighbor, simulated annealing, QUBO solver
- Academic documentation and critical reflection

### 3.2. Technology Stack

Development exclusively used open-source tools:

| Tool | Version | Purpose |
|------|---------|---------|
| Qiskit | 1.x | Quantum circuit framework |
| Qiskit Aer | 0.14+ | Statevector and QASM simulation |
| NumPy/SciPy | 1.24+ | Numerical computing |
| Pygame | 2.5+ | Interactive artifact rendering |
| Jupyter | 7.0+ | Executable documentation |
| Matplotlib | 3.8+ | Results visualization |

*Table 1: Technology stack used in the project.*

### 3.3. Evaluation Metrics

To assess approach effectiveness, metrics were defined across three dimensions:

1. **Curricular coverage**: Percentage of textbook exercises implemented
2. **Code quality**: Adherence to standards (PEP8, type hints, documentation)
3. **Algorithmic performance**: Execution time and solution quality for TSP instances

## 4. Development and Results

### 4.1. Quantum Pong: Gamification as Pedagogical Instrument

The Quantum Pong artifact was conceived as an interactive materialization of the measurement postulate. The system architecture implements a clear separation between the quantum backend (`QuantumPaddle` class) and the rendering frontend (Pygame).

**Core Mechanic**: The player's paddle is represented by a 3-qubit register, encoding 2³ = 8 discrete positions. The player manipulates state through quantum gates:

| Gate | Effect | Physical Analogy |
|------|--------|------------------|
| Hadamard (H) | Uniform superposition | 50/50 beam splitter |
| Pauli-X | Quantum NOT | Spin inversion |
| Pauli-Z | Relative phase π | Optical phase shift |
| CNOT | Entanglement | EPR correlation |

*Table 2: Quantum gates available in Quantum Pong.*

The fundamental game rule explicates wave function collapse: *a paddle in superposition cannot block the ball*. This mechanic forces the player to internalize that measurement is irreversible and that observation timing is critical.

**Quantum Circuit**: The initial state and evolution can be represented as:

$$|\psi\rangle = H^{\otimes 3}|000\rangle = \frac{1}{\sqrt{8}} \sum_{i=0}^{7} |i\rangle \xrightarrow{\text{measurement}} |k\rangle \tag{4}$$

Where k ∈ {0, 1, ..., 7} is the collapsed position with uniform probability 1/8.

### 4.2. Implementation of Canonical Algorithms

#### 4.2.1. Deutsch-Jozsa Algorithm

Implementation of the oracle for functions f: {0,1}ⁿ → {0,1}, demonstrating exponential speedup in determining constant vs. balanced functions. Empirical verification confirmed that a single query to the quantum oracle replaces the 2ⁿ⁻¹ + 1 queries required classically (worst-case).

#### 4.2.2. Grover's Algorithm

Implementation of the diffusion operator and marking oracle for unstructured search:

$$D = 2|s\rangle\langle s| - I, \quad U_x = I - 2|x\rangle\langle x| \tag{5}$$

The optimal number of iterations follows:

$$k_{opt} = \left\lfloor \frac{\pi}{4}\sqrt{N} \right\rfloor \tag{6}$$

For N = 8 (3 qubits), convergence was observed with k = 2 iterations, achieving success probability > 94%, as theoretically expected.

#### 4.2.3. Bell States and Teleportation

Implementation of the four Bell states:

$$|\Phi^{\pm}\rangle = \frac{1}{\sqrt{2}}(|00\rangle \pm |11\rangle), \quad |\Psi^{\pm}\rangle = \frac{1}{\sqrt{2}}(|01\rangle \pm |10\rangle) \tag{7}$$

The teleportation protocol was fully implemented, demonstrating transfer of arbitrary states |ψ⟩ = α|0⟩ + β|1⟩ through 1 shared ebit and 2 classical bits of communication.

### 4.3. Comparative Analysis: Classical vs. Quantum-Inspired TSP

#### 4.3.1. Brute Force Algorithm — O(n!)

The exhaustive implementation verified all (n-1)!/2 distinct routes (fixing origin and eliminating symmetry). Empirical results on Intel i7-10750H CPU:

| n (cities) | Permutations | Time (s) | Memory (MB) |
|------------|--------------|----------|-------------|
| 5 | 12 | 0.001 | < 1 |
| 8 | 2,520 | 0.02 | < 1 |
| 10 | 181,440 | 1.8 | 2 |
| 12 | 19,958,400 | 187 | 15 |
| 13 | 239,500,800 | > 2000 | — |

*Table 3: Brute force algorithm performance for TSP.*

The factorial explosion empirically confirms intractability for n > 12 on conventional hardware.

#### 4.3.2. Nearest Neighbor — O(n²)

Implementation of the greedy heuristic that, at each step, selects the nearest unvisited city:

| n (cities) | Time (s) | Gap vs. Optimal |
|------------|----------|-----------------|
| 10 | 0.001 | 15-25% |
| 50 | 0.008 | 20-30% |
| 100 | 0.025 | 20-35% |

*Table 4: Nearest Neighbor algorithm performance.*

#### 4.3.3. Simulated Annealing — Classical Metaheuristic

Implementation of SA algorithm with exponential temperature schedule:

$$T(k) = T_0 \cdot \alpha^k, \quad \alpha \in (0.95, 0.999) \tag{8}$$

The acceptance probability of worse solutions follows the Boltzmann distribution:

$$P(\Delta E) = \exp\left(-\frac{\Delta E}{k_B T}\right) \tag{9}$$

Results demonstrated convergence to high-quality solutions (gap < 5% of known optimum) in polynomial time.

#### 4.3.4. QUBO Solver — Quantum-Inspired Optimization

The QUBO formulation for TSP uses binary variables x_{ip} ∈ {0,1} indicating whether city i is visited at position p. The cost Hamiltonian assumes the form:

$$H = A\sum_i\left(1 - \sum_p x_{ip}\right)^2 + A\sum_p\left(1 - \sum_i x_{ip}\right)^2 + B\sum_{i,j,p} d_{ij} x_{ip} x_{j,p+1} \tag{10}$$

The first two terms are constraint penalties; the third encodes the objective function.

### 4.4. Comparative Synthesis

| Algorithm | Complexity | Optimality Guarantee | Practical Scalability |
|-----------|------------|----------------------|----------------------|
| Brute Force | O(n!) | Yes | n ≤ 12 |
| Nearest Neighbor | O(n²) | No | n ≤ 10⁵ |
| Simulated Annealing | O(k·n²) | No | n ≤ 10⁴ |
| QUBO (simulated) | O(k·n²) | No | n ≤ 10³ |
| QUBO (quantum annealer) | O(√N)* | No | Limited by connectivity |

*Table 5: Algorithm comparison for TSP. *Theoretical speedup.*

## 5. Discussion

### 5.1. Effectiveness of PBL Approach

The reported experience validates the hypothesis that empirical confrontation with classical computational limitations constitutes superior pedagogical motivation compared to abstract theoretical exposition. Direct observation of factorial growth — watching the computer "freeze" when adding a single city — produces intuitive understanding that no mathematical demonstration can substitute.

The Quantum Pong artifact proved particularly effective in internalizing the measurement postulate. The mechanic of "losing points" by measuring at the wrong time gradually transforms into intuition about observation timing — a skill transferable to real quantum algorithm design.

### 5.2. Achieved Curricular Coverage

| Component | Status | Artifacts |
|-----------|--------|-----------|
| Chapters 1-8 (theory) | 100% | Notes, exercises |
| Chapter 9 (algorithms) | 100% | 4 notebooks + solutions |
| Chapter 10 (applications) | 100% | 5 notebooks + solutions |
| Integrating project | 100% | Quantum Pong |
| Industrial case | 100% | TSP comparison suite |

*Table 6: Coverage of Hughes et al. (2021) curriculum.*

### 5.3. Limitations

This work presents limitations that must be acknowledged:

1. **Single sample**: This is an individual experience report, without control group for statistical validation of pedagogical effectiveness.

2. **Classical simulation**: All quantum implementations were executed on simulators, not real quantum hardware. Effects of noise and decoherence were not directly experienced.

3. **Limited scale**: The QUBO solver was tested only on small instances (n ≤ 15), insufficient to demonstrate advantage over optimized classical metaheuristics.

4. **Absence of QAOA**: Although theoretically discussed, the QAOA algorithm was not implemented due to time constraints.

### 5.4. Future Work

Natural extensions of this work include:

1. **Real hardware**: Execution on IBM Quantum devices and analysis of noise effects
2. **QAOA**: Complete implementation for TSP with variational optimization
3. **Complete VRP**: Extension for capacity constraints and time windows
4. **Pedagogical validation**: Application in classrooms with systematic learning assessment

### 5.5. Implications for QSE Training

The experience suggests that quantum software engineers must develop competence in three domains:

1. **Quantum intuition**: Visceral understanding of superposition, entanglement, and measurement
2. **Mathematical modeling**: Translation of problems to formulations compatible with quantum hardware
3. **Software engineering**: Mastery of frameworks (Qiskit, Cirq, PennyLane) and integration practices

## 6. Conclusion

This work presented an experience report on self-directed learning of Quantum Software Engineering, structured around Project-Based Learning. The combination of rigorous theoretical foundation, implementation of interactive artifacts, and analysis of industrial problems proved pedagogically effective for building QSE competencies.

The main contribution lies in the empirical validation that direct experience of the "classical bottleneck" constitutes superior motivation for studying quantum alternatives. The developed code is available as an open educational resource at [github.com/igorconrado/quantum-computing-university-project](https://github.com/igorconrado/quantum-computing-university-project).

Quantum computing inexorably transitions from laboratory to industry. Training engineers capable of navigating this transition requires pedagogical approaches that transcend abstract mathematical formalism, anchoring learning in concrete problems and tangible experiences.

---

## References

Aiello, C. D., et al. (2021). Achieving a quantum smart workforce. *Quantum Science and Technology*, 6(3), 030501.

Arute, F., et al. (2019). Quantum supremacy using a programmable superconducting processor. *Nature*, 574(7779), 505-510.

Danish Quantum Use Cases. (2020). *Case 10: Optimised Route Planning with Quantum and AI*. KPMG / TDC Net.

Farhi, E., Goldstone, J., & Gutmann, S. (2014). A quantum approximate optimization algorithm. *arXiv preprint arXiv:1411.4028*.

Google Quantum AI. (2023). Suppressing quantum errors by scaling a surface code logical qubit. *Nature*, 614(7949), 676-681.

Grover, L. K. (1996). A fast quantum mechanical algorithm for database search. *Proceedings of the 28th Annual ACM Symposium on Theory of Computing*, 212-219.

Hughes, C., Isaacson, J., Perry, A., Sun, R. F., & Turner, J. (2021). *Quantum Computing for the Quantum Curious*. Springer.

Kadowaki, T., & Nishimori, H. (1998). Quantum annealing in the transverse Ising model. *Physical Review E*, 58(5), 5355.

Krajcik, J. S., & Shin, N. (2014). Project-based learning. In R. K. Sawyer (Ed.), *The Cambridge Handbook of the Learning Sciences* (pp. 275-297). Cambridge University Press.

Lucas, A. (2014). Ising formulations of many NP problems. *Frontiers in Physics*, 2, 5.

Nielsen, M. A., & Chuang, I. L. (2010). *Quantum Computation and Quantum Information: 10th Anniversary Edition*. Cambridge University Press.

Seskir, Z. C., et al. (2022). Quantum games and interactive tools for quantum technologies outreach and education. *Optical Engineering*, 61(8), 081809.

Shor, P. W. (1994). Algorithms for quantum computation: discrete logarithms and factoring. *Proceedings of the 35th Annual Symposium on Foundations of Computer Science*, 124-134.

Wootton, J. (2021). *Programming on Quantum Computers: Coding with Qiskit*. IBM Quantum Learning.
