"""Remove nomes de autores, cursos e plataformas dos arquivos publicados (notebooks/, MAPA-GERAL.md,
materiais/, índices). Roda depois de build.py / build_mapa.py / build_vault.py / build_questoes.py.
Não mexe em URLs (links para a fonte continuam funcionando)."""
import os, re, io, sys, glob
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SUBS = [
    (r'Método Valter Rodrigues', 'Método do autor das videoaulas'),
    (r'Valter Rodrigues', 'o autor das videoaulas de método'),
    (r'\bValter\b', 'o autor das videoaulas'),
    (r'Felippe Loureiro', 'o autor das videoaulas de exatas'),
    (r'\bFelippe\b|\bLoureiro\b', 'o autor das videoaulas'),
    (r'Estrat[ée]gia Concursos', 'curso preparatório'),
    (r'Cerrado Concursos', 'curso preparatório'),
    (r'\bTec ?Concursos\b(?![^\[]*\]\()', 'plataforma de questões'),
    (r'\bQConcursos\b', 'plataforma de questões'),
]
files = glob.glob(os.path.join(ROOT, 'notebooks', '*.md')) + glob.glob(os.path.join(ROOT, 'guias', '*.md')) + [os.path.join(ROOT, 'MAPA-GERAL.md'),
        os.path.join(ROOT, 'vault', 'INDICE-VAULT.md'), os.path.join(ROOT, 'questoes', 'INDICE.md')] + glob.glob(os.path.join(ROOT, 'materiais', '*'))
n = 0
for f in files:
    if not os.path.exists(f): continue
    t = open(f, encoding='utf-8').read(); o = t
    # protege URLs
    urls = re.findall(r'https?://\S+', t)
    for i, u in enumerate(urls): t = t.replace(u, f'@@URL{i}@@')
    for rx, rep in SUBS: t = re.sub(rx, rep, t, flags=re.I)
    for i, u in enumerate(urls): t = t.replace(f'@@URL{i}@@', u)
    if t != o:
        open(f, 'w', encoding='utf-8').write(t); n += 1
print('arquivos alterados', n)
