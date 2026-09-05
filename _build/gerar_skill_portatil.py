"""Gera ferramenta/SKILL.md (versao distribuivel) a partir da skill instalada localmente,
trocando o caminho fixo da maquina do autor por um marcador que a pessoa substitui."""
import os, shutil

BS = chr(92)
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
LOCAL = os.path.join(os.path.expanduser('~'), '.claude', 'skills', 'professor', 'SKILL.md')
DEST = os.path.join(ROOT, 'ferramenta', 'SKILL.md')
MARK = '<PASTA-DO-REPOSITORIO>'

s = open(LOCAL, encoding='utf-8').read()
s = s.replace('C:' + BS + 'Users' + BS + 'USER' + BS + 'Professor' + BS, MARK + '/')
s = s.replace('C:' + BS + 'Users' + BS + 'USER' + BS + 'Professor', MARK)
s = s.replace('python ' + MARK + '/_build/', 'python _build/')

exemplo = ('Ela mora na pasta onde voce clonou este repositorio, chamada aqui de `' + MARK + '`. '
           'Troque esse marcador pelo caminho real, por exemplo `C:' + BS + 'Users' + BS + 'seu-usuario' + BS +
           'professor` no Windows ou `~/professor` no Mac e Linux.')
s = s.replace('Ela mora em `' + MARK + '/`.', exemplo)
s = s.replace('Ela mora em `' + MARK + '`.', exemplo)

open(DEST, 'w', encoding='utf-8').write(s)
print('SKILL portatil gerada com', s.count(MARK), 'marcadores')
assert 'Users' + BS + 'USER' not in s, 'ainda ha caminho pessoal na skill distribuida'

# agente tambem
LOCAL_AG = os.path.join(os.path.expanduser('~'), '.claude', 'agents', 'professor.md')
if os.path.exists(LOCAL_AG):
    a = open(LOCAL_AG, encoding='utf-8').read()
    a = a.replace('C:' + BS + 'Users' + BS + 'USER' + BS + 'Professor', MARK)
    a = a.replace('C:' + BS + 'Users' + BS + 'USER' + BS + '.claude', '~/.claude')
    open(os.path.join(ROOT, 'ferramenta', 'agent-professor.md'), 'w', encoding='utf-8').write(a)
    print('agente portatil gerado')

# normaliza barras invertidas que sobraram depois do marcador e ajusta o que nao vai no repo
import re
s2 = open(DEST, encoding='utf-8').read()
s2 = re.sub(re.escape(MARK) + r'/[^`]*', lambda m: m.group(0).replace(chr(92), '/'), s2)
s2 = s2.replace('Cópia local completa em `' + MARK + '/vault/apostilas/<Matéria>/` (mesmos nomes de arquivo do vault; use esta, não depende do OneDrive).',
                'Se você tiver as apostilas em markdown, aponte o caminho delas aqui; elas não vêm no repositorio.')
open(DEST, 'w', encoding='utf-8').write(s2)
print('barras normalizadas')
