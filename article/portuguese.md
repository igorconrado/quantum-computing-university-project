# Do Lúdico ao Industrial: Uma Abordagem Baseada em Projetos para o Ensino de Engenharia de Software Quântica

## Resumo

Este trabalho apresenta um relato de experiência em Project-Based Learning (PBL) para o ensino de Engenharia de Software Quântica. A metodologia articula fundamentação teórica em mecânica quântica computacional com resolução de problemas NP-difíceis de relevância industrial, operando em dois eixos: (i) consolidação dos fundamentos através do currículo de Hughes et al. (2021) e implementação de artefatos interativos; e (ii) prototipagem de soluções para o Vehicle Routing Problem (VRP) via formulações QUBO. Os resultados evidenciam que a contraposição empírica entre algoritmos clássicos exatos e exploração heurística quantum-inspired constitui instrumento pedagógico eficaz para compreensão de classes de complexidade.

**Palavras-chave:** Engenharia de Software Quântica; Aprendizagem Baseada em Projetos; Otimização Combinatória; Formulação QUBO; Qiskit.

## Abstract

This paper presents a Project-Based Learning (PBL) experience report for teaching Quantum Software Engineering. The methodology combines theoretical foundations in computational quantum mechanics with solving industrially-relevant NP-hard problems, operating on two axes: (i) consolidating fundamentals through Hughes et al. (2021) curriculum and implementing interactive artifacts; and (ii) prototyping solutions for the Vehicle Routing Problem (VRP) via QUBO formulations. Results demonstrate that empirical comparison between exact classical algorithms and quantum-inspired heuristic exploration constitutes an effective pedagogical instrument for understanding complexity classes.

**Keywords:** Quantum Software Engineering; Project-Based Learning; Combinatorial Optimization; QUBO Formulation; Qiskit.

---

## 1. Introdução

A Computação Quântica atravessa um momento de inflexão paradigmática. O que durante décadas permaneceu confinado aos departamentos de física teórica — manipulação coerente de sistemas quânticos de dois níveis, exploração de superposição e emaranhamento para processamento de informação — emerge agora como tecnologia de engenharia aplicada. A demonstração de supremacia quântica pelo Google em 2019 (Arute et al., 2019), os avanços em correção de erros quânticos (Google Quantum AI, 2023) e a disponibilização de hardware via cloud (IBM Quantum, Amazon Braket) sinalizam a maturação da era NISQ (*Noisy Intermediate-Scale Quantum*).

Este cenário impõe um desafio pedagógico não trivial: como formar engenheiros de software capazes de transitar fluentemente entre o paradigma determinístico da lógica booleana e o paradigma probabilístico-interferométrico da computação quântica? A literatura aponta que abordagens puramente teóricas, centradas no formalismo de Dirac e na álgebra linear de espaços de Hilbert, frequentemente alienam estudantes de computação sem background em física (Seskir et al., 2022; Aiello et al., 2021).

### 1.1. Contribuições

O presente trabalho oferece as seguintes contribuições:

1. **Framework pedagógico**: Estruturação de percurso de aprendizado em dois épicos (fundamentação + aplicação industrial) com entregáveis concretos e mensuráveis.

2. **Artefato interativo**: Implementação do Quantum Pong como ferramenta de internalização do postulado da medição, disponível como recurso educacional aberto.

3. **Análise comparativa**: Implementação e benchmarking de algoritmos clássicos (força bruta, simulated annealing) e quantum-inspired (QUBO solver) para o TSP.

4. **Código aberto**: Disponibilização integral do código-fonte em repositório público: [github.com/igorconrado/quantum-computing-university-project](https://github.com/igorconrado/quantum-computing-university-project).

### 1.2. Organização do Artigo

O restante deste artigo está organizado como segue: a Seção 2 apresenta a fundamentação teórica; a Seção 3 descreve a metodologia; a Seção 4 detalha o desenvolvimento e resultados; a Seção 5 discute implicações e limitações; e a Seção 6 conclui o trabalho.

## 2. Fundamentação Teórica

### 2.1. Postulados da Mecânica Quântica Computacional

A computação quântica fundamenta-se em quatro postulados que governam a evolução e medição de sistemas quânticos (Nielsen & Chuang, 2010):

**Postulado 1 (Espaço de Estados):** O estado de um sistema quântico é descrito por um vetor unitário |ψ⟩ em um espaço de Hilbert ℋ de dimensão 2ⁿ para n qubits:

$$|\psi\rangle = \sum_{i=0}^{2^n-1} \alpha_i |i\rangle, \quad \sum_i |\alpha_i|^2 = 1 \tag{1}$$

**Postulado 2 (Evolução Unitária):** A evolução temporal de sistemas fechados é governada por operadores unitários U, onde U†U = I.

**Postulado 3 (Medição Projetiva):** A medição de um observable M com decomposição espectral M = Σₘ m Pₘ colapsa o estado |ψ⟩ para o autoespaço correspondente com probabilidade:

$$p(m) = \langle\psi|P_m|\psi\rangle \tag{2}$$

**Postulado 4 (Composição Tensorial):** O espaço de estados de um sistema composto é o produto tensorial dos espaços componentes: ℋ_AB = ℋ_A ⊗ ℋ_B.

O fenômeno do emaranhamento — impossibilidade de fatoração de certos estados compostos — emerge naturalmente do quarto postulado e constitui o recurso computacional distintivo da computação quântica.

### 2.2. Classes de Complexidade e Vantagem Quântica

O Traveling Salesman Problem (TSP) pertence à classe NP-difícil, implicando que, sob a conjectura P ≠ NP, não existe algoritmo polinomial para sua solução exata. A complexidade do algoritmo de força bruta é O(n!), tornando instâncias com n > 12 computacionalmente intratáveis em hardware convencional.

Algoritmos quânticos oferecem speedups para classes específicas de problemas:

- **Speedup exponencial**: Algoritmo de Shor para fatoração — BQP vs presumivelmente não-P (Shor, 1994)
- **Speedup quadrático**: Algoritmo de Grover para busca não estruturada — O(√N) vs O(N) (Grover, 1996)
- **Speedup via tunelamento**: Quantum annealing para otimização combinatória — heurístico (Kadowaki & Nishimori, 1998)

A formulação QUBO (Quadratic Unconstrained Binary Optimization) permite mapear problemas de otimização combinatória para Hamiltonianos Ising, compatíveis com arquiteturas de quantum annealing (Lucas, 2014).

### 2.3. Algoritmos Variacionais Híbridos

A era NISQ motivou o desenvolvimento de algoritmos variacionais híbridos clássico-quânticos, onde circuitos parametrizados são otimizados classicamente. O QAOA (Quantum Approximate Optimization Algorithm) é particularmente relevante para problemas combinatórios (Farhi et al., 2014):

$$|\gamma, \beta\rangle = \prod_{p=1}^{P} e^{-i\beta_p H_M} e^{-i\gamma_p H_C} |s\rangle \tag{3}$$

Onde H_C codifica a função de custo, H_M é o Hamiltoniano mixer, e os parâmetros (γ, β) são otimizados classicamente.

## 3. Metodologia

### 3.1. Design Pedagógico: Project-Based Learning

A abordagem pedagógica adotada fundamenta-se nos princípios de Project-Based Learning (Krajcik & Shin, 2014), estruturada em dois épicos de desenvolvimento com entregáveis concretos:

**Épico 1 — Fundamentação (8 semanas)**
- Estudo integral de Hughes et al. (2021), Capítulos 1-10
- Implementação de notebooks Jupyter para cada algoritmo canônico
- Desenvolvimento do artefato Quantum Pong como projeto integrador
- Resolução de exercícios teóricos e práticos do livro-texto

**Épico 2 — Aplicação Industrial (4 semanas)**
- Análise crítica do Case 10 (KPMG/TDC Net, 2020)
- Implementação comparativa: força bruta, nearest neighbor, simulated annealing, QUBO solver
- Documentação acadêmica e reflexão crítica

### 3.2. Stack Tecnológico

O desenvolvimento utilizou exclusivamente ferramentas open-source:

| Ferramenta | Versão | Finalidade |
|------------|--------|------------|
| Qiskit | 1.x | Framework para circuitos quânticos |
| Qiskit Aer | 0.14+ | Simulação statevector e QASM |
| NumPy/SciPy | 1.24+ | Computação numérica |
| Pygame | 2.5+ | Renderização do artefato interativo |
| Jupyter | 7.0+ | Documentação executável |
| Matplotlib | 3.8+ | Visualização de resultados |

*Tabela 1: Stack tecnológico utilizado no projeto.*

### 3.3. Métricas de Avaliação

Para avaliar a eficácia da abordagem, foram definidas métricas em três dimensões:

1. **Cobertura curricular**: Percentual de exercícios do livro-texto implementados
2. **Qualidade de código**: Aderência a padrões (PEP8, type hints, documentação)
3. **Performance algorítmica**: Tempo de execução e qualidade de solução para instâncias TSP

## 4. Desenvolvimento e Resultados

### 4.1. Quantum Pong: Gamificação como Instrumento Pedagógico

O artefato Quantum Pong foi concebido como materialização interativa do postulado da medição. A arquitetura do sistema implementa uma separação clara entre o backend quântico (classe `QuantumPaddle`) e o frontend de renderização (Pygame).

**Mecânica Central**: A raquete do jogador é representada por um registrador de 3 qubits, codificando 2³ = 8 posições discretas. O jogador manipula o estado através de portas quânticas:

| Porta | Efeito | Analogia Física |
|-------|--------|-----------------|
| Hadamard (H) | Superposição uniforme | Divisor de feixe 50/50 |
| Pauli-X | NOT quântico | Inversão de spin |
| Pauli-Z | Fase relativa π | Mudança de fase óptica |
| CNOT | Emaranhamento | Correlação EPR |

*Tabela 2: Portas quânticas disponíveis no Quantum Pong.*

A regra fundamental do jogo explicita o colapso da função de onda: *uma raquete em superposição não pode bloquear a bola*. Esta mecânica força o jogador a internalizar que a medição é irreversível e que o timing da observação é crítico.

**Circuito Quântico**: O estado inicial e a evolução podem ser representados como:

$$|\psi\rangle = H^{\otimes 3}|000\rangle = \frac{1}{\sqrt{8}} \sum_{i=0}^{7} |i\rangle \xrightarrow{\text{medição}} |k\rangle \tag{4}$$

Onde k ∈ {0, 1, ..., 7} é a posição colapsada com probabilidade uniforme 1/8.

### 4.2. Implementação dos Algoritmos Canônicos

#### 4.2.1. Algoritmo de Deutsch-Jozsa

Implementação do oráculo para funções f: {0,1}ⁿ → {0,1}, demonstrando speedup exponencial na determinação de funções constantes vs. balanceadas. A verificação empírica confirmou que uma única query ao oráculo quântico substitui as 2ⁿ⁻¹ + 1 queries necessárias classicamente (worst-case).

#### 4.2.2. Algoritmo de Grover

Implementação do operador de difusão e do oráculo de marcação para busca em espaços não estruturados:

$$D = 2|s\rangle\langle s| - I, \quad U_x = I - 2|x\rangle\langle x| \tag{5}$$

O número ótimo de iterações segue:

$$k_{opt} = \left\lfloor \frac{\pi}{4}\sqrt{N} \right\rfloor \tag{6}$$

Para N = 8 (3 qubits), observou-se convergência com k = 2 iterações, alcançando probabilidade de sucesso > 94%, conforme esperado teoricamente.

#### 4.2.3. Estados de Bell e Teletransporte

Implementação dos quatro estados de Bell:

$$|\Phi^{\pm}\rangle = \frac{1}{\sqrt{2}}(|00\rangle \pm |11\rangle), \quad |\Psi^{\pm}\rangle = \frac{1}{\sqrt{2}}(|01\rangle \pm |10\rangle) \tag{7}$$

O protocolo de teletransporte foi implementado integralmente, demonstrando a transferência de estados arbitrários |ψ⟩ = α|0⟩ + β|1⟩ através de 1 ebit compartilhado e 2 bits clássicos de comunicação.

### 4.3. Análise Comparativa: TSP Clássico vs. Quantum-Inspired

#### 4.3.1. Algoritmo de Força Bruta — O(n!)

A implementação exaustiva verificou todas as (n-1)!/2 rotas distintas (fixando origem e eliminando simetria). Resultados empíricos em CPU Intel i7-10750H:

| n (cidades) | Permutações | Tempo (s) | Memória (MB) |
|-------------|-------------|-----------|--------------|
| 5 | 12 | 0.001 | < 1 |
| 8 | 2,520 | 0.02 | < 1 |
| 10 | 181,440 | 1.8 | 2 |
| 12 | 19,958,400 | 187 | 15 |
| 13 | 239,500,800 | > 2000 | — |

*Tabela 3: Desempenho do algoritmo de força bruta para o TSP.*

A explosão fatorial confirma empiricamente a intratabilidade para n > 12 em hardware convencional.

#### 4.3.2. Nearest Neighbor — O(n²)

Implementação da heurística gulosa que, a cada passo, seleciona a cidade não visitada mais próxima:

| n (cidades) | Tempo (s) | Gap vs. Ótimo |
|-------------|-----------|---------------|
| 10 | 0.001 | 15-25% |
| 50 | 0.008 | 20-30% |
| 100 | 0.025 | 20-35% |

*Tabela 4: Desempenho do algoritmo Nearest Neighbor.*

#### 4.3.3. Simulated Annealing — Metaheurística Clássica

Implementação do algoritmo SA com schedule de temperatura exponencial:

$$T(k) = T_0 \cdot \alpha^k, \quad \alpha \in (0.95, 0.999) \tag{8}$$

A probabilidade de aceitação de soluções piores segue a distribuição de Boltzmann:

$$P(\Delta E) = \exp\left(-\frac{\Delta E}{k_B T}\right) \tag{9}$$

Resultados demonstraram convergência para soluções de alta qualidade (gap < 5% do ótimo conhecido) em tempo polinomial.

#### 4.3.4. QUBO Solver — Otimização Quantum-Inspired

A formulação QUBO para TSP utiliza variáveis binárias x_{ip} ∈ {0,1} indicando se a cidade i é visitada na posição p. O Hamiltoniano de custo assume a forma:

$$H = A\sum_i\left(1 - \sum_p x_{ip}\right)^2 + A\sum_p\left(1 - \sum_i x_{ip}\right)^2 + B\sum_{i,j,p} d_{ij} x_{ip} x_{j,p+1} \tag{10}$$

Os dois primeiros termos são penalidades de constraint; o terceiro codifica a função objetivo.

### 4.4. Síntese Comparativa

| Algoritmo | Complexidade | Garantia de Ótimo | Escalabilidade Prática |
|-----------|--------------|-------------------|------------------------|
| Força Bruta | O(n!) | Sim | n ≤ 12 |
| Nearest Neighbor | O(n²) | Não | n ≤ 10⁵ |
| Simulated Annealing | O(k·n²) | Não | n ≤ 10⁴ |
| QUBO (simulado) | O(k·n²) | Não | n ≤ 10³ |
| QUBO (quantum annealer) | O(√N)* | Não | Limitado por conectividade |

*Tabela 5: Comparativo de algoritmos para o TSP. *Speedup teórico.*

## 5. Discussão

### 5.1. Eficácia da Abordagem PBL

A experiência relatada valida a hipótese de que o confronto empírico com limitações computacionais clássicas constitui motivação pedagógica superior à exposição teórica abstrata. A observação direta do crescimento fatorial — ver o computador "travar" ao adicionar uma única cidade — produz compreensão intuitiva que nenhuma demonstração matemática substitui.

O artefato Quantum Pong demonstrou-se particularmente eficaz na internalização do postulado da medição. A mecânica de "perder pontos" por medir no momento errado transforma-se gradualmente em intuição sobre o timing de observação — habilidade transferível para o design de algoritmos quânticos reais.

### 5.2. Cobertura Curricular Alcançada

| Componente | Status | Artefatos |
|------------|--------|-----------|
| Capítulos 1-8 (teoria) | 100% | Anotações, exercícios |
| Capítulo 9 (algoritmos) | 100% | 4 notebooks + soluções |
| Capítulo 10 (aplicações) | 100% | 5 notebooks + soluções |
| Projeto integrador | 100% | Quantum Pong |
| Case industrial | 100% | TSP comparison suite |

*Tabela 6: Cobertura do currículo Hughes et al. (2021).*

### 5.3. Limitações

O presente trabalho apresenta limitações que devem ser reconhecidas:

1. **Amostra unitária**: Trata-se de relato de experiência individual, sem grupo de controle para validação estatística da eficácia pedagógica.

2. **Simulação clássica**: Todas as implementações quânticas foram executadas em simuladores, não em hardware quântico real. Os efeitos de ruído e decoerência não foram experimentados diretamente.

3. **Escala limitada**: O QUBO solver foi testado apenas em instâncias pequenas (n ≤ 15), insuficientes para demonstrar vantagem sobre metaheurísticas clássicas otimizadas.

4. **Ausência de QAOA**: Embora discutido teoricamente, o algoritmo QAOA não foi implementado devido a limitações de tempo.

### 5.4. Trabalhos Futuros

Extensões naturais deste trabalho incluem:

1. **Hardware real**: Execução em dispositivos IBM Quantum e análise de efeitos de ruído
2. **QAOA**: Implementação completa para o TSP com otimização variacional
3. **VRP completo**: Extensão para constraints de capacidade e janelas de tempo
4. **Validação pedagógica**: Aplicação em turmas com avaliação sistemática de aprendizado

### 5.5. Implicações para Formação em QSE

A experiência sugere que o engenheiro de software quântico deve desenvolver competência em três domínios:

1. **Intuição quântica**: Compreensão visceral de superposição, emaranhamento e medição
2. **Modelagem matemática**: Tradução de problemas para formulações compatíveis com hardware quântico
3. **Engenharia de software**: Domínio de frameworks (Qiskit, Cirq, PennyLane) e práticas de integração

## 6. Conclusão

Este trabalho apresentou um relato de experiência em aprendizado autodirigido de Engenharia de Software Quântica, estruturado em torno de Project-Based Learning. A combinação de fundamentação teórica rigorosa, implementação de artefatos interativos e análise de problemas industriais demonstrou-se pedagogicamente eficaz para a construção de competências em QSE.

A contribuição principal reside na validação empírica de que a experiência direta do "gargalo clássico" constitui motivação superior para o estudo de alternativas quânticas. O código desenvolvido encontra-se disponível como recurso educacional aberto em [github.com/igorconrado/quantum-computing-university-project](https://github.com/igorconrado/quantum-computing-university-project).

A computação quântica transita inexoravelmente do laboratório para a indústria. Formar engenheiros capazes de navegar esta transição exige abordagens pedagógicas que transcendam o formalismo matemático abstrato, ancorando o aprendizado em problemas concretos e experiências tangíveis.

---

## Referências Bibliográficas

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
