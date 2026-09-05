import json, os, io, sys, re, glob, unicodedata
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
os.chdir(ROOT)
VAULT_RES = r"C:\Users\USER\OneDrive\EstudoObsidian\Estudo\PCPR 2026\Resumos MD"
rows = {r['id']: r for r in json.load(open('_build/nb_index.json', encoding='utf-8'))}
DISPLAY = {'84eec3f0-185a-475a-bbdb-171dac0733e1': 'Método de estudo para concursos (videoaulas)',
           '5714ea7c-de27-44b2-aab4-aeb30121b411': 'Exatas e lógica (videoaulas)'}
def title(i): return DISPLAY.get(i, rows[i]['title'])
# (matéria do edital, questões na prova, notebooks, matéria no banco/vault)
G = [("Língua Portuguesa", 25, ["5beaebcc-a76f-426c-9551-c4bd3e527600", "e5690053-99e5-4d7e-87e8-98e697a3d047", "ae986a01-c8f9-46fe-9da4-b8e614a86d10"], "Língua Portuguesa"),
     ("Tecnologia, Segurança Cibernética e Crimes Digitais", 25, ["546f0cb3-6aab-4b5b-97ac-7e8c7adec19c"], "Tecnologia e Segurança Cibernética"),
     ("Ciências Forenses", 10, ["367433a3-ad6a-4cf4-9ff1-8221a4c6abb3", "8498c1e7-ece3-49b4-9b95-65c9785541b7"], "Ciências Forenses"),
     ("Raciocínio Lógico-Matemático", 5, ["5714ea7c-de27-44b2-aab4-aeb30121b411"], "Raciocínio Lógico-Matemático"),
     ("Realidade do Paraná", 5, ["42b917ff-915d-4b69-9b5e-e4bda9a4a232"], "Realidade do Paraná"),
     ("Contabilidade Geral", 5, ["73efc3d0-2a26-482e-a98a-f65ee6f3b538"], "Contabilidade Geral"),
     ("Estatística", 5, ["185c9e3e-c37f-4324-9856-9dd96ac71661"], "Estatística"),
     ("Legislação Estadual e Institucional", 5, ["bee037d5-0f9b-4125-ac6e-691b183e57fa"], "Legislação Estadual e Institucional"),
     ("Direito Penal (com Legislação Penal Extravagante)", 3, ["66410a65-3c39-4c6e-b49f-9b2ddcafa4a7"], "Direito Penal"),
     ("Direito Processual Penal", 3, ["ff239db3-703f-43fd-8240-2fbb1843f9fb"], "Direito Processual Penal"),
     ("Direito Constitucional", 3, ["b63c5fdb-187a-4616-a267-e9ac15a926f6"], "Direito Constitucional"),
     ("Direito Administrativo", 3, ["01d11b38-610b-49dd-b95d-1c04513c2b75"], "Direito Administrativo"),
     ("Direitos Humanos", 3, [], "Direitos Humanos")]
EXTRA = [("Método de estudo, memória e mentalidade", ["84eec3f0-185a-475a-bbdb-171dac0733e1", "02ef5b8b-6409-48c5-8066-36b557273692", "8677f4e5-7a16-4a97-a42c-0cb1db02883a", "3b393eaf-1dc1-498c-bd6f-e45d24abb17d", "130465ab-f48f-42c5-9b49-4c015e948c4e", "17b41580-33c9-4eb0-9e58-ed2ad79e84ac"]),
         ("IA e engenharia de prompts", ["831dba20-e87e-4e71-a1d9-e03a9f05deb3"]),
         ("Edital", ["b342beb3-7cc4-497e-b473-5e77c5195673"])]
VAULT_DIR = {"Direito Penal": ["Direito Penal", "Legislação Penal Extravagante"]}

bank = json.load(open('questoes/banco.json', encoding='utf-8')) if os.path.exists('questoes/banco.json') else []
by_m = {}
for q in bank:
    by_m.setdefault(q['materia'], []).append(q)
def qn(m):
    n = len(by_m.get(m, []))
    if m == "Direito Penal": n += len(by_m.get("Legislação Penal Extravagante", []))
    return n
def aulas(m):
    out = []
    for d in VAULT_DIR.get(m, [m]):
        p = os.path.join(VAULT_RES, d)
        seen = set()
        for f in sorted(glob.glob(os.path.join(p, 'Aula *.md'))):
            mm = re.match(r'(Aula [^-]+?) - (.+) - (Resumo|Simplificada|Apostila completa)\.md', os.path.basename(f))
            if mm and mm.group(2).strip() not in seen:
                seen.add(mm.group(2).strip()); out.append(mm.group(2).strip().replace('_', ':'))
    return out
NL = '\n'
tbl = ["| Matéria | Questões na prova | Notebooks | Aulas no cofre | Questões reais no banco |", "|---|---:|---|---:|---:|"]
n_aulas_total = 0; mats_vault = 0
for name, peso, ids, m in G:
    a = aulas(m); n_aulas_total += len(a); mats_vault += 1 if a else 0
    nb = '; '.join(f'[{title(i)}](notebooks/{rows[i]["slug"]}.md)' for i in ids) or 'nenhum'
    tbl.append(f"| {name} | {peso} | {nb} | {len(a)} | {qn(m)} |")
for name, ids in EXTRA:
    nb = '; '.join(f'[{title(i)}](notebooks/{rows[i]["slug"]}.md)' for i in ids)
    tbl.append(f"| {name} | — | {nb} | — | — |")
assuntos = []
for name, peso, ids, m in G:
    qs = by_m.get(m, []) + (by_m.get("Legislação Penal Extravagante", []) if m == "Direito Penal" else [])
    if not qs: continue
    by_a = {}
    for q in qs: by_a[q['assunto'] or '(sem assunto)'] = by_a.get(q['assunto'] or '(sem assunto)', 0) + 1
    top = sorted(by_a.items(), key=lambda x: -x[1])[:12]
    assuntos.append(f"**{name}** ({len(qs)} questões, {len(by_a)} assuntos): " + '; '.join(f"{a} ({n})" for a, n in top) + (f"; e mais {len(by_a)-12} assuntos" if len(by_a) > 12 else "") + ".")
    assuntos.append("")
aul = []
for name, peso, ids, m in G:
    a = aulas(m)
    if a: aul.append(f"**{name}** ({len(a)} aulas): " + '; '.join(a) + "."); aul.append("")
n_assuntos = len({(q['materia'], q['assunto']) for q in bank})
n_fontes = sum(r['n'] for r in rows.values())
mats = sorted(os.listdir('materiais'))
gu = [os.path.getsize(f) for f in glob.glob('guias/*.md')]
guias_kb = str(round(sum(gu) / len(gu) / 1024)) if gu else '?'
# estatísticas de estilo FGV
import statistics
fgv = [q for q in bank if q['banca'].upper().startswith('FGV')]
E = [q['enunciado'] for q in fgv]
alts = [a for q in fgv for _, a in q['alternativas']]
def pct(n, d): return f'{100 * n / d:.0f}%' if d else '0%'
CASO = r'Nesse cenário|Nesse caso|Nessa situação|Diante d|\b(João|Maria|Caio|Tício|Mévio|Pedro|Ana|Paulo|José|Carlos|Joana|Matheus|Lucas)\b'
LEI = r'Lei n[ºo°]|art\.|artigo|Decreto|Súmula|CPC|CF/?88|Constituição'
rows_s = [("Cinco alternativas (A a E)", pct(sum(1 for q in fgv if len(q['alternativas']) == 5), len(fgv))),
          ("Pede a alternativa correta", pct(sum(1 for e in E if re.search(r'(afirmativa|opção|alternativa) correta|é correto afirmar|está correto', e, re.I)), len(fgv))),
          ("Pede a incorreta ou 'exceto'", pct(sum(1 for e in E if re.search(r'incorret|exceto|não é correto|à exceção|errad[ao]', e, re.I)), len(fgv))),
          ("Certo/errado ou V/F", pct(sum(1 for e in E if re.search(r'\(V\)|verdadeir[ao]s? (ou|e) fals', e, re.I)), len(fgv))),
          ("Afirmativas I, II, III", pct(sum(1 for e in E if re.search(r'\bI\.|afirmativas a seguir|itens a seguir', e, re.I)), len(fgv))),
          ("Enunciado com caso concreto (nomes, 'nesse cenário')", pct(sum(1 for e in E if re.search(CASO, e, re.I)), len(fgv))),
          ("Enunciado cita lei, artigo, súmula ou Constituição", pct(sum(1 for e in E if re.search(LEI, e, re.I)), len(fgv))),
          ("Enunciado com mais de 600 caracteres", pct(sum(1 for e in E if len(e) > 600), len(fgv))),
          ("Tamanho mediano do enunciado", f"{statistics.median(len(e) for e in E):.0f} caracteres" if E else '-'),
          ("Tamanho médio de cada alternativa", f"{statistics.mean(len(a) for a in alts):.0f} caracteres" if alts else '-')]
from collections import Counter
gc = Counter(q['gabarito'] for q in fgv if q['gabarito'])
rows_s.append(("Distribuição do gabarito", ', '.join(f"{k} {pct(v, sum(gc.values()))}" for k, v in sorted(gc.items()))))
stats_fgv = NL.join(["| Medida | Valor |", "|---|---|"] + [f"| {a} | {b} |" for a, b in rows_s])
rows_m = ["| Matéria | Questões FGV | Com caso concreto | Cita lei ou artigo | Enunciado mediano |", "|---|---:|---:|---:|---:|"]
for name, peso, ids, m in G:
    qs = [q for q in fgv if q['materia'] == m or (m == 'Direito Penal' and q['materia'] == 'Legislação Penal Extravagante')]
    if len(qs) < 15: continue
    rows_m.append(f"| {name} | {len(qs)} | {pct(sum(1 for q in qs if re.search(CASO, q['enunciado'], re.I)), len(qs))} | {pct(sum(1 for q in qs if re.search(LEI, q['enunciado'], re.I)), len(qs))} | {statistics.median(len(q['enunciado']) for q in qs):.0f} car. |")
stats_materia = NL.join(rows_m)
alt_restritivo = pct(sum(1 for a in alts if re.search(r'\b(somente|apenas|exclusivamente|unicamente)\b', a, re.I)), len(alts))
alt_modal = pct(sum(1 for a in alts if re.search(r'\b(deve|deverá|deverão|obrigatoriamente|pode|poderá|poderão)\b', a, re.I)), len(alts))
n_lidas = 0
try:
    for ln in open('questoes/INDICE.md', encoding='utf-8'):
        mm = re.match(r'\| (.+?) \| (\d+) \| (\d+) \|$', ln.strip())
        if mm and not mm.group(1).startswith('Matéria'): n_lidas += int(mm.group(2))
except Exception: pass
TPL = open(os.path.join(HERE, 'readme_template.md'), encoding='utf-8').read()
TPL = (TPL.replace('{stats_fgv}', stats_fgv).replace('{stats_materia}', stats_materia).replace('{alt_restritivo}', alt_restritivo)
       .replace('{alt_modal}', alt_modal).replace('{n_fgv}', str(len(fgv))).replace('{n_lidas}', str(n_lidas) if n_lidas else 'cerca de 7.000'))
R = (TPL.replace('{n_notebooks}', str(len(rows))).replace('{n_fontes}', str(n_fontes)).replace('{n_aulas}', str(n_aulas_total))
     .replace('{n_materias_vault}', str(mats_vault)).replace('{n_questoes}', str(len(bank))).replace('{n_assuntos}', str(n_assuntos))
     .replace('{n_gabarito}', str(sum(1 for q in bank if q['gabarito']))).replace('{n_sem_alt}', str(sum(1 for q in bank if len(q['alternativas']) < 2)))
     .replace('{tabela_cobertura}', NL.join(tbl)).replace('{assuntos_por_materia}', NL.join(assuntos)).replace('{aulas_por_materia}', NL.join(aul))
     .replace('{n_mats}', str(len(mats))).replace('{guias_kb}', guias_kb))
open('README.md', 'w', encoding='utf-8').write(R)
print('README', len(R), 'aulas', n_aulas_total, 'questoes', len(bank), 'assuntos', n_assuntos)
