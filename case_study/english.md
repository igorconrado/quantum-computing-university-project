# Real-Time Logistics Optimization: From Classical Limits to the Quantum-Inspired Revolution

## Case Study: KPMG/TDC Net (Danish Quantum Use Cases, Case 10)

---

## Executive Summary

This case study analyzes the implementation of quantum-inspired optimization solutions for vehicle routing at TDC Net, a Danish telecommunications company. The project, developed in partnership with KPMG, demonstrated reductions of up to 98% in planning time and 15-20% in total distance traveled. The critical analysis presented contextualizes reported results, discusses methodological limitations, and evaluates applicability to other industrial domains.

**Keywords:** Vehicle Routing Problem; Quantum-Inspired Optimization; QUBO; Logistics; KPMG.

---

## 1. Context and Motivation

### 1.1. The Combinatorial Complexity Challenge

The central problem addressed in Case 10 refers to route optimization for field technicians, technically known as the Vehicle Routing Problem (VRP), a generalization of the Traveling Salesman Problem (TSP). In TDC Net's operational scenario, the challenge involves:

- **Scale**: Hundreds of technicians handling thousands of daily service calls
- **Dynamism**: New calls and cancellations throughout the day
- **Constraints**: Time windows, capacities, technical skills
- **Objective**: Minimize operational costs while maximizing service completions

In classical computing, VRP is classified as NP-Hard, implying exponential complexity growth as new variables are added. For n service points and m vehicles, the search space grows as O(n!/m!), making exact solutions computationally intractable for real-world instances.

### 1.2. Limitations of Traditional Approaches

Market solutions traditionally rely on heuristic and metaheuristic algorithms:

| Approach | Advantage | Limitation |
|----------|-----------|------------|
| Genetic Algorithms | Parallelizable, robust | Slow convergence, many hyperparameters |
| Simulated Annealing | Simple, effective | Sensitive to temperature schedule |
| Ant Colony Optimization | Good for sparse graphs | High computational cost |
| Tabu Search | Avoids cycles | Dependent on neighborhood structure |

*Table 1: Comparison of classical metaheuristics for VRP.*

All these approaches share a fundamental limitation: the tendency to stagnate in **local minima**. The algorithm finds a solution that appears optimal in its neighborhood but remains unaware of globally superior solutions in distant regions of the search space.

---

## 2. Proposed Solution: Quantum-Inspired Optimization

### 2.1. Theoretical Foundations

Quantum-Inspired Optimization (QIO) uses principles from quantum mechanics — specifically the phenomenon of **quantum tunneling** — simulated on classical hardware. Unlike traditional metaheuristics that rely on thermal perturbations to escape local minima, QIO allows "tunneling through" energy barriers via probabilistic transitions inspired by quantum tunneling.

The problem is reformulated as QUBO (Quadratic Unconstrained Binary Optimization):

$$\min_{\mathbf{x} \in \{0,1\}^n} \mathbf{x}^T Q \mathbf{x} \tag{1}$$

Where Q is a matrix encoding both the objective function and problem constraints through penalty terms.

### 2.2. Mathematical Formulation of VRP

For VRP, we define binary variables:

- $x_{ijk} = 1$ if vehicle k travels from point i to point j
- $y_{ik} = 1$ if point i is served by vehicle k

The cost Hamiltonian takes the form:

$$H = \underbrace{\sum_{i,j,k} c_{ij} x_{ijk}}_{H_{distance}} + \underbrace{\lambda_1 \sum_i \left(1 - \sum_k y_{ik}\right)^2}_{H_{coverage}} + \underbrace{\lambda_2 \sum_k \left(\sum_i d_i y_{ik} - C_k\right)^2}_{H_{capacity}} \tag{2}$$

Where:
- $c_{ij}$: cost (distance/time) between points i and j
- $d_i$: demand at point i
- $C_k$: capacity of vehicle k
- $\lambda_1, \lambda_2$: Lagrange multipliers for penalties

### 2.3. KPMG Solution Architecture

The reported implementation uses a hybrid architecture:

```
┌─────────────────┐     ┌──────────────────┐     ┌─────────────────┐
│   ERP/CRM       │────▶│  Preprocessor    │────▶│  QIO Solver     │
│   (data)        │     │  (formulation)   │     │  (optimization) │
└─────────────────┘     └──────────────────┘     └────────┬────────┘
                                                          │
┌─────────────────┐     ┌──────────────────┐              │
│   Dashboard     │◀────│  Postprocessor   │◀─────────────┘
│   (visualization)│    │  (validation)    │
└─────────────────┘     └──────────────────┘
```

*Figure 1: Simplified solution architecture.*

Compatible hardware platforms include:
- **Fujitsu Digital Annealer**: ASIC optimized for QUBO
- **Azure Quantum**: Access to multiple solvers (IonQ, Honeywell, simulators)
- **D-Wave Leap**: Native quantum annealing

---

## 3. Analysis Methodology

### 3.1. Data Source

The results presented in this case study are derived from the public report "Danish Quantum Use Cases" (KPMG, 2020), specifically Case 10: "Optimised Route Planning with Quantum and AI". Quantitative metrics were extracted directly from KPMG's disclosure materials.

**Methodological note**: Reported values represent proof-of-concept (PoC) results in a controlled environment. Production results may vary due to operational factors not captured in the pilot.

### 3.2. Evaluation Metrics

The metrics used follow the standard framework for VRP solution evaluation:

| Metric | Definition | Unit |
|--------|------------|------|
| Planning time | Duration of optimization process | minutes |
| Total distance | Sum of distances traveled by all vehicles | km/day |
| Utilization rate | Percentage of capacity effectively used | % |
| Services/technician | Average number of calls resolved per technician | calls/day |
| Event response time | Latency for dynamic re-optimization | seconds |

*Table 2: Metrics framework for VRP evaluation.*

---

## 4. Reported Results

### 4.1. Quantitative Metrics

The pilot implementation at TDC Net demonstrated the following results:

| Metric | Baseline (Classical) | With QIO | Improvement | Confidence* |
|--------|---------------------|----------|-------------|-------------|
| Planning time | 4-6 hours | < 5 min | ~98% | High |
| Total daily distance | 100% (ref.) | 80-85% | 15-20% | Medium |
| Services/day/technician | ~8 | ~10-12 | 25-50% | Medium |
| Dynamic replanning | Infeasible | Real-time | Enabled | High |

*Table 3: TDC Net pilot results (Source: KPMG, 2020).*

**Note on confidence**: Classification based on specificity of reported data and validation methodology described in source material.

### 4.2. Analysis of Gains

#### Planning Time (98% reduction)

The reduction from 4-6 hours to < 5 minutes represents the most significant and reliable gain. This result is consistent with literature on QUBO solvers, which demonstrate rapid convergence to high-quality solutions even for large instances.

#### Total Distance (15-20% reduction)

The reduction in total distance is attributed to QIO's ability to explore regions of the search space inaccessible to traditional metaheuristics. However, the 15-20% margin suggests variability across instances and possibly dependence on specific characteristics of TDC Net's logistics network.

#### Services per Technician (25-50% increase)

This gain derives from the combination of more efficient routes and dynamic replanning. The wide margin (25-50%) indicates sensitivity to external factors such as service duration and geographic distribution of calls.

---

## 5. Critical Analysis

### 5.1. Strengths

1. **Real-world validation**: The pilot was executed with real operational data from TDC Net, lending credibility to results.

2. **Hybrid architecture**: The combination of classical preprocessing with QIO optimization represents a pragmatic approach for the current state of technology.

3. **Demonstrated scalability**: The solution maintained performance with increasing number of variables, suggesting viability for larger operations.

### 5.2. Limitations and Caveats

1. **Classical hardware**: The implementation uses quantum-inspired (simulation of quantum principles on conventional hardware), not native quantum computing. Reported speedups are relative to suboptimal metaheuristics, not state-of-the-art classical algorithms.

2. **Pilot scale**: Details on the exact number of vehicles and service points in the pilot are not specified, making extrapolation to operations of different scale difficult.

3. **Optimality guarantee**: QIO does not guarantee global optimum — it offers high-quality solutions with high probability, but not mathematical certainty. Comparison with true optimum (when computable) is not reported.

4. **Implementation costs**: The material does not detail TCO (Total Cost of Ownership), including solver licensing, integration infrastructure, and maintenance costs.

### 5.3. Risk Analysis

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Solver failure in production | Low | High | Fallback to classical heuristic |
| Degradation with scale | Medium | Medium | Hierarchical decomposition |
| Vendor lock-in | Medium | High | Abstraction via standardized API |
| Technological obsolescence | High | Low | Modular architecture |

*Table 4: Risk matrix for QIO implementation.*

### 5.4. Economic Analysis (Estimate)

Based on market benchmarks for similar solutions:

| Component | Estimated Cost | Frequency |
|-----------|----------------|-----------|
| QIO solver licensing | $50-200k | Annual |
| Initial integration | $100-300k | One-time |
| Maintenance and support | 15-20% of licensing | Annual |
| Cloud infrastructure | $5-20k | Monthly |

*Table 5: Cost estimate (market values, not specific to TDC Net).*

**Estimated payback**: Considering fuel savings (~15% of 100+ vehicle fleet) and productivity increase, return on investment may occur in 12-24 months for operations of comparable scale.

---

## 6. Comparison with Alternatives

### 6.1. Solution Landscape

| Solution | Type | Distinctive Advantage | Main Limitation |
|----------|------|----------------------|-----------------|
| Google OR-Tools | Open source | Zero cost, active community | Performance on large instances |
| Gurobi/CPLEX | Commercial solver | Optimality guarantee (MIP) | High licensing cost |
| D-Wave Leap | Quantum annealing | Native quantum hardware | Limited connectivity, noise |
| Azure Quantum | Multi-solver platform | Flexibility, Azure integration | Selection complexity |
| Fujitsu Digital Annealer | Specialized ASIC | Performance, deterministic | Proprietary, cost |

*Table 6: Comparison of combinatorial optimization solutions.*

### 6.2. When to Use QIO

Adoption of QIO solutions is recommended when:

- ✅ The problem has natural or easily mappable QUBO structure
- ✅ Traditional metaheuristics demonstrate stagnation in local minima
- ✅ Response time is critical (dynamic re-optimization)
- ✅ Scale justifies investment in licensing

And is **not** recommended when:

- ❌ The problem admits exact solution in acceptable time (branch-and-bound)
- ❌ Scale is small (< 50 variables) and simple heuristics suffice
- ❌ Budget constraints exist for specialized solver licensing

---

## 7. Applicability in Other Domains

### 7.1. Architectural Pattern Transfer

The QUBO + QIO framework is applicable to any problem modelable as binary quadratic optimization:

| Domain | Problem | QUBO Formulation |
|--------|---------|------------------|
| **Logistics** | Vehicle Routing | Coverage + distance |
| **Telecommunications** | Spectrum Allocation | Interference + capacity |
| **Finance** | Portfolio Optimization | Risk + return (Markowitz) |
| **Manufacturing** | Job Shop Scheduling | Precedence + makespan |
| **Energy** | Unit Commitment | Cost + demand |
| **Bioinformatics** | Protein Folding | Energy + conformation |

*Table 7: QUBO applicability across diverse domains.*

### 7.2. Example: Portfolio Optimization

The Markowitz problem for asset selection can be formulated as QUBO:

$$\min_{\mathbf{x}} \left[ \gamma \mathbf{x}^T \Sigma \mathbf{x} - \mu^T \mathbf{x} \right] + \lambda \left( \sum_i x_i - k \right)^2 \tag{3}$$

Where:
- $\Sigma$: return covariance matrix
- $\mu$: expected returns vector
- $\gamma$: risk aversion parameter
- $k$: number of assets to select

---

## 8. Adoption Roadmap

For organizations interested in replicating TDC Net's experience:

### Phase 1: Diagnosis (4-6 weeks)
- [ ] Map existing optimization problems
- [ ] Quantify current inefficiencies (baseline)
- [ ] Evaluate QUBO formulation viability
- [ ] Estimate potential ROI

### Phase 2: Proof of Concept (8-12 weeks)
- [ ] Select limited-scope pilot problem
- [ ] Implement QUBO formulation
- [ ] Test with multiple solvers (benchmarking)
- [ ] Validate results against baseline

### Phase 3: Operational Pilot (12-16 weeks)
- [ ] Integrate with existing systems (ERP/CRM)
- [ ] Execute in parallel with current solution (shadow mode)
- [ ] Collect performance metrics
- [ ] Train operational team

### Phase 4: Production (ongoing)
- [ ] Gradually migrate workload
- [ ] Establish continuous monitoring
- [ ] Iterate on formulation and hyperparameters
- [ ] Document lessons learned

---

## 9. Connection with Project Implementation

This case study served as motivation for the practical implementation developed in the project. The following artifacts were created as learning exercises:

| Artifact | Description | Location |
|----------|-------------|----------|
| `brute_force.py` | Exact O(n!) solver for validation | `programming/tsp_comparison/classical/` |
| `nearest_neighbor.py` | Greedy O(n²) heuristic | `programming/tsp_comparison/classical/` |
| `simulated_annealing.py` | Classical metaheuristic | `programming/tsp_comparison/classical/` |
| `qubo_solver.py` | Quantum-inspired solver | `programming/tsp_comparison/quantum_inspired/` |
| `graph_generator.py` | Test instance generator | `programming/tsp_comparison/utils/` |
| `visualizer.py` | Route and comparison visualization | `programming/tsp_comparison/utils/` |

*Table 8: Code artifacts related to the case study.*

Code available at: [github.com/igorconrado/quantum-computing-university-project](https://github.com/igorconrado/quantum-computing-university-project)

---

## 10. Conclusion

KPMG/TDC Net's Case 10 represents a milestone in the transition of quantum computing from laboratory to industrial applications. The critical analysis presented in this study demonstrates that:

1. **Promising but contextualized results**: Reported gains are significant but represent a pilot under controlled conditions. Extrapolation to other contexts requires specific validation.

2. **Quantum-inspired ≠ Quantum**: The solution uses quantum principles simulated classically, not native quantum hardware. This is both an advantage (immediate availability) and limitation (modest speedups vs. quantum potential).

3. **Value in modeling**: The main contribution lies not in the technology itself, but in the ability to model operational problems as QUBO formulations — a transferable skill independent of execution platform.

4. **Growing maturity**: The QIO solver ecosystem is rapidly evolving, with cost reduction and increased accessibility expected in coming years.

For technology professionals, the strategic lesson is clear: investing in mastery of **mathematical formulations** (QUBO, Ising, QAOA) positions one at the frontier between the current classical paradigm and the emerging quantum paradigm.

---

## References

Danish Quantum Use Cases. (2020). *Case 10: Optimised Route Planning with Quantum and AI*. KPMG / TDC Net. Accessed: Jan 15, 2025.

Farhi, E., Goldstone, J., & Gutmann, S. (2014). A quantum approximate optimization algorithm. *arXiv preprint arXiv:1411.4028*.

Glover, F., Kochenberger, G., & Du, Y. (2019). Quantum Bridge Analytics I: a tutorial on formulating and using QUBO models. *4OR*, 17(4), 335-371.

KPMG Quantum Hub. (2023). *Quantum Technology Services*. https://kpmg.com/quantum. Accessed: Jan 20, 2025.

Lucas, A. (2014). Ising formulations of many NP problems. *Frontiers in Physics*, 2, 5.

Toth, P., & Vigo, D. (Eds.). (2014). *Vehicle Routing: Problems, Methods, and Applications* (2nd ed.). SIAM.
