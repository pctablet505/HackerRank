import os
import json

sep = os.sep

f = open('pctablet505_data.json')
data = json.load(f)
f.close()

c = 0
i = 0
failures = []
languages = set()

banned = ['\\', '/', '!', '*', '"', '<', '>', '?', ':']

for ind, sub in enumerate(data['submissions']):
    if sub['score'] > 2:
        contest = sub['contest']
        fname = sub['challenge']
        lang = sub['language']
        languages.add(lang)
        for x in banned:
            fname = fname.replace(x, '')

        if lang in ('python', 'python3'):
            ext = '.py'

        elif lang == 'pypy3':
            ext = '.pypy'

        elif lang == 'c':
            ext = '.c'

        elif lang == "cpp" or lang == 'cpp14':
            ext = '.cpp'

        elif lang == "java" or lang == 'java8':
            ext = '.java'

        elif lang == 'javascript':
            ext = '.js'

        else:
            ext = '.' + sub['language']

        path = 'hackerrank' + sep

        try:
            if lang in ['db2', 'mysql', 'oracle']:
                path += 'SQL' + sep

            elif lang == 'javascript':
                path += 'JavaScript' + sep
            else:
                path += contest + sep

            if not os.path.exists(path):
                os.makedirs(path)
            if 'code' not in sub:
                failures.append((fname, ind))
                continue

            if os.path.exists(path + fname + ext):
                continue

            with open(path + fname + ext, 'w') as f:
                f.write(sub['code'])

        except:
            print(fname, ind)
            failures.append((fname, ind))
        c += 1
    i += 1

print(i, c)
