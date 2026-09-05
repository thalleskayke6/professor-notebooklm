# Professor: um tutor de concurso construído sobre NotebookLM, Obsidian e um banco de questões reais

## Resumo

Este repositório documenta a construção de um tutor automatizado para a prova de Agente de Polícia Judiciária da Polícia Civil do Paraná (Edital 01/2026, banca FGV). O tutor combina três bases: {n_notebooks} notebooks do Google NotebookLM com {n_fontes} fontes, um cofre do Obsidian com {n_aulas} aulas em formato markdown distribuídas por {n_materias_vault} matérias, e um banco de {n_questoes} questões reais de concurso, deduplicadas e com gabarito, classificadas em {n_assuntos} assuntos. Um conjunto de scripts em Python extrai, normaliza e indexa esse material; uma skill do Claude Code o consulta na hora de responder. O texto descreve as fontes, o pipeline, a cobertura por matéria e assunto, o modo de uso e o que é preciso mudar para reaproveitar a estrutura em outro edital.

## 1. O problema

Quem estuda para concurso acumula material em três lugares que não conversam entre si. As apostilas e videoaulas ficam em um serviço de anotações. Os cadernos de questões ficam na plataforma onde foram resolvidos. As anotações de método, o plano de estudo e o registro de erros ficam em um terceiro lugar. Cada ferramenta responde bem a uma pergunta de cada vez sobre o próprio acervo, mas nenhuma sabe cruzar as três coisas: o que a apostila ensina, como a banca cobra isso na prática e onde o aluno está errando.

O objetivo aqui foi montar um único "professor" que tivesse lido tudo, soubesse o peso de cada matéria na prova e respondesse no recorte da banca, com questões reais como referência.

## 2. Materiais

A base foi montada a partir de três origens. Nomes de autores, cursos e plataformas foram omitidos de propósito; o que importa para reprodução é o tipo de material e o formato.

**Notebooks do NotebookLM.** {n_notebooks} notebooks com {n_fontes} fontes no total: apostilas em PDF, videoaulas, artigos, textos de lei, planilhas e prompts. Treze deles cobrem matérias do edital; seis tratam de método de estudo, memória e mentalidade; um trata de engenharia de prompts; um contém o edital.

**Cofre do Obsidian.** Cerca de 440 notas em markdown. As principais são as apostilas convertidas de PDF, uma por aula, em até três versões (resumo, simplificada e completa), organizadas em {n_materias_vault} matérias com uma nota-hub por matéria. Além delas, notas curadas de método (um catálogo de pegadinhas da banca com códigos fixos, instruções para geração de flashcards), plano de estudo (pesos, ciclo de blocos, reta final) e registro (análise de erros, assuntos a treinar após simulado).

**Cadernos de questões.** Exportações em markdown de uma plataforma de questões, filtradas por banca. Havia 44 arquivos com forte sobreposição (o mesmo caderno exportado mais de uma vez). Após deduplicação pelo identificador da questão na fonte, restaram {n_questoes} questões únicas, {n_gabarito} delas com gabarito.

## 3. Método

### 3.1 Extração dos notebooks

O NotebookLM não expõe o texto consolidado de um notebook. A solução foi perguntar ao próprio NotebookLM, por linha de comando, três coisas sobre cada notebook, com prompts fixos:

| Prompt | Pergunta | Seção gerada |
|---|---|---|
| `p_indice.txt` | Índice hierárquico de todos os temas e subtemas, cobrindo todas as fontes | Índice hierárquico |
| `p_conceitos.txt` | Definições, regras, classificações, prazos, números, fórmulas e exceções por tema | Conceitos-chave por tema |
| `p_pegadinhas.txt` | O que se confunde com o quê, o que a banca cobra, dependências entre temas, lacunas | Pegadinhas, relações e lacunas |

O script também baixa o resumo automático de cada notebook, a lista de fontes, as notas salvas e os artefatos já gerados (relatórios, quizzes, flashcards, mapas mentais, tabelas). O notebook de videoaulas de método, com 63 vídeos, precisou ser extraído em cinco partes temáticas porque um pedido único estourava o limite de resposta da ferramenta.

### 3.2 Extração das questões

Os cadernos vieram em quatro formatos diferentes de markdown, conforme a época e a ferramenta de exportação. O parser reconhece os quatro: cabeçalho com link para a fonte e gabarito em tabela no fim do bloco; cabeçalho com link em rodapé; exportação bruta com linha de banca, linha de matéria e assunto e gabarito inline; e exportação achatada em uma linha por questão. Cada questão é registrada com identificador, banca e órgão, matéria, assunto, enunciado, alternativas, gabarito e arquivo de origem. As 91 rotulagens de matéria encontradas nas fontes foram normalizadas para as 13 matérias do edital mais Legislação Penal Extravagante.

### 3.3 Índice do cofre

Um terceiro script percorre o cofre, lista cada aula com versão e tamanho, associa os cadernos de questões e as notas soltas à matéria correspondente e copia as notas curadas pequenas (hubs, método, plano, registro) para consulta direta. Apostilas e despejos de curso ficam apenas referenciados por caminho, por tamanho e por direitos autorais.

### 3.4 Montagem

Um arquivo por notebook junta resumo, as três respostas, materiais e fontes. Um mapa geral agrupa tudo por matéria da prova, com o peso de cada uma e a contagem de questões reais disponíveis. Todos os passos são idempotentes: rodar de novo só refaz o que falta.

### 3.5 O tutor

A skill (`ferramenta/SKILL.md`) descreve como o assistente deve responder. A ordem é fixa: ler o mapa e escolher a matéria; buscar o tema no arquivo do notebook; buscar o assunto no arquivo de questões e usar duas ou três questões reais como molde; se faltar teoria, abrir a aula certa do cofre; se ainda faltar, perguntar ao notebook ao vivo. A profundidade é proporcional ao peso da matéria. Toda explicação termina com as pegadinhas do tema, codificadas pelo catálogo do usuário (P1 a P10 para pegadinhas jurídicas, T1 a T4 para técnicas). O registro de erros do aluno entra na priorização.

## 4. Cobertura

A prova tem 100 questões de peso igual. A tabela abaixo cruza cada matéria com o que existe na base.

{tabela_cobertura}

Direitos Humanos não tem notebook no NotebookLM. A cobertura dessa matéria vem das apostilas do cofre e das questões do banco.

### 4.1 Assuntos por matéria

Os assuntos abaixo são os rótulos usados pela própria plataforma de questões, ordenados pelo número de questões no banco. Essa ordem é, na prática, a incidência observada da banca no recorte coletado.

{assuntos_por_materia}

### 4.2 Aulas disponíveis no cofre

{aulas_por_materia}

## 5. Como usar

### 5.1 Instalação

```bash
pip install "notebooklm-py[browser]"
notebooklm login                       # autentica no Google uma vez
notebooklm auth check --test --json    # tem que devolver "token_fetch": true

mkdir -p ~/.claude/skills/professor && cp ferramenta/SKILL.md ~/.claude/skills/professor/
cp ferramenta/agent-professor.md ~/.claude/agents/professor.md
```

### 5.2 Reconstrução

```bash
python _build/rebuild.py                 # notebooks: só refaz o que falta
python _build/rebuild.py --force <ID>    # refaz um notebook inteiro
python _build/build_questoes.py          # cadernos novos no cofre
python _build/build_vault.py             # notas novas no cofre
python _build/build_mapa.py              # mapa geral
```

### 5.3 Uso no dia a dia

No Claude Code, `/professor` seguido do pedido. Exemplos de pedidos que a skill trata de forma diferente:

| Pedido | O que o tutor entrega |
|---|---|
| "me explica X" | Definição curta, regra, exceção, uma questão real resolvida, pegadinhas codificadas |
| "revisão de X" | Conceitos-chave em ordem de incidência |
| "questões de X" | Duas reais do banco e três inéditas no mesmo molde, com gabarito comentado |
| "pegadinhas de X" | Pares "parece / é", cada um com código |
| "plano" | Cruzamento de peso da prova, erros registrados e volume de questões por assunto |
| "cards de X" | Itens certo/errado atômicos no formato de importação do Anki |

### 5.4 Estrutura do repositório

```
MAPA-GERAL.md          ponto de entrada: matérias, pesos, notebooks, contagens
notebooks/             um arquivo por notebook (índice, conceitos, pegadinhas, fontes)
questoes/INDICE.md     contagem de questões por matéria e assunto
vault/INDICE-VAULT.md  aulas, cadernos e notas do cofre, por matéria
materiais/             guias de estudo, quizzes, flashcards, mapas mentais gerados
ferramenta/            SKILL.md e agent-professor.md para o Claude Code
_build/                scripts e prompts
```

Os arquivos com as questões na íntegra (`questoes/*.md`, `questoes/banco.json`) e as notas pessoais copiadas do cofre (`vault/notas/`) ficam fora do repositório. O índice de contagens está incluído.

## 6. Reaproveitamento em outro edital

A estrutura não depende do concurso. O que é específico da PC-PR está em poucos lugares:

1. **Pesos e matérias.** A lista `G` em `_build/build_mapa.py` e `_build/make_readme.py` define as matérias, o peso e quais notebooks pertencem a cada uma. Troque pelos blocos do novo edital.
2. **Notebooks.** `_build/nb_index.json` é gerado a partir de `notebooklm list`. Qualquer conjunto de notebooks serve; o `rebuild.py` descobre notebooks novos sozinho.
3. **Cofre.** `build_vault.py` espera uma pasta por matéria com aulas nomeadas `Aula NN - Assunto - {Resumo|Simplificada|Apostila completa}.md` e uma nota-hub `00 — Hub <Matéria>.md`. Ajuste os caminhos no topo do script.
4. **Cadernos.** `build_questoes.py` lê qualquer exportação em markdown com o link da questão na fonte. A tabela `MAT` no script mapeia os rótulos de matéria da plataforma para as matérias do edital; é ela que muda de concurso para concurso.
5. **Skill.** O trecho "Como ensinar" da `SKILL.md` traz os pesos e o estilo da banca. Para outra banca, troque a descrição do estilo (a FGV usa caso concreto e literalidade aplicada; outras bancas usam certo/errado ou cobram doutrina).

Os prompts de extração e o parser de questões são genéricos. O catálogo de pegadinhas com códigos vale para qualquer banca que trabalhe com lei seca.

## 7. Limitações

- As sínteses dos notebooks são geradas por modelo de linguagem a partir das fontes. Podem omitir detalhes; por isso a skill consulta o notebook ao vivo quando o arquivo não basta.
- O comando `notebooklm ask --new` apaga o histórico de chat do notebook. Foi usado uma vez por engano durante a montagem; nenhum script deste repositório usa a opção.
- Pedidos muito longos ao NotebookLM falham com `RPCResponseTooLargeError`, um erro de streaming da ferramenta que não depende do tamanho do notebook. Os scripts tentam de novo com um prompt compacto.
- Cerca de {n_sem_alt} questões vieram sem alternativas legíveis por causa de exportações achatadas; estão no banco marcadas, sem alternativas.
- O banco reflete o recorte coletado pelo aluno, não o universo de questões da banca.

## 8. Ferramentas usadas

- Google NotebookLM, acessado pela linha de comando `notebooklm-py` v0.8.1.
- Obsidian, como cofre de notas em markdown.
- Claude Code, onde a skill roda.
- Anki, destino dos flashcards gerados pelo método descrito nas notas de método.
- Python 3, sem dependências além da biblioteca padrão para os scripts de montagem.

Extração e montagem feitas em 05/09/2026.
