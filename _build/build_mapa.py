import json, os, io, sys, glob, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)
CACHE = os.path.join(HERE, 'cache')
rows = {r['id']: r for r in json.load(open(os.path.join(HERE, 'nb_index.json'), encoding='utf-8'))}
DISPLAY = {'84eec3f0-185a-475a-bbdb-171dac0733e1': 'Método de estudo para concursos (videoaulas)',
           '5714ea7c-de27-44b2-aab4-aeb30121b411': 'Exatas e lógica (videoaulas)'}
def title(i): return DISPLAY.get(i, rows[i]['title'])
def summ(i):
    for base in [CACHE, os.getcwd()]:
        p = os.path.join(base, 'summary', f'{i}.json')
        if os.path.exists(p):
            try: return json.load(open(p, encoding='utf-8')).get('summary', '').replace('**', '')
            except Exception: pass
    return ''
def n_mats(i):
    return len(glob.glob(os.path.join(OUT, 'materiais', f'{i[:8]}_*')))
G = [
 ("Edital e regras do concurso", None, ["b342beb3-7cc4-497e-b473-5e77c5195673"]),
 ("Língua Portuguesa", "25 questões", ["5beaebcc-a76f-426c-9551-c4bd3e527600", "e5690053-99e5-4d7e-87e8-98e697a3d047", "ae986a01-c8f9-46fe-9da4-b8e614a86d10"]),
 ("Tecnologia, Segurança Cibernética e Crimes Digitais", "25 questões", ["546f0cb3-6aab-4b5b-97ac-7e8c7adec19c"]),
 ("Ciências Forenses", "10 questões", ["367433a3-ad6a-4cf4-9ff1-8221a4c6abb3", "8498c1e7-ece3-49b4-9b95-65c9785541b7"]),
 ("Raciocínio Lógico-Matemático", "5 questões", ["5714ea7c-de27-44b2-aab4-aeb30121b411"]),
 ("Realidade do Paraná", "5 questões", ["42b917ff-915d-4b69-9b5e-e4bda9a4a232"]),
 ("Contabilidade Geral", "5 questões", ["73efc3d0-2a26-482e-a98a-f65ee6f3b538"]),
 ("Estatística", "5 questões", ["185c9e3e-c37f-4324-9856-9dd96ac71661"]),
 ("Legislação Estadual e Institucional", "5 questões", ["bee037d5-0f9b-4125-ac6e-691b183e57fa"]),
 ("Direito Penal", "3 questões", ["66410a65-3c39-4c6e-b49f-9b2ddcafa4a7"]),
 ("Direito Processual Penal", "3 questões", ["ff239db3-703f-43fd-8240-2fbb1843f9fb"]),
 ("Direito Constitucional", "3 questões", ["b63c5fdb-187a-4616-a267-e9ac15a926f6"]),
 ("Direito Administrativo", "3 questões", ["01d11b38-610b-49dd-b95d-1c04513c2b75"]),
 ("Direitos Humanos", "3 questões", []),
 ("Método de estudo, memória e mentalidade", None, ["84eec3f0-185a-475a-bbdb-171dac0733e1", "02ef5b8b-6409-48c5-8066-36b557273692", "8677f4e5-7a16-4a97-a42c-0cb1db02883a", "3b393eaf-1dc1-498c-bd6f-e45d24abb17d", "130465ab-f48f-42c5-9b49-4c015e948c4e", "17b41580-33c9-4eb0-9e58-ed2ad79e84ac"]),
 ("IA, chatbots e engenharia de prompts", None, ["831dba20-e87e-4e71-a1d9-e03a9f05deb3"]),
]
# questões por matéria
QMAP = {"Língua Portuguesa": "Língua Portuguesa", "Tecnologia, Segurança Cibernética e Crimes Digitais": "Tecnologia e Segurança Cibernética",
        "Ciências Forenses": "Ciências Forenses", "Raciocínio Lógico-Matemático": "Raciocínio Lógico-Matemático", "Contabilidade Geral": "Contabilidade Geral",
        "Estatística": "Estatística", "Legislação Estadual e Institucional": "Legislação Estadual e Institucional", "Direito Penal": "Direito Penal",
        "Direito Processual Penal": "Direito Processual Penal", "Direito Constitucional": "Direito Constitucional", "Direito Administrativo": "Direito Administrativo",
        "Direitos Humanos": "Direitos Humanos"}
qcount = {}
bp = os.path.join(OUT, 'questoes', 'banco.json')
if os.path.exists(bp):
    for q in json.load(open(bp, encoding='utf-8')):
        qcount[q['materia']] = qcount.get(q['materia'], 0) + 1
def slugq(s):
    import unicodedata
    s = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode().lower()
    return re.sub(r'[^a-z0-9]+', '-', s).strip('-')
L = ["# MAPA GERAL — Professor", "",
     "Base de conhecimento do professor, montada em 05/09/2026 a partir de três origens:", "",
     "1. **23 notebooks do NotebookLM** (819 fontes): um arquivo por notebook em `notebooks/`, com índice hierárquico, conceitos-chave, pegadinhas e fontes, e um guia completo por notebook em `guias/`, gerado como relatório no Studio.",
     f"2. **Banco de {sum(qcount.values())} questões reais** deduplicadas, com gabarito, por matéria e assunto em `questoes/` (índice em `questoes/INDICE.md`).",
     "3. **Vault do Obsidian**: apostilas de 14 matérias por aula, notas de método, plano e registro de erros. Índice em `vault/INDICE-VAULT.md`, notas curadas copiadas em `vault/notas/`.", "",
     "Materiais prontos (guias, quizzes, flashcards, notas, mapas mentais) estão em `materiais/`.", "",
     "## Como usar", "",
     "1. Ache a matéria abaixo. Abra o arquivo do notebook para conceitos e o arquivo de questões para ver como a banca cobra.",
     "2. Para teoria por aula, siga `vault/INDICE-VAULT.md`.",
     "3. Para detalhe além dos arquivos, pergunte ao notebook ao vivo: `notebooklm ask \"pergunta\" -n <ID>` (nunca use `--new`: apaga o histórico do chat).",
     "4. Prova do Agente PC-PR (Edital 01/2026, 100 questões, peso 1): Português e Tecnologia valem 25 cada; os cinco ramos de Direito somados valem 15.", "",
     "## Matérias", ""]
for name, peso, ids in G:
    L.append(f"### {name}" + (f" — {peso}" if peso else ""))
    qm = QMAP.get(name)
    if qm and qm in qcount:
        L.append(f"- Questões reais: **{qcount[qm]}** em [questoes/{slugq(qm)}.md](questoes/{slugq(qm)}.md)")
    if qm:
        L.append(f"- Apostilas e notas do vault: ver seção \"{qm}\" em [vault/INDICE-VAULT.md](vault/INDICE-VAULT.md)")
    if not ids and name == "Direitos Humanos":
        L.append("- Sem notebook no NotebookLM. Cobertura vem das apostilas do vault e do banco de questões.")
    for i in ids:
        r = rows[i]
        gp=os.path.join(OUT,'guias',r['slug']+'.md'); g=f" · [guia completo](guias/{r['slug']}.md)" if os.path.exists(gp) and os.path.getsize(gp)>2000 else ''
        L.append(f"- **[{title(i)}](notebooks/{r['slug']}.md)**{g} — {r['n']} fontes, {n_mats(i)} materiais. ID `{i}`")
        s = summ(i)
        if s: L.append(f"  - {s}")
    L.append("")
if "Legislação Penal Extravagante" in qcount:
    L += ["### Legislação Penal Extravagante (dentro de Direito Penal no edital)",
          f"- Questões reais: **{qcount['Legislação Penal Extravagante']}** em [questoes/legislacao-penal-extravagante.md](questoes/legislacao-penal-extravagante.md)",
          "- Apostilas no vault: ver `vault/INDICE-VAULT.md`.", ""]
L += ["## Materiais baixados (materiais/)", ""]
for m in sorted(os.listdir(os.path.join(OUT, 'materiais'))):
    L.append(f"- [{m}](materiais/{m})")
open(os.path.join(OUT, 'MAPA-GERAL.md'), 'w', encoding='utf-8').write('\n'.join(L))
print('ok', len(L))
