from collections import Counter
from pprint import pprint

with open('pt_BR.dic', encoding='cp1252') as dic_file:
    lines = dic_file.read().strip().split('\n')

print('total lines:', len(lines))
print('length hint:', lines[0])

initials_ct = Counter([s[0].upper() for s in lines[1:]])

print(initials_ct)
pprint(initials_ct.most_common())
