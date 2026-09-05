# Como usar

Guia para quem baixou este repositório e quer estudar com ele. Funciona de dois jeitos:

- **Modo leitura**, sem instalar nada: você abre os arquivos e estuda. Serve em qualquer computador ou celular.
- **Modo professor**, com uma inteligência artificial lendo os arquivos e te ensinando. Funciona no Claude Code, no Claude, no ChatGPT, no Gemini e no NotebookLM.

> [!CAUTION]
> **Uso exclusivo para estudo pessoal. Venda proibida.** Ninguém pode vender, revender, incluir em curso, mentoria, assinatura ou grupo pago, nem monetizar este material. Ver [AVISO-DE-USO.md](AVISO-DE-USO.md) e [LICENSE](LICENSE).

---

## 1. Baixar

### Com git

```bash
git clone https://github.com/thalleskayke6/skill-professor-concurso-publico.git professor
cd professor
```

### Sem git

Abra <https://github.com/thalleskayke6/skill-professor-concurso-publico>, clique no botão verde **Code** e depois em **Download ZIP**. Descompacte onde quiser.

Guarde o caminho da pasta. Ele aparece adiante como `<PASTA-DO-REPOSITORIO>`. Exemplos:

| Sistema | Caminho típico |
|---|---|
| Windows | `C:\Users\seu-usuario\professor` |
| Mac ou Linux | `/home/seu-usuario/professor` ou `~/professor` |

---

## 2. Modo leitura: só estudar os arquivos

Não precisa instalar nada. Comece por aqui:

| Quero | Abra |
|---|---|
| Ver tudo por matéria | [`materias/README.md`](materias/README.md) |
| Estudar uma matéria | `materias/<matéria>/README.md` |
| Teoria completa de um tema | `materias/<matéria>/temas-*/NN-tema.md` |
| Saber o que mais cai | [`questoes/INDICE.md`](questoes/INDICE.md), assuntos em ordem de incidência |
| Visão geral do projeto | [`MAPA-GERAL.md`](MAPA-GERAL.md) |

Os arquivos são markdown puro. Ficam legíveis no GitHub, no bloco de notas, no Obsidian, no Notion e em qualquer leitor de markdown do celular.

**Sugestão de uso no Obsidian:** copie a pasta `materias/` para dentro do seu cofre. Os títulos, tabelas e listas já vêm formatados.

---

## 3. Modo professor no Claude Code

É o modo completo: o professor lê os arquivos sozinho, cruza teoria com as questões e responde no recorte da banca.

### Instalar

**Windows (PowerShell):**

```powershell
mkdir "$env:USERPROFILE\.claude\skills\professor" -Force
copy "<PASTA-DO-REPOSITORIO>\ferramenta\SKILL.md" "$env:USERPROFILE\.claude\skills\professor\"
copy "<PASTA-DO-REPOSITORIO>\ferramenta\agent-professor.md" "$env:USERPROFILE\.claude\agents\professor.md"
```

**Mac ou Linux:**

```bash
mkdir -p ~/.claude/skills/professor ~/.claude/agents
cp ferramenta/SKILL.md ~/.claude/skills/professor/
cp ferramenta/agent-professor.md ~/.claude/agents/professor.md
```

### Ajustar o caminho

Abra `~/.claude/skills/professor/SKILL.md` e troque **todas** as ocorrências de `<PASTA-DO-REPOSITORIO>` pelo caminho onde você baixou o repositório. São 6 ocorrências.

### Usar

Abra o Claude Code dentro da pasta do repositório e peça:

```
/professor me explica cadeia de custódia com as pegadinhas da banca
```

Ou simplesmente faça a pergunta: a skill dispara sozinha em pergunta de matéria.

---

## 4. Modo professor no Claude (site ou aplicativo)

Use **Projetos**, que aceitam arquivos como base de conhecimento.

1. Crie um projeto novo em <https://claude.ai>.
2. Em **Instruções do projeto**, cole o conteúdo de `ferramenta/SKILL.md`, apagando as linhas entre os dois `---` do começo e trocando os caminhos por "os arquivos anexados a este projeto".
3. Em **Conhecimento do projeto**, suba os arquivos da matéria que você vai estudar: o `README.md` da matéria, os guias por tema e o `questoes/INDICE.md`.
4. Converse normalmente: "me explica prescrição", "monta 10 questões de coesão", "quais as pegadinhas de improbidade".

> [!TIP]
> Não suba tudo de uma vez. Um projeto por matéria funciona melhor: o modelo acerta mais quando o material está focado.

---

## 5. Modo professor no ChatGPT

Duas formas:

**Projetos (mais simples).** Crie um projeto, cole o conteúdo de `ferramenta/SKILL.md` nas instruções e anexe os arquivos da matéria.

**GPT personalizado (reutilizável).** Em **Explorar GPTs → Criar**, cole a skill em *Instructions* e suba os arquivos em *Knowledge*. Depois é só abrir o GPT sempre que for estudar.

---

## 6. Modo professor no Gemini

**Gems.** Crie uma Gem nova, cole o conteúdo de `ferramenta/SKILL.md` nas instruções e anexe os arquivos da matéria.

**NotebookLM (recomendado para este material).** Crie um notebook, suba os arquivos `.md` da matéria como fontes e pergunte direto. O NotebookLM cita o trecho de origem de cada resposta, o que ajuda a conferir.

---

## 7. Como pedir as coisas

Vale em qualquer uma das ferramentas acima:

| Pedido | O que volta |
|---|---|
| `me explica <tema>` | Definição curta, regra, exceção, questão real resolvida e as pegadinhas |
| `revisão de <matéria>` | Conceitos-chave na ordem do que mais cai |
| `10 questões de <tema>` | Questões no estilo da banca, com gabarito comentado |
| `pegadinhas de <tema>` | Pares "parece / é", com o código do tipo de armadilha |
| `o que estudar essa semana` | Cruzamento de peso na prova, incidência e seus erros |
| `cards de <tema>` | Itens certo/errado prontos para o Anki |
| `simulado de <matéria>` | Bateria com correção comentada no fim |

---

## 8. Adaptar para o seu concurso

O material vem preenchido com a prova de Agente da Polícia Civil do Paraná de 2026, banca FGV. Para outro edital, veja a seção **Ensinar o professor um edital novo** no [README](README.md#-ensinar-o-professor-um-edital-novo). O resumo:

1. Ajuste as matérias e os pesos em `_build/build_mapa.py`.
2. Exporte cadernos de questões da sua banca em markdown e rode `python _build/build_questoes.py`.
3. Troque a descrição do estilo da banca em `SKILL.md`.

Sem tocar em código, dá para usar assim mesmo: as partes de método de estudo, o catálogo de pegadinhas e a forma de montar cards servem para qualquer concurso.

---

## 9. Problemas comuns

| Sintoma | Causa e solução |
|---|---|
| O professor responde genérico, sem citar os arquivos | O caminho em `SKILL.md` está errado. Confira se `<PASTA-DO-REPOSITORIO>` foi trocado e se a pasta existe |
| `/professor` não aparece no Claude Code | O arquivo precisa estar em `~/.claude/skills/professor/SKILL.md`. Reinicie o Claude Code |
| Ferramenta reclama do tamanho do arquivo | Suba um arquivo por vez, ou só o `README.md` da matéria e os temas que interessam |
| Faltam as questões com enunciado completo | Elas não estão no repositório, são de terceiros. O que existe é a contagem por assunto, que é a incidência |
| Os comandos `notebooklm` dão erro | Só servem para quem vai montar a própria base a partir dos próprios notebooks. Para estudar pelo material pronto, não precisa deles |
