# GUIA DE ESTUDO COMPLETO: ESTATÍSTICA E RACIOCÍNIO LÓGICO (FOCO FGV)

Este guia foi estrategicamente elaborado para a aprovação na **PC-PR (Agente de Polícia Judiciária)**. O perfil da banca **FGV** exige que o candidato priorize o **raciocínio sobre a conta**. A "Regra de Ouro" é clara: domine as propriedades técnicas e as definições, pois a banca prefere testar o conhecimento conceitual do que a habilidade aritmética.

---

### 1. Classificação de Variáveis e Medidas Aplicáveis `[PESO MÉDIO]`

As variáveis determinam o que pode ou não ser calculado em uma análise estatística.

*   **Qualitativas (Categóricas):**
    *   **Nominais:** Sem ordem intrínseca (ex: sexo, bairro, cor, religião).
    *   **Ordinais:** Possuem hierarquia, mas sem distância matemática exata (ex: escolaridade, patente militar, escala Likert).
*   **Quantitativas (Numéricas):**
    *   **Discretas:** Resultam de contagem, geralmente inteiros (ex: número de filhos, número de crimes).
    *   **Contínuas:** Resultam de medição, aceitam decimais (ex: altura, peso, renda, tempo).

**Tabela de Compatibilidade de Medidas**

| Tipo de Variável | Moda | Mediana | Média |
| :--- | :---: | :---: | :---: |
| **Qualitativa Nominal** | Sim | Não | Não |
| **Qualitativa Ordinal** | Sim | Sim | Não |
| **Quantitativa (Discreta/Contínua)** | Sim | Sim | Sim |

**Reflexo de Prova:** A **Moda** é a única medida universal. 
**Alerta de Pegadinha:** A FGV costuma afirmar que "número de filhos" é contínua para induzir ao erro; lembre-se, se é contagem, é **discreta**.

---

### 2. Distribuição de Frequências e Representação Gráfica

*   **Termos Técnicos:** Frequência absoluta (**fi**), relativa (**fri** = $fi/n$), acumulada (**Fi**) e relativa acumulada (**Fri**).
*   **Histograma:** Exclusivo para quantitativas contínuas (barras coladas). Não confunda com o gráfico de barras (qualitativas, barras separadas).
*   **Ogiva:** Representa a frequência acumulada. É o gráfico essencial para encontrar a mediana e quantis por interpolação.
*   **Ramo-e-folhas:** Único gráfico que preserva os dados originais e **não perde informação**.
*   **Boxplot:** Exibe Q1, Mediana, Q3 e outliers. 
    *   **NOTA DE ATENÇÃO:** O Boxplot **NÃO** mostra a média nem a moda.

---

### 3. Medidas de Posição e Assimetria `[PESO ALTÍSSIMO]`

*   **Atalho da Soma:** Para a FGV, não pense em média, pense em **SOMA TOTAL** ($Média \times n = Soma$). Se a média de 12 funcionários é 2400, a soma é 28.800. Se um sai e outro entra, basta ajustar a soma e dividir novamente.
*   **Média Combinada:** $\frac{(n_1 \cdot \bar{x}_1 + n_2 \cdot \bar{x}_2)}{(n_1 + n_2)}$. Só será a média das médias se os grupos forem de tamanhos iguais.
*   **Mediana e Quantis (Interpolação Linear):** Técnica fundamental para dados em classes (Ogiva).
    *   *Exemplo Q3 (75%):* Se 70% estão abaixo de 20km e 90% abaixo de 30km, a faixa tem 20 pontos percentuais. Para chegar aos 75% (faltam 5 pontos dos 20 da faixa, ou seja, 1/4 ou 0,25), o valor será $20 + (0,25 \times 10) = 22,5\text{km}$.
*   **Assimetria:** 
    *   **Simétrica:** Média = Mediana = Moda.
    *   **Direita (Positiva):** Moda < Mediana < Média (Cauda longa à direita).
    *   **Esquerda (Negativa):** Média < Mediana < Moda (Cauda longa à esquerda).
    *   **Mnemônico:** A média sempre "corre atrás da cauda".
    *   **Pegadinha FGV:** "Média > Mediana" significa que a maioria dos valores está **abaixo** da média (puxada por extremos).

---

### 4. Medidas de Dispersão e Variabilidade `[PESO ALTO]`

Quantificam a incerteza e o espalhamento dos dados em torno da média.

**Tabela de Resumo: Unidade e Robustez**

| Medida | Unidade | Robustez a Outliers |
| :--- | :--- | :--- |
| **Amplitude Total** | Mesma dos dados | Péssima (Muito sensível) |
| **Amplitude Interquartílica (DI)** | Mesma dos dados | Boa (Robusta) |
| **Desvio Médio Absoluto** | Mesma dos dados | Moderada |
| **Variância ($s^2$)** | **AO QUADRADO** | Péssima (Não robusta) |
| **Desvio-Padrão ($s$)** | Mesma dos dados | Péssima (Não robusta) |
| **Coeficiente de Variação (CV)** | Adimensional (%) | Sensível |

**Propriedades Matemáticas (Regra $Y = aX + b$):**
1.  **Somar constante ($b$):** Altera Média e Mediana, mas **NÃO altera** Variância, Desvio-Padrão ou DI.
2.  **Multiplicar por constante ($a$):** Altera Média, Mediana e Desvio-Padrão ($|a| \cdot s$). **Atenção:** O sinal negativo de $a$ "some" no desvio-padrão devido ao módulo. A Variância multiplica por $a^2$. O CV permanece invariante na multiplicação.

---

### 5. Probabilidade e Análise Combinatória `[PESO ALTÍSSIMO]`

*   **Reflexo de Prova:** Leu "pelo menos um", calcule pelo complementar: $1 - P(\text{Nenhum})$.
*   **Independência vs. Exclusividade:** Se $P(A)$ e $P(B) > 0$ e são mutuamente exclusivos, eles são **dependentes** (se um ocorre, o outro torna-se impossível).
*   **Teorema de Bayes (Árvore):** Monte os ramos. O denominador é a Probabilidade Total (soma dos caminhos que levam ao evento observado); o numerador é o caminho específico desejado.
*   **Análise Combinatória:**
    *   **Combinação:** Ordem **NÃO** importa (comissões, sorteios simultâneos).
    *   **Arranjo:** Ordem **IMPORTA** (senhas, pódios, cargos distintos).
    *   *Teste:* Troque dois elementos. Mudou o resultado? Se sim, é Arranjo.

---

### 6. Métodos de Amostragem `[PESO MÉDIO]`

*   **Estratificada:** População dividida em **Estratos (internamente homogêneos)**. Sorteia-se dentro de cada estrato.
*   **Conglomerado:** Sorteiam-se grupos inteiros. Os **Conglomerados são internamente heterogêneos** (mini-populações).
*   **Regra de Precisão:** Para dobrar a precisão (reduzir o erro à metade), é necessário **quadruplicar** ($4\times$) o tamanho da amostra.

---

### 7. Fundamentos da Lógica Proposicional

Proposição é uma oração declarativa com verbo e sentido completo, passível de valoração única (V ou F).

**Sentenças NÃO-Propositivas (Cuidado FGV):**
1.  Exclamativas, Interrogativas, Imperativas e Optativas.
2.  **Alta Subjetividade:** "Maria é formosíssima" ou "João é incrível" (Opiniões não são valoradas objetivamente).
3.  **Sentenças Abertas:** "Ele foi preso" ou "$x + 5 = 10$" (sem quantificador).
4.  **Paradoxos:** "Esta frase é mentira".

---

### 8. Proposições Simples e Compostas

*   **Negação de Período Composto:** Em períodos por subordinação, nega-se a **oração principal**. "O tribunal entende que o réu é culpado" nega-se como "O tribunal **não** entende que o réu é culpado".
*   **Precedência de Operadores:** 1º Negação ($\sim$); 2º Conjunção ($\wedge$) e Disjunção ($\vee$); 3º Disjunção Exclusiva ($\underline{\vee}$); 4º Condicional ($\rightarrow$); 5º Bicondicional ($\leftrightarrow$).

**Tabela de Conectivos Lógicos**

| Conectivo | Símbolo | Nome Técnico | Regra de Valoração |
| :--- | :---: | :--- | :--- |
| **e / mas / nem** | $\wedge$ | Conjunção | V apenas se ambos forem V |
| **ou** | $\vee$ | Disjunção Inclusiva | F apenas se ambos forem F |
| **ou...ou** | $\underline{\vee}$ | Disjunção Exclusiva | V se os valores forem diferentes |
| **se...então** | $\rightarrow$ | Condicional | F apenas no caso Vera Fischer ($V \rightarrow F$) |
| **se e somente se** | $\leftrightarrow$ | Bicondicional | V se os valores forem iguais (V-V ou F-F) |

---

### 9. Classificações Lógicas

*   **Tautologia:** Sempre V. **Contradição:** Sempre F. **Contingência:** V e F.
*   **Método da Prova por Absurdo:** Para testar Tautologia, force o resultado a ser Falso. Se encontrar uma impossibilidade lógica (ex: uma proposição sendo V e F ao mesmo tempo), a sentença é Tautologia.

---

### 10. Bloco: Pegadinhas FGV

*   **Unidade da Variância:** A banca dirá que é a mesma dos dados. **Mentira.** É a unidade ao quadrado.
*   **Tamanho do DP:** Se a variância for $< 1$ (ex: $0,25$), o desvio-padrão ($0,5$) será **maior** que a variância.
*   **DP igual a Zero:** Não implica média zero. Implica que **todos os valores da lista são iguais**.
*   **Negação de Antônimos:** Não se nega "vencer" com "perder". A negação correta é "não vencer" (pois inclui o empate).
*   **Independência:** Eventos independentes não são mutuamente exclusivos. Se $P(A \cap B) = 0$, eles são dependentes.

---

### 11. Bloco: Perguntas que a Banca Faz

1.  **Escala com Negativo:** "Se a média de $X$ é 10 e o desvio é 4, qual o novo desvio de $Y = 30 - 2X$?". Resposta: $|-2| \times 4 = 8$. (O sinal negativo é ignorado).
2.  **Amostragem:** "Para reduzir o erro padrão da média pela metade, o que deve ser feito com $n$?". Resposta: Multiplicar por 4.
3.  **Lógica:** "A sentença 'João é um policial honesto' é proposição?". Resposta: Para a FGV, adjetivos subjetivos ("honesto", "incrível") invalidam a proposição em certos contextos de subjetividade. 
4.  **Linhas da Tabela:** "Quantas linhas tem a tabela de $(p \wedge q) \rightarrow (r \vee \sim s)$?". Resposta: $2^4 = 16$ linhas.
5.  **Probabilidade:** "Qual a chance de tirar pelo menos uma cara em 3 lançamentos?". Resposta: $1 - P(\text{Nenhuma cara}) = 1 - (1/2)^3 = 7/8$.