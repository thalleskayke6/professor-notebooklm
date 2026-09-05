# GUIA DE ESTUDO COMPLETO: MATEMÁTICA BÁSICA, RAZÃO, PROPORÇÃO E PORCENTAGEM (FOCO FGV)

Este guia foi estruturado sob a ótica da **Engenharia de Provas**, focado na realidade dos concursos policiais da FGV. Aqui, não apenas revisamos conceitos; entregamos os atalhos e as "pegadinhas de guerra" que a banca utiliza para derrubar o candidato calculista.

---

### 1. Matemática Básica e Fundamentos Quantitativos

A FGV exige precisão na classificação de dados. O domínio das variáveis é o primeiro passo para não cair em itens de "Certo ou Errado".

*   **Classificações de Variáveis:**
    *   **Qualitativas (Atributos):** 
        *   *Nominais:* Sem hierarquia (ex: sexo, cor dos olhos, bairro).
        *   *Ordinais:* Existe uma ordem (ex: escolaridade, patente policial, escala Likert).
    *   **Quantitativas (Numéricas):**
        *   *Discretas:* Fruto de contagem (ex: número de crimes, número de filhos). **Atenção:** Mesmo que a média seja 1,5, a variável continua sendo discreta.
        *   *Contínuas:* Fruto de medição, aceitam decimais (ex: altura, tempo de resposta, peso).

*   **Pilar das Medidas (A Regra da Universalidade):**
    Abaixo, a tabela de compatibilidade entre tipos de variáveis e medidas de posição.
    
    | Medida | Nominal | Ordinal | Quantitativa |
    | :--- | :---: | :---: | :---: |
    | **Moda** | Sim | Sim | Sim |
    | **Mediana** | Não | Sim | Sim |
    | **Média** | Não | Não | Sim |
    
    **Regra de Ouro:** A **Moda** é a única medida que serve para **todos** os tipos de variáveis. A FGV cobra isso como item conceitual puro.

*   **Frequências e Ponto Médio:**
    *   $fi$: Frequência Absoluta (contagem bruta).
    *   $fri$: Frequência Relativa ($fi / n$). Identidade: $fri \times 100 = \%$.
    *   $Fi$ e $Fri$: Acumuladas (essenciais para localizar a Mediana).
    *   **Ponto Médio ($PM$):** Em classes (ex: $10 \vdash 20$), o valor representativo é $PM = \frac{Li + Ls}{2}$.

---

### 2. Razão e Proporção (Amostragem e Interpolação)

Para a FGV, o raciocínio proporcional supera a conta braçal.

*   **Amostragem (O Diferencial):**
    *   **Estratificada:** Divide a população em grupos **internamente homogêneos** (estratos) e retira uma amostra proporcional de cada um.
    *   **Conglomerado:** Sorteia grupos inteiros. O conglomerado é **internamente heterogêneo** (um mini-retrato da população).
*   **Interpolação Linear (Cálculo de Quantis):**
    Utilizada para achar Mediana ou Percentis em ogivas.
    *   *Exemplo Real FGV:* 30% moram a menos de 10km; 70% a menos de 20km. 
    *   **Mediana (P50):** Está entre 10 e 20km. Faltam 20 pontos percentuais dos 40 daquela faixa (ou seja, 50%). Resultado: $10 + 5 = 15\text{km}$.
    *   **Percentil 75 (Q3):** Se 70% estão abaixo de 20km e 90% abaixo de 30km, o P75 está na faixa 20-30km. Faltam 5 pontos percentuais de um total de 20 daquela faixa ($5/20 = 25\%$). Resultado: $20 + (25\% \text{ de } 10) = 22,5\text{km}$.

*   **Atalho da Soma (Guerra):**
    Se a média de 12 agentes era R$ 2400 (Soma = 28.800). Sai um ganhando R$ 3000 e entra um ganhando R$ 1800. A soma cai 1200. Nova média: $28.800 - 1200 = 27.600 / 12 = 2300$. **Pense sempre na Soma.**

---

### 3. Porcentagem e Probabilidade

A base é a razão entre casos favoráveis e possíveis.

*   **Mnemônico do Complementar:** Ao ler **"pelo menos um"**, não calcule todos os casos. Use: $P(\text{pelo menos um}) = 1 - P(\text{nenhum})$.
*   **Eventos Exclusive vs. Independentes (Nível Caveira):**
    *   Se dois eventos são **mutuamente exclusivos** ($P(A \cap B) = 0$) e possuem probabilidade positiva, eles são obrigatoriamente **dependentes**. Por quê? Porque se um ocorreu, o outro tornou-se impossível.
*   **Reposição:** Com reposição, as chances são constantes (independência). Sem reposição, o denominador diminui.

---

### 4. Fórmulas e Transformações Lineares ($Y = aX + b$)

O comportamento das medidas frente a alterações é o assunto mais rentável da FGV.

*   **Atalho da Variância:** $\text{Variância} = \text{Média dos quadrados} - (\text{Média})^2$.
    *   *Exemplo:* Lista 8, 3, 11, 1, 7 (Média = 6). Quadrados: 64, 9, 121, 1, 49 (Soma = 244, Média dos Quadrados = 48,8).
    *   $\text{Variância Populacional} = 48,8 - 36 = 12,8$.

*   **Tabela de Transformações ($Y = aX + b$):**
    
    | Medida | Somar Constante ($b$) | Multiplicar Constante ($a$) |
    | :--- | :--- | :--- |
    | **Média/Mediana/Moda** | Soma $b$ | Multiplica por $a$ |
    | **Variância** | Não muda (Invariante) | Multiplica por $a^2$ |
    | **Desvio-Padrão** | Não muda (Invariante) | Multiplica pelo módulo $|a|$ |
    | **Coef. de Variação** | **Muda** | Não muda (Invariante) |

**Cuidado com a Unidade:** Desvio-padrão tem a mesma unidade dos dados. Variância é sempre $\text{unidade}^2$.

---

### 5. Matemática da Lógica: Proposições e Conectivos

Trate a lógica como uma álgebra binária (V ou F).

*   **Negação de Período Composto (A Armadilha do Verbo):**
    Em frases como *"O tribunal entende que o réu tem culpa"*, a FGV tentará te fazer negar a subordinada. **Erro!** Nega-se sempre o **verbo principal**.
    *   Correto: *"O tribunal **não** entende que o réu tem culpa"*.
*   **Conectivos e Mnemonicos:**
    *   **Condicional ($\rightarrow$):** Falso apenas em $V \rightarrow F$. Mnemônico: **"Vera Fischer é Falsa"**.
    *   **Disjunção Exclusiva ($\underline{\lor}$):** Verdadeiro se os valores forem **diferentes**.
    *   **Bicondicional ($\leftrightarrow$):** Verdadeiro se os valores forem **iguais**.

---

### 6. Pegadinhas Clássicas (Checklist de Guerra)

1.  **Mnemônico da Cauda:** Em distribuições assimétricas, **"A média sempre corre atrás da cauda"**. Se a média é maior que a mediana (Assimétrica à Direita), a maioria dos valores está **abaixo** da média.
2.  **Robustez:** A **Amplitude Total** é péssima contra *outliers*. A **Amplitude Interquartílica** ($Q3 - Q1$) é robusta (ignora os extremos).
3.  **DP x Variância:** Se a variância é $0,25$, o desvio-padrão é $0,5$. Logo, o DP é **maior** que a variância (isso ocorre quando a variância está entre 0 e 1).
4.  **DP = 0:** Significa que todos os valores da lista são **iguais**, não necessariamente zero.

---

### 7. Perguntas que a Banca Faz

*   *"Qual o valor do desvio-padrão se $Y = 30 - 2X$ e $DP(X) = 4$?"* 
    *   **Resposta:** $|-2| \times 4 = 8$. (O 30 é ignorado).
*   *"A frase 'Que dia lindo!' é uma proposição?"* 
    *   **Resposta:** Não. Sentenças exclamativas, interrogativas e ordens (imperativas) estão fora.
*   *"Quantas linhas tem a tabela-verdade de $(p \land q) \leftrightarrow r$?"*
    *   **Resposta:** $2^3 = 8$ linhas.

---

### 8. Protocolo de Resolução (Checklist Final)

1.  **Leia o comando final antes do enunciado:** Economize tempo em textos longos.
2.  **Propriedade ou Conta?** Se as alternativas forem "A > B", é propriedade. Não calcule.
3.  **Ordene a Lista:** Antes de qualquer Mediana ou Quartil, coloque os dados em **ROL**.
4.  **Reflexo do Complementar:** Leu "pelo menos um"? Pense em $1 - P(\text{nenhum})$.
5.  **Unidade de Medida:** Verifique se o resultado deve estar na unidade original ou ao quadrado ($\text{unidade}^2$).