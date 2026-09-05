"""Baixa os guias completos gerados como relatório (report custom) em cada notebook.
Idempotente: pula o que já está em Professor/guias/<slug>.md. Roda até 'max_min' minutos esperando os pendentes."""
import json, subprocess, io, sys, os, time
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
OUT = os.path.join(ROOT, 'guias'); os.makedirs(OUT, exist_ok=True)
tasks = json.load(open(os.path.join(HERE, 'guias', 'tasks.json'), encoding='utf-8'))
max_min = float(sys.argv[1]) if len(sys.argv) > 1 else 9
t0 = time.time()
while True:
    pend = []
    for nb, t in tasks.items():
        if not t.get('task_id'): continue
        out = os.path.join(OUT, t['slug'] + '.md')
        if os.path.exists(out) and os.path.getsize(out) > 2000: continue
        r = subprocess.run(['notebooklm', 'download', 'report', out, '-a', t['task_id'], '-n', nb], capture_output=True, text=True, encoding='utf-8')
        if os.path.exists(out) and os.path.getsize(out) > 2000:
            print('OK', t['slug'], os.path.getsize(out) // 1024, 'KB')
        else:
            if os.path.exists(out): os.remove(out)
            pend.append(t['slug'])
    if not pend:
        print('TODOS BAIXADOS'); break
    if time.time() - t0 > max_min * 60:
        print('PENDENTES', len(pend), pend); break
    time.sleep(45)
