import sys
import re
from subprocess import call, check_output, CalledProcessError
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
                result = check_output('deppkgs ' + package, shell=True)
            except Exception:
                sys.stderr.write(package + ' return error' + '\n')
                continue
            if len(result.strip()) == 0:
                continue
            # print(result[0:-1])
            A_list.extend(result.strip().split('\n'))
    if package_or in A_set:
        A_set.remove(package_or)
    print(package_or + ';' + ','.join(A_set))


# recursively_call(sys.argv[1])
for line in sys.stdin:
    iterate_call(line.strip())

# direct downstreams
'''
for line in sys.stdin:
    result = check_output('deppkgs ' + line.strip(), shell=True)
    print(line.strip() + ';' + re.sub(r'\n', r',', result.strip()))
'''
