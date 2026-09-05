# Guia de Estudo de Reta Final: Estatística PCPR (Banca FGV)

Este guia sintetiza os pontos fundamentais da estatística para o concurso de Agente da PCPR, com foco exclusivo na abordagem lógica e prática da banca FGV.

---

## 1. Mapa de Prioridades

Com base no histórico da banca para cargos de nível médio e superior da área policial, a incidência dos temas é distribuída da seguinte forma:

| Peso | Temas Principais | Foco da FGV |
| :--- | :--- | :--- |
| **Altíssimo** | Média (Aritmética e Ponderada) e Quantis | Médias combinadas, trocas de elementos e interpolação em ogivas. |
| **Alto** | Dispersão e Propriedades de $Y = aX + b$ | Comparação de desvios e efeito de transformações lineares. |
| **Médio** | Probabilidade e Amostragem | Probabilidade condicional, "pelo menos um" e tipos de amostragem. |
| **Baixo** | Assimetria, Binomial e Normal | Definições conceituais e relações entre média, mediana e moda. |

---

## 2. Pilares de Alta Incidência: Fórmulas e Atalhos

### A. Média Aritmética e Ponderada
*   **Fórmula Essencial:** $\bar{x} = \frac{\sum x_i}{n}$
*   **Atalho de Cálculo:** Trabalhe com a **SOMA TOTAL**, não com a média. Se a média de 10 pessoas é 20, a soma é 200. Se uma pessoa de valor 30 sai, a nova soma é 170.
*   **Exemplo Resolvido:** A média de 5 números é 19 (Soma = 95). A média dos 2 primeiros é 16 (Soma = 32). Qual a média dos outros 3?
    *   *Resolução:* $95 - 32 = 63$. Média dos 3 restantes: $63 / 3 = 21$.

### B. Mediana e Quantis (Interpolação)
*   **Fórmula Essencial:** Para listas, ordene e ache a posição $\frac{n+1}{2}$. Para classes, use a proporção da frequência acumulada.
*   **Atalho de Cálculo:** Interpolação Linear. Se a mediana está em uma faixa de 10 unidades que cobre 40% da frequência, e você precisa de 20% para chegar ao centro, a mediana está exatamente no meio da faixa.
*   **Exemplo Resolvido:** 30% das pessoas moram a menos de 10km; 70% a menos de 20km. Onde está a mediana (50%)?
    *   *Resolução:* A mediana está entre 10 e 20km. Faltam 20 pontos percentuais para os 50% desejados dentro de uma faixa que tem 40 pontos (70-30). Como 20 é metade de 40, a mediana é 10 + metade da amplitude (5) = 15km.

### C. Variância (Atalho do "Quadrado da Média")
*   **Fórmula Essencial:** $Var(X) = \frac{\sum (x_i - \bar{x})^2}{n}$
*   **Atalho de Cálculo:** $Var(X) = (\text{Média dos Quadrados}) - (\text{Quadrado da Média})$.
*   **Exemplo Resolvido:** Dados 1 e 3. Média = 2. Quadrado da média = 4. Quadrados dos dados: 1 e 9 (Média dos quadrados = 5).
    *   *Resolução:* $Var = 5 - 4 = 1$.

---

## 3. Propriedades das Medidas: Transformação $Y = aX + b$

Este é o tema mais rentável para a FGV. A regra define como as medidas se comportam quando somamos ($b$) ou multiplicamos ($a$) uma constante a todos os valores do conjunto.

| Medida | Somar constante ($b$) | Multiplicar por ($a$) |
| :--- | :--- | :--- |
| **Posição** (Média, Mediana, Moda, Quantis) | Altera: Soma-se $b$ | Altera: Multiplica-se por $a$ |
| **Dispersão** (Variância) | **NÃO ALTERA** | Altera: Multiplica-se por $a^2$ |
| **Dispersão** (Desvio-padrão, Amplitude) | **NÃO ALTERA** | Altera: Multiplica-se por $|a|$ |
| **C.V.** (Coeficiente de Variação) | Altera | **NÃO ALTERA** |

**A Lógica por trás:**
*   **Somar ($b$):** Imagine um gráfico. Somar uma constante apenas desloca o gráfico para a direita ou esquerda sem "esticá-lo". A distância entre os pontos (dispersão) permanece a mesma. Por isso, Variância e Desvio-Padrão não mudam.
*   **Multiplicar ($a$):** Multiplicar "estica" ou "comprime" o gráfico. A distância entre os pontos aumenta proporcionalmente, alterando a dispersão.

---

## 4. Catálogo de Pegadinhas Conceituais

| Situação | Veredito | Justificativa |
| :--- | :--- | :--- |
| "O desvio-padrão é uma medida adimensional." | **ERRADO** | O DP possui a mesma unidade de medida dos dados originais. |
| "Se a média é maior que a mediana, a maioria dos valores está acima da média." | **ERRADO** | A média é puxada por extremos; na assimetria à direita, a maioria dos dados fica **abaixo** da média. |
| "A moda pode ser calculada para variáveis qualitativas nominais." | **CERTO** | A moda é a única medida de tendência central que serve para qualquer tipo de variável. |
| "Desvio-padrão igual a zero implica que a média também é zero." | **ERRADO** | DP = 0 significa apenas que todos os valores do conjunto são iguais entre si. |
| "Eventos independentes são necessariamente mutuamente exclusivos." | **ERRADO** | São conceitos distintos; se forem exclusivos e tiverem probabilidade > 0, são dependentes. |
| "A variância é sempre maior que o desvio-padrão." | **ERRADO** | Se a variância for entre 0 e 1 (ex: 0,25), o desvio-padrão será maior (ex: 0,5). |
| "O Boxplot permite visualizar a média e a moda da distribuição." | **ERRADO** | O Boxplot exibe quartis, mediana, valores máximos/mínimos e outliers, mas não a média ou moda. |

---

## 5. Protocolo de Resolucão em Prova

Para otimizar o tempo e evitar erros bobos na FGV, siga este protocolo:

1.  **Leitura Inversa:** Leia o comando final da questão antes do texto. A FGV costuma usar enunciados longos para pedir propriedades simples.
2.  **Triagem Propriedade vs. Conta:** Identifique se a questão pode ser resolvida por propriedades ($Y=ax+b$). Se sim, não faça cálculos desnecessários.
3.  **Ordenação Imediata:** Se a questão pedir Mediana, Quartis ou Decis, ordene os dados (Rol) imediatamente. A banca sempre os fornece desordenados.
4.  **Pensamento em Soma:** Para questões de média, trabalhe com a soma dos elementos para facilitar substituições ou exclusões.
5.  **Filtro de Unidade:** Verifique se a alternativa pede Variância (unidade ao quadrado) ou Desvio-Padrão (unidade original).
6.  **Caminho do Complementar:** Se ler "pelo menos um", calcule a probabilidade de "nenhum" e subtraia de 1 ($1 - P(\text{nada})$).

---

## 6. O que NÃO compensa estudar (Custo-Benefício Negativo)

Considerando o perfil da prova para Agente da PCPR e o histórico da banca FGV, não perca tempo com:
*   Cálculos complexos de Regressão Linear Múltipla.
*   Testes de Hipóteses profundos (t de Student, Qui-quadrado, ANOVA).
*   Distribuições contínuas específicas (Exponencial, Gama, Beta).
*   Números-índices e Séries Temporais (salvo se houver menção explícita e forte no edital, o que é raro para este cargo).
*   Demonstrações matemáticas de fórmulas.

**Prioridade Máxima:** Foque na lógica das propriedades e na interpretação de gráficos (Histogramas e Ogivas).