# 🎓 Professor: um tutor de concurso que aprende com o seu material

> [!IMPORTANT]
> **TL;DR.** Um professor particular para o Claude Code que lê tudo o que você juntou para um concurso, sabe o **peso de cada matéria** na prova, sabe o que a banca **mais cobra** e responde com **questões reais** como referência.
>
> Ele não decora a matéria. Ele decora **como a banca pergunta**.

> [!CAUTION]
> **Uso exclusivo para estudo. Venda proibida.** Todo o conteúdo aqui é para estudo pessoal e particular. É **expressamente proibida qualquer utilização comercial**, por qualquer pessoa, a qualquer tempo: venda, revenda, curso pago, mentoria, assinatura, grupo pago ou qualquer forma de monetização. A proibição vale para o autor e para quem receber o material. Detalhes em [AVISO-DE-USO.md](AVISO-DE-USO.md).

> [!NOTE]
> **De onde veio.** Construído para a prova de Agente de Polícia Judiciária da Polícia Civil do Paraná (Edital 01/2026, banca FGV). Por isso o exemplo é de carreira policial. A estrutura, porém, não sabe nada de polícia: ela aprende qualquer edital a partir de três coisas que todo concurseiro já tem, **notebooks com o material**, **cadernos de questões** e **as próprias anotações**. A seção "Ensinar outro edital" mostra como trocar.

---

## 🧠 A ideia central: três bases que não conversavam

Quem estuda por questões acumula material em três lugares. Cada um responde bem sobre o próprio acervo. Nenhum cruza os três.

| | 📓 Notebooks | 📝 Questões | 🗂️ Anotações |
|---|---|---|---|
| **O que tem** | Apostilas, aulas, leis | Cadernos resolvidos, com gabarito | Método, plano, erros |
| **O que responde** | "O que a apostila ensina?" | "Como a banca cobra?" | "Onde eu erro?" |
| **O que não sabe** | Como isso vira questão | O que a apostila diz | Nada da matéria |

```mermaid
flowchart LR
    N["📓 Notebooks<br/>o que a apostila ensina"] ==> P{{"🎓 Professor"}}
    Q["📝 Questões reais<br/>como a banca cobra"] ==> P
    V["🗂️ Anotações<br/>onde você erra"] ==> P
    P ==>|"responde com peso, incidência e pegadinha"| R["✅ Resposta no recorte da banca"]
```

---

## 🧩 As quatro camadas

Tudo gerado por script a partir do material do aluno. Nomes de autores, cursos e plataformas foram omitidos de propósito: para reproduzir, o que importa é o **tipo** de material e o **formato**.

| Camada | O que é | De onde vem |
|---|---|---|
| 🗺️ **Mapa** | Uma página por concurso: matérias, peso na prova, notebooks, contagens | Gerado pelos scripts |
| 📓 **Notebooks** | Um arquivo por notebook com índice hierárquico, conceitos-chave e pegadinhas, mais um guia completo por notebook e um guia por tema | {n_notebooks} notebooks do NotebookLM, {n_fontes} fontes |
| 📝 **Questões reais** | {n_questoes} questões únicas com gabarito, por matéria e assunto | Cadernos exportados de uma plataforma de questões |
| 🗂️ **Cofre** | {n_aulas} aulas em markdown, notas de método, plano e registro de erros | Cofre do Obsidian |

---

## ⚙️ Como funciona por dentro

```mermaid
flowchart LR
    A["📓 NotebookLM<br/>notebooks por matéria"] -->|"CLI: ask, report, download"| B["notebooks/ e guias/"]
    C["🗂️ Cofre Obsidian<br/>apostilas, método, erros"] -->|"build_vault.py"| D["vault/"]
    E["📝 Cadernos exportados<br/>em markdown"] -->|"build_questoes.py"| F["questoes/"]
    B --> G["🗺️ MAPA-GERAL.md"]
    D --> G
    F --> G
    G --> H{{"🎓 Skill /professor<br/>no Claude Code"}}
    H -.->|"pergunta pontual ao vivo"| A
```

### 📓 Extração dos notebooks

O NotebookLM não entrega o texto consolidado de um notebook. Duas estratégias foram combinadas, ambas por linha de comando:

> [!TIP]
> **Três perguntas fixas no chat.** Para cada notebook, três prompts (em `_build/`) pedem o índice hierárquico completo, os conceitos-chave por tema e as pegadinhas. As respostas viram as seções do arquivo `notebooks/<notebook>.md`.

> [!TIP]
> **Relatórios no Studio.** O chat tem teto de tamanho por resposta. O painel Studio gera relatórios em formato livre, que saem inteiros em markdown. O script pede um guia completo por notebook (`guias/<notebook>.md`, {guias_kb} KB em média) e, nos notebooks de matéria, **um guia por tema** do índice (`guias/<notebook>/NN-tema.md`). É o caminho com mais conteúdo por pedido.

O script também baixa o resumo automático, a lista de fontes, as notas salvas e os artefatos já existentes (quizzes, flashcards, mapas mentais).

### 🗂️ Índice do cofre

Um script percorre o cofre, lista cada aula com versão (resumo, simplificada, completa) e tamanho, associa cadernos e notas soltas à matéria e copia as notas curadas pequenas para consulta direta. Apostilas inteiras ficam só referenciadas por caminho.

### 🎓 A skill

A skill é um arquivo de instruções que o Claude Code carrega quando você chama `/professor` ou faz uma pergunta de matéria. Ela fixa a **ordem de consulta**:

```mermaid
flowchart TD
    S1["1. Ler o mapa<br/>escolher a matéria"] --> S2["2. Grep no guia e no notebook<br/>pelo tema"]
    S2 --> S3["3. Grep nas questões reais<br/>pegar 2 ou 3 como molde"]
    S3 --> S4{"Faltou teoria?"}
    S4 -->|"sim"| S5["4. Abrir a aula certa do cofre"]
    S4 -->|"não"| S7
    S5 --> S6{"Ainda falta?"}
    S6 -->|"sim"| S8["5. Perguntar ao notebook ao vivo"]
    S6 -->|"não"| S7["✅ Responder"]
    S8 --> S7
```

E fixa o **jeito de responder**: profundidade proporcional ao peso da matéria, estilo da banca, pegadinhas codificadas, e sempre dizer de onde veio cada ponto.

---

## 🔍 Como as questões foram lidas, passo a passo

O banco de questões é a parte mais valiosa da base e a mais trabalhosa de montar, porque cada exportação veio de um jeito. O script `_build/build_questoes.py` faz o seguinte, nesta ordem:

**1. Localizar os arquivos.** Todos os `.md` da pasta de cadernos, da pasta de arquivo legado e da raiz do cofre, exceto hubs, inventários e prompts. Foram 44 arquivos.

**2. Detectar o formato.** Cada arquivo é classificado por marcadores no texto:

| Formato | Como reconhecer | Onde estão banca, matéria e gabarito |
|---|---|---|
| **Curado v1** | `**Q123** · banca · [ver na fonte](url)` | Banca no cabeçalho; matéria no `##` e assunto no `###` acima; gabarito em tabela `Q123 / C` no fim do bloco |
| **Curado v2** | `**Q001** · banca` e rodapé `<sub>[.../questoes/ID] · assunto</sub>` | Igual ao v1, mas link e assunto ficam no rodapé de cada questão |
| **Exportação bruta** | Link `www.../questoes/ID`, linha da banca terminando em `/ano`, linha `Matéria - Assunto`, `N)` | Tudo em linhas próprias; gabarito inline `Gabarito: X` |
| **Exportação achatada** | Tudo da questão em uma linha só | Banca, matéria, enunciado e alternativas separados por expressão regular na mesma linha |

**3. Segmentar.** O texto é cortado no link da questão na fonte (`questoes/<ID>`). Cada pedaço é uma questão; o ID vira a chave.

**4. Ler o cabeçalho.** A linha da banca traz banca, órgão, cargo e ano no padrão `FGV - Cargo (Órgão)/Órgão/Área/2025`. Ela é reconhecida por terminar em barra e quatro dígitos. Rodapés de página das exportações em PDF (`19/49`, data e hora, título do caderno) são descartados.

**5. Achar matéria e assunto.** Conforme o formato: a linha `Matéria - Assunto` após a banca, ou os títulos `##` e `###` mais próximos acima, ou o rodapé `<sub>`. Quando uma questão não tem a linha, herda a da anterior.

**6. Separar enunciado de alternativas.** Uma expressão regular reconhece o início de alternativa (`a)`, `(A)`, `- **(A)**`). Tudo antes da primeira alternativa é enunciado; linhas seguintes sem marcador são continuação da alternativa anterior. Imagens e rodapés são limpos.

**7. Achar o gabarito.** Inline (`Gabarito: B`) nas exportações brutas, ou na tabela de gabaritos do bloco da matéria nos cadernos curados, casada pelo número local da questão (`Q271`).

**8. Deduplicar.** O mesmo ID em dois arquivos vira um registro só. Quando as versões diferem, fica a que tem gabarito; em empate, a que tem mais alternativas legíveis. Dos {n_lidas} registros lidos sobraram **{n_questoes} únicos**.

**9. Normalizar a matéria.** As fontes usavam 91 rótulos ("Direito Administrativo (Doutrina e Leis Federais)", "Direito Digital", "TI", "Análise das Demonstrações Contábeis"). Uma tabela de expressões regulares os leva para as matérias do edital; o rótulo original fica guardado em `materia_original`. Arquivos soltos sem rótulo recebem a matéria pelo nome do arquivo.

**10. Gravar.** Um `banco.json` com todos os campos, um `.md` por matéria com as questões agrupadas por assunto e gabarito logo abaixo de cada uma, e um `INDICE.md` com as contagens. O professor consulta os `.md` por Grep, pelo assunto ou por palavra-chave.

> [!WARNING]
> **O que não deu certo.** {n_sem_alt} questões de uma exportação achatada ficaram sem alternativas legíveis, porque as alternativas foram coladas em linhas fora de ordem. Estão no banco com enunciado e gabarito, marcadas.

---

## 🪤 Como a FGV derruba candidatos

Duas coisas aqui: o que os **números do banco** mostram sobre a forma das questões, e o **catálogo de mecanismos de erro** que o aluno montou a partir das próprias questões erradas e que o professor usa para codificar cada pegadinha.

### 📊 A forma da questão, em números

Das {n_questoes} questões do banco, **{n_fgv} são da FGV**, a maioria de 2024 a 2026. Medidas sobre essas:

{stats_fgv}

O que isso diz: a FGV quase não usa certo/errado nem "assinale a incorreta". Ela prefere **cinco alternativas**, enunciado de tamanho médio e **uma história antes da pergunta**. O gabarito é distribuído de forma quase uniforme entre A e E: **chute por letra não existe**. E a proporção de caso concreto muda muito por matéria:

{stats_materia}

Em Direito Penal, seis em cada dez questões começam com uma narrativa ("João, policial civil, ...") e a pergunta só vem no fim. Em Português, o texto-base é o próprio caso. Em Ciências Forenses, a pergunta é direta e curta, e o erro mora na classificação.

### 🎭 Os mecanismos

> [!CAUTION]
> A banca raramente pergunta algo que você **não sabe**. Ela pergunta algo que você **sabe**, de um jeito que faz a memória entregar a resposta errada.

Os mecanismos abaixo foram catalogados a partir das próprias questões erradas e recebem um **código**, usado no verso de cada flashcard e nas respostas do professor.

| Código | Mecanismo | Como aparece na alternativa |
|---|---|---|
| 🎭 **P1** | Modal deôntico | "pode" vira "deve": a faculdade vira obrigação, ou o contrário |
| 🎭 **P2** | Restritivo enxertado | "somente", "sempre", "em qualquer hipótese" enfiados numa regra que tem exceção |
| 📋 **P3** | Requisito cumulativo | Some um requisito, ou troca o "e" cumulativo por "ou" |
| 📐 **P4** | Sujeito ou competência | Troca quem decreta, requisita, investiga ou julga (juiz por delegado, MP por juiz) |
| 📐 **P5** | Prazo ou número | Muda dias, frações, percentuais, idades (24 horas por 48, 1/6 por 1/3) |
| 📋 **P7** | Inversão regra e exceção | Apresenta a exceção como se fosse a regra geral |
| 🎭 **P8** | Conector condicional | "salvo se" vira "mesmo que"; "desde que" vira "independentemente de" |
| 🔀 **P9** | Deslocamento de instituto | Atribui a um conceito o regime jurídico de outro parecido (prisão temporária com prazo da preventiva) |
| 📋 **P10** | Enxerto elegante | Acrescenta uma exigência plausível que a lei não faz |
| 💻 **T1** | Sigla ou protocolo | Troca protocolo, algoritmo ou ferramenta (TCP por UDP, hash por criptografia) |
| 💻 **T2** | Pilar ou princípio | Troca confidencialidade, integridade, disponibilidade, autenticidade |
| 🧬 **T3** | Sequência | Inverte a ordem de etapas (cadeia de custódia, fases da perícia) |
| 🔀 **T4** | Classificação técnica | Troca classes de lesão, fenômenos cadavéricos, tipos de variável estatística |

Nas alternativas do banco, **{alt_restritivo}** contêm um restritivo do tipo P2 ("somente", "apenas", "exclusivamente") e **{alt_modal}** contêm um modal do tipo P1. Parece pouco, mas é onde a diferença entre a alternativa certa e a "quase certa" costuma estar.

```mermaid
flowchart LR
    L["📜 Regra da lei<br/>como está escrita"] ==>|"alternativa certa"| C["✅ Literalidade<br/>dentro do caso"]
    L -.->|"troca uma palavra"| D1["🎭 P1 pode vira deve"]
    L -.->|"enxerta restrição"| D2["🎭 P2 somente, sempre"]
    L -.->|"troca o sujeito"| D3["📐 P4 juiz vira delegado"]
    L -.->|"muda o número"| D4["📐 P5 24h vira 48h"]
    D1 & D2 & D3 & D4 -.-> Q["❌ A alternativa quase certa"]
```

### 📏 As regras de leitura que o professor aplica

> [!WARNING]
> **Item incompleto não é item errado.** Uma afirmação que não esgota as hipóteses continua correta, a não ser que enxerte uma restrição ("exclusivamente"). Quem marca errado porque "faltou coisa" cai.

> [!WARNING]
> **A alternativa quase certa.** Toda questão tem uma distratora que repete a regra quase inteira e troca uma palavra. Por isso o professor sempre fecha um tema com "parece / é": a frase da distratora ao lado da frase correta.

> [!WARNING]
> **Literalidade dentro do caso.** A banca cobra a letra da lei, mas dentro de uma história. Primeiro você acha qual instituto a história descreve (isso é P9), só depois lembra a regra. O parágrafo ou inciso menos lido é alvo preferido, e lei alterada recentemente é cobrada na redação nova.

Em Português o mecanismo é outro: reescrita mantendo o sentido, valor semântico dos conectivos, pronome que retoma o termo errado, vírgula que muda a função sintática. Nas questões de interpretação, a alternativa errada costuma **extrapolar o texto** ou **inverter causa e consequência**.

---

## 📊 Como a incidência decide o que importa

Três números entram na priorização, e os três vêm do material, não de opinião.

```mermaid
flowchart LR
    W["⚖️ Peso no edital<br/>questões da matéria na prova"] ==> PR{{"🎯 Prioridade"}}
    I["📈 Incidência observada<br/>questões por assunto no banco"] ==> PR
    ER["🩺 Erros do aluno<br/>registro do cofre"] ==> PR
    PR ==> O1["Ordem da revisão"]
    PR ==> O2["Profundidade da explicação"]
    PR ==> O3["Fila do plano"]
```

| Número | O que é | Onde está |
|---|---|---|
| ⚖️ **Peso no edital** | Quantas questões a matéria tem na prova. Na PC-PR, Português e Tecnologia têm 25 cada; cada ramo de Direito tem 3 | Lista de matérias dos scripts e no mapa |
| 📈 **Incidência observada** | Quantas questões de cada assunto existem no banco. Como os cadernos foram filtrados por banca, o volume por assunto é a incidência real daquela banca no recorte coletado | `questoes/INDICE.md`, assuntos em ordem |
| 🩺 **Erros do aluno** | Autópsia de erros e assuntos a treinar após simulado | Notas de registro do cofre |

> [!TIP]
> Um assunto com 253 questões (Interpretação de Textos) pesa mais que um com 4 (Pronomes Demonstrativos), e o professor trata os dois de acordo. Um pedido de "revisão de Português" volta com os conceitos **em ordem de incidência**; um pedido de "plano" cruza peso, incidência e erros; um tema com peso 3 recebe explicação curta, direto na literalidade que a banca cobra.

Para alimentar o professor com os assuntos mais importantes de um edital novo, basta exportar os cadernos daquela banca e rodar o parser. **A incidência se recalcula sozinha.**

---

## 📚 Cobertura atual

{tabela_cobertura}

> [!NOTE]
> Direitos Humanos não tem notebook. A cobertura vem das apostilas do cofre e das questões do banco.

### Assuntos por matéria, em ordem de incidência

{assuntos_por_materia}

### Aulas disponíveis no cofre

{aulas_por_materia}

---

## 🎯 Como usar no dia a dia

No Claude Code, `/professor` seguido do pedido, ou só a pergunta de matéria. A skill trata cada tipo de pedido de um jeito:

| Pedido | O que o professor entrega |
|---|---|
| 💬 "me explica X" | Definição curta, regra, exceção, uma questão real resolvida, pegadinhas codificadas |
| 🔁 "revisão de X" | Conceitos-chave em ordem de incidência |
| 📝 "questões de X" | Duas reais do banco e três inéditas no mesmo molde, com gabarito comentado |
| 🪤 "pegadinhas de X" | Pares "parece / é", cada um com código do catálogo |
| 🗓️ "plano" ou "o que estudar" | Cruzamento de peso, incidência e erros registrados |
| 🃏 "cards de X" | Itens certo/errado atômicos, prontos para importar no Anki |

> [!TIP]
> Depois de algumas centenas de cards com o código no verso, a cor e o código sozinhos já avisam o tipo de erro antes de você ler a explicação.

---

## 🔁 Ensinar o professor um edital novo

O que é específico do concurso está em poucos lugares.

```mermaid
flowchart LR
    E1["1. Notebooks<br/>um por matéria"] --> E2["2. Cadernos<br/>filtrados pela banca"] --> E3["3. Matérias e pesos<br/>lista G e tabela MAT"] --> E4["4. Cofre<br/>opcional"] --> E5["5. Banca<br/>estilo na SKILL"] --> E6["6. Rodar<br/>os scripts"] --> E7["7. Testar<br/>revisão da matéria de maior peso"]
```

**Passo 1. Notebooks.** Crie um notebook no NotebookLM por matéria do novo edital e suba o material (apostilas, aulas, leis). Notebooks de método e de edital são opcionais. Rode `notebooklm list` para confirmar que aparecem.

**Passo 2. Cadernos.** Na plataforma de questões, monte um caderno por matéria filtrado pela banca do concurso e exporte em markdown. Coloque os arquivos na pasta de cadernos do cofre (ou ajuste o caminho no topo de `_build/build_questoes.py`). Se a exportação vier em outro formato, o parser precisa de um quinto ramo; os quatro atuais estão comentados no início do script.

**Passo 3. Matérias e pesos.** Edite a lista `G` em `_build/build_mapa.py` e em `_build/make_readme.py`: nome da matéria como está no edital, número de questões, IDs dos notebooks. Edite a tabela `MAT` em `_build/build_questoes.py` para mapear os rótulos da plataforma para as matérias do edital.

**Passo 4. Cofre.** Se houver apostilas em markdown, organize uma pasta por matéria com aulas nomeadas `Aula NN - Assunto - {Resumo|Simplificada|Apostila completa}.md` e uma nota-hub `00 — Hub <Matéria>.md`. Ajuste os caminhos no topo de `_build/build_vault.py`. Sem cofre, o professor funciona só com notebooks e questões.

**Passo 5. Banca.** Na `SKILL.md`, troque o trecho "Como ensinar": os pesos e a descrição do estilo da banca. A FGV usa caso concreto e literalidade aplicada; outras bancas usam certo/errado ou cobram doutrina.

> [!TIP]
> Se a banca for outra, o catálogo de pegadinhas provavelmente muda de **proporção**, não de lista. P1, P2, P4 e P5 aparecem em qualquer banca que trabalhe com lei seca.

**Passo 6. Rodar.**

```bash
python _build/rebuild.py            # extrai os notebooks
python _build/gerar_guias.py        # dispara os guias completos no Studio
python _build/gerar_guias_temas.py  # dispara um guia por tema
python _build/baixar_guias.py 9     # baixa o que ficou pronto (repetir)
python _build/baixar_guias_temas.py 9
python _build/build_questoes.py     # banco de questões
python _build/build_vault.py        # índice do cofre
python _build/build_mapa.py         # mapa geral
```

**Passo 7. Testar.** Peça "revisão de <matéria de maior peso>". Se a ordem dos conceitos bater com os assuntos mais cobrados no `questoes/INDICE.md`, o professor aprendeu o edital.

---

## 🛠️ Instalação e reconstrução

```bash
pip install "notebooklm-py[browser]"
notebooklm login                       # autentica no Google uma vez
notebooklm auth check --test --json    # tem que devolver "token_fetch": true

mkdir -p ~/.claude/skills/professor && cp ferramenta/SKILL.md ~/.claude/skills/professor/
cp ferramenta/agent-professor.md ~/.claude/agents/professor.md
```

Os caminhos dentro da skill apontam para `C:\Users\USER\Professor`. Quem clonar em outro lugar precisa ajustar.

```
MAPA-GERAL.md          ponto de entrada: matérias, pesos, notebooks, contagens
notebooks/             um arquivo por notebook (índice, conceitos, pegadinhas, fontes)
guias/                 guia completo por notebook e, nos de matéria, um guia por tema
questoes/INDICE.md     contagem de questões por matéria e assunto (a incidência)
vault/INDICE-VAULT.md  aulas, cadernos e notas do cofre, por matéria
materiais/             guias de estudo, quizzes, flashcards, mapas mentais gerados
ferramenta/            SKILL.md e agent-professor.md para o Claude Code
_build/                scripts e prompts
```

Os arquivos com as questões na íntegra e as notas pessoais do cofre ficam fora do repositório. Só os índices sobem.

---

## ⚠️ Limitações

> [!WARNING]
> - As sínteses e os guias são gerados por modelo de linguagem a partir das fontes. Podem omitir detalhes; por isso a skill consulta o notebook ao vivo quando os arquivos não bastam.
> - Cada relatório do Studio tem teto de tamanho. Por isso existe um guia por tema, não só um por notebook.
> - O comando `notebooklm ask --new` **apaga o histórico de chat** do notebook. Nenhum script deste repositório usa a opção.
> - Pedidos muito longos ao chat falham com `RPCResponseTooLargeError`, um erro de streaming da ferramenta que não depende do tamanho do notebook. Os scripts tentam de novo com um prompt compacto.
> - {n_sem_alt} questões vieram sem alternativas legíveis por causa de exportações achatadas; estão no banco marcadas.
> - O banco reflete o recorte coletado pelo aluno, não o universo de questões da banca.

---

## 🗺️ Mapa

```mermaid
mindmap
  root((Professor))
    Bases
      Notebooks do NotebookLM
      Questões reais com gabarito
      Cofre com apostilas e erros
    Extração
      Três perguntas no chat
      Relatórios no Studio por tema
      Parser de quatro formatos
      Dedup por ID da fonte
    Priorização
      Peso no edital
      Incidência por assunto
      Erros do aluno
    Banca FGV
      Cinco alternativas
      Caso concreto antes da pergunta
      Alternativa quase certa
      Códigos P1 a P10 e T1 a T4
    Uso
      Explicar
      Revisar
      Questões
      Pegadinhas
      Plano
      Cards Anki
    Outro edital
      Notebooks novos
      Cadernos da banca
      Pesos e mapa de matérias
      Estilo da banca na skill
```

---

## 📌 Cola rápida

| Pilar | Em uma frase |
|---|---|
| 🎓 **O que é** | Um tutor no Claude Code que responde a partir do seu material, no recorte da banca |
| 🧩 **Bases** | Notebooks, questões reais e anotações, cruzados num mapa por matéria |
| ⚖️ **Prioridade** | Peso no edital × incidência por assunto × seus erros |
| 🪤 **Banca** | Cinco alternativas, história antes da pergunta, e uma "quase certa" que troca uma palavra |
| 🔍 **Questões** | 44 arquivos, 4 formatos, dedup por ID, 13 matérias, {n_questoes} questões únicas |
| 🔁 **Outro edital** | Notebooks novos, cadernos da banca, lista de pesos, estilo na skill, rodar os scripts |
| 🛠️ **Ferramentas** | NotebookLM por CLI, Obsidian, Claude Code, Anki, Python padrão |

---

## 📄 Licença e uso do conteúdo

> [!CAUTION]
> **Proibida a venda.** Este material é para **estudo pessoal e particular**. Nenhuma pessoa pode vendê-lo, revendê-lo, incluí-lo em curso, mentoria, assinatura, grupo pago ou qualquer produto comercial, nem monetizá-lo de forma direta ou indireta. A proibição vale para o autor deste repositório e para qualquer pessoa que obtenha o material. Leia o [AVISO-DE-USO.md](AVISO-DE-USO.md).

> [!NOTE]
> **Pode:** ler, copiar para uso próprio, adaptar ao seu concurso e compartilhar com outros estudantes, sempre sem cobrança.
>
> **Scripts e skill** (`_build/`, `ferramenta/`) estão sob licença MIT: use à vontade para montar a sua própria base a partir do seu próprio material.
>
> **Origem:** os arquivos em `notebooks/`, `guias/`, `materias/` e `materiais/` são sínteses geradas por modelo de linguagem a partir do material de estudo do autor. Não reproduzem apostilas, aulas nem questões na íntegra. Apostilas de curso, enunciados completos e anotações pessoais não estão no repositório.
>
> **Sem garantia:** síntese gerada por modelo pode conter erro. Confira na fonte primária antes de decidir por ela.

## 🔎 Palavras-chave

Para quem chegou aqui procurando: professor de concurso com inteligência artificial, tutor de concurso público, estudo por questões, engenharia reversa de banca, estudo reverso FGV, como a FGV cobra, pegadinhas da FGV, incidência de assuntos por banca, NotebookLM para concursos, NotebookLM CLI, Claude Code skill, Obsidian para concurso, Anki para concurso, flashcards certo ou errado, carreiras policiais, Polícia Civil do Paraná, PC-PR 2026, agente de polícia judiciária, banco de questões em markdown, plano de estudo por incidência.

`#concurso` `#concursopublico` `#professordeconcurso` `#estudoporquestoes` `#engenhariareversa` `#estudoreverso` `#FGV` `#pegadinhasFGV` `#NotebookLM` `#ClaudeCode` `#Obsidian` `#Anki` `#carreiraspoliciais` `#PCPR2026` `#policiacivil` `#bancodequestoes` `#incidencia` `#tutorIA`

Extração e montagem feitas em 05/09/2026.
