# Quantum Pong

Jogo Pong com mecânicas quânticas, baseado na série [Programming on Quantum Computers](https://www.youtube.com/playlist?list=PLeKiDAn3TQtz_HDE_iwVGHUZAgG-AfxGO).

## Conceito

O Quantum Pong usa princípios de computação quântica para controlar elementos do jogo:

- **Superposição:** A raquete pode estar em múltiplas posições simultaneamente
- **Medição:** Ao medir o estado quântico, a posição da raquete é definida
- **Portas Quânticas:** O jogador usa portas (H, X, etc.) para manipular o estado

## Estrutura Sugerida

```
quantum_pong/
├── README.md           # Este arquivo
├── game.py             # Loop principal do jogo (Pygame)
├── quantum_paddle.py   # Lógica quântica da raquete
├── renderer.py         # Renderização visual
└── main.py             # Entry point
```

## Arquivos para Implementar

### 1. `quantum_paddle.py`
Classe que gerencia o estado quântico da raquete.

```python
# Estrutura sugerida
class QuantumPaddle:
    def __init__(self, num_qubits: int):
        # Inicializar circuito quântico
        pass

    def apply_gate(self, gate: str):
        # Aplicar porta (H, X, Y, Z)
        pass

    def measure(self) -> int:
        # Medir e retornar posição
        pass

    def get_probabilities(self) -> list:
        # Retornar probabilidades de cada posição
        pass
```

### 2. `game.py`
Loop principal usando Pygame.

### 3. `main.py`
Entry point que inicializa e roda o jogo.

## Recursos

- [Vídeo: Quantum Pong](https://www.youtube.com/watch?v=a1NZC5rqQD8) (da playlist)
- [Pygame Documentation](https://www.pygame.org/docs/)
- [Qiskit Visualization](https://qiskit.org/documentation/apidoc/visualization.html)

## Executar

```bash
conda activate qiskit_env
pip install pygame
python main.py
```

## Extensões Possíveis (Minicurso Ensino Médio)

- Visualização da Bloch Sphere em tempo real
- Modo tutorial explicando cada porta
- Multiplayer: um jogador clássico vs jogador quântico
