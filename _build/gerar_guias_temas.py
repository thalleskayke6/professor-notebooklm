"""Dispara um relatório custom por TEMA (### do índice hierárquico) em cada notebook de matéria.
Grava guias/tasks_temas.json: {notebook_id: {slug, temas: [{n, tema, task_id}]}}. Idempotente: pula temas já baixados em guias/<slug>/NN-*.md."""
import json, subprocess, io, sys, os, re, unicodedata
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE); os.chdir(HERE)
MAX_TEMAS = int(sys.argv[1]) if len(sys.argv) > 1 else 18
SKIP = {'84eec3f0-185a-475a-bbdb-171dac0733e1', '02ef5b8b-6409-48c5-8066-36b557273692', '8677f4e5-7a16-4a97-a42c-0cb1db02883a',
        '3b393eaf-1dc1-498c-bd6f-e45d24abb17d', '130465ab-f48f-42c5-9b49-4c015e948c4e', '17b41580-33c9-4eb0-9e58-ed2ad79e84ac',
        '831dba20-e87e-4e71-a1d9-e03a9f05deb3', 'b342beb3-7cc4-497e-b473-5e77c5195673'}  # método/IA/edital: um guia só basta
def slug(s):
    s = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode().lower()
    return re.sub(r'[^a-z0-9]+', '-', s).strip('-')[:50]
def temas_de(slugnb):
    t = open(os.path.join(ROOT, 'notebooks', slugnb + '.md'), encoding='utf-8').read()
    m = re.search(r'## Índice hierárquico\n(.*?)\n## ', t, re.S)
    if not m: return []
    hs = [re.sub(r'^[\dIVX]+[.)]?\s*', '', h.strip()).strip('* ') for h in re.findall(r'^###\s+(.+)$', m.group(1), re.M)]
    out = []
    for h in hs:
        if h and h not in out: out.append(h)
    return out[:MAX_TEMAS]
rows = json.load(open('nb_index.json', encoding='utf-8'))
tp = os.path.join('guias', 'tasks_temas.json')
tasks = json.load(open(tp, encoding='utf-8')) if os.path.exists(tp) else {}
PROMPT = ("Escreva um GUIA DE ESTUDO COMPLETO em markdown, em português, SOMENTE sobre o tema \"{tema}\", usando tudo o que as fontes deste notebook "
          "trazem sobre ele. Cubra todos os subtemas: definições exatas, regras, classificações, prazos, números, fórmulas, exceções, exemplos, "
          "jurisprudência citada e as pegadinhas típicas da banca FGV (o que se confunde com o quê). Use ### por subtema, listas curtas e tabelas "
          "para comparações. Termine com um bloco 'Pegadinhas' e um bloco 'Perguntas que a banca faz'. Seja o mais longo e exaustivo possível; "
          "prefira completude a concisão. Não cite números de fonte.")
n_launch = 0
for r in rows:
    if r['id'] in SKIP: continue
    temas = temas_de(r['slug'])
    d = os.path.join(ROOT, 'guias', r['slug']); os.makedirs(d, exist_ok=True)
    ent = tasks.setdefault(r['id'], {'slug': r['slug'], 'temas': []})
    done_n = {x['n'] for x in ent['temas'] if x.get('task_id')}
    for n, tema in enumerate(temas, 1):
        if n in done_n: continue
        if any(f.startswith(f'{n:02d}-') for f in os.listdir(d)): continue
        pf = os.path.join('guias', f'_p_{r["slug"]}_{n:02d}.txt')
        open(pf, 'w', encoding='utf-8').write(PROMPT.format(tema=tema))
        p = subprocess.run(['notebooklm', 'generate', 'report', '--prompt-file', pf, '--format', 'custom', '--language', 'pt_BR',
                            '-n', r['id'], '--retry', '2', '--json'], capture_output=True, text=True, encoding='utf-8')
        try:
            dd = json.loads(p.stdout); tid = dd.get('task_id')
        except Exception:
            tid = None
        ent['temas'].append({'n': n, 'tema': tema, 'task_id': tid, 'err': None if tid else (p.stdout + p.stderr)[-150:]})
        n_launch += 1 if tid else 0
        print('OK ' if tid else 'ERR', r['slug'][:30], n, tema[:60])
        tmp = tp + '.tmp'
        json.dump(tasks, open(tmp, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        os.replace(tmp, tp)  # gravação atômica: dois lançadores simultâneos corromperiam o arquivo
print('lançados', n_launch)
