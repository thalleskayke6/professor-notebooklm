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
TPL = open(os.path.join(ROOT, '_build', 'readme_template.md'), encoding='utf-8').read()
README = TPL.replace('{n_mats}', str(len(mats))).replace('{tabela}', NL.join(tbl)).replace('{materiais}', NL.join(f'- [{m}](materiais/{m})' for m in mats))
open('README.md', 'w', encoding='utf-8').write(README)
print('README', len(README))
