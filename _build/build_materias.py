"""Monta materias/<materia>/ para leitura pública: guia completo do notebook, guias por tema, conceitos e pegadinhas,
assuntos em ordem de incidência, aulas disponíveis (só títulos) e notas curadas de autoria do próprio usuário
(Português FGV e catálogo de pegadinhas). NÃO copia apostilas de curso nem questões na íntegra."""
import os, re, io, sys, json, shutil, glob, unicodedata
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
VAULT = r"C:\Users\USER\OneDrive\EstudoObsidian\Estudo\PCPR 2026"
OUT = os.path.join(ROOT, 'materias')
rows = {r['id']: r for r in json.load(open(os.path.join(HERE, 'nb_index.json'), encoding='utf-8'))}
def slug(s):
    s = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode().lower()
    return re.sub(r'[^a-z0-9]+', '-', s).strip('-')
M = [  # (matéria, peso, notebooks, matéria no banco, pasta no vault, notas curadas extras)
 ("Língua Portuguesa", 25, ["5beaebcc-a76f-426c-9551-c4bd3e527600", "e5690053-99e5-4d7e-87e8-98e697a3d047", "ae986a01-c8f9-46fe-9da4-b8e614a86d10"], "Língua Portuguesa", ["Língua Portuguesa"], ["Português FGV"]),
 ("Tecnologia, Segurança Cibernética e Crimes Digitais", 25, ["546f0cb3-6aab-4b5b-97ac-7e8c7adec19c"], "Tecnologia e Segurança Cibernética", ["Tecnologia e Segurança Cibernética"], []),
 ("Ciências Forenses", 10, ["367433a3-ad6a-4cf4-9ff1-8221a4c6abb3", "8498c1e7-ece3-49b4-9b95-65c9785541b7"], "Ciências Forenses", ["Ciências Forenses"], []),
 ("Raciocínio Lógico-Matemático", 5, ["5714ea7c-de27-44b2-aab4-aeb30121b411"], "Raciocínio Lógico-Matemático", ["Raciocínio Lógico-Matemático"], []),
 ("Realidade do Paraná", 5, ["42b917ff-915d-4b69-9b5e-e4bda9a4a232"], "Realidade do Paraná", ["Realidade do Paraná"], []),
 ("Contabilidade Geral", 5, ["73efc3d0-2a26-482e-a98a-f65ee6f3b538"], "Contabilidade Geral", ["Contabilidade Geral"], []),
 ("Estatística", 5, ["185c9e3e-c37f-4324-9856-9dd96ac71661"], "Estatística", ["Estatística"], []),
 ("Legislação Estadual e Institucional", 5, ["bee037d5-0f9b-4125-ac6e-691b183e57fa"], "Legislação Estadual e Institucional", ["Legislação Estadual e Institucional"], []),
 ("Direito Penal e Legislação Penal Extravagante", 3, ["66410a65-3c39-4c6e-b49f-9b2ddcafa4a7"], "Direito Penal", ["Direito Penal", "Legislação Penal Extravagante"], []),
 ("Direito Processual Penal", 3, ["ff239db3-703f-43fd-8240-2fbb1843f9fb"], "Direito Processual Penal", ["Direito Processual Penal"], []),
 ("Direito Constitucional", 3, ["b63c5fdb-187a-4616-a267-e9ac15a926f6"], "Direito Constitucional", ["Direito Constitucional"], []),
 ("Direito Administrativo", 3, ["01d11b38-610b-49dd-b95d-1c04513c2b75"], "Direito Administrativo", ["Direito Administrativo"], []),
 ("Direitos Humanos", 3, [], "Direitos Humanos", ["Direitos Humanos"], []),
 ("Método de estudo", 0, ["84eec3f0-185a-475a-bbdb-171dac0733e1", "02ef5b8b-6409-48c5-8066-36b557273692", "8677f4e5-7a16-4a97-a42c-0cb1db02883a", "3b393eaf-1dc1-498c-bd6f-e45d24abb17d", "130465ab-f48f-42c5-9b49-4c015e948c4e", "17b41580-33c9-4eb0-9e58-ed2ad79e84ac"], None, [], ["Método"]),
]
METODO_OK = {"Catálogo de pegadinhas.md", "Método FGV — instruções do projeto.md", "Guia — montar o método do zero.md", "Prompt Mestre — Professor Reverso FGV.md", "Prompt Mestre — Engenharia Reversa FGV (PCPR 2026).md"}
bank = json.load(open(os.path.join(ROOT, 'questoes', 'banco.json'), encoding='utf-8')) if os.path.exists(os.path.join(ROOT, 'questoes', 'banco.json')) else []
if os.path.isdir(OUT): shutil.rmtree(OUT)
os.makedirs(OUT)
idx = ["# Materiais por matéria", "", "Uma pasta por matéria da prova de Agente da PC-PR 2026 (banca FGV). Cada pasta tem um `README.md` com o que existe para aquela matéria.",
       "Todo o conteúdo aqui é síntese gerada a partir do material de estudo (guias por tema, conceitos, pegadinhas) ou nota de autoria própria. Apostilas de curso e questões na íntegra não estão aqui.", "",
       "| Matéria | Questões na prova | Guias | Notas |", "|---|---:|---:|---:|"]
for nome, peso, ids, qm, vdirs, extras in M:
    d = os.path.join(OUT, slug(nome)); os.makedirs(d)
    L = [f"# {nome}", ""]
    if peso: L.append(f"**{peso} questões** na prova do Agente PC-PR 2026 (de 100).")
    L.append("")
    n_g = n_n = 0
    # guias completos + conceitos
    for i in ids:
        r = rows[i]; s = r['slug']
        g = os.path.join(ROOT, 'guias', s + '.md')
        if os.path.exists(g):
            shutil.copy(g, os.path.join(d, f'guia-{s}.md')); n_g += 1
            L.append(f"- 📘 [Guia completo: {r['title']}](guia-{s}.md)")
        nb = os.path.join(ROOT, 'notebooks', s + '.md')
        if os.path.exists(nb):
            L.append(f"- 🧩 [Índice, conceitos-chave e pegadinhas](../../notebooks/{s}.md)")
        td = os.path.join(ROOT, 'guias', s)
        if os.path.isdir(td):
            tf = sorted(f for f in os.listdir(td) if f.endswith('.md'))
            if tf:
                sub = os.path.join(d, 'temas-' + s); os.makedirs(sub, exist_ok=True)
                L.append(f"- 📚 Guias por tema ({len(tf)}):")
                for f in tf:
                    shutil.copy(os.path.join(td, f), os.path.join(sub, f)); n_g += 1
                    L.append(f"  - [{f[3:-3].replace('-', ' ')}](temas-{s}/{f})")
    # notas curadas do usuário
    for ex in extras:
        src = os.path.join(VAULT, ex)
        for f in sorted(glob.glob(os.path.join(src, '*.md'))):
            bn = os.path.basename(f)
            if ex == 'Método' and bn not in METODO_OK: continue
            if bn.startswith('00 ') or 'Sem título' in bn: continue
            sub = os.path.join(d, 'notas'); os.makedirs(sub, exist_ok=True)
            shutil.copy(f, os.path.join(sub, bn)); n_n += 1
    if n_n:
        L.append(f"- ✍️ Notas de autoria própria ({n_n}) em [notas/](notas/)")
    # incidência
    if qm:
        qs = [q for q in bank if q['materia'] == qm or (qm == 'Direito Penal' and q['materia'] == 'Legislação Penal Extravagante')]
        if qs:
            by_a = {}
            for q in qs: by_a[q['assunto'] or '(sem assunto)'] = by_a.get(q['assunto'] or '(sem assunto)', 0) + 1
            L += ["", f"## Assuntos em ordem de incidência ({len(qs)} questões da banca no banco)", ""]
            L += [f"- {a} ({n})" for a, n in sorted(by_a.items(), key=lambda x: -x[1])]
    # aulas (títulos)
    aulas = []
    for vd in vdirs:
        for f in sorted(glob.glob(os.path.join(VAULT, 'Resumos MD', vd, 'Aula *.md'))):
            mm = re.match(r'(Aula [^-]+?) - (.+) - (Resumo|Simplificada|Apostila completa)\.md', os.path.basename(f))
            if mm:
                t = f"{mm.group(1).strip()} · {mm.group(2).strip()}"
                if t not in aulas: aulas.append(t)
    if aulas:
        L += ["", f"## Programa de aulas coberto ({len(aulas)})", ""] + [f"- {a}" for a in aulas]
    open(os.path.join(d, 'README.md'), 'w', encoding='utf-8').write('\n'.join(L))
    idx.append(f"| [{nome}]({slug(nome)}/README.md) | {peso or '—'} | {n_g} | {n_n} |")
open(os.path.join(OUT, 'README.md'), 'w', encoding='utf-8').write('\n'.join(idx))
print('materias ok')
