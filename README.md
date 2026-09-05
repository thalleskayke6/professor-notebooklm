# Professor: um tutor de concurso construído sobre NotebookLM, Obsidian e um banco de questões reais

## Resumo

Este repositório documenta a construção de um tutor automatizado para a prova de Agente de Polícia Judiciária da Polícia Civil do Paraná (Edital 01/2026, banca FGV). O tutor combina três bases: 23 notebooks do Google NotebookLM com 819 fontes, um cofre do Obsidian com 205 aulas em formato markdown distribuídas por 13 matérias, e um banco de 4482 questões reais de concurso, deduplicadas e com gabarito, classificadas em 445 assuntos. Um conjunto de scripts em Python extrai, normaliza e indexa esse material; uma skill do Claude Code o consulta na hora de responder. O texto descreve as fontes, o pipeline, a cobertura por matéria e assunto, o modo de uso e o que é preciso mudar para reaproveitar a estrutura em outro edital.

## 1. O problema

Quem estuda para concurso acumula material em três lugares que não conversam entre si. As apostilas e videoaulas ficam em um serviço de anotações. Os cadernos de questões ficam na plataforma onde foram resolvidos. As anotações de método, o plano de estudo e o registro de erros ficam em um terceiro lugar. Cada ferramenta responde bem a uma pergunta de cada vez sobre o próprio acervo, mas nenhuma sabe cruzar as três coisas: o que a apostila ensina, como a banca cobra isso na prática e onde o aluno está errando.

O objetivo aqui foi montar um único "professor" que tivesse lido tudo, soubesse o peso de cada matéria na prova e respondesse no recorte da banca, com questões reais como referência.

## 2. Materiais

A base foi montada a partir de três origens. Nomes de autores, cursos e plataformas foram omitidos de propósito; o que importa para reprodução é o tipo de material e o formato.

**Notebooks do NotebookLM.** 23 notebooks com 819 fontes no total: apostilas em PDF, videoaulas, artigos, textos de lei, planilhas e prompts. Treze deles cobrem matérias do edital; seis tratam de método de estudo, memória e mentalidade; um trata de engenharia de prompts; um contém o edital.

**Cofre do Obsidian.** Cerca de 440 notas em markdown. As principais são as apostilas convertidas de PDF, uma por aula, em até três versões (resumo, simplificada e completa), organizadas em 13 matérias com uma nota-hub por matéria. Além delas, notas curadas de método (um catálogo de pegadinhas da banca com códigos fixos, instruções para geração de flashcards), plano de estudo (pesos, ciclo de blocos, reta final) e registro (análise de erros, assuntos a treinar após simulado).

**Cadernos de questões.** Exportações em markdown de uma plataforma de questões, filtradas por banca. Havia 44 arquivos com forte sobreposição (o mesmo caderno exportado mais de uma vez). Após deduplicação pelo identificador da questão na fonte, restaram 4482 questões únicas, 4323 delas com gabarito.

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

| Matéria | Questões na prova | Notebooks | Aulas no cofre | Questões reais no banco |
|---|---:|---|---:|---:|
| Língua Portuguesa | 25 | [PCPR 2026 — Língua Portuguesa (Apostilas)](notebooks/pcpr-2026-lingua-portuguesa-apostilas.md); [PCPR 2026 — Português](notebooks/pcpr-2026-portugues.md); [PC-PR PORTUGUÊS](notebooks/pc-pr-portugues.md) | 17 | 722 |
| Tecnologia, Segurança Cibernética e Crimes Digitais | 25 | [PC-PR TECNOLOGIA DA INFORMAÇÃO](notebooks/pc-pr-tecnologia-da-informacao.md) | 30 | 446 |
| Ciências Forenses | 10 | [PCPR 2026 — Ciências Forenses](notebooks/pcpr-2026-ciencias-forenses.md); [exame de corpo de delito](notebooks/exame-de-corpo-de-delito.md) | 11 | 72 |
| Raciocínio Lógico-Matemático | 5 | [Exatas e lógica (videoaulas)](notebooks/exatas-e-logica-videoaulas.md) | 25 | 250 |
| Realidade do Paraná | 5 | [PCPR 2026 — Realidade do Paraná](notebooks/pcpr-2026-realidade-do-parana.md) | 6 | 0 |
| Contabilidade Geral | 5 | [PCPR 2026 — Contabilidade Geral](notebooks/pcpr-2026-contabilidade-geral.md) | 12 | 809 |
| Estatística | 5 | [Estatística FGV — PCPR 2026 (Recorte de Prova)](notebooks/estatistica-fgv-pcpr-2026-recorte-de-prova.md) | 13 | 552 |
| Legislação Estadual e Institucional | 5 | [PC-PR Legislação Estadual e Institucional](notebooks/pc-pr-legislacao-estadual-e-institucional.md) | 14 | 60 |
| Direito Penal (com Legislação Penal Extravagante) | 3 | [PCPR 2026 — Direito Penal (Apostilas)](notebooks/pcpr-2026-direito-penal-apostilas.md) | 28 | 280 |
| Direito Processual Penal | 3 | [PC-PR PROCESSO PENAL](notebooks/pc-pr-processo-penal.md) | 9 | 113 |
| Direito Constitucional | 3 | [PC-PR Direito constitucional](notebooks/pc-pr-direito-constitucional.md) | 14 | 214 |
| Direito Administrativo | 3 | [PC-PR Direito Administrativo](notebooks/pc-pr-direito-administrativo.md) | 15 | 601 |
| Direitos Humanos | 3 | nenhum | 11 | 363 |
| Método de estudo, memória e mentalidade | — | [Método de estudo para concursos (videoaulas)](notebooks/metodo-de-estudo-para-concursos.md); [Ciência da Memória: Guia de Aprendizagem Ativa e Anki](notebooks/ciencia-da-memoria-guia-de-aprendizagem-ativa.md); [Estratégias de Aprendizagem e o Poder da Prática de Recuperação](notebooks/estrategias-de-aprendizagem-e-o-poder-da-prat.md); [Neurociência e Aprendizagem](notebooks/neurociencia-e-aprendizagem.md); [Guia do Palácio da Memória: Técnicas, Ciência e Tecnologia](notebooks/guia-do-palacio-da-memoria-tecnicas-ciencia-e.md); [Cognitive Toolkits for Deep Learning and Mastery](notebooks/cognitive-toolkits-for-deep-learning-and-mast.md) | — | — |
| IA e engenharia de prompts | — | [Guia Completo de Chatbots e Prompt Engineering para Educadores](notebooks/guia-completo-de-chatbots-e-prompt-engineerin.md) | — | — |
| Edital | — | [Edital 01/2026 Concurso Público Polícia Civil do Paraná](notebooks/edital-01-2026-concurso-publico-policia-civil.md) | — | — |

Direitos Humanos não tem notebook no NotebookLM. A cobertura dessa matéria vem das apostilas do cofre e das questões do banco.

### 4.1 Assuntos por matéria

Os assuntos abaixo são os rótulos usados pela própria plataforma de questões, ordenados pelo número de questões no banco. Essa ordem é, na prática, a incidência observada da banca no recorte coletado.

**Língua Portuguesa** (722 questões, 56 assuntos): Interpretação de Textos (Compreensão) (254); (sem assunto) (71); Tipologia e Gênero Textual (49); Coerência. Coesão (Anáfora, Catáfora, Uso dos Conectores - Pronomes Relativos, Conjunções, etc) (40); Reescrita de Frases. Substituição de Palavras ou Trechos de Texto. (37); Adjetivo (19); Pontuação (Ponto, Vírgula, Travessão, Aspas, Parênteses, etc) (15); Figuras de Linguagem (14); Acentuação (11); Sinônimos e Antônimos (11); Fatos da Língua Portuguesa (Porque, Por Que, Porquê e Por Quê; Onde, Aonde e Donde; Há e A, etc) (10); Formação e Estrutura das Palavras (10); e mais 44 assuntos.

**Tecnologia, Segurança Cibernética e Crimes Digitais** (446 questões, 73 assuntos): Disposições Preliminares (arts. 1º a 6º da Lei nº 13.709/2018 - LGPD) (114); Do Tratamento de Dados Pessoais Sensíveis (arts. 11 a 13 da Lei nº 13.709/2018 - LGPD) (33); Dos Requisitos para o Tratamento de Dados Pessoais (arts. 7º a 10 da Lei nº 13.709/2018 - LGPD) (31); Dos Direitos do Titular (arts. 17 a 22 da Lei nº 13.709/2018 - LGPD) (18); Das Regras para Tratamento de Dados Pessoais (arts. 23 a 30 da Lei nº 13.709/2018 - LGPD) (16); Redes de Computadores - Cloud Computing (Computação em Nuvem) (16); Das Sanções Administrativas (arts. 52 a 54 da Lei nº 13.709/2018 - LGPD) (12); Segurança da Informação - Conceitos, Princípios e Atributos da Segurança da Informação (11); Redes de Computadores - Máscara e Endereçamento IP (10); Segurança da Informação - Algoritmos de Criptografia (10); Da Segurança e do Sigilo de Dados (arts. 46 a 49 da Lei nº 13.709/2018 - LGPD) (9); Do Encarregado pelo Tratamento de Dados Pessoais (art. 41 da Lei nº 13.709/2018 - LGPD) (9); e mais 61 assuntos.

**Ciências Forenses** (72 questões, 9 assuntos): Fenômenos Cadavéricos (62); Criminologia (conceito, objeto, método, função, finalidade) (3); Locais de Crime (1); Resolução CNJ nº 417/2021 - Banco Nacional de Medidas Penais e Prisões (BNMP 3.0) (1); Evolução Histórica e Escolas Criminológicas (Clássica, Positiva, Terza Scuola) (1); Agronegócio (1); Provas, Vestígios e Indícios (1); Traumatologia: Energia de Ordem Mecânica (1); Identificação de Ossadas (1).

**Raciocínio Lógico-Matemático** (250 questões, 39 assuntos): Porcentagem (72); Análise Combinatória (Princípio Fundamental da Contagem, Arranjos, Combinações, Permutações) (23); Unidades de Medida (Distância, Massa, Volume, Tempo, etc) (14); Quadriláteros (Propriedades, Área, Perímetro, Soma dos Ângulos, etc) (13); Proporções. Grandezas Proporcionais. Divisão em Partes Proporcionais (11); Equivalências Lógicas (Inclui Negação de Proposições Compostas) (10); Adição, Subtração, Multiplicação e Divisão de Números Naturais (10); Divisibilidade, Números Primos, Fatores Primos, Divisor e Múltiplo Comum (MMC) (10); Frações e Dízimas Periódicas (10); Orientação no Plano, no Espaço e no Tempo (9); Associação de Informações (7); Exercícios Envolvendo Datas e Calendários (6); e mais 27 assuntos.

**Contabilidade Geral** (809 questões, 14 assuntos): Balanço Patrimonial (168); Provisões, Passivos e Ativos Contingentes (CPC 25, Lei 6.404) (130); Demonstração do Resultado do Exercício (DRE) e Destinação do Resultado (126); Índices de Liquidez. Capital Circulante Líquido (96); CPC 16 - Tratamento Contábil para os Estoques (77); Elaboração e Apresentação das Demonstrações Contábeis (CPC 26, Lei 6.404, arts. 176 e 177) (68); Demonstração de Fluxo de Caixa (DFC - CPC 03, Lei 6.404, art. 188, I) (58); Demonstração do Valor Adicionado (DVA - CPC 09, Lei 6.404, art. 188, II) (39); Demonstração Contábil Consolidada (CPC 36, Lei 6.404, art. 249 e 250) (23); Demonstração das Mutações do Patrimônio Líquido (DMPL) (11); Notas Explicativas (Contabilidade Geral) (9); Origens, Aplicações, Capital Circulante Líquido (2); e mais 2 assuntos.

**Estatística** (552 questões, 42 assuntos): Problemas Introdutórios de Probabilidade: Eventos Equiprováveis e Abordagem Frequentista (71); Cálculo de Probabilidades Usando Análise Combinatória (66); Média para Dados não Agrupados (47); Probabilidade Condicional (33); Desvio Padrão e Variância (32); Probabilidade da Intersecção (30); Quantis (Mediana, Quartil, Decil, Percentil) e Interpolação Linear da Ogiva (28); Probabilidade do Evento Complementar (22); Teorema da Probabilidade Total (22); Eventos Independentes e Eventos Mutuamente Excludentes (19); Probabilidade da União (19); Amostragem Estratificada (17); e mais 30 assuntos.

**Legislação Estadual e Institucional** (60 questões, 16 assuntos): Lei nº 14.735/2023 - Lei Orgânica Nacional das Polícias Civis (9); Do Regime Disciplinar (arts. 272 a 305 da Lei Estadual nº 6.174/1970) (9); Do Provimento dos Cargos (arts. 18 a 122 da Lei Estadual nº 6.174/1970) (8); Da Organização dos Poderes (arts. 52 a 128 da CE-PR) (6); Da Organização do Estado e dos Municípios (arts. 1º a 26 da CE-PR) (5); Dos Tributos e dos Orçamentos (arts. 129 a 138 da CE-PR) (4); Da Administração Pública (arts. 27 a 51 da CE-PR) (3); Dos Direitos, Vantagens e Concessões (arts. 128 a 254 da Lei Estadual nº 6.174/1970) (3); Da Ordem Social (arts. 165 a 226 da CE-PR) (3); Lei Complementar Estadual nº 37/2004 - Estatuto da Polícia Civil (PI) (3); Dos Cargos e da Função Gratificada (arts. 3º a 17 da Lei Estadual nº 6.174/1970) (2); Do Processo Administrativo e sua Revisão (arts. 306 a 341 da Lei Estadual nº 6.174/1970) (1); e mais 4 assuntos.

**Direito Penal (com Legislação Penal Extravagante)** (280 questões, 92 assuntos): Lei nº 12.037/2009 - Identificação Criminal (55); Lei nº 13.869/2019 - Lei de Abuso de Autoridade (antiga Lei nº 4.898/1965) (43); Imputabilidade Penal (arts. 26 a 28 do CP) (6); Peculato (art. 312 do CP) (6); Lei nº 8.072/1990 - Crimes Hediondos (6); Dos Crimes contra a Honra (arts. 138 a 145 do CP) (5); Dos Crimes contra a Liberdade Sexual e da Exposição da Intimidade Sexual (arts. 213 a 216-B do CP) (5); Da Violência Doméstica e Familiar Contra a Mulher (arts. 5º a 7º da Lei nº 11.340/2006) (5); Concurso de Crimes (arts. 69 a 76 do CP) (4); Do Roubo e da Extorsão (arts. 157 a 160 do CP) (4); Estado de Necessidade (art. 24 do CP) (4); Potencial Consciência da Ilicitude: Erro de Proibição e Descriminantes Putativas (arts. 20, §1º, e 21 do CP) (4); e mais 80 assuntos.

**Direito Processual Penal** (113 questões, 13 assuntos): Do Exame de Corpo de Delito, da Cadeia de Custódia e das Perícias em Geral (arts. 158 a 184 do CPP) (88); Inquérito Policial (arts. 4º a 23 do CPP) (5); Questões Mescladas sobre Prisão, Medidas Cautelares e Liberdade Provisória (arts. 282 a 350 do CPP) (5); Da Busca e Apreensão (arts. 240 a 250 do CPP) (2); Da Prisão em Flagrante (arts. 301 a 310 do CPP) (2); Jurisprudência dos Tribunais Superiores sobre Inquérito Policial (2); Questões Mescladas sobre a Prova (arts. 155 a 250 do CPP) (2); Teoria Geral da Prova Penal (arts. 155 a 157 do CPP) (2); Da Liberdade Provisória, com ou sem Fiança (arts. 321 a 350 do CPP) (1); Jurisprudência dos Tribunais Superiores sobre Teoria Geral da Prova Penal (1); Da Acareação (arts. 229 a 230 do CPP) (1); Da Prisão Domiciliar (arts. 317 e 318 do CPP) (1); e mais 1 assuntos.

**Direito Constitucional** (214 questões, 10 assuntos): Dos Direitos e Deveres Individuais e Coletivos (art. 5º da CF/1988) (84); União: Bens e Competências Exclusivas, Privativas, Comuns e Concorrentes (arts. 20 a 24 da CF/1988) (73); Jurisprudência dos Tribunais Superiores sobre Direitos e Deveres Individuais e Coletivos (50); Habeas Data (1); Das Atribuições do Congresso Nacional (arts. 48 a 50 da CF/1988) (1); Segurança Pública (art. 144 da CF/1988) (1); Ação Declaratória de Constitucionalidade (ADC) (1); Questões Mescladas de Ministério Público (arts. 127 a 130 da CF/1988) (1); Ação Popular (1); Perda da Nacionalidade (1).

**Direito Administrativo** (601 questões, 20 assuntos): Contratação Direta, Inexigibilidade e Dispensa (arts. 72 a 75 da Lei nº 14.133/2021) (62); Das Restrições de Acesso à Informação (arts. 21 a 31 da Lei nº 12.527/2011) (54); Do Procedimento Administrativo e do Processo Judicial (arts. 14 a 18-A da Lei nº 8.429/1992) (48); Modalidades de Licitação (arts. 28 a 32 da Lei nº 14.133/2021) (47); Do Procedimento de Acesso à Informação (arts. 10 a 20 da Lei nº 12.527/2011) (45); Terceiro Setor (OSs, OSCIPs, Sistema S e Fundações de Apoio) (45); Dos Atos de Improbidade (arts. 9º a 11 da Lei nº 8.429/1992) (41); Administração Indireta (40); Lei nº 11.079/2004 - Parceria Público-Privada (PPP) (37); Das Definições (art. 6º da Lei nº 14.133/2021) (37); Disposições Gerais (arts. 1º a 5º da Lei nº 12.527/2011) (36); Do Acesso a Informações e da sua Divulgação (arts. 6º a 9º da Lei nº 12.527/2011) (32); e mais 8 assuntos.

**Direitos Humanos** (363 questões, 61 assuntos): Disposições Gerais (arts. 1º ao 3º da Lei nº 13.146/2015) (30); Sistema Interamericano de Direitos Humanos (22); Direitos Humanos na Constituição Federal (20); Conceitos, Histórico e Gerações dos Direitos Humanos (16); Da Igualdade e da Não Discriminação (arts. 4º ao 9º da Lei nº 13.146/2015) (16); Do Direito à Saúde (arts. 15 ao 19 da Lei nº 10.741/2003) (16); Incorporação dos Tratados Internacionais de DH ao Direito Brasileiro. Posição Hierárquica. (14); Outros Temas e Tópicos Mesclados de Proteção dos Direitos Humanos (14); Do Direito à Educação (arts. 27 a 30 da Lei nº 13.146/2015) (13); Deveres dos Estados e Direitos Protegidos (arts. 1º a 32 da CADH-OAS) (12); Lei nº 8.842/1994 - Política Nacional do Idoso (12); Agenda 2030 - Desenvolvimento Sustentável (11); e mais 49 assuntos.


### 4.2 Aulas disponíveis no cofre

**Língua Portuguesa** (17 aulas): Nivelamento; Ortografia e acentuação gráfica; Classes de palavras I; Classes de palavras II; Classes de palavras III; Estrutura e formação de palavras; Organização sintática das frases; Tipologia da frase e pontuação; Concordância verbal e nominal; Regência verbal e nominal e crase; Coesão e coerência; Semântica: sinônimos, antônimos e parônimos; Interpretação e compreensão de texto; Tipos textuais; Norma culta e registros de linguagem; Atos de comunicação e dicionários; Aula extra.

**Tecnologia, Segurança Cibernética e Crimes Digitais** (30 aulas): Internet, redes e tecnologias digitais; Intranet: VPN; Computação em nuvem: dispositivos e serviços em nuvem; Navegadores: cookies: cache; Correio eletrônico; Redes sociais: plataformas digitais; Segurança da informação e segurança cibernética; Vulnerabilidades: malware: ransomware: phishing; Segurança em redes: Firewall; Backup: recuperação de dados; Prevenção e resposta a incidentes de segurança; Microsoft 365 (BR) - Excel; LibreOffice-BrOffice - Calc; Microsoft 365 (BR) - Word; LibreOffice-BrOffice - Writer; Microsoft 365 (BR) - PowerPoint; LibreOffice-BrOffice - Impress; Sistemas operacionais - Windows 11 (BR); Android e iOS - instalação, configuração e segurança; Google Workspace; Fundamentos de informática - hardware e software; Noções de lógica de programação; Aplicações web, HTML; CSS; Bancos de dados; APIs; JavaScript; Legislação e ética digital - LGPD; Marco Civil da Internet (Lei 12.965-2014); Lei dos Crimes Informáticos (Lei 12.737-2012).

**Ciências Forenses** (11 aulas): Perícias Médico-Legais; Medicina Legal - Conceitos e Divisões; Antropologia Forense; Identificação Humana; Traumatologia Forense; Asfixiologia; Balística Forense; Tanatologia Forense e Cronotanatognose; Local de Crime, Vestígios e Cadeia de Custódia; Documentoscopia e Grafoscopia; Escolas e Teorias da Criminologia.

**Raciocínio Lógico-Matemático** (25 aulas): Estruturas Lógicas I; Estruturas Lógicas II; Equivalências e Negações Lógicas; Diagramas Lógicos; Lógica de Primeira Ordem; Lógica de Argumentação; Raciocínio Sequencial; Problemas de Lógica I; Problemas de Lógica II; Teoria dos Conjuntos; Conjuntos Numéricos; Operações Básicas, Potenciação e Radiciação; Unidades de Medida; Frações, Razão e Proporção; Regra de Três Simples e Composta; Porcentagem; Equações de 1º Grau; Geometria Plana; Geometria Espacial; Matrizes e Determinantes; Sistemas Lineares; Geometria Analítica; Diagramas, Tabelas e Gráficos; Análise Combinatória; Probabilidade.

**Realidade do Paraná** (6 aulas): Período Pré-Colonial e Colonial (Povos Indígenas); Geografia do Paraná - Aspectos Naturais; Geografia do Paraná - Aspectos Humanos e Econômicos; História do Paraná Colonial; História do Paraná Imperial; História do Paraná Republicano.

**Contabilidade Geral** (12 aulas): Conceitos, objetivos e finalidades; Situação Líquida e Equação Fundamental; Atos e Fatos Contábeis; Plano de Contas e Partidas Dobradas; Regime de Competência e de Caixa; Demonstrações contábeis; Balanço patrimonial: Estoques; Depreciação e Exaustão. CPC 27 - Ativo Imobilizado; CPC 01 Redução ao Valor Recuperável de Ativos; CPC 04 (R1) - Ativo Intangível. Amortização; Princípios contábeis; Movimentações Bancárias Aplicadas à Perícia Contábil.

**Estatística** (13 aulas): Apresentação de Dados; Médias; Medidas Separatrizes ou Quantis; Moda; Medidas de Variabilidade ou Dispersão; Análise Combinatória; Probabilidade; Teoria da Amostragem; Regressão Linear Simples; Séries Temporais; Números Índices; Análise Exploratória de Dados; Porcentagem.

**Legislação Estadual e Institucional** (14 aulas): Constituição do Estado do Paraná; Lei 6.174-1970 - Disposições Constitucionais aos Servidores; Lei 6.174-1970 - Provimento e Vacância; Lei 6.174-1970 - Direitos e Vantagens; Lei 6.174-1970 - Deveres, Proibições e Responsabilidades; Sindicância e Processo Administrativo Disciplinar; Ética no serviço público e sigilo funcional; Lei de Acesso à Informação (12.527-2011); LGPD (13.709-2018); Lei de Abuso de Autoridade; Legislação Institucional e Policial (parte 2); Lei Orgânica Nacional das Polícias Civis (14.735-2023); Estruturação das Carreiras da PC-PR; Lei Orgânica da Polícia Civil do Paraná.

**Direito Penal (com Legislação Penal Extravagante)** (28 aulas): Princípios do Direito Penal; Aplicação da Lei Penal; Teoria do Delito I; Teoria do Delito II; Concurso de pessoas e de crimes; Das penas: espécies e cominação; Aplicação da pena e livramento condicional; Efeitos da condenação e extinção da punibilidade; Crimes contra a pessoa; Crimes contra o patrimônio; Crimes contra a dignidade sexual; Crimes contra a fé pública; Crimes contra a administração pública I; Crimes contra a administração pública II; Crimes contra a administração pública III; Crimes em licitações e contratos; Lei de Execução Penal (7.210-1984); Lei dos Crimes Hediondos (8.072-1990); Crimes contra a ordem tributária e econômica; Lei de Interceptação Telefônica (9.296-1996); Estatuto do Desarmamento (10.826-2003); Lei Maria da Penha (11.340-2006); Lei de Drogas (11.343-2006); Lei das Organizações Criminosas (12.850-2013); Pacote Anticrime (13.964-2019); Estatuto da Advocacia e OAB (8.906-1994); Lavagem de Dinheiro (Lei 9.613-1998); Código de Trânsito Brasileiro.

**Direito Processual Penal** (9 aulas): Introdução e princípios do Processo Penal; Inquérito Policial; Processo, procedimento e relação jurídica processual; Jurisdição e competência; Sujeitos processuais; Provas I: teoria geral e preservação do local; Provas II: provas em espécie; Prisão e liberdade provisória I; Prisão e liberdade provisória II.

**Direito Constitucional** (14 aulas): Aplicabilidade das normas constitucionais; Princípios fundamentais da CF; Direitos e garantias fundamentais I; Direitos e garantias fundamentais II; Direitos sociais; Nacionalidade; Direitos políticos; Organização do Estado; Poder Executivo; Poder Legislativo; Processo Legislativo; Poder Judiciário; Segurança pública na CF (art. 144); Controle de constitucionalidade.

**Direito Administrativo** (15 aulas): Princípios do Direito Administrativo; Conceito e fontes; Administração direta e indireta: autarquias; Fundações, empresas públicas e sociedades de economia mista; Poderes administrativos; Atos administrativos; Licitações I (Lei 14.133-2021); Licitações II (Lei 14.133-2021); Contratos administrativos; Serviços públicos; Controle da Administração Pública; Responsabilidade civil do Estado; Agentes públicos: cargos, empregos e funções; Improbidade administrativa (Lei 8.429-1992); Lei de Introdução às Normas do Direito Brasileiro (LINDB).

**Direitos Humanos** (11 aulas): Teoria Geral dos Direitos Humanos; Características e evolução histórica dos Direitos Humanos; Sistemas de proteção I; Sistemas de proteção II; Tratados internacionais de proteção; Democracia, cidadania e Direitos Humanos; Grupos vulneráveis; Segurança pública e Direitos Humanos; Política Nacional de Direitos Humanos; Agenda 2030 e ODS; CF-88 e Direitos Humanos.


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
- Cerca de 109 questões vieram sem alternativas legíveis por causa de exportações achatadas; estão no banco marcadas, sem alternativas.
- O banco reflete o recorte coletado pelo aluno, não o universo de questões da banca.

## 8. Ferramentas usadas

- Google NotebookLM, acessado pela linha de comando `notebooklm-py` v0.8.1.
- Obsidian, como cofre de notas em markdown.
- Claude Code, onde a skill roda.
- Anki, destino dos flashcards gerados pelo método descrito nas notas de método.
- Python 3, sem dependências além da biblioteca padrão para os scripts de montagem.

Extração e montagem feitas em 05/09/2026.
