import sys
import re
from subprocess import call, check_output
'''
if len(sys.argv) != 2:
    sys.exit('usage python aaa.py <package>')
# print(sys.argv[1])
'''
'''
#resursively doesn't work, wonder if it's because of memory usage.
def recursively_call(package):
    result = check_output('deppkgs ' + package, shell=True)
    if len(result) == 0:
        return
    print(result[0:-1])
    for i in result.split('\n'):
        recursively_call(i)
    # print(len(result))
    # print(result)
    # print(result)
    # deppkgs package
    # print(result)
'''

# iteration


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


# recursively_call(sys.argv[1])
# iterate_call(sys.argv[1])

# direct downstreams
for line in sys.stdin:
    result = check_output('deppkgs ' + line.strip(), shell=True)
    print(line.strip() + ';' + re.sub(r'\n', r',', result.strip()))
