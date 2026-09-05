import json, os, io, sys, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
rows = {r['id']: r for r in json.load(open('_build/nb_index.json', encoding='utf-8'))}
G = [("Edital", ["b342beb3-7cc4-497e-b473-5e77c5195673"]),
     ("Língua Portuguesa (25 q)", ["5beaebcc-a76f-426c-9551-c4bd3e527600", "e5690053-99e5-4d7e-87e8-98e697a3d047", "ae986a01-c8f9-46fe-9da4-b8e614a86d10"]),
     ("Tecnologia / Segurança Cibernética (25 q)", ["546f0cb3-6aab-4b5b-97ac-7e8c7adec19c"]),
     ("Ciências Forenses (10 q)", ["367433a3-ad6a-4cf4-9ff1-8221a4c6abb3", "8498c1e7-ece3-49b4-9b95-65c9785541b7"]),
     ("Raciocínio Lógico (5 q)", ["5714ea7c-de27-44b2-aab4-aeb30121b411"]),
     ("Realidade do Paraná (5 q)", ["42b917ff-915d-4b69-9b5e-e4bda9a4a232"]),
     ("Contabilidade (5 q)", ["73efc3d0-2a26-482e-a98a-f65ee6f3b538"]),
     ("Estatística (5 q)", ["185c9e3e-c37f-4324-9856-9dd96ac71661"]),
     ("Legislação Estadual (5 q)", ["bee037d5-0f9b-4125-ac6e-691b183e57fa"]),
     ("Direito Penal (3 q)", ["66410a65-3c39-4c6e-b49f-9b2ddcafa4a7"]),
     ("Processo Penal (3 q)", ["ff239db3-703f-43fd-8240-2fbb1843f9fb"]),
     ("Constitucional (3 q)", ["b63c5fdb-187a-4616-a267-e9ac15a926f6"]),
     ("Administrativo (3 q)", ["01d11b38-610b-49dd-b95d-1c04513c2b75"]),
     ("Método, memória e mentalidade", ["84eec3f0-185a-475a-bbdb-171dac0733e1", "02ef5b8b-6409-48c5-8066-36b557273692", "8677f4e5-7a16-4a97-a42c-0cb1db02883a", "3b393eaf-1dc1-498c-bd6f-e45d24abb17d", "130465ab-f48f-42c5-9b49-4c015e948c4e", "17b41580-33c9-4eb0-9e58-ed2ad79e84ac"]),
     ("IA e prompts", ["831dba20-e87e-4e71-a1d9-e03a9f05deb3"])]


def temas(slug):
    t = open(f'notebooks/{slug}.md', encoding='utf-8').read()
    m = re.search(r'## Índice hierárquico\n(.*?)\n## ', t, re.S)
    if not m:
        return []
    hs = [h.strip().replace('|', '/') for h in re.findall(r'^###\s+(.+)$', m.group(1), re.M)]
    return hs[:14]


tbl = ["| Área | Notebook | Fontes | Temas principais |", "|---|---|---|---|"]
for area, ids in G:
    for i in ids:
        r = rows[i]
        th = temas(r['slug'])
        tbl.append(f"| {area} | [{r['title']}](notebooks/{r['slug']}.md) | {r['n']} | {'; '.join(th)} |")
mats = sorted(os.listdir('materiais'))
NL = '\n'
README = f"""# Professor NotebookLM — PC-PR 2026

Um "professor particular" para o Claude Code que domina o conteúdo de **23 notebooks do Google NotebookLM** (819 fontes: apostilas, vídeos, artigos, leis, prompts). Cobre todas as matérias da prova de Agente de Polícia Judiciária da PC-PR 2026 (banca FGV) e os notebooks de método de estudo, memória e IA.

Este repositório contém **a base de conhecimento extraída** (conceitos de todos os notebooks, em markdown) e **a ferramenta** que a mantém e a usa.

## Como funciona

```
NotebookLM (23 notebooks, 819 fontes)
        │  notebooklm-py CLI  (summary, source list, ask, download)
        ▼
_build/rebuild.py  ──►  notebooks/<slug>.md   (índice + conceitos + pegadinhas + fontes)
                   ──►  materiais/            (guias, quizzes, flashcards, notas, mapas mentais)
                   ──►  MAPA-GERAL.md         (índice por matéria, peso na prova, ID do notebook)
        │
        ▼
Skill /professor (Claude Code)  ──►  lê MAPA-GERAL → abre o notebook certo → responde no estilo FGV
                                ──►  se faltar detalhe: `notebooklm ask "..." -n <ID>` ao vivo
```

### 1. Extração

Para cada notebook o script faz três perguntas ao NotebookLM (via `notebooklm ask`), cada uma com um prompt fixo em `_build/`:

| Prompt | Pergunta | Vira a seção |
|---|---|---|
| `p_indice.txt` | Índice hierárquico completo de todos os temas e subtemas, cobrindo todas as fontes | **Índice hierárquico** |
| `p_conceitos.txt` | Definições, regras, classificações, prazos, números, fórmulas, exceções por tema | **Conceitos-chave por tema** |
| `p_pegadinhas.txt` | O que se confunde com o quê, o que a FGV cobra, dependências entre temas, lacunas | **Pegadinhas, relações e lacunas** |

Além disso baixa o resumo automático do notebook, a lista de fontes, as notas do usuário e os artefatos já gerados (relatórios, quizzes, flashcards, mapas mentais, tabelas). O notebook "Valter Rodrigues" (63 vídeos) foi extraído em 5 partes temáticas porque o pedido único estourava o limite do CLI.

Tudo é **idempotente**: `rebuild.py` só refaz o que estiver faltando ou o que for forçado com `--force <ID>`.

### 2. Montagem

`build.py` junta resumo + três respostas + materiais + fontes em um arquivo por notebook. `build_mapa.py` gera o `MAPA-GERAL.md` agrupando os notebooks por matéria da prova, com o peso de cada uma (Edital 01/2026, cargo de Agente: Português e Tecnologia valem 25 questões cada; cada ramo de Direito vale 3).

### 3. O professor

`ferramenta/SKILL.md` é uma skill do Claude Code (copiar para `~/.claude/skills/professor/`). Fluxo de resposta:

1. Ler `MAPA-GERAL.md` e escolher o notebook pela matéria.
2. Ler (ou fazer Grep em) `notebooks/<slug>.md`.
3. Se faltar detalhe, perguntar ao notebook ao vivo com `notebooklm ask "..." -n <ID>`.
4. Responder no estilo FGV: literalidade em caso concreto, parágrafo esquecido, alternativa quase certa, sempre fechando com as pegadinhas. Dizer de qual notebook veio.
5. Profundidade proporcional ao peso na prova.

Modos: explicar, revisar, gerar questões, listar pegadinhas, montar plano, gerar cards Anki (padrão do prompt v5.3 em `materiais/`). `ferramenta/agent-professor.md` é a mesma coisa como subagente.

## Estrutura

```
MAPA-GERAL.md          índice geral por matéria (comece aqui)
notebooks/             23 arquivos, um por notebook (todos os conceitos)
materiais/             {len(mats)} guias de estudo, quizzes, flashcards, notas e mapas mentais
ferramenta/            SKILL.md (skill Claude Code) e agent-professor.md
_build/                rebuild.py, build.py, build_mapa.py, dl.py, prompts, nb_index.json
```

## Instalação e uso

```bash
pip install "notebooklm-py[browser]"
notebooklm login                       # autentica no Google uma vez
notebooklm auth check --test --json    # exige "token_fetch": true

# instalar o professor no Claude Code
mkdir -p ~/.claude/skills/professor && cp ferramenta/SKILL.md ~/.claude/skills/professor/
cp ferramenta/agent-professor.md ~/.claude/agents/professor.md

# reconstruir/atualizar a base depois de adicionar fontes ou notebooks
python _build/rebuild.py
python _build/rebuild.py --force <ID-do-notebook>
```

No Claude Code: `/professor me explica cadeia de custódia com as pegadinhas da FGV`.

Os caminhos dentro da skill apontam para `C:\\Users\\USER\\Professor`; ajuste para onde clonar.

## Armadilhas do CLI (aprendidas na prática)

- **Nunca** use `notebooklm ask --new`: apaga o histórico de chat do notebook. O `rebuild.py` não usa.
- Pedidos exaustivos ao `ask` falham com `RPCResponseTooLargeError` (bug de streaming do CLI, não é tamanho do notebook). Solução: perguntar em partes ou pedir "compacto, máx. 90 linhas, sem citar fontes" (prompts `pc_*.txt`, usados como fallback automático).
- A sessão expira no meio de lotes longos. `notebooklm login` resolve sozinho se o perfil do navegador já estiver logado.
- Sempre passe `-n <ID>` em vez de `notebooklm use`, para rodar lotes em paralelo sem conflito de contexto.

## O que está coberto (todos os conceitos estão em `notebooks/`)

{NL.join(tbl)}

**Lacuna conhecida:** Direitos Humanos (3 questões) não tem notebook.

## Materiais baixados

{NL.join(f'- [{m}](materiais/{m})' for m in mats)}

## Dados

Extração feita em 05/09/2026 com notebooklm-py v0.8.1. Os arquivos em `notebooks/` são sínteses geradas pelo NotebookLM a partir das fontes do usuário; o texto integral das fontes não está neste repositório.
"""
open('README.md', 'w', encoding='utf-8').write(README)
print('README', len(README))
