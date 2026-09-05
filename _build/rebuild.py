"""Reconstrói a base do Professor a partir do NotebookLM.
Uso: python rebuild.py            -> reextrai só o que falta (idempotente)
     python rebuild.py --force ID -> reextrai um notebook inteiro
Requer: notebooklm CLI autenticado (notebooklm auth check --test).
Cache de extração fica em _build/cache/. NUNCA usa `ask --new` (apagaria o histórico do chat).
"""
import json,subprocess,os,sys,re,io,shutil
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
HERE=os.path.dirname(os.path.abspath(__file__)); os.chdir(HERE)
CACHE=os.path.join(HERE,'cache'); os.makedirs(CACHE,exist_ok=True)
for d in ['ask2','valter','src','summary','notes','arts','dl']: os.makedirs(os.path.join(CACHE,d),exist_ok=True)
os.chdir(CACHE)
for f in ['nb_index.json','ids.txt']+[x for x in os.listdir(HERE) if x.endswith('.txt') or x.endswith('.py')]:
    shutil.copy(os.path.join(HERE,f),f)
force=sys.argv[2] if len(sys.argv)>2 and sys.argv[1]=='--force' else None
def run(args): return subprocess.run(['notebooklm']+args,capture_output=True,text=True,encoding='utf-8')
# 1. notebooks list -> refresh index (novos notebooks entram com slug automático)
r=run(['list','--json']); nbs=json.load(open('nb_index.json',encoding='utf-8')); known={n['id'] for n in nbs}
def slug(s):
    s=s.lower()
    for a,b in zip('áàãâéêíóôõúçñ','aaaaeeiooouc n'): s=s.replace(a,b)
    return re.sub(r'[^a-z0-9]+','-',s).strip('-')[:45]
for n in json.loads(r.stdout)['notebooks']:
    if n['id'] not in known: nbs.append({'id':n['id'],'title':n['title'],'slug':slug(n['title']),'n':0}); print('novo notebook',n['title'])
json.dump(nbs,open('nb_index.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
open('ids.txt','w',encoding='utf-8').write(''.join(f"{n['id']} | {n['title']}\n" for n in nbs))
def ok(p): return os.path.exists(p) and os.path.getsize(p)>300
for n in nbs:
    i=n['id']
    if force==i:
        for p in ['indice','conceitos','pegadinhas']:
            try: os.remove(f'ask2/{i}_{p}.json')
            except: pass
    if not ok(f'src/{i}.json') or force==i:
        open(f'src/{i}.json','w',encoding='utf-8').write(run(['source','list','-n',i,'--json']).stdout)
        n['n']=len(json.load(open(f'src/{i}.json',encoding='utf-8')).get('sources',[]))
    if not ok(f'summary/{i}.json'): open(f'summary/{i}.json','w',encoding='utf-8').write(run(['summary','-n',i,'--json']).stdout)
    if not ok(f'notes/{i}.json'): open(f'notes/{i}.json','w',encoding='utf-8').write(run(['note','list','-n',i,'--json']).stdout)
    if not ok(f'arts/{i}.json'): open(f'arts/{i}.json','w',encoding='utf-8').write(run(['artifact','list','-n',i,'--json']).stdout)
    if i.startswith('84eec3f0'): continue  # Valter: extração manual em 5 partes (valter/)
    for p in ['indice','conceitos','pegadinhas']:
        out=f'ask2/{i}_{p}.json'
        if ok(out): continue
        for pf in [f'p_{p}.txt',f'pc_{p}.txt']:
            print('ask',n['title'][:40],p,pf)
            r=run(['ask','--prompt-file',pf,'-n',i,'--json'])
            open(out,'w',encoding='utf-8').write(r.stdout)
            if ok(out) and '"error"' not in r.stdout[:40]: break
json.dump(nbs,open('nb_index.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
subprocess.run([sys.executable,'dl.py']); subprocess.run([sys.executable,'build.py']); subprocess.run([sys.executable,'build_mapa.py'])
print('REBUILD OK')
