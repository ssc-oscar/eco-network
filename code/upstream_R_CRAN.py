from collections import defaultdict
import sys
sys.path.append('/da4_data/play/python-semanticversion.github')
from semantic_version import *

file1 = '/da4_data/play/libraries.io.depens/R_CRAN_direct_upstream_withV'
file2 = '/da4_data/play/libraries.io.depens/R_CRAN_direct_upstream_noV'
file3 = '/da4_data/play/libraries.io.depens/R_CRAN_upstream_recurs_withV'
file4 = '/da4_data/play/libraries.io.depens/R_CRAN_upstream_recurs_noV'

# no worry about grep CRAN, verified $1 == CRAN && $7 != CRAN doesn't exist
# stdin input = cat
# da4:/data/play/libraries.io.data/dependencies-1.0.0-2017-06-15.csv |
# grep CRAN |

proj2versions = defaultdict(set)
prover2dirupstream = defaultdict(set)

stack1 = []
stack2 = set()
prover_set_stack = set()


for line in sys.stdin:
    items = line.strip().split(',')
    if len(items) != 12:
        sys.stderr(line + '## line above num of items error\n')
        continue
    '''
    if items[1] != 'CRAN' or items[7] != 'CRAN':
        print(line.strip())
        sys.exit()
    '''
    # This is for query
    proj2versions[items[2]].add(items[4])
    #
    prover2dirupstream[items[2] + '|' + items[4]
                       ].add(items[6] + '|' + items[10])

f1 = open(file1, 'w')
f2 = open(file2, 'w')
for key, values in prover2dirupstream.items():
    f1.write(key + ';')
    f2.write(key + ';')
    f2.write(','.join(set(map(lambda x: x.split('|')[0], values))) + '\n')
    f1.write(','.join(values) + '\n')

f1.close()
f2.close()


f3 = open(file3, 'w')
f4 = open(file4, 'w')

f4_ouptput_set = set()
output_stack = []


for prover in prover2dirupstream:
    f4_ouptput_set.clear()
    prover_set_stack.clear()
    f3.write(prover)
    f4.write(prover)

    stack2 = prover2dirupstream[prover]
    while len(stack2) != 0:
        stack1 = list(stack2)
        stack2.clear()
        for pro_requirement in stack1:
            potential_pro, spec = pro_requirement.split('|')
            for avail_ver in proj2versions[potential_pro]:
                if potential_pro + '|' + avail_ver in prover_set_stack:
                    continue
                prover_set_stack.add(potential_pro + '|' + avail_ver)
                try:
                    if Version(avail_ver, partial=True) in Spec(spec):
                        output_stack.append(potential_pro + '|' + avail_ver)
                        f4_ouptput_set.add(potential_pro)
                except ValueError as e:
                    sys.stderr.write('version: ' + avail_ver +
                                     '  Requirement: ' + spec + '\n')
                    sys.stderr.write(e.message + '\n')
        if len(output_stack) != 0:
            f3.write(';' + ','.join(output_stack))
            for i in output_stack:
                if i not in prover2dirupstream:
                    continue
                stack2.update(prover2dirupstream[i])
            output_stack[:] = []
    f3.write('\n')
    f4.write(';' + ','.join(f4_ouptput_set) + '\n')
f3.close()
f4.close()
