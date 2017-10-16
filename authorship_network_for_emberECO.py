import requests
import json
import sys

prefix = 'https://api.npms.io/v2/'


file1 = 'ECOpackage2otherpackagesThuau'
file2 = 'ECOpackage2otherpackagesThuma'
# file3 = 'ECOpackage2otherpackagesThuau.ma'

f1 = open(file1, 'w')
f2 = open(file2, 'w')
# f3 = open(file3, 'w')

for line in sys.stdin:
    package = line.strip()
    r1 = requests.get(prefix + 'package/' + package)
    if r1.ok:
        result = r1.text
        try:
            package_data = json.loads(result)
            meta = package_data['collected']['metadata']

            if 'author' in meta:
                linked_au_set = set()
                if len(meta['author']) != 0 and 'username' in meta['author']:
                    r2 = requests.get(prefix + 'search?q=author:' +
                                      meta['author']['username'])
                    if r2.ok:

                        for pac in json.loads(r2.text)['results']:
                            linked_au_set.add(pac['package']['name'])
                        if package in linked_au_set:
                            linked_au_set.remove(package)
                f1.write(package + ';' + ','.join(linked_au_set) + '\n')

            if 'maintainers' in meta:
                linked_ma_set = set()
                if len(meta['maintainers']) != 0:
                    for eachma in meta['maintainers']:
                        if 'username' in eachma:
                            r3 = requests.get(prefix + 'search?q=maintainer:' +
                                              eachma['username'])
                            if r3.ok:
                                for pac in json.loads(r3.text)['results']:
                                    linked_ma_set.add(pac['package']['name'])
                    if package in linked_ma_set:
                        linked_ma_set.remove(package)
                f2.write(package + ';' + ','.join(linked_ma_set) + '\n')
        except Exception as e:
            print(package + ' error! ' + e.message)
