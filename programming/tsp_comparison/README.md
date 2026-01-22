# TSP Comparison - Classical vs Quantum-Inspired

Comparação entre algoritmos clássicos e quânticos para o Traveling Salesperson Problem (TSP).

## Objetivo

Demonstrar na prática o "gargalo clássico" mencionado no estudo de caso KPMG/TDC Net:
- Implementar força bruta (O(n!)) e ver o tempo explodir
- Implementar heurísticas clássicas (Nearest Neighbor, Simulated Annealing)
- Comparar com abordagem QUBO/quantum-inspired

## Estrutura Sugerida

```
tsp_comparison/
├── README.md                # Este arquivo
├── classical/
│   ├── brute_force.py       # Força bruta O(n!)
│   ├── nearest_neighbor.py  # Heurística gulosa
│   └── simulated_annealing.py
├── quantum_inspired/
│   └── qubo_solver.py       # Formulação QUBO
├── utils/
│   ├── graph_generator.py   # Gerar grafos de teste
│   └── visualizer.py        # Plotar rotas
├── benchmarks/
│   └── comparison.ipynb     # Notebook comparando todos
└── data/
    └── cities.json          # Dados de teste
```

## Arquivos para Implementar

### 1. `classical/brute_force.py`

```python
# Estrutura sugerida
from itertools import permutations
import time

def tsp_brute_force(distance_matrix: list) -> tuple:
    """
    Resolve TSP por força bruta.
    Returns: (best_route, best_distance, execution_time)
    """
    # Testar todas as permutações
    # Retornar a melhor rota
    pass

# Teste com 5, 6, 7, 8, 9, 10 cidades
# Observe o tempo crescer fatorialmente!
```

### 2. `classical/simulated_annealing.py`

Implementar Simulated Annealing para comparar com força bruta.

### 3. `quantum_inspired/qubo_solver.py`

Formular o TSP como problema QUBO (Quadratic Unconstrained Binary Optimization).

### 4. `benchmarks/comparison.ipynb`

Notebook que:
- Gera grafos de diferentes tamanhos
- Executa cada algoritmo
- Plota gráficos de tempo vs número de cidades
- Compara qualidade das soluções

## Recursos

- [TSP Game (interativo)](https://algorithms.discrete.ma.tum.de/graph-games/tsp-game/index_en.html)
- [Simulated Annealing TSP](https://www.fourmilab.ch/documents/travelling/anneal/)
- [Qiskit Optimization - TSP](https://qiskit-community.github.io/qiskit-optimization/tutorials/06_examples_max_cut_and_tsp.html)
- [D-Wave TSP Tutorial](https://docs.ocean.dwavesys.com/en/stable/examples/tsp.html)

## Dados de Teste

O arquivo `data/cities.json` deve conter coordenadas de cidades para teste:

```json
{
  "small": {
    "cities": ["A", "B", "C", "D", "E"],
    "coordinates": [[0,0], [1,5], [5,2], [6,6], [8,3]]
  },
  "medium": {
    "cities": ["...10 cidades..."],
    "coordinates": ["..."]
  }
}
```

## Executar

```bash
conda activate qiskit_env

# Testar força bruta
python classical/brute_force.py

# Rodar comparação completa
jupyter notebook benchmarks/comparison.ipynb
```
