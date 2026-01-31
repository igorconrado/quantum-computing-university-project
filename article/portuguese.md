# Do Lúdico ao Industrial: Uma Abordagem Baseada em Projetos para o Ensino de Engenharia de Software Quântica

## Resumo

A transição da computação quântica do domínio teórico para aplicações industriais concretas impõe uma reformulação urgente na formação de engenheiros de software. Este trabalho apresenta um relato de experiência estruturado em Project-Based Learning (PBL), articulando a fundamentação teórica em mecânica quântica computacional com a resolução de problemas NP-difíceis de relevância industrial. A metodologia proposta opera em dois eixos complementares: (i) consolidação dos fundamentos através do currículo de Hughes et al. (2021) e implementação de artefatos interativos (Quantum Pong) para internalização dos postulados da medição quântica; e (ii) análise crítica e prototipagem de soluções para o Vehicle Routing Problem (VRP), tomando como referência o Case 10 do consórcio KPMG/TDC Net. Os resultados evidenciam que a contraposição empírica entre a explosão combinatória de algoritmos clássicos exatos e a exploração heurística via formulações QUBO constitui um instrumento pedagógico eficaz para a compreensão intuitiva de classes de complexidade e do potencial de speedup quântico.

**Palavras-chave:** Engenharia de Software Quântica; Aprendizagem Baseada em Projetos; Otimização Combinatória; Formulação QUBO; Qiskit.

---

## 1. Introdução

A Computação Quântica atravessa um momento de inflexão paradigmática. O que durante décadas permaneceu confinado aos departamentos de física teórica — manipulação coerente de sistemas quânticos de dois níveis, exploração de superposição e emaranhamento para processamento de informação — emerge agora como tecnologia de engenharia aplicada. A demonstração de supremacia quântica pelo Google em 2019 (Arute et al., 2019) e os subsequentes avanços em correção de erros quânticos sinalizam a proximidade da era NISQ (*Noisy Intermediate-Scale Quantum*) com aplicabilidade industrial.

Este cenário impõe um desafio pedagógico não trivial: como formar engenheiros de software capazes de transitar fluentemente entre o paradigma determinístico da lógica booleana e o paradigma probabilístico-interferométrico da computação quântica? A literatura aponta que abordagens puramente teóricas, centradas no formalismo de Dirac e na álgebra linear de espaços de Hilbert, frequentemente alienam estudantes de computação sem background em física (Seskir et al., 2022).

O presente trabalho relata uma experiência de aprendizado autodirigido estruturada em torno de dois objetivos complementares:

1. **Fundamentação teórico-prática**: Domínio integral do currículo proposto por Hughes et al. (2021) em *Quantum Computing for the Quantum Curious*, com ênfase na implementação computacional dos algoritmos canônicos (Deutsch-Jozsa, Grover, protocolos de teletransporte);

2. **Aplicação industrial**: Análise crítica do Case 10 do programa Danish Quantum Use Cases (KPMG/TDC Net, 2020), com prototipagem de solvers clássicos e quantum-inspired para o Traveling Salesman Problem (TSP).

A hipótese subjacente é que a experiência visceral do "gargalo clássico" — observar empiricamente a explosão fatorial do tempo de execução — constitui motivação pedagógica superior à mera exposição teórica de classes de complexidade.

## 2. Fundamentação Teórica

### 2.1. Postulados da Mecânica Quântica Computacional

A computação quântica fundamenta-se em quatro postulados que governam a evolução e medição de sistemas quânticos (Nielsen & Chuang, 2010):

1. **Espaço de estados**: O estado de um sistema quântico é descrito por um vetor unitário |ψ⟩ em um espaço de Hilbert ℋ de dimensão 2ⁿ para n qubits.

2. **Evolução unitária**: A evolução temporal de sistemas fechados é governada por operadores unitários U, onde U†U = I.

3. **Medição projetiva**: A medição de um observable M com decomposição espectral M = Σₘ m Pₘ colapsa o estado |ψ⟩ para o autoespaço correspondente com probabilidade p(m) = ⟨ψ|Pₘ|ψ⟩.

4. **Composição tensorial**: O espaço de estados de um sistema composto é o produto tensorial dos espaços componentes: ℋ_AB = ℋ_A ⊗ ℋ_B.

O fenômeno do emaranhamento — impossibilidade de fatoração de certos estados compostos — emerge naturalmente do quarto postulado e constitui o recurso computacional distintivo da computação quântica.

### 2.2. Classes de Complexidade e Vantagem Quântica

O TSP pertence à classe NP-difícil, implicando que, sob a conjectura P ≠ NP, não existe algoritmo polinomial para sua solução exata. A complexidade do algoritmo de força bruta é O(n!), tornando instâncias com n > 12 computacionalmente intratáveis em hardware convencional.

Algoritmos quânticos oferecem speedups para classes específicas de problemas:
- **Speedup exponencial**: Algoritmo de Shor para fatoração (BQP vs presumivelmente não-P)
- **Speedup quadrático**: Algoritmo de Grover para busca não estruturada (O(√N) vs O(N))
- **Speedup via tunelamento**: Quantum annealing para otimização combinatória (heurístico)

A formulação QUBO permite mapear problemas de otimização combinatória para Hamiltonianos Ising, compatíveis com arquiteturas de quantum annealing (Lucas, 2014).

## 3. Metodologia

### 3.1. Design Pedagógico: Project-Based Learning

A abordagem pedagógica adotada fundamenta-se nos princípios de Project-Based Learning (Krajcik & Shin, 2014), estruturada em dois épicos de desenvolvimento com entregáveis concretos:

**Épico 1 — Fundamentação (8 semanas)**
- Estudo integral de Hughes et al. (2021), Capítulos 1-10
- Implementação de notebooks Jupyter para cada algoritmo canônico
- Desenvolvimento do artefato Quantum Pong como projeto integrador

**Épico 2 — Aplicação Industrial (4 semanas)**
- Análise crítica do Case 10 (KPMG/TDC Net)
- Implementação comparativa: força bruta, simulated annealing, QUBO solver
- Documentação e reflexão crítica

### 3.2. Stack Tecnológico

O desenvolvimento utilizou exclusivamente ferramentas open-source:
- **Qiskit 1.x** (IBM): Framework para construção e simulação de circuitos quânticos
- **Qiskit Aer**: Backend de simulação statevector e QASM
- **NumPy/SciPy**: Computação numérica e álgebra linear
- **Pygame**: Renderização do artefato interativo
- **Jupyter Notebooks**: Documentação executável dos algoritmos

## 4. Desenvolvimento e Resultados

### 4.1. Quantum Pong: Gamificação como Instrumento Pedagógico

O artefato Quantum Pong foi concebido como materialização interativa do postulado da medição. A arquitetura do sistema implementa uma separação clara entre o backend quântico (classe `QuantumPaddle`) e o frontend de renderização (Pygame).

**Mecânica Central**: A raquete do jogador é representada por um registrador de 3 qubits, codificando 2³ = 8 posições discretas. O jogador manipula o estado através de portas quânticas:

- **Hadamard (H)**: Induz superposição uniforme, distribuindo amplitude igualmente entre todas as posições
- **Pauli-X**: Operação NOT quântica, inversão de amplitude
- **Pauli-Z**: Introdução de fase relativa π
- **CNOT**: Emaranhamento entre qubits do registrador

A regra fundamental do jogo explicita o colapso da função de onda: *uma raquete em superposição não pode bloquear a bola*. Esta mecânica força o jogador a internalizar que a medição é irreversível e que o timing da observação é crítico — análogo direto ao problema de decoerência em sistemas quânticos reais.

**Implementação Técnica**: O circuito quântico é mantido em memória e atualizado a cada aplicação de porta. A medição é realizada via simulação statevector, com amostragem probabilística das posições. Após medição, o circuito é reinicializado no estado clássico correspondente.

```
|ψ⟩ = H⊗³|000⟩ = (1/√8) Σᵢ |i⟩   (superposição uniforme)
       ↓ MEDIÇÃO
|ψ'⟩ = |k⟩                        (colapso para posição k)
```

### 4.2. Implementação dos Algoritmos Canônicos

#### 4.2.1. Algoritmo de Deutsch-Jozsa

Implementação do oráculo para funções f: {0,1}ⁿ → {0,1}, demonstrando speedup exponencial na determinação de funções constantes vs. balanceadas. A verificação empírica confirmou que uma única query ao oráculo quântico substitui as 2ⁿ⁻¹ + 1 queries necessárias classicamente (caso worst-case).

#### 4.2.2. Algoritmo de Grover

Implementação do operador de difusão D = 2|s⟩⟨s| - I e do oráculo de marcação Uₓ = I - 2|x⟩⟨x| para busca em espaços não estruturados. Verificação experimental do número ótimo de iterações:

$$k_{opt} = \lfloor \frac{\pi}{4}\sqrt{N} \rfloor$$

Para N = 8 (3 qubits), observou-se convergência com k = 2 iterações, alcançando probabilidade de sucesso > 94%.

#### 4.2.3. Estados de Bell e Teletransporte

Implementação dos quatro estados de Bell e verificação das correlações EPR. O protocolo de teletransporte foi implementado integralmente, demonstrando a transferência de estados arbitrários |ψ⟩ = α|0⟩ + β|1⟩ através de 1 ebit compartilhado e 2 bits clássicos de comunicação.

### 4.3. Análise Comparativa: TSP Clássico vs. Quantum-Inspired

#### 4.3.1. Algoritmo de Força Bruta — O(n!)

A implementação exaustiva verificou todas as (n-1)!/2 rotas distintas (fixando origem e eliminando simetria). Resultados empíricos:

| n (cidades) | Permutações | Tempo (s) |
|-------------|-------------|-----------|
| 5 | 12 | 0.001 |
| 8 | 2,520 | 0.02 |
| 10 | 181,440 | 1.8 |
| 12 | 19,958,400 | ~180 |

A explosão fatorial confirma empiricamente a intratabilidade para n > 12 em hardware convencional.

#### 4.3.2. Simulated Annealing — Metaheurística Clássica

Implementação do algoritmo SA com schedule de temperatura exponencial:

$$T(k) = T_0 \cdot \alpha^k, \quad \alpha \in (0,1)$$

A probabilidade de aceitação de soluções piores segue a distribuição de Boltzmann:

$$P(\Delta E) = \exp\left(-\frac{\Delta E}{k_B T}\right)$$

Resultados demonstraram convergência para soluções de qualidade aceitável (< 5% do ótimo) em tempo polinomial, validando a eficácia de metaheurísticas para instâncias industriais.

#### 4.3.3. QUBO Solver — Otimização Quantum-Inspired

A formulação QUBO para TSP utiliza variáveis binárias xᵢₚ ∈ {0,1} indicando se a cidade i é visitada na posição p da rota. O Hamiltoniano de custo assume a forma:

$$H = A\sum_i\left(1 - \sum_p x_{ip}\right)^2 + A\sum_p\left(1 - \sum_i x_{ip}\right)^2 + B\sum_{i,j,p} d_{ij} x_{ip} x_{j,p+1}$$

Os dois primeiros termos são penalidades de constraint (cada cidade visitada exatamente uma vez, cada posição ocupada por exatamente uma cidade). O terceiro termo codifica a função objetivo (minimização da distância total).

O solver implementado utiliza técnicas de *simulated quantum annealing*, onde a probabilidade de transição entre estados simula o tunelamento quântico através de barreiras de energia, permitindo escape de mínimos locais inacessíveis ao simulated annealing clássico.

### 4.4. Síntese Comparativa

| Algoritmo | Complexidade | Garantia de Ótimo | Escalabilidade |
|-----------|--------------|-------------------|----------------|
| Força Bruta | O(n!) | Sim | n ≤ 12 |
| Simulated Annealing | O(k·n²) | Não | n ≤ 10⁴ |
| QUBO (clássico) | O(k·n²) | Não | n ≤ 10³ |
| QUBO (quantum annealer) | O(√N)* | Não | Limitado por conectividade |

*Speedup teórico; implementação atual é simulação clássica.

## 5. Discussão

### 5.1. Eficácia da Abordagem PBL

A experiência relatada valida a hipótese de que o confronto empírico com limitações computacionais clássicas constitui motivação pedagógica superior à exposição teórica abstrata. A observação direta do crescimento fatorial — ver o computador "travar" ao adicionar uma única cidade — produz compreensão intuitiva que nenhuma demonstração matemática substitui.

O artefato Quantum Pong demonstrou-se particularmente eficaz na internalização do postulado da medição. A frustração inicial de "perder pontos" por medir no momento errado transforma-se gradualmente em intuição sobre o timing de observação — habilidade transferível para o design de algoritmos quânticos reais.

### 5.2. Limitações e Trabalhos Futuros

O presente trabalho apresenta limitações metodológicas que devem ser reconhecidas:

1. **Amostra unitária**: Trata-se de relato de experiência individual, sem grupo de controle para validação estatística da eficácia pedagógica.

2. **Simulação clássica**: Todas as implementações quânticas foram executadas em simuladores, não em hardware quântico real. Os efeitos de ruído e decoerência não foram experimentados.

3. **Escala limitada**: O QUBO solver foi testado apenas em instâncias pequenas (n ≤ 15), insuficientes para demonstrar vantagem sobre metaheurísticas clássicas otimizadas.

Trabalhos futuros incluem: (i) execução em hardware quântico real via IBM Quantum Experience; (ii) implementação de algoritmos variacionais (QAOA) para o TSP; (iii) extensão para o VRP completo com constraints de capacidade e janelas de tempo.

### 5.3. Implicações para a Formação em QSE

A experiência sugere que o engenheiro de software quântico não necessita tornar-se físico teórico, mas deve desenvolver competência em três domínios:

1. **Intuição quântica**: Compreensão visceral de superposição, emaranhamento e medição — melhor desenvolvida através de artefatos interativos que simulações estáticas.

2. **Modelagem matemática**: Capacidade de traduzir problemas de domínio para formulações compatíveis com hardware quântico (QUBO, Hamiltonianos Ising).

3. **Engenharia de software**: Domínio de frameworks (Qiskit, Cirq, PennyLane), práticas de teste e integração com sistemas clássicos.

## 6. Conclusão

Este trabalho apresentou um relato de experiência em aprendizado autodirigido de Engenharia de Software Quântica, estruturado em torno de Project-Based Learning. A combinação de fundamentação teórica rigorosa (Hughes et al., 2021), implementação de artefatos interativos (Quantum Pong) e análise de problemas industriais (Case 10 KPMG) demonstrou-se pedagogicamente eficaz para a construção de competências em QSE.

A contribuição principal reside na validação empírica de que a experiência direta do "gargalo clássico" — observar a intratabilidade de algoritmos exatos para problemas NP-difíceis — constitui motivação superior para o estudo de alternativas quânticas. O código desenvolvido encontra-se disponível como recurso educacional aberto, podendo servir como template para iniciativas similares.

A computação quântica transita inexoravelmente do laboratório para a indústria. Formar engenheiros capazes de navegar esta transição exige abordagens pedagógicas que transcendam o formalismo matemático abstrato, ancorando o aprendizado em problemas concretos e experiências tangíveis. O presente trabalho oferece uma contribuição modesta, porém empiricamente validada, nesta direção.

---

## Referências Bibliográficas

Arute, F., et al. (2019). Quantum supremacy using a programmable superconducting processor. *Nature*, 574(7779), 505-510.

Danish Quantum Use Cases. (2020). *Case 10: Optimised Route Planning with Quantum and AI*. KPMG / TDC Net.

Hughes, C., Isaacson, J., Perry, A., Sun, R. F., & Turner, J. (2021). *Quantum Computing for the Quantum Curious*. Springer.

Krajcik, J. S., & Shin, N. (2014). Project-based learning. In R. K. Sawyer (Ed.), *The Cambridge Handbook of the Learning Sciences* (pp. 275-297). Cambridge University Press.

Lucas, A. (2014). Ising formulations of many NP problems. *Frontiers in Physics*, 2, 5.

Nielsen, M. A., & Chuang, I. L. (2010). *Quantum Computation and Quantum Information: 10th Anniversary Edition*. Cambridge University Press.

Seskir, Z. C., et al. (2022). Quantum games and interactive tools for quantum technologies outreach and education. *Optical Engineering*, 61(8), 081809.

Wootton, J. (2021). *Programming on Quantum Computers: Coding with Qiskit*. IBM Quantum Learning.
