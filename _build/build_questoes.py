"""Extrai todas as questões dos cadernos do vault do Obsidian para Professor/questoes/.

Formatos reconhecidos:
  A) caderno curado v1: **Q123** · banca · [ver na fonte](url) ... gabarito em tabela | Q123 | C | no fim do bloco
  C) caderno curado v2: **Q001** · banca ... <sub>[tecconcursos.com.br/questoes/ID](url) · assunto</sub>, gabarito em tabela
  B) export TecConcursos: link questoes/ID, linha banca (termina em /ano), linha "Matéria - Assunto", "N)" ... "Gabarito: X"
  D) export achatado numa linha só (pcpi): "banca/ano Matéria - Assunto 1) enunciado a) ... e) ... Gabarito: X"
Dedup por ID do TecConcursos. Saída: banco.json, INDICE.md, <materia>.md
"""
import os, re, json, io, sys, glob, unicodedata
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
VAULT = r"C:\Users\USER\OneDrive\EstudoObsidian\Estudo"
OUT = r"C:\Users\USER\Professor\questoes"
if os.path.isdir(OUT):  # limpa saidas antigas do parser anterior
    for _f in os.listdir(OUT):
        if _f.endswith('.md'):
            os.remove(os.path.join(OUT, _f))
os.makedirs(OUT, exist_ok=True)

def slug(s):
    s = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode().lower()
    return re.sub(r'[^a-z0-9]+', '-', s).strip('-')[:60]

def clean(t):
    t = t.replace('\u00a0', ' ')
    t = re.sub(r'!\[\]\([^)]*\)', '', t)
    t = re.sub(r'<sub>.*?</sub>', '', t, flags=re.S)
    t = re.sub(r'!?\[[^\]]*\]\(chrome-extension://[^)]*\)', '', t)
    t = re.sub(r'[ \t]+\n', '\n', t)
    t = re.sub(r'\n{3,}', '\n\n', t)
    return t.strip()

ALT_LINE = re.compile(r'^\s*(?:-\s*)?\*{0,2}\(?([a-eA-E])[\)\.]\*{0,2}\s+(.*)$')
BANCA_RE = re.compile(r'^[A-ZÀ-Ú][^\n]{2,120}/\d{4}\s*$')
FOOTER_RE = re.compile(r'^(\d+/\d+|\d{2}/\d{2}/\d{4},? \d{2}:\d{2}.*|Caderno .*|https?://\S+|www\.\S+|Ordenação:.*|Direito .* para .* - \d{4})$')

def split_alts(lines):
    enun, alts = [], []
    for ln in lines:
        am = ALT_LINE.match(ln)
        if am and len(ln.strip()) > 3:
            alts.append([am.group(1).upper(), am.group(2).strip()])
        elif alts:
            if ln.strip():
                alts[-1][1] += ' ' + ln.strip()
        else:
            enun.append(ln)
    return clean('\n'.join(enun)), [(a[0], clean(a[1])) for a in alts]

def gab_table(text):
    return {m.group(1): m.group(2) for m in re.finditer(r'\|\s*Q(\d+)\s*\|\s*([A-E])\s*\|', text)}

def heading_clean(h):
    return re.sub(r'^[^\wÀ-ú]+', '', h).strip()

def parse_curated(text, fname):
    qs, gab = {}, gab_table(text)
    materia = assunto = ''
    for b in re.split(r'\n---\n', text):
        for h in re.findall(r'^##\s+(.+)$', b, re.M):
            materia = heading_clean(h)
        for h in re.findall(r'^###\s+(.+)$', b, re.M):
            assunto = h.strip()
        m = re.search(r'\*\*Q(\d+)\*\*\s*·\s*(.+?)\s*·\s*\[ver na fonte\]\((https?://[^)]+/questoes/(\d+))\)', b)
        if m:
            qn, banca, url, tid = m.group(1), m.group(2), m.group(3), m.group(4)
            body = b[m.end():]
        else:
            m = re.search(r'\*\*Q(\d+)\*\*\s*·\s*(.+)', b)
            s = re.search(r'<sub>\[[^\]]*questoes/(\d+)\]\((https?://[^)]+)\)(?:\s*·\s*([^<]+))?</sub>', b)
            if not m or not s:
                continue
            qn, banca, tid, url = m.group(1), m.group(2).strip(), s.group(1), s.group(2)
            if s.group(3): assunto = s.group(3).strip()
            body = b[m.end():s.start()]
        body = re.split(r'\n#{2,3}\s', body)[0]
        enun, alts = split_alts(body.split('\n'))
        qs[tid] = dict(id=tid, url=url, banca=banca, materia=materia, assunto=assunto, enunciado=enun,
                       alternativas=alts, gabarito=gab.get(qn, ''), origem=fname)
    return qs

def parse_flat_line(line):
    m = re.match(r'^\s*(.*?/\d{4})\s+(.+?)\s+\d+\)\s+(.*)$', line)
    if not m:
        return None
    banca, ma, rest = m.groups()
    gm = re.search(r'Gabarito:\s*\**([A-E])', rest)
    gab = gm.group(1) if gm else ''
    rest = rest[:gm.start()] if gm else rest
    parts = re.split(r'\s(?=[a-e]\)\s)', rest)
    enun = parts[0].strip()
    alts = []
    for p in parts[1:]:
        am = re.match(r'([a-e])\)\s*(.*)', p.strip(), re.S)
        if am: alts.append((am.group(1).upper(), am.group(2).strip()))
    return banca, ma, enun, alts, gab

def parse_raw(text, fname):
    qs = {}
    text = text.replace('\r', '')
    parts = re.split(r'\[?(?:https?://)?www\.tecconcursos\.com\.br/questoes/(\d+)\]?(?:\([^)]*\))?', text)
    last_ma = ''
    for i in range(1, len(parts) - 1, 2):
        tid, body = parts[i], parts[i + 1]
        lines = body.split('\n')
        ne = [l.strip() for l in lines if l.strip() and not FOOTER_RE.match(l.strip())]
        if not ne:
            continue
        flat = parse_flat_line(ne[0]) if re.search(r'/\d{4}\s+\S.*\s\d+\)\s', ne[0]) else None
        if flat:
            banca, ma, enun, alts, gab = flat
        else:
            banca = next((l for l in ne[:3] if BANCA_RE.match(l)), ne[0])
            after = ne[ne.index(banca) + 1:]
            ma = next((l for l in after[:2] if ' - ' in l and len(l) < 220 and not re.match(r'^\**\d+\)', l) and not l.endswith(('?', ':', '.'))), '')
            if not ma:
                ma = last_ma
            gm = re.search(r'Gabarito:\s*\**([A-E])', body)
            gab = gm.group(1) if gm else ''
            body2 = body[:gm.start()] if gm else body
            out, skipped = [], set()
            for ln in body2.split('\n'):
                s = ln.strip()
                if s and (s == banca or s == ma) and s not in skipped:
                    skipped.add(s); continue
                if s and FOOTER_RE.match(s):
                    continue
                out.append(ln)
            txt = re.sub(r'^\s*\**\d+\)\**\s*', '', '\n'.join(out).strip(), count=1)
            enun, alts = split_alts(txt.split('\n'))
        last_ma = ma
        materia, assunto = (ma.split(' - ', 1) + [''])[:2] if ' - ' in ma else (ma, '')
        if not alts and not enun:
            continue
        qs[tid] = dict(id=tid, url=f'https://www.tecconcursos.com.br/questoes/{tid}', banca=banca.strip(),
                       materia=materia.strip(), assunto=assunto.strip(), enunciado=enun,
                       alternativas=alts, gabarito=gab, origem=fname)
    return qs

MAT = [  # (regex sobre matéria original, matéria normalizada)
    (r'^Língua Portuguesa', 'Língua Portuguesa'),
    (r'Contabilidade|Demonstrações Contábeis', 'Contabilidade Geral'),
    (r'^Direito Administrativo Estadual|^Direito Constitucional Estadual|Segurança Pública e Legislação Policial|Legislação Estadual', 'Legislação Estadual e Institucional'),
    (r'^Direito Administrativo', 'Direito Administrativo'),
    (r'^Direito Constitucional', 'Direito Constitucional'),
    (r'^Direitos Humanos|Ciências Sociais|Direito Educacional|Criança e do Adolescente', 'Direitos Humanos'),
    (r'^Estatística', 'Estatística'),
    (r'Direito Digital|^TI$|Informática|Tecnologia', 'Tecnologia e Segurança Cibernética'),
    (r'Matemática|Raciocínio Lógico', 'Raciocínio Lógico-Matemático'),
    (r'Legislação Penal|Penal Especial', 'Legislação Penal Extravagante'),
    (r'^Direito Processual Penal', 'Direito Processual Penal'),
    (r'^Direito Penal', 'Direito Penal'),
    (r'Criminalística|Medicina Legal|Criminologia|Perícia', 'Ciências Forenses'),
    (r'Ética Profissional', 'Legislação Estadual e Institucional'),
]
FILE_MAT = {'exame de corpo de delito': 'Ciências Forenses', 'Fenômenos Cadavéricos': 'Ciências Forenses', 'pcpi questoes': 'Ciências Forenses',
            'Dos Direitos e Deveres': 'Direito Constitucional', 'União Bens': 'Direito Constitucional', 'Jurisprudência dos Tribunais': 'Direito Constitucional',
            'Reescrita de Frases': 'Língua Portuguesa', 'questoes direito adm': 'Direito Administrativo'}
def normalize(q):
    q['materia_original'] = q['materia']
    m = q['materia']
    for rx, norm in MAT:
        if re.search(rx, m, re.I):
            q['materia'] = norm; return
    for k, v in FILE_MAT.items():
        if k in q['origem']:
            q['materia'] = v; return
    q['materia'] = 'Outras'

files = []
for pat in ['PCPR 2026/Cadernos de Questões/*.md', 'PCPR 2026/Questoes/*.md', '*.md']:
    files += glob.glob(os.path.join(VAULT, pat))
files = [f for f in files if not os.path.basename(f).startswith(('00 ', '_')) and 'inventario' not in f
         and 'prompt' not in f.lower() and 'Sem título' not in f]
bank, stats = {}, []
for f in files:
    t = open(f, encoding='utf-8', errors='replace').read()
    name = os.path.relpath(f, VAULT).replace('\\', '/')
    if '[ver na fonte]' in t or '<sub>[tecconcursos' in t:
        qs = parse_curated(t, name)
    elif 'tecconcursos.com.br/questoes/' in t:
        qs = parse_raw(t, name)
    else:
        continue
    new = 0
    for k, v in qs.items():
        better = k in bank and not bank[k]['gabarito'] and v['gabarito']
        if k not in bank or better or (k in bank and len(v['alternativas']) > len(bank[k]['alternativas'])):
            if k not in bank: new += 1
            bank[k] = v
    stats.append((name, len(qs), new))
    print(f'{len(qs):5d} q  {new:5d} novas  {name}')
for q in bank.values():
    normalize(q)
bad = [q for q in bank.values() if len(q['alternativas']) < 2]
print('sem alternativas (mantidas, marcadas):', len(bad))
json.dump(list(bank.values()), open(os.path.join(OUT, 'banco.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=0)

by_m = {}
for q in bank.values():
    by_m.setdefault(q['materia'], []).append(q)
idx = ['# Banco de questões (vault Obsidian)', '',
       f'{len(bank)} questões únicas (dedup por ID da fonte), {sum(1 for q in bank.values() if q["gabarito"])} com gabarito, extraídas de {len(stats)} arquivos do vault.',
       'Cada arquivo abaixo tem as questões da matéria agrupadas por assunto, com gabarito logo após cada questão.',
       'Uso pelo professor: Grep pelo assunto ou por palavra-chave no arquivo da matéria; use as questões reais como modelo antes de inventar uma.', '',
       '> Os arquivos por matéria, com os enunciados na íntegra, ficam só na máquina local: são questões de terceiros.',
       '> O que este índice publica é a contagem por matéria e assunto, que é a incidência observada da banca.', '',
       '| Matéria | Questões | Com gabarito | Assuntos | Arquivo |', '|---|---:|---:|---:|---|']
for m in sorted(by_m, key=lambda x: -len(by_m[x])):
    qs = by_m[m]
    fn = slug(m) + '.md'
    by_a = {}
    for q in qs:
        by_a.setdefault(q['assunto'] or '(sem assunto)', []).append(q)
    idx.append(f'| {m} | {len(qs)} | {sum(1 for q in qs if q["gabarito"])} | {len(by_a)} | `{fn}` |')
    L = [f'# {m} — {len(qs)} questões', '', '## Assuntos (por volume)', '']
    for a in sorted(by_a, key=lambda x: -len(by_a[x])):
        L.append(f'- {a}: {len(by_a[a])}')
    for a in sorted(by_a, key=lambda x: -len(by_a[x])):
        L.append(f'\n## {a} ({len(by_a[a])})\n')
        for q in by_a[a]:
            L.append(f'### {q["id"]} · {q["banca"]}')
            L.append(q['enunciado'] or '(enunciado não recuperado)')
            L.append('')
            for k, v in q['alternativas']:
                L.append(f'- ({k}) {v}')
            L.append(f'\n**Gabarito: {q["gabarito"] or "?"}** · [fonte]({q["url"]})\n')
    open(os.path.join(OUT, fn), 'w', encoding='utf-8').write('\n'.join(L))
idx += ['', '## Assuntos por matéria', '']
for m in sorted(by_m, key=lambda x: -len(by_m[x])):
    by_a = {}
    for q in by_m[m]:
        by_a.setdefault(q['assunto'] or '(sem assunto)', 0); by_a[q['assunto'] or '(sem assunto)'] += 1
    idx.append(f'### {m}')
    idx += [f'- {a} ({n})' for a, n in sorted(by_a.items(), key=lambda x: -x[1])]
    idx.append('')
idx += ['## Arquivos de origem', '', '| Arquivo do vault | Questões lidas | Novas após dedup |', '|---|---:|---:|']
idx += [f'| {n} | {a} | {b} |' for n, a, b in stats]
open(os.path.join(OUT, 'INDICE.md'), 'w', encoding='utf-8').write('\n'.join(idx))
print('TOTAL', len(bank), 'com gabarito', sum(1 for q in bank.values() if q['gabarito']))
for m in sorted(by_m, key=lambda x: -len(by_m[x])):
    print(f'  {len(by_m[m]):5d}  {m}')
