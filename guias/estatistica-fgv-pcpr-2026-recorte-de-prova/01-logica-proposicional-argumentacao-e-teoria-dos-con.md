# GUIA DE ESTUDO COMPLETO: LÓGICA PROPOSICIONAL (FOCO PC-PR / FGV)

Atenção, Agente. Este não é um material teórico comum; é o seu **Resumo de Guerra**. A banca FGV não quer apenas que você saiba lógica; ela quer que você cometa erros por falta de malícia técnica. Para vencer a concorrência na PC-PR, você precisa **blindar** seu conhecimento com este arsenal de propriedades e antídotos contra as pegadinhas da banca.

---

### 1. Fundamentos das Proposições Lógicas

**Definição e Requisitos de Elite**
Uma proposição lógica é uma oração declarativa com sentido completo, presença obrigatória de verbo e que admite um, e apenas um, dos dois valores lógicos: Verdadeiro (V) ou Falso (F).
*   *Exemplos de Guerra:* "Porto Alegre é a capital do Rio Grande do Sul" (V) ou "A raiz quadrada de 16 é 8" (F).

**O que NÃO é proposição (O Campo Minado da FGV)**
A banca tentará te confundir com sentenças sem valor lógico. Se não pode ser valorado como V ou F de forma objetiva, **não é proposição**:
*   **Interrogativas/Exclamativas:** "Qual sua idade?" ou "Pelé é o maior jogador de todos os tempos!".
*   **Imperativas (Ordens):** "Saia daqui!" ou "Chute a bola".
*   **Sentenças Abertas:** Sentenças com variáveis ($x, y$) ou pronomes indefinidos sem contexto. Ex: "$x + 9 = 10$" ou "Ele foi o melhor aluno".
*   **Paradoxos:** Frases que se contradizem. Ex: "Esta frase é uma mentira".
*   **Alta Subjetividade:** "Maria é formosíssima" ou "João é incrível". Opinião não é lógica.

**Conversão de Sentenças Abertas**
O uso de **quantificadores** (Todo, Algum, Existe, Nenhum) transforma uma sentença aberta em proposição.
*   *Exemplo:* "Ele correu 100 metros" (Aberta) vs. "Usain Bolt correu 100 metros em 9,58 segundos em 2009" (Proposição).

---

### 2. Proposições Simples e a Arte da Negação

**Regras de Negação ($\sim$ ou $\neg$)**
Negar é inverter o valor lógico. Se $p$ é V, $\sim p$ é F.
*   **Negação de Negação:** $\sim(\sim p) \equiv p$. Um número **par** de negações mantém o valor original; um número **ímpar** equivale a uma negação simples.
*   **Regra de Ouro da Subordinação:** Em períodos compostos por subordinação, **nega-se apenas a oração principal**.
    *   *Caso Real:* "O tribunal entende que o réu tem culpa".
    *   *Negação Correta:* "O tribunal **não** entende que o réu tem culpa". (Negar "o réu não tem culpa" é erro fatal).
    *   *Outro Exemplo:* "Pedro respondeu que estudou". Negação: "Pedro **não** respondeu que estudou".

**Antídotos contra Antônimos**
Cuidado! Nem todo antônimo serve como negação. Para negar, você deve cobrir **todas** as possibilidades restantes.
*   **Caso Canguru Vermelho:** "O canguru vermelho é o maior marsupial". A negação **não** é "é o menor", mas sim "não é o maior" (pois ele pode ser de tamanho mediano).
*   **Caso Joinville vs. Florianópolis:** "Joinville é a cidade mais bonita". A negação é "Joinville **não** é a mais bonita". Dizer que "Florianópolis é a mais bonita" não nega a primeira, são fatos distintos.
*   **Esportes:** A negação de "Vencer" é "Não vencer", o que inclui o **empate**.

---

### 3. Arsenal de Conectivos Lógicos (Proposições Compostas)

| Tipo de Conectivo | Símbolo | Notação | Termos na Língua Portuguesa | Regra do Valor Lógico (Caso Crítico) |
| :--- | :---: | :---: | :--- | :--- |
| **Conjunção** | $\wedge$ | $p \wedge q$ | e, **mas**, entretanto, nem (e não) | **V** apenas se **ambas** forem V. |
| **Disjunção Inclusiva**| $\vee$ | $p \vee q$ | ou | **F** apenas se **ambas** forem F. |
| **Disjunção Exclusiva**| $\underline{\vee}$ | $p \underline{\vee} q$ | ou... ou..., mas não ambos | **F** se os valores forem **iguais**. |
| **Condicional** | $\rightarrow$ | $p \rightarrow q$ | se... então, logo, pois, quando | **F** apenas se **V $\rightarrow$ F**. |
| **Bicondicional** | $\leftrightarrow$ | $p \leftrightarrow q$ | se e somente se, assim como | **V** se os valores forem **iguais**. |

**Táticas de Combate:**
*   **O "Mas" de Guerra:** Na lógica, a oposição do "mas" é irrelevante. Ele é puramente uma **conjunção** ($\wedge$).
*   **Condicional Invertida:** A FGV ama esconder o antecedente. "q, se p", "q, pois p" ou "q porque p" são todas $p \rightarrow q$.
    *   *Exemplo:* "João empresta dinheiro, consequentemente ele é meu amigo" $\rightarrow$ A causa (ser amigo) aponta para a consequência (emprestar).
*   **Condição Suficiente vs. Necessária:** No $p \rightarrow q$:
    *   $p$ (Antecedente) é **Suficiente**. (O "Se" sempre aponta para o suficiente).
    *   $q$ (Consequente) é **Necessário**.

---

### 4. Tabela-Verdade e Estruturas Matemáticas

**Cálculo de Linhas:** A fórmula é $2^n$, onde $n$ é o número de proposições simples distintas.
*   **Atenção:** O número de linhas é **sempre par** (2, 4, 8, 16...). Negações não aumentam o número de linhas.

**Ordem de Precedência (Protocolo FGV):**
1.  **Negação** ($\sim$);
2.  **Conjunção** ($\wedge$) e **Disjunção** ($\vee$): Possuem a **mesma prioridade**. Resolva na ordem em que aparecerem (da esquerda para a direita).
3.  **Disjunção Exclusiva** ($\underline{\vee}$);
4.  **Condicional** ($\rightarrow$);
5.  **Bicondicional** ($\leftrightarrow$).

**O Antídoto da Vírgula:** A vírgula funciona como um parêntese visual.
*   *Exemplo:* "Se Pedro é matemático, então ele passou no vestibular, e hoje sabe calcular integrais" $\equiv (p \rightarrow v) \wedge s$.
*   *Sem vírgula:* "Se Pedro é matemático então ele passou no vestibular e hoje sabe calcular integrais" $\equiv p \rightarrow (v \wedge s)$.

---

### 5. Classificação e o Método do Absurdo

*   **Tautologia:** Sempre V (Ex: $p \vee \sim p$).
*   **Contradição:** Sempre F (Ex: $p \wedge \sim p$).
*   **Contingência:** Pode ser V ou F.

**Tática de Elite: Método do Absurdo**
Para testar se uma proposição é tautologia, você deve tentar forçá-la a ser **Falsa** e procurar uma contradição.
*   *Exemplo:* $[(p \wedge q) \wedge r] \rightarrow [p \leftrightarrow (q \vee r)]$
    1.  **Hipótese:** Suponha que a proposição inteira é **Falsa (0)**.
    2.  **Análise da Condicional:** Para ser F, o Antecedente $[(p \wedge q) \wedge r]$ deve ser **V** e o Consequente $[p \leftrightarrow (q \vee r)]$ deve ser **F**.
    3.  **Cadeia de Valores:** Se $[(p \wedge q) \wedge r]$ é V, então $p, q$ e $r$ devem ser todos **V**.
    4.  **Teste do Consequente:** Substitua os valores em $[p \leftrightarrow (q \vee r)]$. Teremos $[V \leftrightarrow (V \vee V)] \Rightarrow [V \leftrightarrow V]$, que resulta em **Verdadeiro**.
    5.  **Conclusão:** Tentamos forçar Falso, mas resultou em Verdadeiro. Isso é um **Absurdo**. Portanto, a frase nunca pode ser falsa. Ela é uma **Tautologia**.

---

### 6. Tabela-Resumo das Pegadinhas (Confusão vs. Realidade)

| Confusão do Candidato | Realidade Lógica FGV | Antídoto Tático |
| :--- | :--- | :--- |
| "Somente se" é bicondicional. | É uma **condicional** simples. | Lembre-se: "Se e somente se" é o único bicondicional. |
| "Mas" indica oposição. | É uma **conjunção** ($\wedge$). | Trate como um "e" comum. |
| Negar a oração subordinada. | Deve-se negar a **principal**. | Foque no primeiro verbo/verbo de comando. |
| $V \rightarrow F$ é verdadeiro. | É o único caso **Falso** (Vera Fischer). | Blindagem total no "V $\rightarrow$ F". |
| Antecedente é Necessário. | Ele é **Suficiente**. | "Se" aponta para o Suficiente. |
| Média > Mediana = Mais valores acima. | Significa maioria **abaixo** da média. | A média é puxada por extremos (cauda). |

---

### 7. Comandos Típicos da Banca FGV

Fique atento a estes comandos nos enunciados da PC-PR:
*   "Assinale a alternativa que apresenta uma proposição lógica." (Busque verbos e declarações sem variáveis).
*   "Se a sentença [X] é falsa, conclui-se corretamente que..." (Aplique os valores críticos dos conectivos).
*   "A negação da frase 'O tribunal entende que o réu tem culpa' é..." (Foco na oração principal).
*   "Assinale a alternativa que apresenta uma tautologia." (Aplique o Método do Absurdo).
*   "O número de linhas da tabela-verdade da proposição P é..." (Aplique $2^n$).
*   "Ao estudar para um concurso, eu me dedico." (Identifique a condicional implícita: $Estudar \rightarrow Dedicar$).