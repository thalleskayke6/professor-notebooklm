# GUIA DE ESTUDO COMPLETO: RACIOCÍNIO LÓGICO E ESTATÍSTICA (FOCO FGV)

Este é o seu **Resumo de Guerra**. Esqueça as teorias extensas; aqui está o que a FGV cobra e como ela tenta te derrubar. A regra de ouro da banca é: **raciocínio sobre o cálculo**. No nível de Agente, ela raramente exige contas hercúleas, mas sim o domínio das propriedades.

---

## 1. Fundamentos da Lógica de Proposições

### Definições e Filtros
Uma **proposição lógica** é uma oração declarativa com sentido completo (verbo) e valor lógico único (V ou F).
*   **Dica de Elite:** Ter verbo não basta. "Chute a bola!" possui verbo, mas é uma ordem (imperativa), logo, não é proposição.

### O que NÃO é proposição (Obrigatoriamente Decorar)
*   **Exclamativas/Interrogativas:** "Que prova difícil!" ou "Quem é você?"
*   **Imperativas/Optativas:** "Estude agora!" ou "Deus te ajude."
*   **Sentenças Abertas:** Variáveis ($x + 2 = 5$) ou pronomes indefinidos ("Ele foi aprovado").
*   **Paradoxos e Subjetividade:** "Esta frase é mentira" ou "João é um excelente policial" (opinião/subjetivo).

### Transformação: Sentença Aberta $\rightarrow$ Proposição
Usa-se a determinação da variável ou **quantificadores**:
*   **Universais:** Todo, nenhum, para qualquer.
*   **Existenciais:** Algum, existe, pelo menos um.

### Negação de Proposições Simples
*   **Antônimos são armadilhas:** A negação de "O Grêmio venceu" **não é** "O Grêmio perdeu" (existe o empate). O correto é "O Grêmio **não** venceu".
*   **Subordinação:** Nega-se apenas o **verbo da oração principal**.
    *   *Exemplo:* "O tribunal entende que o réu tem culpa" $\rightarrow$ "O tribunal **não entende** que o réu tem culpa".
*   **Dupla Negação:** $\sim(\sim p) \equiv p$. Número par de negações mantém o valor original; ímpar inverte.

---

## 2. Conectivos Lógicos e Operações Compostas

### Tabela de Conectivos (Foco nos Favoritos da FGV)

| Tipo | Conectivo | Símbolo | Termos "Pegadinha" FGV |
| :--- | :--- | :---: | :--- |
| **Conjunção** | e | $\land$ | **Mas, nem, entretanto, embora**, vírgula |
| **Disjunção Inclusiva** | ou | $\lor$ | Pelo menos um |
| **Disjunção Exclusiva** | ou... ou | $\underline{\lor}$ | Ou... ou, mas não ambos |
| **Condicional** | se... então | $\rightarrow$ | Logo, pois, implica, quando, toda vez que |
| **Bicondicional** | se e somente se | $\leftrightarrow$ | Condição necessária e suficiente |

### Regras de Ouro (Valoração)
1.  **Conjunção ($e$):** Só V se **ambas forem V**.
2.  **Disjunção Inclusiva ($ou$):** Só F se **ambas forem F**.
3.  **Disjunção Exclusiva ($ou...ou$):** Só F se os valores forem **iguais** (V-V ou F-F).
4.  **Condicional ($se...então$):** Só F no caso "Vera Fischer" (**V $\rightarrow$ F = F**).
5.  **Bicondicional ($se \leftrightarrow se$):** Só V se os valores forem **iguais**.

### Hierarquia da Condicional ($p \rightarrow q$)
*   **$p$ (Antecedente):** Condição **Suficiente**.
*   **$q$ (Consequente):** Condição **Necessária**.

---

## 3. Estruturas Lógicas Avançadas

*   **Tabela-Verdade:** Número de linhas = **$2^n$** ($n$ = proposições simples distintas). A negação não altera $n$.
*   **Tautologia:** Sempre V (Ex: $p \lor \sim p$).
*   **Contradição:** Sempre F (Ex: $p \land \sim p$).
*   **Método do Absurdo:** Para testar tautologia em condicionais, tente forçar o resultado **Falso** (Antecedente V e Consequente F). Se houver contradição nos valores, é Tautologia.

---

## 4. Estatística Descritiva: Variáveis e Gráficos

### Classificação de Variáveis e Medidas

| Tipo | Subdivisão | Medidas Permitidas |
| :--- | :--- | :--- |
| **Qualitativa** | Nominal (cor) / Ordinal (patente) | Moda (Nominal); Moda/Mediana (Ordinal) |
| **Quantitativa** | Discreta (contagem) / Contínua (medida) | Moda, Mediana e Média |

*   **Dica de Elite:** A **Moda** é a única que serve para todos os tipos de variáveis.

### Gráficos: O que observar
*   **Boxplot:** Exibe quartis (Q1, Mediana, Q3) e outliers. **Não mostra média nem moda**.
*   **Ramo-e-Folhas:** Único que preserva os dados originais (não perde informação).
*   **Histograma:** Para variáveis contínuas (barras coladas).

---

## 5. Medidas de Posição e Assimetria

### O Atalho da Soma (Questões de "Troca")
Não recalcule a média do zero. Use: **Soma = Média $\times n$**.
*   *Exemplo:* Média de 12 funcionários é 2400. Lúcio (3000) sai e entra Felipe (1800). A soma total caiu 1200. Dividido por 12, a média cai 100. Nova média = 2300.

### Média Combinada (Média de Médias)
$\bar{x}_{comb} = \frac{(n_1 \cdot \bar{x}_1 + n_2 \cdot \bar{x}_2)}{(n_1 + n_2)}$.
*   *Exemplo FGV:* Turma A (20 alunos, média 80) e Turma B (30 alunos, média 72). Resultado: $(1600 + 2160) / 50 = 75,2$ (e não 76!).

### Mediana e Interpolação (Técnica mais Rentável)
Para dados em classes/ogiva, use a proporção.
*   *Exemplo FGV:* 30% moram a menos de 10km; 70% a menos de 20km. A mediana (50%) está exatamente no meio da faixa (entre 30% e 70%). Logo, Mediana = **15km**.

### Assimetria
*   **Mnemônico:** "A média sempre corre atrás da cauda".
*   **Simétrica:** Média = Mediana = Moda.
*   **À Direita (Positiva):** Moda < Mediana < **Média** (Cauda longa à direita).
*   **À Esquerda (Negativa):** **Média** < Mediana < Moda (Cauda longa à esquerda).

---

## 6. Medidas de Dispersão e Propriedades

### Propriedades de Transformação ($Y = aX + b$)
Este é o assunto que mais aprova. Se multiplicarmos os dados por $a$ e somarmos $b$:

| Medida | Impacto da Soma ($+b$) | Impacto da Mult. ($\times a$) |
| :--- | :--- | :--- |
| **Posição (Média/Mediana)** | Soma $b$ | Multiplica por $a$ |
| **Dispersão (DP/Amplitude)** | **Inalterada** | Multiplica por **$|a|$** (Módulo) |
| **Variância** | **Inalterada** | Multiplica por **$a^2$** |
| **Coef. Variação (CV)** | **Muda** (pois a média muda) | **Inalterada** (escala junta) |

*   **Atenção:** O sinal negativo de $a$ some no DP. Se $Y = 30 - 2X$, o Desvio-Padrão de $Y$ é **$2 \times$** o DP de $X$.

### Dicas de Raciocínio (Comparação)
Se a questão pedir para comparar desvios-padrão de listas, não calcule. **Visualize o espalhamento**: a lista com valores mais distantes do centro tem o maior DP. Se uma lista é apenas a outra deslocada (ex: 1, 2, 3 vs 11, 12, 13), o DP é **igual**.

---

## 7. Probabilidade e Combinatória

*   **Regra do Complementar:** $P(\text{Ao menos um}) = 1 - P(\text{Nenhum})$. Use sempre que ler "pelo menos".
*   **Independência $\neq$ Exclusividade:**
    *   **Mutuamente Exclusivos:** Não podem ocorrer juntos ($P(A \cap B) = 0$).
    *   **Independentes:** Um não afeta o outro. Se são exclusivos e têm prob. > 0, eles são **dependentes** (se um ocorre, o outro é impossível).
*   **Combinatória:** Ordem importa? Sim $\rightarrow$ **Arranjo** (senhas/pódios). Não $\rightarrow$ **Combinação** (comissões/grupos).

---

## 8. Amostragem e Inferência

*   **Estratificada:** Divide em estratos **internamente homogêneos** (ex: por sexo). Sorteia-se dentro de cada estrato.
*   **Conglomerado:** Sorteia-se o grupo inteiro. Conglomerados são **internamente heterogêneos** (miniaturas da população).
*   **Precisão:** O erro padrão é proporcional a $1/\sqrt{n}$. Para dobrar a precisão (reduzir erro à metade), deve-se **quadruplicar ($4\times$)** o tamanho da amostra.

---

## 9. Tabela de Antídotos para Pegadinhas FGV

| Armadilha (Trap) | Antídoto (Ação Corretiva) |
| :--- | :--- |
| "Média > Mediana significa mais valores acima da média." | Errado. Significa mais valores **abaixo** da média (ela foi puxada por extremos altos). |
| "Somar 10 a todos os dados aumenta o Desvio-Padrão." | Errado. A soma de constante **não altera** dispersão. |
| "Desvio-padrão é adimensional." | Errado. DP mantém a unidade original. Adimensional é o **CV**. |
| "O 'ou' em lógica é sempre inclusivo." | Cuidado. Pode ser exclusivo se o contexto impedir a simultaneidade (ex: "vivo ou morto"). |
| "DP igual a zero significa que os valores são nulos." | Errado. Significa apenas que **todos os valores são iguais**. |

---

## 10. Perguntas que a Banca Faz

*   **"Qual o impacto no desvio-padrão se incluirmos um valor igual à média?"**
    *   *Resposta:* O desvio-padrão **diminui**. O valor extra não aumenta a soma dos desvios, mas o denominador ($n$) aumenta.
*   **"Sabendo que a condicional é falsa, o que se afirma sobre as proposições?"**
    *   *Resposta:* O antecedente é **Verdadeiro** e o consequente é **Falso** (Caso Vera Fischer).
*   **"A variância é sempre maior que o desvio-padrão?"**
    *   *Resposta:* **Não**. Se a variância for entre 0 e 1 (ex: 0,25), o DP (0,5) será maior.
*   **"Dada uma transformação linear $Y = aX + b$, o novo CV é igual ao antigo?"**
    *   *Resposta:* Só se $b=0$. Se houver soma de constante, o CV muda.