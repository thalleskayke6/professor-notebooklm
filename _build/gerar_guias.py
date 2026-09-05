"""Dispara, em cada notebook, a geração do guia completo como relatório custom no Studio (prompt em p_guia.txt).
Grava os task_ids em guias/tasks.json. Pula notebooks que já têm guias/<slug>.md."""
import json, subprocess, io, sys, os
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE); os.chdir(HERE)
os.makedirs('guias', exist_ok=True)
rows = json.load(open('nb_index.json', encoding='utf-8'))
tp = os.path.join('guias', 'tasks.json')
tasks = json.load(open(tp, encoding='utf-8')) if os.path.exists(tp) else {}
for r in rows:
    if os.path.exists(os.path.join(ROOT, 'guias', r['slug'] + '.md')): continue
    p = subprocess.run(['notebooklm', 'generate', 'report', '--prompt-file', 'p_guia.txt', '--format', 'custom', '--language', 'pt_BR',
                        '-n', r['id'], '--retry', '2', '--json'], capture_output=True, text=True, encoding='utf-8')
    try:
        d = json.loads(p.stdout); tasks[r['id']] = {'task_id': d.get('task_id'), 'status': d.get('status'), 'slug': r['slug']}; print('OK ', r['slug'])
    except Exception:
        tasks[r['id']] = {'task_id': None, 'error': (p.stdout + p.stderr)[-200:], 'slug': r['slug']}; print('ERR', r['slug'])
json.dump(tasks, open(tp, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
