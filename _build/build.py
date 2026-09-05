import json,os,re,io,sys,shutil,glob
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
OUT=r"C:\Users\USER\Professor"
NB=os.path.join(OUT,"notebooks"); MAT=os.path.join(OUT,"materiais")
os.makedirs(NB,exist_ok=True); os.makedirs(MAT,exist_ok=True)
rows=json.load(open('nb_index.json',encoding='utf-8'))
def ans(path):
    try:
        txt=open(path,encoding='utf-8').read()
        d=json.JSONDecoder().raw_decode(txt[txt.find('{'):])[0]
        if d.get('error'): return None
        a=d.get('answer','')
        # strip citation markers like [1], [2-4], [1, 3]
        a=re.sub(r'\s?\[\d+(?:[-–,]\s?\d+)*\]','',a)
        return a.strip()
    except Exception: return None
def summ(i):
    try: return json.load(open(f'summary/{i}.json',encoding='utf-8')).get('summary','')
    except: return ''
missing=[]
index_lines=[]
for r in rows:
    i=r['id']; slug=r['slug']; title=r['title']
    srcs=json.load(open(f'src/{i}.json',encoding='utf-8'))['sources']
    parts=[]
    parts.append(f"# {title}\n")
    parts.append(f"- **Notebook ID:** `{i}`\n- **Fontes:** {len(srcs)}\n- **Consultar ao vivo:** `notebooklm ask \"pergunta\" -n {i}`\n")
    s=summ(i)
    if s: parts.append(f"\n## Resumo do NotebookLM\n\n{s}\n")
    if i.startswith('84eec3f0'):
        secs=[('1_indice','Índice hierárquico'),('2_metodo','Metodologia de estudo'),('3_mente','Mentalidade e vida de concurseiro'),('4_anki_ia','Anki, IA e prompts'),('5_plano','Plano de Elite e relações')]
        for f,h in secs:
            a=ans(f'valter/{f}.json')
            if a: parts.append(f"\n## {h}\n\n{a}\n")
            else: missing.append((title,h))
    else:
        for p,h in [('indice','Índice hierárquico'),('conceitos','Conceitos-chave por tema'),('pegadinhas','Pegadinhas, relações e lacunas')]:
            a=ans(f'ask2/{i}_{p}.json')
            if a: parts.append(f"\n## {h}\n\n{a}\n")
            else: missing.append((title,h))
    gd=os.path.join(OUT,'guias',slug)
    if os.path.isdir(gd):
        tf=sorted(f for f in os.listdir(gd) if f.endswith('.md'))
        if tf:
            parts.append(f"
### Guias por tema ({len(tf)})
")
            for f in tf: parts.append(f"- [{f[3:-3].replace('-',' ')}](../guias/{slug}/{f})")
            parts.append('')
    # materials
    mats=sorted(glob.glob(f'dl/{i[:8]}_*'))
    if mats:
        parts.append("\n## Materiais baixados deste notebook\n")
        for m in mats:
            bn=os.path.basename(m); dst=os.path.join(MAT,bn); shutil.copy(m,dst)
            parts.append(f"- [{bn}](../materiais/{bn})")
        parts.append("")
    parts.append("\n## Fontes\n")
    for s_ in srcs:
        parts.append(f"- {s_.get('title','')} `({s_.get('type','')})`")
    open(os.path.join(NB,slug+'.md'),'w',encoding='utf-8').write('\n'.join(parts))
    index_lines.append((r,len(mats)))
print('missing',len(missing))
for m in missing: print('  ',m)
json.dump([f"{a}|{b}" for a,b in missing],open('missing.json','w',encoding='utf-8'),ensure_ascii=False)
