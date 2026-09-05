"""Baixa os relatórios por tema (guias/tasks_temas.json) para guias/<slug>/NN-<tema>.md. Idempotente. Espera até max_min minutos."""
import json, subprocess, io, sys, os, time, re, unicodedata
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
tp = os.path.join(HERE, 'guias', 'tasks_temas.json')
max_min = float(sys.argv[1]) if len(sys.argv) > 1 else 9
def slug(s):
    s = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode().lower()
    return re.sub(r'[^a-z0-9]+', '-', s).strip('-')[:50]
t0 = time.time()
while True:
    tasks = json.load(open(tp, encoding='utf-8'))
    pend, ok = 0, 0
    for nb, ent in tasks.items():
        d = os.path.join(ROOT, 'guias', ent['slug']); os.makedirs(d, exist_ok=True)
        for x in ent['temas']:
            if not x.get('task_id'): continue
            out = os.path.join(d, f"{x['n']:02d}-{slug(x['tema'])}.md")
            if os.path.exists(out) and os.path.getsize(out) > 1500: ok += 1; continue
            subprocess.run(['notebooklm', 'download', 'report', out, '-a', x['task_id'], '-n', nb], capture_output=True, text=True, encoding='utf-8')
            if os.path.exists(out) and os.path.getsize(out) > 1500:
                ok += 1; print('OK', ent['slug'][:28], x['n'], os.path.getsize(out) // 1024, 'KB')
            else:
                if os.path.exists(out): os.remove(out)
                pend += 1
    print(f'baixados {ok}, pendentes {pend}')
    if pend == 0: print('TODOS BAIXADOS'); break
    if time.time() - t0 > max_min * 60: print('PENDENTES', pend); break
    time.sleep(60)
