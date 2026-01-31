# Quantum Pong

Jogo Pong com mecânicas quânticas, baseado na série [Programming on Quantum Computers](https://www.youtube.com/playlist?list=PLeKiDAn3TQtz_HDE_iwVGHUZAgG-AfxGO).

## Conceito

O Quantum Pong usa princípios de computação quântica para controlar a raquete do jogador:

- **Superposição:** A raquete pode estar em múltiplas posições simultaneamente (8 posições possíveis com 3 qubits)
- **Medição:** Ao medir o estado quântico, a posição da raquete é definida
- **Portas Quânticas:** O jogador usa portas (H, X, Z, CNOT) para manipular o estado

### Mecânica de Jogo

1. A raquete quântica começa no estado |000⟩ (posição 0, topo da tela)
2. Aplique a porta Hadamard (H) para criar superposição em todas as 8 posições
3. **Importante:** Uma raquete em superposição NÃO pode bloquear a bola!
4. Pressione SPACE para medir (colapsar) a posição quando a bola se aproximar
5. A posição medida é determinada pelas probabilidades quânticas

## Estrutura

```
quantum_pong/
├── README.md           # Este arquivo
├── main.py             # Entry point
├── game.py             # Loop principal do jogo (Pygame)
└── quantum_paddle.py   # Lógica quântica da raquete (Qiskit)
```

## Controles

| Tecla | Ação | Descrição |
|-------|------|-----------|
| H | Hadamard | Cria superposição (distribui probabilidade igualmente) |
| X | NOT | Inverte o primeiro qubit |
| Z | Phase | Aplica mudança de fase |
| C | CNOT | Entrelaça qubits (controle-alvo) |
| R | Reset | Retorna ao estado |000⟩ |
| SPACE | Medir | Colapsa a superposição para posição definida |
| P | Pause | Pausa/continua o jogo |
| ESC | Sair | Fecha o jogo |

## Executar

```bash
# 1. Ativar ambiente
conda activate qiskit_env

# 2. Instalar dependências (se necessário)
pip install pygame qiskit qiskit-aer

# 3. Rodar o jogo
cd programming/quantum_pong
python main.py
```

## Conceitos Quânticos Demonstrados

### Superposição
Com 3 qubits, a raquete pode estar em 2³ = 8 posições simultaneamente. Após aplicar H em todos os qubits:
```
|ψ⟩ = 1/√8 (|000⟩ + |001⟩ + |010⟩ + ... + |111⟩)
```

### Medição
A medição "colapsa" o estado quântico. A probabilidade de cada posição depende do estado atual do circuito.

### Portas Quânticas
- **Hadamard (H):** Cria superposição balanceada
- **Pauli-X:** Equivalente ao NOT clássico
- **Pauli-Z:** Muda a fase (afeta interferência)
- **CNOT:** Entrelaça dois qubits

## Visualização

A raquete quântica mostra:
- **Segmentos coloridos:** Intensidade indica probabilidade de cada posição
- **Retângulo azul:** Posição medida (quando colapsado)
- **Indicador de estado:** Mostra se está em SUPERPOSITION ou POSITION: N

## Recursos

- [Vídeo: Quantum Pong](https://www.youtube.com/watch?v=P5cGeDKOIP0) (playlist)
- [Pygame Documentation](https://www.pygame.org/docs/)
- [Qiskit Documentation](https://qiskit.org/documentation/)

## Extensões Possíveis

- Visualização da Bloch Sphere em tempo real
- Modo tutorial explicando cada porta
- Multiplayer: jogador clássico vs jogador quântico
- Níveis de dificuldade (velocidade da bola, IA do oponente)
