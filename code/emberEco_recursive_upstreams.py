import sys
import re
from subprocess import call, check_output
import json
# iteration


def iterate_call(package_or):
    A_set = set()
    A_list = []
    A_list.append(package_or)
    # A_set.add()
    while len(A_list) != 0:
        package = A_list.pop(0)
        if package not in A_set:
            A_set.add(package)
            try:
                result = check_output(
                    'npm view --json ' + package.strip(), shell=True)
            except Exception:
                sys.stderr.write(package + ' return error' + '\n')
                continue
            ll = json.loads(result)
            if 'dependencies' in ll:
                A_list.extend(ll['dependencies'].keys())
    if package_or in A_set:
        A_set.remove(package_or)
    print(package_or + ';' + ','.join(A_set))


for line in sys.stdin:
    iterate_call(line.strip())
