# Capítulo 10 - Worksheets & Practice

## Conteúdo do Capítulo

O capítulo 10 contém exercícios práticos (worksheets) para consolidar os conceitos:

- Manipulação de qubits
- Portas quânticas (X, Y, Z, H, CNOT, etc.)
- Medições e probabilidades
- Circuitos multi-qubit
- Emaranhamento (Bell States)

## Exercícios para Implementar

### 1. `single_qubit_gates.ipynb`
Praticar todas as portas de um qubit e visualizar na Bloch Sphere.

### 2. `multi_qubit_circuits.ipynb`
Construir circuitos com múltiplos qubits e portas controladas.

### 3. `bell_states.ipynb`
Criar e medir os 4 estados de Bell (emaranhamento).

### 4. `quantum_teleportation.ipynb`
Implementar o protocolo de teletransporte quântico.

## Dicas

```python
# Visualizar circuito
circuit.draw('mpl')

# Visualizar Bloch Sphere
from qiskit.visualization import plot_bloch_multivector
plot_bloch_multivector(statevector)

# Simular circuito
from qiskit_aer import AerSimulator
simulator = AerSimulator()
result = simulator.run(circuit).result()
```

## Referências

- Livro: Capítulo 10, Worksheets 1-5
- [Qiskit Textbook - Single Qubit Gates](https://qiskit.org/textbook/ch-states/single-qubit-gates.html)
