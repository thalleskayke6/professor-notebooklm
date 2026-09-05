# Professor NotebookLM — PC-PR 2026

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
materiais/             49 guias de estudo, quizzes, flashcards, notas e mapas mentais
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

Os caminhos dentro da skill apontam para `C:\Users\USER\Professor`; ajuste para onde clonar.

## Armadilhas do CLI (aprendidas na prática)

- **Nunca** use `notebooklm ask --new`: apaga o histórico de chat do notebook. O `rebuild.py` não usa.
- Pedidos exaustivos ao `ask` falham com `RPCResponseTooLargeError` (bug de streaming do CLI, não é tamanho do notebook). Solução: perguntar em partes ou pedir "compacto, máx. 90 linhas, sem citar fontes" (prompts `pc_*.txt`, usados como fallback automático).
- A sessão expira no meio de lotes longos. `notebooklm login` resolve sozinho se o perfil do navegador já estiver logado.
- Sempre passe `-n <ID>` em vez de `notebooklm use`, para rodar lotes em paralelo sem conflito de contexto.

## O que está coberto (todos os conceitos estão em `notebooks/`)

| Área | Notebook | Fontes | Temas principais |
|---|---|---|---|
| Edital | [Edital 01/2026 Concurso Público Polícia Civil do Paraná](notebooks/edital-01-2026-concurso-publico-policia-civil.md) | 2 | 1. Organização do Certame e Disposições Preliminares; 2. Cargos, Requisitos, Atribuições e Remunerações; 3. Inscrições, Taxas e Isenções de Pagamento; 4. Regime de Cotas e Bancas de Heteroidentificação; 5. Atendimentos Especiais e Diferenciados; 6. Provas Escritas: Objetiva e Discursiva; 7. Exame de Inspeção de Saúde e do TAF; 8. Avaliação Psicológica, Investigação Social e Prova Oral; 9. Títulos, Classificação Final, Recursos e Posse |
| Língua Portuguesa (25 q) | [PCPR 2026 — Língua Portuguesa (Apostilas)](notebooks/pcpr-2026-lingua-portuguesa-apostilas.md) | 17 | Aula 00 - Nivelamento da Língua; Aula 01 - Ortografia e Acentuação Gráfica; Aula 02 - Classes de Palavras I; Aula 03 - Classes de Palavras II; Aula 04 - Classes de Palavras III; Aula 05 - Estrutura e Formação de Palavras; Aula 06 - Organização Sintática das Frases; Aula 07 - Tipologia da Frase e Pontuação; Aula 08 - Concordância Verbal e Nominal; Aula 09 - Regência Verbal e Nominal e Crase; Aula 10 - Coesão e Coerência; Aula 11 - Semântica: Sinônimos, Antônimos e Parônimos; Aula 12 - Interpretação e Compreensão de Texto; Aula 13 - Gêneros Textuais e Domínios Discursivos |
| Língua Portuguesa (25 q) | [PCPR 2026 — Português](notebooks/pcpr-2026-portugues.md) | 19 | I. Guia-Mestre e Estratégia de Prova (O Jeito FGV); II. Morfologia Contextual e Formação de Palavras; III. Sintaxe do Período Simples e Composto; IV. Sintaxe das Orações Reduzidas; V. Regência Verbal, Nominal e Emprego da Crase; VI. Concordância Verbal e Nominal; VII. Colocação Pronominal; VIII. Paralelismo Sintático e Semântico; IX. Pontuação como Sintaxe Aplicada; X. Coerência e Coesão Textual (Anáfora, Catáfora e Conectores); XI. Semântica, Relações Lexicais e Modalização Discursiva; XII. Reescrita de Frases e Técnicas de Substituição de Trechos; XIII. Clareza, Correção e Propriedades de Estilo do Período; XIV. Tipologia, Gênero Textual e Intertextualidade |
| Língua Portuguesa (25 q) | [PC-PR PORTUGUÊS](notebooks/pc-pr-portugues.md) | 24 | Nivelamento e Fonologia Básica; Ortografia, Acentuação Gráfica e Prosódia; Morfologia I: Classes de Palavras Variáveis; Morfologia II: Classes de Palavras Invariáveis e Conectivos; Verbos e Sintaxe Verbal; Estrutura e Formação das Palavras; Organização Sintática da Oração e do Período; Pontuação e Tipologia da Frase; Mecanismos de Concordância; Regência e Crase; Semântica e Figuras de Linguagem; Coesão e Coerência Textual; Compreensão, Interpretação e Análise Textual; Variação Linguística, Atos de Fala e Lexicografia |
| Tecnologia / Segurança Cibernética (25 q) | [PC-PR TECNOLOGIA DA INFORMAÇÃO](notebooks/pc-pr-tecnologia-da-informacao.md) | 49 | Redes de Computadores e Internet; Intranets, Extranets e VPNs; Computação em nuvem; Navegadores, Cookies e Cache; Correio Eletrônico; Redes sociais e plataformas digitais; Segurança da Informação e Segurança Cibernética; Ameaças Cibernéticas e Malwares; Segurança de Redes e Firewalls; Backup e Recuperação de Dados; Prevenção e Resposta a Incidentes de Segurança; Planilhas Eletrônicas: MS Excel e LibreOffice Calc; Processadores de Texto: MS Word e LibreOffice Writer; Editores de Apresentação: MS PowerPoint e LibreOffice Impress |
| Ciências Forenses (10 q) | [PCPR 2026 — Ciências Forenses](notebooks/pcpr-2026-ciencias-forenses.md) | 16 | Perícias Médico-Legais e Legislação Processual; Traumatologia Forense (Lesonologia); Balística Forense; Asfixiologia Forense; Tanatologia Forense e Cronotanatognose; Antropologia Forense e Identificação Humana; Local de Crime, Vestígios e Cadeia de Custódia; Documentoscopia e Grafoscopia; Criminologia |
| Ciências Forenses (10 q) | [exame de corpo de delito](notebooks/exame-de-corpo-de-delito.md) | 3 |  |
| Raciocínio Lógico (5 q) | [Felippe Loureiro](notebooks/felippe-loureiro.md) | 292 | Raciocínio Lógico Proposicional; Matemática Básica para Concursos; Análise Combinatória e Probabilidade; Matemática Financeira e Estatística; Técnicas de Estudo e Preparação Mental |
| Realidade do Paraná (5 q) | [PCPR 2026 — Realidade do Paraná](notebooks/pcpr-2026-realidade-do-parana.md) | 12 | I. Período Pré-Colonial e Povos Originários do Paraná; II. O Peabiru e a Colonização Espanhola do Guairá; III. Colonização Portuguesa e Mineração Litorânea; IV. O Tropeirismo e a Ocupação dos Campos Gerais; V. A Emancipação Política do Paraná (1853); VI. O Ciclo da Erva-Mate e a Modernização dos Transportes; VII. Ciclos da Madeira, do Café e a Colonização do Século XX; VIII. Imigração Europeia e Formação Étnica; IX. Geografia Física e Aspectos Naturais do Paraná; X. Geografia Humana, Economia e Patrimônio do Paraná |
| Contabilidade (5 q) | [PCPR 2026 — Contabilidade Geral](notebooks/pcpr-2026-contabilidade-geral.md) | 15 |  |
| Estatística (5 q) | [Estatística FGV — PCPR 2026 (Recorte de Prova)](notebooks/estatistica-fgv-pcpr-2026-recorte-de-prova.md) | 53 | I. Lógica Proposicional, Argumentação e Teoria dos Conjuntos; II. Matemática Básica, Razão, Proporção e Porcentagem; III. Álgebra Linear, Matrizes, Determinantes e Sistemas; IV. Geometria Plana, Espacial e Analítica; V. Estatística Descritiva, Medidas Estatísticas e Amostragem; VI. Análise Combinatória e Teoria da Probabilidade |
| Legislação Estadual (5 q) | [PC-PR Legislação Estadual e Institucional](notebooks/pc-pr-legislacao-estadual-e-institucional.md) | 14 | I. Regulação Constitucional e Administrativa Geral (CE/PR); II. Estatuto dos Servidores Públicos Civis do Paraná (Lei Estadual nº 6.174/1970); III. Sindicância e Processo Administrativo Disciplinar (Lei Estadual nº 20.655/2021); IV. Ética e Sigilo no Serviço Público; V. Lei Geral de Proteção de Dados Pessoais (Lei Federal nº 13.709/2018 - LGPD); VI. Lei de Acesso à Informação (Lei Federal nº 12.527/2011 - LAI); VII. Lei de Abuso de Autoridade (Lei Federal nº 13.869/2019); VIII. Identificação Criminal (Lei Federal nº 12.037/2009); IX. Lei Orgânica Nacional das Polícias Civis (Lei Federal nº 14.735/2023); X. Estruturação das Carreiras da Polícia Civil do Estado do Paraná (Lei Complementar nº 259/2023); XI. Organização Administrativa e Operacional (Lei Orgânica da PCPR - Lei Estadual nº 23.213/2026) |
| Direito Penal (3 q) | [PCPR 2026 — Direito Penal (Apostilas)](notebooks/pcpr-2026-direito-penal-apostilas.md) | 3 | Princípios do Direito Penal; Aplicação da Lei Penal no Tempo e Espaço; Conflito de Normas e Interpretação; Teoria Geral da Infração Penal e Fato Típico; Elemento Subjetivo do Tipo; Iter Criminis e Graus de Desenvolvimento; Teoria da Ilicitude |
| Processo Penal (3 q) | [PC-PR PROCESSO PENAL](notebooks/pc-pr-processo-penal.md) | 23 | I. Introdução e Princípios do Processo Penal; II. Juiz das Garantias; III. Inquérito Policial; IV. Ação Penal e Acordo de Não Persecução Penal (ANPP); V. Jurisdição e Competência; VI. Sujeitos Processuais e Auxiliares da Justiça; VII. Teoria Geral da Prova e Cadeia de Custódia; VIII. Provas em Espécie; IX. Prisão e Liberdade Provisória; X. Legislação Penal e Processual Penal Extravagante |
| Constitucional (3 q) | [PC-PR Direito constitucional](notebooks/pc-pr-direito-constitucional.md) | 23 | Aplicabilidade das Normas Constitucionais; Princípios Fundamentais (Arts. 1º a 4º da CF/88); Direitos e Deveres Individuais e Coletivos (Art. 5º da CF/88); Direitos Sociais (Arts. 6º a 11 da CF/88); Nacionalidade (Arts. 12 e 13 da CF/88); Direitos Políticos e Partidos Políticos (Arts. 14 a 17 da CF/88); Organização do Estado e Repartição de Competências (Arts. 18 a 24 da CF/88); Poder Executivo (Arts. 76 a 83 da CF/88); Poder Legislativo e Processo Legislativo (Arts. 44 a 75 da CF/88); Poder Judiciário (Arts. 92 a 126 da CF/88); Defesa do Estado e Segurança Pública (Art. 136 a 144 da CF/88); Noções de Controle de Constitucionalidade (Aula 13) |
| Administrativo (3 q) | [PC-PR Direito Administrativo](notebooks/pc-pr-direito-administrativo.md) | 21 | Conceito, Fontes e Princípios do Direito Administrativo; Organização da Administração Pública; Poderes e Deveres Administrativos; Atos Administrativos; Licitações Públicas (Lei nº 14.133/2021); Contratos Administrativos (Lei nº 14.133/2021); Serviços Públicos (Lei nº 8.987/1995); Controle da Administração Pública; Responsabilidade Civil do Estado; Agentes Públicos; Improbidade Administrativa (Lei nº 8.429/1992); Lei de Introdução às Normas do Direito Brasileiro (LINDB) |
| Método, memória e mentalidade | [Valter Rodrigues](notebooks/valter-rodrigues.md) | 63 | I. Mentalidade Inabalável, Psicologia e Comportamento do Concurseiro; II. Fundamentos e Princípios de Estudo Ativo; III. Planejamento de Ciclos de Estudo, Filtros e Cronogramas; IV. Utilização Científica e Algorítmica do Anki; V. Engenharia de Prompts de Inteligência Artificial para Concursos; VI. Estratégias por Disciplinas e Concursos Específicos; 💡 Minha sugestão para você: |
| Método, memória e mentalidade | [Ciência da Memória: Guia de Aprendizagem Ativa e Anki](notebooks/ciencia-da-memoria-guia-de-aprendizagem-ativa.md) | 33 | I. Ciência Cognitiva e Teoria da Aprendizagem Humana; II. Sequenciamento e Organização da Prática de Estudo; III. Sistemas e Algoritmos de Repetição Espaçada (Spaced Repetition); IV. Configuração Prática de Estudo no Anki; V. Engenharia de Prompts para Criação de Flashcards Atômicos |
| Método, memória e mentalidade | [Estratégias de Aprendizagem e o Poder da Prática de Recuperação](notebooks/estrategias-de-aprendizagem-e-o-poder-da-prat.md) | 44 | Prática de Recuperação e o Efeito de Teste; Teoria das Dificuldades Desejáveis; Efeito de Teste Progressivo (Forward Testing Effect); Engenharia de Estudo Prático e Repetição Espaçada; O Método do Estudo Reverso; Neurobiologia, fMRI e Dinâmicas de Reconsolidação; Feedback Corretivo no Aprendizado Ativo |
| Método, memória e mentalidade | [Neurociência e Aprendizagem](notebooks/neurociencia-e-aprendizagem.md) | 3 | E-book: Neurociência e Aprendizagem (Lucas Gazarini); Livro: Tudo O Que Tu E O Teu Professor Precisam De Saber Acerca De Um Cérebro Em Aprendizagem (Frontiers for Young Minds); Artigo: Spaced Repetition Promotes Efficient and Effective Learning (Sean H. K. Kang) |
| Método, memória e mentalidade | [Guia do Palácio da Memória: Técnicas, Ciência e Tecnologia](notebooks/guia-do-palacio-da-memoria-tecnicas-ciencia-e.md) | 8 | 1. Origens Históricas e Fundamentação do Método de Loci; 2. Neurociência da Memória Espacial e Estudos de fMRI; 3. Evidências Clínicas de Eficácia e Limitações; 4. Planejamento, Construção e Prática do Palácio da Memória; 5. Aplicações Práticas Setoriais; 6. Tecnologia e Gamificação da Memória Humana (Mind Palace App); 7. Arquitetura Tecnológica de Memória para IA (MemPalace); 8. Análise Crítica, Benchmarks e Controvérsias do MemPalace |
| Método, memória e mentalidade | [Cognitive Toolkits for Deep Learning and Mastery](notebooks/cognitive-toolkits-for-deep-learning-and-mast.md) | 50 | I. Fundamentos Neurobiológicos e Plasticidade Sináptica; II. Prática de Recuperação Ativa e Efeito de Testagem; III. Espaçamento de Estudo e Repetição Espaçada; IV. Prática Intercalada (*Interleaving*) e Aprendizagem de Categorias; V. Processamento Semântico e Técnicas de Elaboração; VI. Teoria da Carga Cognitiva (CLT) e Design Instrucional; VII. Metacognição, Mentalidade de Crescimento e Autorregulação; VIII. Suporte Fisiológico, Estilo de Vida e Saúde Cognitiva |
| IA e prompts | [Guia Completo de Chatbots e Prompt Engineering para Educadores](notebooks/guia-completo-de-chatbots-e-prompt-engineerin.md) | 32 |  |

**Lacuna conhecida:** Direitos Humanos (3 questões) não tem notebook.

## Materiais baixados

- [01d11b38_note_guia-de-improbidade-administrativa-para-concursos.md](materiais/01d11b38_note_guia-de-improbidade-administrativa-para-concursos.md)
- [01d11b38_quiz_improbidade-quiz_059d56.md](materiais/01d11b38_quiz_improbidade-quiz_059d56.md)
- [185c9e3e_flash_estat-stica-flashcards.md](materiais/185c9e3e_flash_estat-stica-flashcards.md)
- [185c9e3e_mindmap_estat-stica-mapa.json](materiais/185c9e3e_mindmap_estat-stica-mapa.json)
- [185c9e3e_quiz_estat-stica-quiz_213a1a.md](materiais/185c9e3e_quiz_estat-stica-quiz_213a1a.md)
- [185c9e3e_report_guia-de-estudo-de-reta-final-estat-stica-pcpr-banc.md](materiais/185c9e3e_report_guia-de-estudo-de-reta-final-estat-stica-pcpr-banc.md)
- [367433a3_note_guia-pr-tico-de-tanatologia-forense-e-fen-menos-ca.md](materiais/367433a3_note_guia-pr-tico-de-tanatologia-forense-e-fen-menos-ca.md)
- [367433a3_quiz_medicina-quiz_f729ab.md](materiais/367433a3_quiz_medicina-quiz_f729ab.md)
- [367433a3_quiz_quiz-forense_aa7976.md](materiais/367433a3_quiz_quiz-forense_aa7976.md)
- [367433a3_quiz_tanatologia-quiz_52205e.md](materiais/367433a3_quiz_tanatologia-quiz_52205e.md)
- [367433a3_quiz_tanatologia-quiz_702617.md](materiais/367433a3_quiz_tanatologia-quiz_702617.md)
- [42b917ff_quiz_paran-quiz_13b145.md](materiais/42b917ff_quiz_paran-quiz_13b145.md)
- [42b917ff_quiz_paran-quiz_15bab7.md](materiais/42b917ff_quiz_paran-quiz_15bab7.md)
- [42b917ff_quiz_paran-quiz_2c0a15.md](materiais/42b917ff_quiz_paran-quiz_2c0a15.md)
- [42b917ff_quiz_paran-quiz_3f6982.md](materiais/42b917ff_quiz_paran-quiz_3f6982.md)
- [42b917ff_report_guia-de-estudo-realidade-tnica-social-hist-rica-ge.md](materiais/42b917ff_report_guia-de-estudo-realidade-tnica-social-hist-rica-ge.md)
- [546f0cb3_quiz_nuvem-quiz_a712ac.md](materiais/546f0cb3_quiz_nuvem-quiz_a712ac.md)
- [5714ea7c_flash_conjuntos-flashcards.md](materiais/5714ea7c_flash_conjuntos-flashcards.md)
- [5714ea7c_note_dom-nio-da-an-lise-combinat-ria-guia-pr-tico-de-co.md](materiais/5714ea7c_note_dom-nio-da-an-lise-combinat-ria-guia-pr-tico-de-co.md)
- [5714ea7c_note_estrat-gia-de-alta-performance-para-concursos-de-e.md](materiais/5714ea7c_note_estrat-gia-de-alta-performance-para-concursos-de-e.md)
- [5714ea7c_note_guia-de-alta-performance-para-exatas-pcpr.md](materiais/5714ea7c_note_guia-de-alta-performance-para-exatas-pcpr.md)
- [5714ea7c_quiz_l-gica-quiz_093710.md](materiais/5714ea7c_quiz_l-gica-quiz_093710.md)
- [73efc3d0_quiz_contabilidade-quiz_066eaf.md](materiais/73efc3d0_quiz_contabilidade-quiz_066eaf.md)
- [73efc3d0_quiz_contabilidade-quiz_532919.md](materiais/73efc3d0_quiz_contabilidade-quiz_532919.md)
- [73efc3d0_quiz_contabilidade-quiz_706b7a.md](materiais/73efc3d0_quiz_contabilidade-quiz_706b7a.md)
- [73efc3d0_quiz_quiz-contabilidade_4f9a5f.md](materiais/73efc3d0_quiz_quiz-contabilidade_4f9a5f.md)
- [73efc3d0_report_guia-de-estudo-contabilidade-geral-para-pc-pr-2026.md](materiais/73efc3d0_report_guia-de-estudo-contabilidade-geral-para-pc-pr-2026.md)
- [8498c1e7_quiz_per-cia-quiz_622a64.md](materiais/8498c1e7_quiz_per-cia-quiz_622a64.md)
- [8498c1e7_quiz_per-cias-quiz_78e9e3.md](materiais/8498c1e7_quiz_per-cias-quiz_78e9e3.md)
- [84eec3f0_mindmap_concursos-mapa.json](materiais/84eec3f0_mindmap_concursos-mapa.json)
- [84eec3f0_note_plano-de-elite-estrat-gia-de-aprova-o-para-pc-pr.md](materiais/84eec3f0_note_plano-de-elite-estrat-gia-de-aprova-o-para-pc-pr.md)
- [84eec3f0_note_prompt-definitivo.md](materiais/84eec3f0_note_prompt-definitivo.md)
- [84eec3f0_note_prompt-gerador-de-quest-es-e-flashcards-pcpr-v5-3.md](materiais/84eec3f0_note_prompt-gerador-de-quest-es-e-flashcards-pcpr-v5-3.md)
- [84eec3f0_table_estrat-gias-e-dicas-para-estudos-e-concursos-p-bli.csv](materiais/84eec3f0_table_estrat-gias-e-dicas-para-estudos-e-concursos-p-bli.csv)
- [ae986a01_quiz_coes-o-quiz_080f60.md](materiais/ae986a01_quiz_coes-o-quiz_080f60.md)
- [ae986a01_quiz_g-neros-quiz_64e9e9.md](materiais/ae986a01_quiz_g-neros-quiz_64e9e9.md)
- [ae986a01_quiz_gram-tica-quiz_bc2181.md](materiais/ae986a01_quiz_gram-tica-quiz_bc2181.md)
- [ae986a01_quiz_gram-tica-quiz_f9cd84.md](materiais/ae986a01_quiz_gram-tica-quiz_f9cd84.md)
- [ae986a01_quiz_pontua-o-quiz_76ec87.md](materiais/ae986a01_quiz_pontua-o-quiz_76ec87.md)
- [ae986a01_report_resumo-estrat-gico-ortografia-acentua-o-e-classes.md](materiais/ae986a01_report_resumo-estrat-gico-ortografia-acentua-o-e-classes.md)
- [b63c5fdb_note_constitucional-pc-bens-e-compet-ncias-da-uni-o-e-e.md](materiais/b63c5fdb_note_constitucional-pc-bens-e-compet-ncias-da-uni-o-e-e.md)
- [b63c5fdb_note_guia-definitivo-do-artigo-5-para-carreiras-policia.md](materiais/b63c5fdb_note_guia-definitivo-do-artigo-5-para-carreiras-policia.md)
- [b63c5fdb_quiz_direito-quiz_96d209.md](materiais/b63c5fdb_quiz_direito-quiz_96d209.md)
- [b63c5fdb_quiz_quiz-constitucional_3c496d.md](materiais/b63c5fdb_quiz_quiz-constitucional_3c496d.md)
- [bee037d5_quiz_legisla-o-quiz_304f42.md](materiais/bee037d5_quiz_legisla-o-quiz_304f42.md)
- [bee037d5_quiz_lgpd-quiz_4a2270.md](materiais/bee037d5_quiz_lgpd-quiz_4a2270.md)
- [bee037d5_quiz_pc-pr-quiz_3d6635.md](materiais/bee037d5_quiz_pc-pr-quiz_3d6635.md)
- [e5690053_mindmap_portugu-s-mapa.json](materiais/e5690053_mindmap_portugu-s-mapa.json)
- [e5690053_report_guia-de-estudo-completo-portugu-s-padr-o-fgv.md](materiais/e5690053_report_guia-de-estudo-completo-portugu-s-padr-o-fgv.md)

## Dados

Extração feita em 05/09/2026 com notebooklm-py v0.8.1. Os arquivos em `notebooks/` são sínteses geradas pelo NotebookLM a partir das fontes do usuário; o texto integral das fontes não está neste repositório.
