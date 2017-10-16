import sys
import re
from subprocess import call, check_output
import json

# iteration

'''
def iterate_call(package):
    A_set = set()
    A_list = []
    A_list.append(package)
    # A_set.add()
    while len(A_list) != 0:
        package = A_list.pop(0)
        if package not in A_set:
            A_set.add(package)
            result = check_output('deppkgs ' + package, shell=True)
            if len(result) == 0:
                continue
            # print(result[0:-1])
            A_list.extend(result.split('\n'))
    for i in A_set:
        print(i)
'''

# recursively_call(sys.argv[1])
# iterate_call(sys.argv[1])

# direct downstreams
for line in sys.stdin:
    result = check_output('npm view --json ' + line.strip(), shell=True)
    ll = json.loads(result)
    if 'dependencies' in ll:
        print(line.strip() + ';' + ','.join(ll['dependencies'].keys()))
    else:
        print(line.strip() + ';')
