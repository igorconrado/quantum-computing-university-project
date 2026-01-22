# Do Lúdico ao Industrial: Uma Abordagem Baseada em Projetos para o Ensino de Engenharia de Software Quântica

## Resumo

A iminente "vantagem quântica" impõe a necessidade de formar engenheiros de software capazes de integrar componentes quânticos em sistemas clássicos. Este artigo relata uma experiência de aprendizado baseada em projetos (PBL) que transita da teoria fundamental para problemas industriais complexos. A metodologia adotada divide-se em duas fases: (1) A fundamentação teórica baseada no currículo de Hughes et al., com a implementação de algoritmos e jogos (Quantum Pong) para fixação de conceitos; e (2) A análise e prototipagem de uma solução para o Vehicle Routing Problem (VRP), baseada no "Case 10" da KPMG/TDC Net. Os resultados demonstram que a comparação entre a exaustão computacional clássica e a otimização inspirada em quântica facilita a compreensão de classes de complexidade NP-Difíceis.

**Palavras-chave:** Engenharia de Software Quântica; Aprendizagem Baseada em Projetos; Otimização Logística; Qiskit.

---

## 1. Introdução

A Computação Quântica está deixando de ser uma disciplina puramente teórica da Física para se tornar uma ferramenta de engenharia aplicada. No entanto, o ensino tradicional enfrenta o desafio de preparar estudantes para transitar da lógica booleana determinística para a probabilística.

O objetivo deste trabalho é relatar a experiência prática no desenvolvimento de competências em Engenharia de Software Quântica (QSE). A proposta curricular seguiu um roteiro híbrido: iniciou-se com a base teórica acessível de Hughes et al. (2021) e culminou na análise do "Caso 10" (Otimização de Rotas - KPMG), demonstrando como algoritmos quânticos podem solucionar gargalos logísticos modernos.

## 2. Metodologia de Aprendizado

A abordagem pedagógica adotada fundamenta-se na Project-Based Learning (Aprendizagem Baseada em Projetos), estruturada em dois épicos de desenvolvimento:

### 2.1. Fase de Fundamentação

Seguindo a estrutura proposta por Hughes et al. e demais autores em *Quantum Computing for the Quantum Curious*, o estudo abrangeu a obra integralmente (Capítulos 1 ao 10).

**Objetivo:** Construir o conhecimento de forma holística, cobrindo todo o arco de aprendizado proposto pelos autores: desde os fundamentos físicos e matemáticos (Caps. 1-8) até a aplicação em algoritmos e exercícios práticos (worksheets) nos capítulos finais (9 e 10).

**Aplicação:** O domínio do conteúdo completo do livro permitiu não apenas a reprodução mecânica de código, mas a compreensão profunda dos fenômenos físicos subjacentes (superposição e emaranhamento) necessários para a implementação do jogo Quantum Pong e para a modelagem de problemas complexos.

### 2.2. Fase de Pesquisa Aplicada (Case 10)

Focada na resolução de problemas de otimização combinatória (NP-Hard) com relevância industrial, analisando o caso da empresa dinamarquesa TDC Net.

## 3. Desenvolvimento e Resultados

### 3.1. Do Livro ao Código: Quantum Pong

A implementação do Quantum Pong serviu como validação prática dos conceitos abordados no Capítulo 9 de Hughes et al. Ao codificar a raquete controlada por portas quânticas, foi possível tangibilizar o conceito de "medida", onde a observação do estado quântico define a posição física do objeto no jogo. Esta etapa removeu o medo inicial da sintaxe quântica.

### 3.2. Estudo de Caso: Otimização Logística (VRP)

A segunda etapa debruçou-se sobre o problema de agendamento dinâmico de técnicos (VRP - Vehicle Routing Problem).

**O Gargalo Clássico:** Foi desenvolvido um algoritmo de "Força Bruta" em Python para resolver o TSP (Traveling Salesperson Problem). Testes práticos confirmaram que o tempo de execução cresce fatorialmente (N!), validando a teoria de complexidade apresentada na bibliografia base.

**A Solução Quântica (QIO):** O estudo do caso KPMG revelou o uso de Quantum-Inspired Optimization. Diferente dos algoritmos clássicos que estagnam em mínimos locais, a abordagem quântica utiliza o tunelamento para explorar o espaço de soluções globalmente. A modelagem do problema via formulações QUBO (Quadratic Unconstrained Binary Optimization) mostrou-se o elo perdido entre a teoria de algoritmos (Cap. 9 do livro) e a aplicação real de mercado.

### 3.3. Implementação Prática com Qiskit

> **TODO:** Seção a ser completada após desenvolvimento da aplicação usando computação quântica e Qiskit.

## 4. Discussão

A utilização da obra de Hughes et al. como guia provou-se essencial para "suavizar" a curva de aprendizado. Enquanto textos tradicionais de física focam na derivação matemática, a abordagem "para curiosos" permitiu focar na lógica algorítmica necessária para a engenharia de software. A transição para o problema da KPMG demonstrou que o engenheiro de software quântico não precisa ser um físico, mas sim um especialista em traduzir problemas reais para modelos matemáticos (Hamiltonianos) que o hardware quântico possa resolver.

## 5. Conclusão

Este relato sugere que o ensino de QSE é mais eficaz quando ancorado em duas pontas: uma base bibliográfica acessível e orientada a exercícios (Hughes et al.) e um problema real de ineficiência clássica (KPMG). O "Case 10" serviu como laboratório ideal para demonstrar que a vantagem quântica reside na capacidade de lidar com dinamismo e complexidade combinatória.

## Referências Bibliográficas

- Hughes, C., Isaacson, J., Perry, A., Sun, R. F., & Turner, J. (2021). *Quantum Computing for the Quantum Curious*. Springer. (Foco especial nos Capítulos 9 e 10).
- Danish Quantum Use Cases. (2020). Case 10: Optimised Route Planning with Quantum and AI (KPMG / TDC Net).
- Wootton, J. *Programming on Quantum Computers: Coding with Qiskit*. IBM Quantum.
