# Otimização Logística em Tempo Real: Do Limite Clássico à Revolução Quantum-Inspired

## Estudo de Caso: KPMG/TDC Net (Danish Quantum Use Cases, Case 10)

---

## Resumo Executivo

Este estudo de caso analisa a implementação de soluções de otimização quantum-inspired para roteamento de veículos na TDC Net, empresa de telecomunicações dinamarquesa. O projeto, desenvolvido em parceria com a KPMG, demonstrou reduções de até 98% no tempo de planejamento e 15-20% na distância total percorrida. A análise crítica apresentada contextualiza os resultados reportados, discute limitações metodológicas e avalia a aplicabilidade para outros domínios industriais.

**Palavras-chave:** Vehicle Routing Problem; Quantum-Inspired Optimization; QUBO; Logística; KPMG.

---

## 1. Contexto e Motivação

### 1.1. O Desafio da Complexidade Combinatória

O problema central abordado no Case 10 refere-se à otimização de rotas para técnicos de campo, tecnicamente conhecido como Vehicle Routing Problem (VRP), uma generalização do Traveling Salesman Problem (TSP). No cenário operacional da TDC Net, o desafio envolve:

- **Escala**: Centenas de técnicos atendendo milhares de chamados diários
- **Dinamismo**: Novos chamados e cancelamentos ao longo do dia
- **Restrições**: Janelas de tempo, capacidades, habilidades técnicas
- **Objetivo**: Minimizar custos operacionais maximizando atendimentos

Na computação clássica, o VRP é classificado como NP-Difícil, implicando crescimento exponencial da complexidade conforme novas variáveis são adicionadas. Para n pontos de atendimento e m veículos, o espaço de busca cresce como O(n!/m!), tornando a solução exata computacionalmente intratável para instâncias reais.

### 1.2. Limitações das Abordagens Tradicionais

As soluções de mercado tradicionalmente dependem de algoritmos heurísticos e metaheurísticos:

| Abordagem | Vantagem | Limitação |
|-----------|----------|-----------|
| Algoritmos Genéticos | Paralelizável, robusto | Convergência lenta, muitos hiperparâmetros |
| Simulated Annealing | Simples, eficaz | Sensível ao schedule de temperatura |
| Ant Colony Optimization | Bom para grafos esparsos | Alto custo computacional |
| Tabu Search | Evita ciclos | Dependente de estrutura de vizinhança |

*Tabela 1: Comparativo de metaheurísticas clássicas para VRP.*

Todas estas abordagens compartilham uma limitação fundamental: a tendência de estagnar em **mínimos locais**. O algoritmo encontra uma solução que parece ótima em sua vizinhança, mas desconhece a existência de soluções globalmente superiores em regiões distantes do espaço de busca.

---

## 2. Solução Proposta: Quantum-Inspired Optimization

### 2.1. Fundamentos Teóricos

A Quantum-Inspired Optimization (QIO) utiliza princípios da mecânica quântica — especificamente o fenômeno de **tunelamento quântico** — simulados em hardware clássico. Diferentemente de metaheurísticas tradicionais que dependem de perturbações térmicas para escapar de mínimos locais, a QIO permite "atravessar" barreiras de energia através de transições probabilísticas inspiradas no tunelamento.

O problema é reformulado como QUBO (Quadratic Unconstrained Binary Optimization):

$$\min_{\mathbf{x} \in \{0,1\}^n} \mathbf{x}^T Q \mathbf{x} \tag{1}$$

Onde Q é uma matriz que codifica tanto a função objetivo quanto as restrições do problema através de termos de penalidade.

### 2.2. Formulação Matemática do VRP

Para o VRP, definimos variáveis binárias:

- $x_{ijk} = 1$ se o veículo k viaja do ponto i para o ponto j
- $y_{ik} = 1$ se o ponto i é atendido pelo veículo k

O Hamiltoniano de custo assume a forma:

$$H = \underbrace{\sum_{i,j,k} c_{ij} x_{ijk}}_{H_{distância}} + \underbrace{\lambda_1 \sum_i \left(1 - \sum_k y_{ik}\right)^2}_{H_{cobertura}} + \underbrace{\lambda_2 \sum_k \left(\sum_i d_i y_{ik} - C_k\right)^2}_{H_{capacidade}} \tag{2}$$

Onde:
- $c_{ij}$: custo (distância/tempo) entre pontos i e j
- $d_i$: demanda do ponto i
- $C_k$: capacidade do veículo k
- $\lambda_1, \lambda_2$: multiplicadores de Lagrange para penalidades

### 2.3. Arquitetura da Solução KPMG

A implementação reportada utiliza uma arquitetura híbrida:

```
┌─────────────────┐     ┌──────────────────┐     ┌─────────────────┐
│   ERP/CRM       │────▶│  Preprocessador  │────▶│  Solver QIO     │
│   (dados)       │     │  (formulação)    │     │  (otimização)   │
└─────────────────┘     └──────────────────┘     └────────┬────────┘
                                                          │
┌─────────────────┐     ┌──────────────────┐              │
│   Dashboard     │◀────│  Pós-processador │◀─────────────┘
│   (visualização)│     │  (validação)     │
└─────────────────┘     └──────────────────┘
```

*Figura 1: Arquitetura simplificada da solução.*

Plataformas de hardware compatíveis incluem:
- **Fujitsu Digital Annealer**: ASIC otimizado para QUBO
- **Azure Quantum**: Acesso a múltiplos solvers (IonQ, Honeywell, simuladores)
- **D-Wave Leap**: Quantum annealing nativo

---

## 3. Metodologia de Análise

### 3.1. Fonte dos Dados

Os resultados apresentados neste estudo de caso são derivados do relatório público "Danish Quantum Use Cases" (KPMG, 2020), especificamente o Case 10: "Optimised Route Planning with Quantum and AI". As métricas quantitativas foram extraídas diretamente do material de divulgação da KPMG.

**Nota metodológica**: Os valores reportados representam resultados de prova de conceito (PoC) em ambiente controlado. Resultados em produção podem variar devido a fatores operacionais não capturados no piloto.

### 3.2. Métricas de Avaliação

As métricas utilizadas seguem o framework padrão para avaliação de soluções VRP:

| Métrica | Definição | Unidade |
|---------|-----------|---------|
| Tempo de planejamento | Duração do processo de otimização | minutos |
| Distância total | Soma das distâncias percorridas por todos os veículos | km/dia |
| Taxa de utilização | Percentual de capacidade efetivamente utilizada | % |
| Atendimentos/técnico | Número médio de chamados resolvidos por técnico | chamados/dia |
| Tempo de resposta a eventos | Latência para reotimização dinâmica | segundos |

*Tabela 2: Framework de métricas para avaliação de VRP.*

---

## 4. Resultados Reportados

### 4.1. Métricas Quantitativas

A implementação piloto na TDC Net demonstrou os seguintes resultados:

| Métrica | Baseline (Clássico) | Com QIO | Melhoria | Confiança* |
|---------|---------------------|---------|----------|------------|
| Tempo de planejamento | 4-6 horas | < 5 min | ~98% | Alta |
| Distância total diária | 100% (ref.) | 80-85% | 15-20% | Média |
| Atendimentos/dia/técnico | ~8 | ~10-12 | 25-50% | Média |
| Replanejamento dinâmico | Inviável | Tempo real | Habilitado | Alta |

*Tabela 3: Resultados do piloto TDC Net (Fonte: KPMG, 2020).*

**Nota sobre confiança**: Classificação baseada na especificidade dos dados reportados e na metodologia de validação descrita no material fonte.

### 4.2. Análise dos Ganhos

#### Tempo de Planejamento (98% de redução)

A redução de 4-6 horas para < 5 minutos representa o ganho mais significativo e confiável. Este resultado é consistente com a literatura sobre solvers QUBO, que demonstram convergência rápida para soluções de alta qualidade mesmo em instâncias grandes.

#### Distância Total (15-20% de redução)

A redução na distância total é atribuída à capacidade da QIO de explorar regiões do espaço de busca inacessíveis a metaheurísticas tradicionais. Contudo, a margem de 15-20% sugere variabilidade entre instâncias e possivelmente dependência de características específicas da malha logística da TDC Net.

#### Atendimentos por Técnico (25-50% de aumento)

Este ganho é derivado da combinação de rotas mais eficientes e replanejamento dinâmico. A ampla margem (25-50%) indica sensibilidade a fatores externos como duração dos atendimentos e distribuição geográfica dos chamados.

---

## 5. Análise Crítica

### 5.1. Pontos Fortes

1. **Validação em ambiente real**: O piloto foi executado com dados operacionais reais da TDC Net, conferindo credibilidade aos resultados.

2. **Arquitetura híbrida**: A combinação de preprocessamento clássico com otimização QIO representa uma abordagem pragmática para o estado atual da tecnologia.

3. **Escalabilidade demonstrada**: A solução manteve performance com aumento do número de variáveis, sugerindo viabilidade para operações maiores.

### 5.2. Limitações e Ressalvas

1. **Hardware clássico**: A implementação utiliza quantum-inspired (simulação de princípios quânticos em hardware convencional), não computação quântica nativa. Os speedups reportados são em relação a metaheurísticas subótimas, não a algoritmos clássicos estado-da-arte.

2. **Escala do piloto**: Detalhes sobre o número exato de veículos e pontos de atendimento no piloto não são especificados, dificultando a extrapolação para operações de escala diferente.

3. **Garantia de otimalidade**: QIO não garante o ótimo global — oferece soluções de alta qualidade com alta probabilidade, mas não certeza matemática. A comparação com o ótimo verdadeiro (quando computável) não é reportada.

4. **Custos de implementação**: O material não detalha TCO (Total Cost of Ownership), incluindo licenciamento de solvers, infraestrutura de integração e custos de manutenção.

### 5.3. Análise de Riscos

| Risco | Probabilidade | Impacto | Mitigação |
|-------|---------------|---------|-----------|
| Falha do solver em produção | Baixa | Alto | Fallback para heurística clássica |
| Degradação com escala | Média | Médio | Decomposição hierárquica |
| Vendor lock-in | Média | Alto | Abstração via API padronizada |
| Obsolescência tecnológica | Alta | Baixo | Arquitetura modular |

*Tabela 4: Matriz de riscos para implementação de QIO.*

### 5.4. Análise Econômica (Estimativa)

Baseado em benchmarks de mercado para soluções similares:

| Componente | Custo Estimado | Frequência |
|------------|----------------|------------|
| Licenciamento solver QIO | $50-200k | Anual |
| Integração inicial | $100-300k | Único |
| Manutenção e suporte | 15-20% do licenciamento | Anual |
| Infraestrutura cloud | $5-20k | Mensal |

*Tabela 5: Estimativa de custos (valores de mercado, não específicos para TDC Net).*

**Payback estimado**: Considerando economia de combustível (~15% de frota de 100+ veículos) e aumento de produtividade, o retorno sobre investimento pode ocorrer em 12-24 meses para operações de escala comparável.

---

## 6. Comparativo com Alternativas

### 6.1. Landscape de Soluções

| Solução | Tipo | Vantagem Distintiva | Limitação Principal |
|---------|------|---------------------|---------------------|
| Google OR-Tools | Open source | Custo zero, comunidade ativa | Performance em instâncias grandes |
| Gurobi/CPLEX | Solver comercial | Garantia de otimalidade (MIP) | Custo de licenciamento elevado |
| D-Wave Leap | Quantum annealing | Hardware quântico nativo | Conectividade limitada, ruído |
| Azure Quantum | Plataforma multi-solver | Flexibilidade, integração Azure | Complexidade de seleção |
| Fujitsu Digital Annealer | ASIC especializado | Performance, determinístico | Proprietário, custo |

*Tabela 6: Comparativo de soluções para otimização combinatória.*

### 6.2. Quando Usar QIO

A adoção de soluções QIO é recomendada quando:

- ✅ O problema tem estrutura QUBO natural ou facilmente mapeável
- ✅ Metaheurísticas tradicionais demonstram estagnação em mínimos locais
- ✅ O tempo de resposta é crítico (reotimização dinâmica)
- ✅ A escala justifica o investimento em licenciamento

E **não** é recomendada quando:

- ❌ O problema admite solução exata em tempo aceitável (branch-and-bound)
- ❌ A escala é pequena (< 50 variáveis) e heurísticas simples são suficientes
- ❌ Há restrições orçamentárias para licenciamento de solvers especializados

---

## 7. Aplicabilidade em Outros Domínios

### 7.1. Transferência do Padrão Arquitetural

O framework QUBO + QIO é aplicável a qualquer problema modelável como otimização quadrática binária:

| Domínio | Problema | Formulação QUBO |
|---------|----------|-----------------|
| **Logística** | Vehicle Routing | Cobertura + distância |
| **Telecomunicações** | Alocação de espectro | Interferência + capacidade |
| **Finanças** | Otimização de portfólio | Risco + retorno (Markowitz) |
| **Manufatura** | Job Shop Scheduling | Precedência + makespan |
| **Energia** | Unit Commitment | Custo + demanda |
| **Bioinformática** | Protein Folding | Energia + conformação |

*Tabela 7: Aplicabilidade de QUBO em domínios diversos.*

### 7.2. Exemplo: Otimização de Portfólio

O problema de Markowitz para seleção de ativos pode ser formulado como QUBO:

$$\min_{\mathbf{x}} \left[ \gamma \mathbf{x}^T \Sigma \mathbf{x} - \mu^T \mathbf{x} \right] + \lambda \left( \sum_i x_i - k \right)^2 \tag{3}$$

Onde:
- $\Sigma$: matriz de covariância dos retornos
- $\mu$: vetor de retornos esperados
- $\gamma$: parâmetro de aversão a risco
- $k$: número de ativos a selecionar

---

## 8. Roadmap de Adoção

Para organizações interessadas em replicar a experiência da TDC Net:

### Fase 1: Diagnóstico (4-6 semanas)
- [ ] Mapear problemas de otimização existentes
- [ ] Quantificar ineficiências atuais (baseline)
- [ ] Avaliar viabilidade de formulação QUBO
- [ ] Estimar ROI potencial

### Fase 2: Prova de Conceito (8-12 semanas)
- [ ] Selecionar problema piloto de escopo limitado
- [ ] Implementar formulação QUBO
- [ ] Testar com múltiplos solvers (benchmarking)
- [ ] Validar resultados contra baseline

### Fase 3: Piloto Operacional (12-16 semanas)
- [ ] Integrar com sistemas existentes (ERP/CRM)
- [ ] Executar em paralelo com solução atual (shadow mode)
- [ ] Coletar métricas de performance
- [ ] Treinar equipe operacional

### Fase 4: Produção (ongoing)
- [ ] Migrar carga de trabalho gradualmente
- [ ] Estabelecer monitoramento contínuo
- [ ] Iterar sobre formulação e hiperparâmetros
- [ ] Documentar lições aprendidas

---

## 9. Conexão com Implementação do Projeto

Este estudo de caso serviu como motivação para a implementação prática desenvolvida no projeto. Os seguintes artefatos foram criados como exercício de aprendizado:

| Artefato | Descrição | Localização |
|----------|-----------|-------------|
| `brute_force.py` | Solver exato O(n!) para validação | `programming/tsp_comparison/classical/` |
| `nearest_neighbor.py` | Heurística gulosa O(n²) | `programming/tsp_comparison/classical/` |
| `simulated_annealing.py` | Metaheurística clássica | `programming/tsp_comparison/classical/` |
| `qubo_solver.py` | Solver quantum-inspired | `programming/tsp_comparison/quantum_inspired/` |
| `graph_generator.py` | Gerador de instâncias de teste | `programming/tsp_comparison/utils/` |
| `visualizer.py` | Visualização de rotas e comparativos | `programming/tsp_comparison/utils/` |

*Tabela 8: Artefatos de código relacionados ao estudo de caso.*

O código está disponível em: [github.com/igorconrado/quantum-computing-university-project](https://github.com/igorconrado/quantum-computing-university-project)

---

## 10. Conclusão

O Case 10 da KPMG/TDC Net representa um marco na transição da computação quântica do laboratório para aplicações industriais. A análise crítica apresentada neste estudo demonstra que:

1. **Resultados promissores, mas contextualizados**: Os ganhos reportados são significativos, mas representam um piloto em condições controladas. A extrapolação para outros contextos requer validação específica.

2. **Quantum-inspired ≠ Quantum**: A solução utiliza princípios quânticos simulados classicamente, não hardware quântico nativo. Isto é uma vantagem (disponibilidade imediata) e limitação (speedups modestos vs. potencial quântico).

3. **Valor na modelagem**: A contribuição principal não está na tecnologia em si, mas na capacidade de modelar problemas operacionais como formulações QUBO — competência transferível independente da plataforma de execução.

4. **Maturidade crescente**: O ecossistema de solvers QIO está em rápida evolução, com redução de custos e aumento de acessibilidade previstos para os próximos anos.

Para o profissional de tecnologia, a lição estratégica é clara: investir no domínio de **formulações matemáticas** (QUBO, Ising, QAOA) posiciona-se na fronteira entre o paradigma clássico atual e o paradigma quântico emergente.

---

## Referências

Danish Quantum Use Cases. (2020). *Case 10: Optimised Route Planning with Quantum and AI*. KPMG / TDC Net. Acesso em: 15 jan. 2025.

Farhi, E., Goldstone, J., & Gutmann, S. (2014). A quantum approximate optimization algorithm. *arXiv preprint arXiv:1411.4028*.

Glover, F., Kochenberger, G., & Du, Y. (2019). Quantum Bridge Analytics I: a tutorial on formulating and using QUBO models. *4OR*, 17(4), 335-371.

KPMG Quantum Hub. (2023). *Quantum Technology Services*. https://kpmg.com/quantum. Acesso em: 20 jan. 2025.

Lucas, A. (2014). Ising formulations of many NP problems. *Frontiers in Physics*, 2, 5.

Toth, P., & Vigo, D. (Eds.). (2014). *Vehicle Routing: Problems, Methods, and Applications* (2nd ed.). SIAM.
