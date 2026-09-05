"""Indexa o vault do Obsidian para o Professor.
- Professor/vault/INDICE-VAULT.md : por matéria, hub + aulas (caminho, tamanho, versão R/S/A), cadernos, notas curadas
- Professor/vault/notas/            : cópia das notas curadas pequenas do próprio usuário (método, plano, registro, hubs, Português FGV, método)
Apostilas (Resumos MD) e dumps de curso (Baralhos/MD Estudo) ficam só referenciados por caminho.
"""
import os, re, io, sys, shutil, glob, unicodedata
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
VAULT = r"C:\Users\USER\OneDrive\EstudoObsidian\Estudo"
P = os.path.join(VAULT, 'PCPR 2026')
OUT = r"C:\Users\USER\Professor\vault"
NOTAS = os.path.join(OUT, 'notas')
os.makedirs(NOTAS, exist_ok=True)

def kb(p): return os.path.getsize(p) // 1024
def rel(p): return os.path.relpath(p, VAULT).replace('\\', '/')

PESO = {'Língua Portuguesa': 25, 'Tecnologia e Segurança Cibernética': 25, 'Ciências Forenses': 10,
        'Raciocínio Lógico-Matemático': 5, 'Realidade do Paraná': 5, 'Contabilidade Geral': 5, 'Estatística': 5,
        'Legislação Estadual e Institucional': 5, 'Direito Penal': 3, 'Direito Processual Penal': 3,
        'Direito Constitucional': 3, 'Direito Administrativo': 3, 'Direitos Humanos': 3,
        'Legislação Penal Extravagante': 3}
CADERNO = {'Língua Portuguesa': ['Caderno — Língua Portuguesa.md'],
           'Tecnologia e Segurança Cibernética': ['Caderno — Tecnologia e Direito Digital.md', 'Caderno — LGPD.md', 'Nuvem — Questões Mais Difíceis (Cloud Computing).md'],
           'Direitos Humanos': ['Caderno — Direitos Humanos.md'], 'Estatística': ['Caderno — Estatística.md', 'Caderno Estatística para Agente - PC-PR 2026 (Tec).md'],
           'Contabilidade Geral': ['Caderno — Contabilidade Geral.md', 'BALANCOPATRIMONIAL.md', 'CPC 16 - Tratamento Contábil para os Estoques.md',
                                   'Provisões, Passivos e Ativos Contingentes (CPC 25, Lei 6.404).md', 'Índices de Liquidez. Capital Circulante Líquido.md',
                                   'Demonstração do Resultado do Exercício (DRE) e Destinação do Resultado.md',
                                   'Elaboração e Apresentação das Demonstrações Contábeis (CPC 26, Lei 6.404, arts. 176 e 177).md'],
           'Raciocínio Lógico-Matemático': ['Caderno — Raciocínio Lógico e Matemática.md'],
           'Direito Penal': ['Caderno — Direito Penal e Processual Penal.md'], 'Direito Processual Penal': ['Caderno — Direito Penal e Processual Penal.md'],
           'Legislação Estadual e Institucional': ['Caderno Legislação Estadual e Institucional - PC-PR 2026.md', 'Caderno Inéditas - PC-PR 2026.md'],
           'Direito Constitucional': ['Caderno Inéditas - PC-PR 2026.md'], 'Direito Administrativo': ['Caderno Inéditas - PC-PR 2026.md']}
RAIZ = {'Direito Administrativo': ['questoes direito adm.md'], 'Ciências Forenses': ['exame de corpo de delito.md', 'Fenômenos Cadavéricos.md', 'pcpi questoes.md'],
        'Direito Constitucional': ['Dos Direitos e Deveres Individuais e Coletivos (art. 5º da CF1988).md',
                                   'União Bens e Competências Exclusivas, Privativas, Comuns e Concorrentes (arts. 20 a 24 da CF 1988).md',
                                   'Questões Jurisprudência dos Tribunais Superiores sobre Direitos e Deveres Individuais e Coletivos.md'],
        'Língua Portuguesa': ['Reescrita de Frases. Substituição de Palavras ou Trechos de Texto..md', 'PCPR 2026/PCPR 2026 — Língua Portuguesa FGV.md',
                              'PCPR 2026/Relatório de Incidência — Língua Portuguesa FGV.md'],
        'Realidade do Paraná': ['PCPR 2026/REALIDADE DO PARÁNA.md'],
        'Tecnologia e Segurança Cibernética': ['PCPR 2026/PCPR 2026 — TI, Direito Digital e Da Prova (CPP)_2.md']}
L = ['# Índice do vault do Obsidian', '', f'Vault: `{VAULT}` (OneDrive; conferir se a pasta está baixada antes de concluir que algo não existe).',
     'Comece pelo hub de cada matéria. Apostilas têm até três versões: R = resumo, S = simplificada, A = apostila completa.',
     'Questões já extraídas e deduplicadas estão em `../questoes/` (ver `INDICE.md` lá).', '',
     '> As notas listadas abaixo são copiadas para `vault/notas/` na máquina local, para o professor consultar.',
     '> Essa pasta não faz parte do repositório público (conteúdo pessoal), por isso os nomes aparecem sem link.', '',
     '## Matérias', '']
copied = []
def copy_note(src):
    if not os.path.exists(src) or kb(src) > 120: return None
    dst = os.path.join(NOTAS, os.path.basename(src))
    shutil.copy(src, dst); copied.append(os.path.basename(src)); return 'notas/' + os.path.basename(src)
for mat in sorted(PESO, key=lambda m: -PESO[m]):
    d = os.path.join(P, 'Resumos MD', mat)
    if not os.path.isdir(d): continue
    L.append(f'### {mat} — {PESO[mat]} questões')
    hub = os.path.join(d, f'00 — Hub {mat}.md')
    if os.path.exists(hub):
        copy_note(hub)
        L.append(f'- Hub: `{os.path.basename(hub)}`  ·  vault: `{rel(hub)}`')
    aulas = {}
    for f in sorted(glob.glob(os.path.join(d, 'Aula *.md'))):
        m = re.match(r'(Aula [^-]+?) - (.+) - (Resumo|Simplificada|Apostila completa)\.md', os.path.basename(f))
        if not m: continue
        key = (m.group(1).strip(), m.group(2).strip())
        aulas.setdefault(key, []).append((m.group(3)[0], kb(f), rel(f)))
    L.append(f'- Apostilas ({len(aulas)} aulas) em `{rel(d)}/`:')
    for (n, t), vs in aulas.items():
        L.append(f'  - {n} · {t} · ' + ' · '.join(f'{v} {k}KB' for v, k, _ in vs))
    cads = [os.path.join(P, 'Cadernos de Questões', c) for c in CADERNO.get(mat, [])]
    cads = [c for c in cads if os.path.exists(c)]
    if cads:
        L.append('- Cadernos de questões (vault): ' + ' · '.join(f'`{rel(c)}` ({kb(c)}KB)' for c in cads))
    for r in RAIZ.get(mat, []):
        src = os.path.join(VAULT, r)
        if os.path.exists(src): L.append(f'- Nota solta: `{rel(src)}` ({kb(src)}KB)')
    L.append('')
# curated folders
L += ['## Notas curadas do usuário (copiadas em `notas/`)', '']
for folder, desc in [('Plano', 'plano de estudo, pesos, rotina, ciclo de blocos'), ('Método', 'método FGV, catálogo de pegadinhas P1-P10/T1-T4, prompts mestres'),
                     ('Registro', 'autópsia de erros, simulado, decisões'), ('Português FGV', '18 notas por tema de Português no recorte FGV'),
                     ('Valter', 'método de estudo em 10 notas'), ('Leis e Doutrina', 'lei de carreira da PC-PR'), ('Baralhos', 'mapa de baralhos e workflow Anki'),
                     ('Cadernos de Questões', 'hub dos cadernos'), ('NotebookLM', 'uma nota por notebook do NotebookLM'), ('PROMPTS NOTEBOOKLM', 'prompts usados no NotebookLM'),
                     ('.', 'MOC, índice e mapa do vault')]:
    d = os.path.join(P, folder)
    fs = sorted(glob.glob(os.path.join(d, '*.md')))
    if folder == 'Cadernos de Questões': fs = [f for f in fs if os.path.basename(f).startswith('00')]
    if folder == '.': fs = [f for f in fs] + [os.path.join(VAULT, '_inventario-do-vault.md')]
    if not fs: continue
    L.append(f'### {folder if folder != "." else "PCPR 2026 (raiz)"} — {desc}')
    for f in fs:
        if 'Sem título' in f: continue
        c = copy_note(f)
        L.append(f'- `{os.path.basename(f)}`' if c else f'- `{rel(f)}` ({kb(f)}KB, não copiada)')
    L.append('')
L += ['## Dumps de curso (só referência)', '']
for f in sorted(glob.glob(os.path.join(P, 'Baralhos', 'MD Estudo', '*.md'))):
    L.append(f'- `{rel(f)}` ({kb(f)}KB)')
L += ['', '## Cards Anki já gerados', '']
for f in sorted(glob.glob(os.path.join(P, 'Cards', '*'))):
    L.append(f'- `{rel(f)}` ({kb(f)}KB)')
open(os.path.join(OUT, 'INDICE-VAULT.md'), 'w', encoding='utf-8').write('\n'.join(L))
print('INDICE-VAULT linhas', len(L), 'notas copiadas', len(copied))
