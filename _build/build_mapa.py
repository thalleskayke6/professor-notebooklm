import json,os,io,sys,glob
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
OUT=r"C:\Users\USER\Professor"
rows={r['id']:r for r in json.load(open('nb_index.json',encoding='utf-8'))}
def summ(i):
    try: return json.load(open(f'summary/{i}.json',encoding='utf-8')).get('summary','').replace('**','')
    except: return ''
G=[
 ("Edital e regras do concurso",None,["b342beb3-7cc4-497e-b473-5e77c5195673"]),
 ("Língua Portuguesa","25 questões",["5beaebcc-a76f-426c-9551-c4bd3e527600","e5690053-99e5-4d7e-87e8-98e697a3d047","ae986a01-c8f9-46fe-9da4-b8e614a86d10"]),
 ("Tecnologia, Segurança Cibernética e Crimes Digitais","25 questões",["546f0cb3-6aab-4b5b-97ac-7e8c7adec19c"]),
 ("Ciências Forenses","10 questões",["367433a3-ad6a-4cf4-9ff1-8221a4c6abb3","8498c1e7-ece3-49b4-9b95-65c9785541b7"]),
 ("Raciocínio Lógico-Matemático","5 questões",["5714ea7c-de27-44b2-aab4-aeb30121b411"]),
 ("Realidade do Paraná","5 questões",["42b917ff-915d-4b69-9b5e-e4bda9a4a232"]),
 ("Contabilidade Geral","5 questões",["73efc3d0-2a26-482e-a98a-f65ee6f3b538"]),
 ("Estatística","5 questões",["185c9e3e-c37f-4324-9856-9dd96ac71661"]),
 ("Legislação Estadual e Institucional","5 questões",["bee037d5-0f9b-4125-ac6e-691b183e57fa"]),
 ("Direito Penal","3 questões",["66410a65-3c39-4c6e-b49f-9b2ddcafa4a7"]),
 ("Direito Processual Penal","3 questões",["ff239db3-703f-43fd-8240-2fbb1843f9fb"]),
 ("Direito Constitucional","3 questões",["b63c5fdb-187a-4616-a267-e9ac15a926f6"]),
 ("Direito Administrativo","3 questões",["01d11b38-610b-49dd-b95d-1c04513c2b75"]),
 ("Direitos Humanos","3 questões",[]),
 ("Método de estudo, memória e mentalidade",None,["84eec3f0-185a-475a-bbdb-171dac0733e1","02ef5b8b-6409-48c5-8066-36b557273692","8677f4e5-7a16-4a97-a42c-0cb1db02883a","3b393eaf-1dc1-498c-bd6f-e45d24abb17d","130465ab-f48f-42c5-9b49-4c015e948c4e","17b41580-33c9-4eb0-9e58-ed2ad79e84ac"]),
 ("IA, chatbots e engenharia de prompts",None,["831dba20-e87e-4e71-a1d9-e03a9f05deb3"]),
]
L=["# MAPA GERAL — Professor NotebookLM","",
"Base de conhecimento extraída de **23 notebooks** do NotebookLM (819 fontes) em 05/09/2026.",
"Cada notebook tem um arquivo em `notebooks/` com índice hierárquico, conceitos-chave, pegadinhas, materiais baixados e lista de fontes.",
"Materiais prontos (guias de estudo, quizzes, flashcards, notas, mapas mentais) estão em `materiais/`.","",
"## Como usar","",
"1. Ache a matéria abaixo e abra o arquivo do notebook.",
"2. Para detalhe além do arquivo, pergunte ao notebook ao vivo: `notebooklm ask \"pergunta\" -n <ID>` (nunca use `--new`: apaga o histórico do chat).",
"3. Prova do Agente PC-PR (Edital 01/2026, 100 questões, peso 1): Português e Tecnologia valem 25 cada; os cinco ramos de Direito somados valem 15.","",
"## Notebooks por área",""]
seen=set()
for name,peso,ids in G:
    L.append(f"### {name}" + (f" — {peso}" if peso else ""))
    if not ids: L.append("- *(nenhum notebook cobre esta matéria — lacuna)*")
    for i in ids:
        r=rows[i]; seen.add(i)
        n_mat=len(glob.glob(f'dl/{i[:8]}_*'))
        L.append(f"- **[{r['title']}](notebooks/{r['slug']}.md)** — {r['n']} fontes, {n_mat} materiais. ID `{i}`")
        s=summ(i)
        if s: L.append(f"  - {s}")
    L.append("")
rest=[i for i in rows if i not in seen]
if rest:
    L.append("### Outros")
    for i in rest: L.append(f"- [{rows[i]['title']}](notebooks/{rows[i]['slug']}.md) `{i}`")
L+=["","## Materiais baixados (materiais/)",""]
for m in sorted(os.listdir(os.path.join(OUT,'materiais'))):
    L.append(f"- [{m}](materiais/{m})")
open(os.path.join(OUT,'MAPA-GERAL.md'),'w',encoding='utf-8').write('\n'.join(L))
print('ok',len(L))
