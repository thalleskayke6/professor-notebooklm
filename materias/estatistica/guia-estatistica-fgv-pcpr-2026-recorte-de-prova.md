# GUIA DEFINITIVO DE ESTATÍSTICA E RACIOCÍNIO LÓGICO – FOCO FGV (PC-PR 2026)

Este não é um material teórico genérico; é o seu **Resumo de Guerra**. A banca FGV não exige apenas cálculos; ela exige o domínio das propriedades. Se você tentar resolver tudo no braço, vai faltar tempo. Se dominar a lógica das medidas, você garante a vaga.

---

## 0. SEQUÊNCIA DE ATAQUE (ESTRATÉGIA DO MENTOR)
Para vencer a FGV, não estude de forma linear. Siga esta ordem de prioridade para blindar seu conhecimento:
1. **Propriedades ($Y=aX+b$)**: O assunto que mais derruba candidatos.
2. **Médias via SOMA**: Atalho para questões de troca de elementos.
3. **Quantis por Interpolação**: Essencial para dados agrupados.
4. **Probabilidade pelo Complementar**: Onde você ganha tempo.
5. **Dispersão Conceitual**: Entender o comportamento da Variância e DP.
6. **Amostragem**: Diferença entre Estratos e Conglomerados.

---

## 1. FUNDAMENTOS E TIPOS DE VARIÁVEL

### 1.1 Classificação de Variáveis
Identificar o dado é o primeiro passo. A FGV adora perguntar o que pode ser calculado em cada tipo.

*   **Qualitativa (Categórica):** 
    *   **Nominal:** Sem ordem (Ex: Cor, Sexo, Bairro).
    *   **Ordinal:** Existe ordem, mas não distância matemática (Ex: Escolaridade, Patente, Escala Likert).
*   **Quantitativa (Numérica):** 
    *   **Discreta:** Contagem, números inteiros (Ex: Número de filhos, Número de crimes).
    *   **Contínua:** Medição, aceita decimais (Ex: Altura, Peso, Renda).

**Tabela: Aplicabilidade de Medidas de Posição**

| Tipo de Variável | Moda | Mediana | Média |
| :--- | :---: | :---: | :---: |
| **Qualitativa Nominal** | Sim | Não | Não |
| **Qualitativa Ordinal** | Sim | Sim | Não |
| **Quantitativa (Geral)** | Sim | Sim | Sim |

> **ALERTA DO MENTOR:** A **Moda** é a única medida aplicável a **todos** os tipos de variáveis. Nunca esqueça: Mediana não serve para variáveis nominais!

### 1.2 Gráficos: O que a FGV cobra
1.  **Histograma:** Variáveis contínuas (barras coladas). **Não** confunda com gráfico de barras.
2.  **Ramo-e-Folhas:** O "queridinho" da banca. É o único que preserva o dado original sem perda de informação.
3.  **Boxplot:** Mostra $Q_1, Mediana, Q_3$ e *outliers*. 
    *   **NUNCA ESQUEÇA:** É impossível identificar a **Média** ou a **Moda** em um Boxplot. A FGV vai tentar te induzir a isso.
4.  **Ogiva:** Gráfico de frequências acumuladas ($F_i$ ou $Fr_i$). É a base para a interpolação da mediana.

---

## 2. MEDIDAS DE POSIÇÃO E ASSIMETRIA

### 2.1 Média: O Atalho da SOMA
Em questões de substituição (ex: um funcionário sai e outro entra), esqueça a fórmula da média. Foque na **SOMA TOTAL**.
*   **Média Combinada (Média de Médias):** Só será a média simples se os grupos tiverem o mesmo tamanho.
*   **Exemplo Real FGV:** Turma A (20 alunos, média 80) e Turma B (30 alunos, média 72).
    *   Cálculo: $\frac{(20 \times 80) + (30 \times 72)}{20 + 30} = \frac{1600 + 2160}{50} = 75,2$.
    *   A banca colocará **76** nas opções para te pegar. Não caia nessa!

### 2.2 Mediana e Interpolação Linear
Sempre **ORDENE** a lista antes de começar. Para dados agrupados em classes, use a proporção.
*   *Exemplo:* 30% moram a menos de 10km; 70% a menos de 20km. 
*   A mediana (50%) está no intervalo 10-20km. Como 50% é o meio entre 30% e 70%, a mediana é o ponto médio: **15km**.

### 2.3 Assimetria: "A Média corre atrás da cauda"
*   **Simétrica:** $Média = Mediana = Moda$.
*   **Assimétrica à Direita (Positiva):** $Moda < Mediana < Média$ (Cauda longa à direita).
*   **Assimétrica à Esquerda (Negativa):** $Média < Mediana < Moda$ (Cauda longa à esquerda).
*   **PEGADINHA FINA:** "Se a média é maior que a mediana, há mais valores acima da média". **ERRADO!** Se a média é maior, ela foi puxada por extremos, o que significa que a **maioria** dos valores está **ABAIXO** da média.

---

## 3. DISPERSÃO E VARIABILIDADE

### 3.1 O Arsenal de Dispersão
*   **Variância ($\sigma^2$):** Unidade ao quadrado. **Atalho de Ouro:** $\sigma^2 = (\text{Média dos quadrados}) - (\text{Média})^2$. Use isso para ganhar tempo.
*   **Desvio-Padrão ($\sigma$):** Raiz da variância. Mesma unidade dos dados. 
*   **Coeficiente de Variação (CV):** $CV = \sigma / \mu$. Adimensional (usado para comparar homogeneidade).
*   **Propriedade Crítica:** Incluir um valor **exatamente igual à média** no conjunto **REDUZ** o Desvio-Padrão (aumenta $n$ sem aumentar a soma dos desvios quadráticos).

### 3.2 Propriedades Lineares ($Y = aX + b$)
Este quadro resume 30% da sua prova de estatística:

| Operação | Posição (Média/Med/Moda) | Dispersão (Var/DP/Amp) | CV |
| :--- | :--- | :--- | :--- |
| **Somar ($+b$)** | Soma $b$ | **NÃO ALTERA** | Altera |
| **Multiplicar ($\times a$)** | Multiplica por $a$ | **$\times a$ (DP) / $\times a^2$ (Var)** | **NÃO ALTERA** |

---

## 4. PROBABILIDADE E VARIÁVEIS ALEATÓRIAS

### 4.1 O Paradoxo da Independência
**ALERTA DE TRAIA:** Se dois eventos têm probabilidade positiva e são **mutuamente exclusivos**, eles são **NECESSARIAMENTE DEPENDENTES**. Por quê? Porque se um ocorre, a chance do outro ocorrer vira zero (um afeta o outro).

### 4.2 Ferramentas de Ataque
*   **Pelo menos um:** Sempre use $1 - P(\text{Nenhum})$.
*   **Condicional:** $P(A|B) = P(A \cap B) / P(B)$. Se pedirem para inverter a lógica ("sabendo que o teste deu positivo..."), use a árvore de probabilidades (Bayes).
*   **Binomial:** Sucesso/Fracasso. $\text{Média} = n \cdot p$; $\text{Variância} = n \cdot p \cdot q$.
*   **Normal:** Padronize com $Z = (X - \mu) / \sigma$. Lembre da regra 68-95-99,7.

---

## 5. AMOSTRAGEM
Não troque os conceitos de **Estrato** e **Conglomerado**:

| Método | Homogeneidade | Heterogeneidade |
| :--- | :--- | :--- |
| **ESTRATIFICADA** | **Interna** (dentro do grupo) | **Externa** (entre grupos) |
| **CONGLOMERADO** | **Externa** (entre grupos) | **Interna** (dentro do grupo) |

*   **Regra de Precisão:** Para dobrar a precisão (reduzir o erro à metade), você precisa **quadruplicar** ($2^2$) a amostra.

---

## 6. LÓGICA PROPOSICIONAL: FUNDAMENTOS
**O que NÃO é proposição:**
*   Interrogativas, Exclamativas e Optativas (desejos).
*   **Imperativas:** "Saia daqui!" ou "Faça o relatório!" não têm valor lógico.
*   Sentenças abertas ($x+1=2$) e paradoxos.

**Negação de Subordinação:** 
Para negar "O tribunal entende que o réu é culpado", você nega a **principal**: "**O tribunal NÃO entende** que o réu é culpado". Ignorar a subordinada é o erro comum.

---

## 7. CONECTIVOS E TABELAS-VERDADE

### 7.1 Os Cinco Conectivos (Sinônimos FGV)
1.  **Conjunção ($\wedge$):** "e", "mas", "**nem**" (e + não). Tudo deve ser V para ser V.
2.  **Disjunção Inclusiva ($\vee$):** "ou". Basta um V.
3.  **Disjunção Exclusiva ($\underline{\vee}$):** "ou... ou", "mas não ambos". Valores diferentes.
4.  **Condicional ($\rightarrow$):** "Se..., então", "Como p, q", "Quando p, q", "p implica q", "p, logo q", "p somente se q". 
    *   **Regra:** Só é falsa no caso $V \rightarrow F$ (Vera Fischer).
5.  **Bicondicional ($\leftrightarrow$):** "se e somente se", "assim como", "condição necessária e suficiente". Valores iguais.

### 7.2 Suficiente vs. Necessária
Na condicional $p \rightarrow q$:
*   $p$ é **Suficiente**.
*   $q$ é **Necessária**.
*   Mnemônico: "O **S**e aponta para o **S**uficiente".

---

## 8. ESTRUTURAS LÓGICAS E PROVA POR ABSURDO
**Número de linhas:** $2^n$. Negações (~) não aumentam o número de linhas!
**Precedência:** 1. Negação; 2. $\wedge$ e $\vee$; 3. $\underline{\vee}$; 4. $\rightarrow$; 5. $\leftrightarrow$.

### 8.1 Método da Prova por Absurdo
Para provar que $p \rightarrow (q \rightarrow p)$ é Tautologia:
1.  Tente forçar o resultado **Falso**. 
2.  Para uma condicional ser F, o antecedente ($p$) deve ser **V** e o consequente ($q \rightarrow p$) deve ser **F**.
3.  Para $q \rightarrow p$ ser **F**, $q$ deve ser **V** e $p$ deve ser **F**.
4.  **Absurdo!** O $p$ não pode ser V e F ao mesmo tempo. Logo, é impossível ser Falsa. É uma **Tautologia**.

---

## 9. PROTOCOLO FINAL DE PROVA
1.  **Leia a pergunta antes do enunciado:** A FGV conta histórias longas para pedir um conceito de 10 segundos.
2.  **Atalho da Soma:** Trocou elemento? Use a soma total.
3.  **Variância Rápida:** Média dos quadrados menos o quadrado da média.
4.  **Pelo menos um?** Use o complementar ($1 - P(\text{nenhum})$).
5.  **Gráficos:** Viu Boxplot? Risque "Média" e "Moda" das opções de análise.
6.  **Variável Discreta:** Contagem (ex: crimes). **Contínua:** Medição (ex: tempo de pena).# Final Output Rule:
# Your output must be only the final document. Begin with the document's main title, formatted as a Markdown H1 (#). Do not include any preambles, summaries of changes, or any other surrounding text.