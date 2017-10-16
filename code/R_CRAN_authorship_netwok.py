import json
import sys
import re
from collections import defaultdict

auth2pkg = defaultdict(set)
maintainer2pkg = defaultdict(set)

pkg2auth = defaultdict(set)
pkg2maintainer = defaultdict(set)

file1 = '/data/play/R_CRAN_data/R_CRAN_fromMetaCRAN'
f1 = open(file1, 'r')

#fileaudumphell = '/data/play/R_CRAN_data/authdumphell'
#faudumphell = open(fileaudumphell, 'w')

META_CRAN = json.load(f1)
for each in META_CRAN:
    if '_source' not in each:
        continue
    # if 'Author' not in each['_source']['Author']:
    if each['_source']['Author'] == '':
        sys.stderr.write('Author field missing in ' +
                         each['_source']['Package'])
        sys.exit('Author missing')
    # if 'Maintainer' not in each['_source']:
    if each['_source']['Maintainer'] == '':
        sys.stderr.write('Maintainer field missing in ' +
                         each['_source']['Package'])
        sys.exit('Maintainer missing')
    # parse name and email
# here is my assumption:
# <1> name is the unique id otherwise can't find a better to link
# data error found: coerce: <U+000a>;[ctb];[aut;[aut]
# with contributions from  => filter out the contributor
# Based on ...    => throw it away.
# remove punctions  => re.sub(r'[.,]',r'',target)
# still there are cases crap of data there.

    prepro_data = each['_source']['Author'].strip().encode('utf-8')
    prepro_data = re.sub(r'\r\n', r' ', prepro_data)
    prepro_data = re.sub(r'\n', r' ', prepro_data)
    prepro_data = re.sub(r'&', r'and', prepro_data)
    prepro_data = re.sub(r'\[.*?\]', r'', prepro_data)
    prepro_data = re.sub(r'\(.*?(\([^)(]*\))*?\)', r'', prepro_data)
    prepro_data = re.sub(r'<U\+000a>', r' ', prepro_data)
    prepro_data = re.sub(r'Based on.*$', r'', prepro_data, flags=re.IGNORECASE)
    prepro_data = re.sub(r'with contributions from', r'',
                         prepro_data, flags=re.IGNORECASE)
    prepro_data = re.sub(r'with contributions by', r'',
                         prepro_data, flags=re.IGNORECASE)

    Auths2 = prepro_data.split(',')

    if len(Auths2) == 1 and ';' in Auths2:
        Auths2 = prepro_data.split(';')
    AAA = []
    for anyone in Auths2:
        if ' and ' in anyone:
            AAA += anyone.split(' and ')
        else:
            AAA.append(anyone)
    Auths = map(lambda x: re.sub(r'[.,;"]', r'', x), AAA)
    #faudumphell.write(','.join(Auths) + ';')
    #faudumphell.write(each['_source']['Package'] + '\n')

    for eachAu in Auths:
        if '<' in eachAu and '>' in eachAu:
            try:
                match = re.match(r'\s*(.*?)\s*<(.*)>',
                                 eachAu.strip())
            except Exception as e:
                print('###' + eachAu + '###')
#                sys.exit()
            if match:
                author = match.group(1)
                email = match.group(2)
                if author.strip() != '':
                    auth2pkg[author].add(each['_source']['Package'])
                    pkg2auth[each['_source']['Package']].add(author)
            else:
                try:
                    # pass
                    print('###' + eachAu + '###')
                    # sys.exit('author email match error')
                except UnicodeEncodeError:
                    continue
        else:
            if eachAu.strip() != '':
                auth2pkg[eachAu.strip()].add(each['_source']['Package'])
                pkg2auth[each['_source']['Package']].add(eachAu.strip())

    prepro_data = each['_source']['Maintainer'].strip().encode('utf-8')
    prepro_data = re.sub(r'\r\n', r' ', prepro_data)
    prepro_data = re.sub(r'\n', r' ', prepro_data)
    prepro_data = re.sub(r'&', r'and', prepro_data)
    prepro_data = re.sub(r'\[.*?\]', r'', prepro_data)
    prepro_data = re.sub(r'\(.*?(\([^)(]*\))*?\)', r'', prepro_data)
    prepro_data = re.sub(r'<U\+000a>', r' ', prepro_data)
    prepro_data = re.sub(r'Based on.*$', r'', prepro_data, flags=re.IGNORECASE)
    prepro_data = re.sub(r'with contributions from', r'',
                         prepro_data, flags=re.IGNORECASE)
    prepro_data = re.sub(r'with contributions by', r'',
                         prepro_data, flags=re.IGNORECASE)

    Maintainers = prepro_data.split(',')

    if len(Maintainers) == 1 and ';' in Maintainers:
        Maintainers = prepro_data.split(';')
    MMM = []
    for anyone in Maintainers:
        if ' and ' in anyone:
            MMM += anyone.split(' and ')
        else:
            MMM.append(anyone)
    Mas = map(lambda x: re.sub(r'[.,;"]', r'', x), MMM)
#    faudumphell.write(','.join(Mas) + ';')
#    faudumphell.write(each['_source']['Package'] + '\n')

    for eachMa in Mas:
        if '<' in eachMa and '>' in eachMa:
            try:
                match = re.match(r'\s*(.*?)\s*<(.*)>',
                                 eachMa.strip())
            except Exception as e:
                print('###' + eachMa + '###')
#                sys.exit()
            if match:
                author = match.group(1)
                email = match.group(2)
                if author.strip() != '':
                    maintainer2pkg[author].add(each['_source']['Package'])
                    pkg2maintainer[each['_source']['Package']].add(author)
            else:
                try:
                    # pass
                    print('###' + eachMa + '###')
                    # sys.exit('author email match error')
                except UnicodeEncodeError:
                    continue
        else:
            if eachMa.strip() != '':
                maintainer2pkg[eachMa.strip()].add(each['_source']['Package'])
                pkg2maintainer[each['_source']['Package']].add(eachMa.strip())


# author and matintainer dump
fileaudump = '/data/play/R_CRAN_data/authdump'
filemadump = '/data/play/R_CRAN_data/madump'
faudump = open(fileaudump, 'w')
fmadump = open(filemadump, 'w')


faudump.write('\n'.join(auth2pkg.keys()))
fmadump.write('\n'.join(maintainer2pkg.keys()))
faudump.close()
fmadump.close()


file2 = '/data/play/R_CRAN_data/package2otherpackages.THRU.au'
f2 = open(file2, 'w')

for package in pkg2auth:
    otherpackages = set()
#    print(package)
    for au in pkg2auth[package]:
        #        print(au)
        otherpackages.update(auth2pkg[au])
#        print(auth2pkg[au])
    otherpackages.remove(package)
    if len(otherpackages) != 0:
        f2.write(package + ';' + ','.join(otherpackages) + '\n')

f2.close()


file4 = '/data/play/R_CRAN_data/package2otherpackages.THRU.ma'
f4 = open(file4, 'w')

for package in pkg2maintainer:
    otherpackages = set()
#    print(package)
    for au in pkg2maintainer[package]:
        #        print(au)
        otherpackages.update(maintainer2pkg[au])
#        print(auth2pkg[au])
    otherpackages.remove(package)
    if len(otherpackages) != 0:
        f4.write(package + ';' + ','.join(otherpackages) + '\n')

f4.close()


file3 = '/data/play/R_CRAN_data/package2otherpackages.THRU.au.ma'
f3 = open(file3, 'w')

for package in pkg2auth:
    otherpackages = set()

    for au in pkg2auth[package]:
        otherpackages.update(auth2pkg[au])
        if au in maintainer2pkg:
            otherpackages.update(maintainer2pkg[au])

    for ma in pkg2maintainer[package]:
        otherpackages.update(maintainer2pkg[ma])
        if ma in auth2pkg:
            otherpackages.update(auth2pkg[ma])
    otherpackages.remove(package)
    if len(otherpackages) != 0:
        f3.write(package + ';' + ','.join(otherpackages) + '\n')
f3.close()
