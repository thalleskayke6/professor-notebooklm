import json,subprocess,io,sys,re,os
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
ids=[l.split('|')[0].strip() for l in open('ids.txt',encoding='utf-8')]
def slug(s): return re.sub(r'[^a-z0-9]+','-',s.lower())[:50].strip('-')
def ok(p): return os.path.exists(p) and os.path.getsize(p)>50
for i in ids:
    try: notes=json.load(open(f'notes/{i}.json',encoding='utf-8')).get('notes',[])
    except: notes=[]
    for n in notes:
        out=f"dl/{i[:8]}_note_{slug(n.get('title',''))}.md"
        if ok(out): continue
        r=subprocess.run(['notebooklm','note','get',n['id'],'-n',i,'--json'],capture_output=True,text=True,encoding='utf-8')
        try:
            d=json.loads(r.stdout); c=d.get('note',d).get('content') or d.get('content') or r.stdout
        except: c=r.stdout
        open(out,'w',encoding='utf-8').write(c or ''); print('note',out,len(c or ''))
    try: arts=json.load(open(f'arts/{i}.json',encoding='utf-8')).get('artifacts',[])
    except: arts=[]
    for a in arts:
        t=a.get('type'); aid=a['id']; s=slug(a.get('title',''))
        if t=='Report': out=f"dl/{i[:8]}_report_{s}.md"; cmd=['notebooklm','download','report',out,'-a',aid,'-n',i]
        elif t=='Quiz': out=f"dl/{i[:8]}_quiz_{s}_{aid[:6]}.md"; cmd=['notebooklm','download','quiz','--format','markdown',out,'-a',aid,'-n',i]
        elif t=='Flashcards': out=f"dl/{i[:8]}_flash_{s}.md"; cmd=['notebooklm','download','flashcards','--format','markdown',out,'-a',aid,'-n',i]
        elif t=='Mind Map': out=f"dl/{i[:8]}_mindmap_{s}.json"; cmd=['notebooklm','download','mind-map',out,'-a',aid,'-n',i]
        elif t=='Data Table': out=f"dl/{i[:8]}_table_{s}.csv"; cmd=['notebooklm','download','data-table',out,'-a',aid,'-n',i]
        else: continue
        if ok(out): continue
        r=subprocess.run(cmd,capture_output=True,text=True,encoding='utf-8')
        print(t,out,'rc',r.returncode,(r.stderr or '')[-100:].replace('\n',' '))
print('DL DONE')
