# Case Study: Análise Estratégica para o Novo Centro de Distribuição (CD) do Magazine Luiza no Nordeste

**Autor:** Thiago Cunha

**Data:** 07 de Setembro de 2025

---

## 1. Resumo do Projeto

Este documento detalha a análise e a resolução do case "O Dilema do Novo Centro de Distribuição". O objetivo principal foi determinar, com base em uma análise de dados robusta, a localização mais estratégica para um novo CD do Magazine Luiza na região Nordeste, visando a otimização dos prazos de entrega e a melhoria da eficiência logística. As duas cidades candidatas para a análise foram **Recife (PE)** e **Salvador (BA)**.

A recomendação final deste estudo, após uma avaliação criteriosa de múltiplos fatores, é a cidade de **Recife (PE)**.

---

## 2. O Desafio Estratégico

A expansão do e-commerce e a crescente demanda por entregas rápidas (`same-day` e `next-day delivery`) exigem uma malha logística cada vez mais capilar e eficiente. A região Nordeste representa um mercado de enorme potencial de crescimento, e a instalação de um novo CD é um passo fundamental para capturar essa oportunidade.

O case nos apresentou três perguntas centrais a serem respondidas:

1.  **Qual das duas cidades, Recife ou Salvador, apresenta a localização mais estratégica para a empresa?**
2.  **Quais são os principais fatores que sustentam essa decisão?**
3.  **Quais ferramentas e metodologias foram utilizadas para fundamentar o case?**

---

## 3. Metodologia Aplicada: Uma Abordagem Data-Driven

Para garantir uma decisão objetiva, imparcial e puramente baseada em evidências, foi desenvolvida uma metodologia quantitativa estruturada em torno de um **Scorecard Ponderado**.

### 3.1. Estrutura do Scorecard

O Scorecard foi projetado para avaliar as duas cidades candidatas com base em três critérios fundamentais. A cada critério foi atribuído um peso, refletindo sua importância estratégica para o objetivo principal do projeto: agilizar as entregas.

| Critério | Peso (Importância) | Justificativa |
| :--- | :--- | :--- |
| **Agilidade Logística** | 50% | O principal objetivo do projeto. Mede a eficiência e a velocidade da distribuição para os principais mercados consumidores. |
| **Acesso a Mercados** | 30% | Avalia a proximidade e o alcance dos maiores polos de consumo da região, garantindo que a agilidade seja direcionada para onde há mais demanda. |
| **Custo Imobiliário** | 20% | Fator financeiro importante, mas secundário em relação à eficiência operacional e estratégica. |

### 3.2. Fontes de Dados

Para alimentar a análise, foram utilizadas fontes de dados públicas e de mercado, garantindo a credibilidade dos inputs:

-   **Dados Demográficos e Econômicos:** Censo 2022 e estimativas de PIB por estado do **IBGE**.
-   **Dados de Malha Viária e Logística:** Tempos de rota para caminhões calculados via **Google Maps API**.
-   **Dados de Custo Imobiliário:** Pesquisa de mercado em plataformas especializadas e relatórios do setor logístico para o custo médio de aluguel de galpões (R$/m²).

---

## 4. Análise Detalhada dos Critérios

A seguir, apresento a análise comparativa para cada um dos três pilares da decisão.

### 4.1. Custo Imobiliário (Peso: 20%)

Neste critério, a análise buscou identificar qual cidade oferecia um custo mais competitivo para a locação de um galpão logístico de grande porte (estimado entre 30.000 m² e 50.000 m²).

**Tabela de Custo Médio de Aluguel:**

| Cidade | Custo Médio de Aluguel (por m²) | Média de Custo (para 40.000 m²) |
| :--- | :--- | :--- |
| Recife, PE | R$ 22,00 - R$ 27,00 | R$ 980.000 / mês |
| **Salvador, BA** | **R$ 18,00 - R$ 22,00** | **R$ 800.000 / mês** |

**Conclusão do Critério:**
**Salvador apresenta uma clara vantagem de custo**, sendo aproximadamente 15-20% mais econômica. Esta vantagem foi refletida na nota atribuída no scorecard.

### 4.2. Acesso a Mercados (Peso: 30%)

Esta análise avaliou qual cidade está mais próxima do "centro de gravidade" do consumo no Nordeste. Para isso, foi utilizado o PIB de cada estado como um indicador do potencial de consumo.

**Tabela de Potencial de Consumo (PIB por Estado):**

| Estado | PIB (R$ bi) | % do Total do Nordeste |
| :--- | :--- | :--- |
| Bahia (BA) | 352 | 28.4% |
| Pernambuco (PE) | 220 | 17.8% |
| Ceará (CE) | 194 | 15.7% |
| Maranhão (MA) | 124 | 10.0% |
| Outros 5 estados | 348 | 28.1% |
| **Total Nordeste** | **1.238** | **100%** |

**Análise Estratégica:**
-   **Salvador** está localizada no maior mercado individual (Bahia), o que lhe confere acesso otimizado a 28.4% do PIB da região.
-   **Recife**, por sua vez, está posicionada de forma a atender com extrema agilidade um cluster de mercados muito relevantes (PE, PB, RN, CE) que, **somados, representam mais de 46% do PIB do Nordeste**.

**Conclusão do Critério:**
Embora Salvador esteja no maior mercado, **Recife oferece acesso mais estratégico a um volume maior e mais diversificado de mercados consumidores**, recebendo uma nota superior neste quesito.

### 4.3. Agilidade Logística (Peso: 50%)

Este foi o critério mais importante. A análise mediu o tempo de viagem de caminhão de cada cidade-base para as outras capitais, e esses tempos foram ponderados pelo PIB do estado de destino para criar um "custo de oportunidade logístico".

**Tabela Comparativa de Tempos de Viagem (em horas):**

| Capital de Destino | Partindo de RECIFE | Partindo de SALVADOR | Vantagem Clara |
| :--- | :--- | :--- | :--- |
| Maceió, AL | **4h** | 8h | **Recife** |
| João Pessoa, PB | **2h** | 13.5h | **Recife** |
| Natal, RN | **4h** | 15h | **Recife** |
| Aracaju, SE | 7.5h | **4.5h** | **Salvador** |
| Fortaleza, CE | **10.5h** | 16.5h | **Recife** |
| Teresina, PI | 16h | 16h | Empate |
| São Luís, MA | **22.5h** | 24h | **Recife** |

**Análise do Custo Logístico Ponderado:**
A superioridade de Recife é avassaladora. A cidade não só é mais rápida para a maioria dos destinos, como é drasticamente mais eficiente para chegar a mercados grandes e estratégicos (como Ceará e Paraíba). O custo logístico ponderado total de Recife foi **12% menor** que o de Salvador.

**Conclusão do Critério:**
**Recife demonstrou uma superioridade logística incontestável**, sendo a escolha óbvia para quem busca agilidade e eficiência na distribuição regional.

---

## 5. O Scorecard Final: A Decisão em Números

A compilação de todas as análises no Scorecard Ponderado nos fornece um resultado numérico claro e defensável.

| Critério | Peso | Nota Recife (0-10) | Nota Salvador (0-10) | Pontos Recife | Pontos Salvador |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Custo Imobiliário | 20% | 4.5 | 5.5 | 0.90 | **1.10** |
| Agilidade Logística | 50% | **5.8** | 4.2 | **2.90** | 2.10 |
| Acesso a Mercados | 30% | **5.3** | 4.7 | **1.59** | 1.41 |
| **TOTAL** | **100%** | | | **5.39** | **4.61** |

O placar final mostra que, embora Salvador vença em custo, a **vantagem esmagadora de Recife em Agilidade Logística e Acesso a Mercados** — os critérios de maior peso estratégico — a torna a escolha superior.

---

## 6. Conclusão e Recomendação Final

Com base na análise quantitativa apresentada, **recomendo fortemente a instalação do novo Centro de Distribuição do Magazine Luiza na cidade de Recife, Pernambuco.**

Esta decisão se fundamenta na clara superioridade estratégica da cidade em:
-   **Eficiência Logística:** Posição geográfica central que reduz drasticamente o tempo de entrega para a maioria dos mercados do Nordeste.
-   **Alcance de Mercado:** Acesso rápido e otimizado a um conjunto de estados que somam quase metade do potencial de consumo da região.

O investimento adicional no custo imobiliário em Recife é justificado pelo imenso ganho em velocidade, eficiência e posicionamento estratégico, alinhando-se perfeitamente com a missão do Magazine Luiza de encantar o cliente com a entrega mais rápida do Brasil.
