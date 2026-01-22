# Quantum Computing University Project

Projeto acadêmico: Estudo de Computação Quântica com foco em casos de uso, programação com Qiskit e desenvolvimento de artigos para publicação em congressos da SBC.

## Estrutura do Projeto

```
quantum-computing-university-project/
│
├── article/                    # Artigo para congressos SBC
│   └── portuguese.md           # Versão em português
│
├── case_study/                 # Estudo de caso (Grupo de Estudos)
│   └── portuguese.md           # Case 10: KPMG/TDC Net - Otimização de Rotas
│
└── programming/                # Parte prática (Qiskit)
    ├── setup-guide.md          # Guia de instalação
    ├── requirements.txt        # Dependências Python
    │
    ├── exercises/              # Exercícios do livro
    │   ├── chapter_09/         # Algoritmos quânticos
    │   └── chapter_10/         # Worksheets práticos
    │
    ├── quantum_pong/           # Jogo Quantum Pong
    │
    └── tsp_comparison/         # Comparação TSP clássico vs quântico
        ├── classical/          # Algoritmos clássicos
        ├── quantum_inspired/   # Abordagem QUBO
        ├── benchmarks/         # Comparações
        ├── utils/              # Utilitários
        └── data/               # Dados de teste
```

## Quick Start

```bash
# 1. Criar ambiente
conda create -n qiskit_env python=3.11
conda activate qiskit_env

# 2. Instalar dependências
pip install -r programming/requirements.txt

# 3. Iniciar Jupyter
jupyter notebook
```

## Componentes do Trabalho

### 1. Grupo de Estudos
- **Tema:** Case 10 - Optimised Route Planning (KPMG/TDC Net)
- **Foco:** VRP (Vehicle Routing Problem) e TSP
- **Documentação:** [case_study/portuguese.md](case_study/portuguese.md)

### 2. Programação
- **Base teórica:** Capítulos 9 e 10 - *Quantum Computing for the Quantum Curious*
- **Vídeos:** [Programming on Quantum Computers](https://www.youtube.com/playlist?list=PLeKiDAn3TQtz_HDE_iwVGHUZAgG-AfxGO)
- **Projeto prático:** Quantum Pong

### 3. Trabalho Final
- **Artigo:** [article/portuguese.md](article/portuguese.md)
- **Destino:** Congressos da SBC (Sociedade Brasileira de Computação)

## Referências

- Hughes, C. et al. (2021). *Quantum Computing for the Quantum Curious*. Springer.
- [16 Danish Quantum Use Cases](https://www.oqi.dk/files/pdf/Digitalt-brochure-enkelt.pdf)
- [Qiskit Documentation](https://qiskit.org/documentation/)
- [IBM Quantum Platform](https://quantum.ibm.com/)

## Recursos Úteis

- [TSP Game (interativo)](https://algorithms.discrete.ma.tum.de/graph-games/tsp-game/index_en.html)
- [Simulated Annealing Visualization](https://www.fourmilab.ch/documents/travelling/anneal/)
- [KPMG Quantum Hub](https://kpmg.com/xx/en/home/services/advisory/management-consulting/technology-consulting/quantum-technology.html)
