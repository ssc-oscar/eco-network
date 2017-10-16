from collections import defaultdict
import sys
sys.path.append('/da4_data/play/python-semanticversion.github')
from semantic_version import *

prodistance_pro = defaultdict(set)
allpros = set()  # with version attached in the end

file1 = '/da4_data/play/libraries.io.depens/R_CRAN_downstream_recurs_withV'
file2 = '/da4_data/play/libraries.io.depens/R_CRAN_downstream_recurs_noV'
file4 = '/da4_data/play/libraries.io.depens/R_CRAN_downstream_direct_noV'

file3 = '/da4_data/play/libraries.io.depens/R_CRAN_upstream_recurs_withV'

# reverse downstream has to be generated from file3
# first I need to melt each record and turn it into a tuple

f3 = open(file3, 'r')


for line in f3:
    layers = line.strip().split(';')
    thepro = layers[0]
    allpros.add(thepro)
    for i in range(1, len(layers)):
        for pro in layers[i].split(','):
            prodistance_pro[pro + ';' + str(i)].add(thepro)
            allpros.add(pro)
f3.close()


f1 = open(file1, 'w')
f2 = open(file2, 'w')
f2_ouptput_set = set()

f4 = open(file4, 'w')

for anypro in allpros:
    f2_ouptput_set.clear()
    if anypro + ';' + str(1) not in prodistance_pro:
        continue
    f1.write(anypro)
    f2.write(anypro)
    f4.write(anypro + ';' + ','.join(set(map(lambda x: x.split('|')
                                             [0], prodistance_pro[anypro + ';' + str(1)]))) + '\n')
    start = 1
    while anypro + ';' + str(start) in prodistance_pro:
        f1.write(';' + ','.join(prodistance_pro[anypro + ';' + str(start)]))
        f2_ouptput_set.update(
            set(map(lambda x: x.split('|')[0], prodistance_pro[anypro + ';' + str(start)])))
        start += 1
    f1.write('\n')
    f2.write(';' + ','.join(f2_ouptput_set) + '\n')

f1.close()
f2.close()
f4.close()
