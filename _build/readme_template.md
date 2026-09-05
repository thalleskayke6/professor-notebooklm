# Professor NotebookLM: como transformei 23 notebooks em um professor particular

Eu estudo para o concurso de Agente de Polícia Judiciária da PC-PR 2026, banca FGV. Ao longo dos meses fui jogando tudo no Google NotebookLM: apostilas, aulas em vídeo, artigos, leis, prompts que escrevi para gerar questões. Deu 23 notebooks e 819 fontes. O problema é que o NotebookLM responde bem a uma pergunta de cada vez, mas não sabe olhar para o conjunto. Eu queria alguém que tivesse lido tudo aquilo e soubesse me explicar qualquer tema do edital do jeito que a FGV cobra.

Este repositório é o resultado. Tem duas partes: a base de conhecimento, que é o conteúdo dos notebooks convertido em markdown, e a ferramenta, que é o script que monta essa base mais a skill do Claude Code que a usa para responder.

## A ideia em uma imagem

```
NotebookLM (23 notebooks, 819 fontes)
        |  notebooklm-py CLI  (summary, source list, ask, download)
        v
_build/rebuild.py  -->  notebooks/<slug>.md   (indice + conceitos + pegadinhas + fontes)
                   -->  materiais/            (guias, quizzes, flashcards, notas, mapas mentais)
                   -->  MAPA-GERAL.md         (indice por materia, peso na prova, ID do notebook)
        |
        v
Skill /professor (Claude Code)  -->  le o MAPA-GERAL, abre o notebook certo, responde no estilo FGV
                                -->  se faltar detalhe: `notebooklm ask "..." -n <ID>` ao vivo
```

## Como a base é extraída

Não dá para baixar o texto de 819 fontes e esperar que um modelo leia tudo a cada pergunta. O caminho que funcionou foi pedir ao próprio NotebookLM que resumisse cada notebook de três ângulos diferentes. Cada ângulo é um prompt fixo, guardado em `_build/`, enviado com `notebooklm ask`.

| Prompt | O que pede | Seção que gera |
|---|---|---|
| `p_indice.txt` | Um índice hierárquico de todos os temas e subtemas, cobrindo todas as fontes e não só as primeiras | Índice hierárquico |
| `p_conceitos.txt` | Definições, regras, classificações, prazos, números, fórmulas e exceções, tema a tema | Conceitos-chave por tema |
| `p_pegadinhas.txt` | O que se confunde com o quê, o que a FGV costuma cobrar, quais temas dependem de quais, o que o notebook não cobre | Pegadinhas, relações e lacunas |

Além das três perguntas, o script baixa o resumo automático que o NotebookLM já faz para cada notebook, a lista de fontes, as notas que eu tinha salvo lá dentro e os artefatos que já existiam: relatórios, quizzes, flashcards, mapas mentais e tabelas.

O notebook do Valter Rodrigues foi a exceção. São 63 vídeos e um pedido único estourava o limite de resposta do CLI. Ele foi extraído em cinco partes temáticas: índice, metodologia de estudo, mentalidade, Anki com IA, e o plano de aprovação.

Tudo isso é idempotente. Se eu rodar `rebuild.py` de novo, ele só refaz o que estiver faltando. Quando quero forçar um notebook inteiro, passo `--force` com o ID.

## Como os arquivos são montados

O `build.py` junta, para cada notebook, o resumo automático, as três respostas, a lista de materiais baixados e a lista de fontes, e grava um arquivo em `notebooks/`. O `build_mapa.py` gera o `MAPA-GERAL.md`, que agrupa os notebooks por matéria da prova.

O agrupamento carrega o peso de cada matéria, porque isso muda como se estuda. Pelo Edital 01/2026, a prova do Agente tem 100 questões de peso 1. Português e Tecnologia valem 25 cada, ou seja, metade da prova. Ciências Forenses vale 10. Lógica, Realidade do Paraná, Contabilidade, Estatística e Legislação Estadual valem 5 cada. Direito Penal, Processo Penal, Constitucional, Administrativo e Direitos Humanos valem 3 cada. Um professor que não sabe disso gasta o mesmo tempo em tudo.

## Como o professor responde

A skill fica em `ferramenta/SKILL.md`. Copiada para `~/.claude/skills/professor/`, ela vira o comando `/professor` no Claude Code. Quando recebe uma pergunta, segue esta ordem:

1. Lê o `MAPA-GERAL.md` e escolhe o notebook pela matéria.
2. Lê o arquivo do notebook em `notebooks/`. Se a pergunta for pontual, faz Grep em vez de ler o arquivo inteiro, porque alguns passam de 100 KB.
3. Se o arquivo não tiver o detalhe pedido, pergunta ao notebook ao vivo com `notebooklm ask "..." -n <ID>`.
4. Responde no estilo da FGV: a letra da lei aplicada a um caso concreto, o parágrafo que ninguém lê, a alternativa quase certa. Sempre fecha com as pegadinhas do tema e diz de qual notebook a informação veio.
5. Calibra a profundidade pelo peso da matéria na prova.

Ela sabe explicar, revisar, gerar questões, listar pegadinhas, montar plano de estudo e escrever cards para o Anki no padrão do prompt v5.3 que está em `materiais/`. O arquivo `ferramenta/agent-professor.md` é a mesma coisa em formato de subagente.

## O que tem em cada pasta

```
MAPA-GERAL.md          indice geral por materia (comece aqui)
notebooks/             23 arquivos, um por notebook (todos os conceitos)
materiais/             {n_mats} guias de estudo, quizzes, flashcards, notas e mapas mentais
ferramenta/            SKILL.md (skill Claude Code) e agent-professor.md
_build/                rebuild.py, build.py, build_mapa.py, dl.py, prompts, nb_index.json
```

## Instalação

```bash
pip install "notebooklm-py[browser]"
notebooklm login                       # autentica no Google uma vez
notebooklm auth check --test --json    # tem que devolver "token_fetch": true

# instalar o professor no Claude Code
mkdir -p ~/.claude/skills/professor && cp ferramenta/SKILL.md ~/.claude/skills/professor/
cp ferramenta/agent-professor.md ~/.claude/agents/professor.md

# reconstruir ou atualizar a base depois de adicionar fontes ou notebooks
python _build/rebuild.py
python _build/rebuild.py --force <ID-do-notebook>
```

Depois disso, no Claude Code: `/professor me explica cadeia de custódia com as pegadinhas da FGV`.

Os caminhos dentro da skill apontam para `C:\Users\USER\Professor`. Quem clonar em outro lugar precisa ajustar.

## O que quebrou no caminho

Anoto aqui porque perdi tempo com cada um desses.

O `notebooklm ask --new` apaga o histórico de chat do notebook. Eu usei sem saber no primeiro lote e perdi as conversas de dois notebooks antes de perceber. O `rebuild.py` não usa essa flag em lugar nenhum.

Pedidos muito grandes ao `ask` falham com `RPCResponseTooLargeError`. Não tem a ver com o tamanho do notebook: um notebook de três PDFs falhou tanto quanto um de 50 páginas web. É um bug de streaming do CLI. O que resolve é perguntar em partes, ou pedir uma resposta compacta, com no máximo 90 linhas e sem citar fontes. Os prompts `pc_*.txt` fazem isso e o script usa eles como segunda tentativa automática.

A sessão do Google expira no meio de lotes longos. Se o perfil do navegador ainda estiver logado, `notebooklm login` resolve sozinho, sem abrir nada para clicar.

Para rodar vários notebooks em paralelo, o jeito é passar `-n <ID>` em cada comando. O `notebooklm use` grava um contexto compartilhado e os lotes atropelam uns aos outros.

## O que está coberto

Todos os conceitos estão em `notebooks/`. A tabela abaixo mostra os temas de primeiro nível de cada índice.

{tabela}

Direitos Humanos vale 3 questões e não tem notebook. É a única matéria do edital sem cobertura.

## Materiais baixados

{materiais}

## Sobre os dados

A extração foi feita em 05/09/2026 com o notebooklm-py v0.8.1. Os arquivos em `notebooks/` são sínteses que o NotebookLM gerou a partir das minhas fontes. O texto integral das fontes não está aqui.
